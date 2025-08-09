from venv import logger

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import xgboost as xgb
import pandas as pd
import numpy as np
import os
import logging
from dotenv import load_dotenv
from google.cloud import storage
import logging


load_dotenv()
# ---------------------------
# Logging Setup
# ---------------------------
log_file_path = os.path.join(os.path.dirname(__file__), 'app.log')
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------------------
# FastAPI Initialization
# ---------------------------
app = FastAPI()

# ---------------------------
# GCS Model Download & Load
# ---------------------------
MODEL_PATH = "model.json"

def download_model_from_gcs():
    bucket_name = os.getenv("GCS_BUCKET_NAME")
    blob_name = os.getenv("GCS_BLOB_NAME")

    if not bucket_name or not blob_name:
        logging.error("GCS_BUCKET_NAME or GCS_BLOB_NAME environment variables are missing.")
        raise ValueError("Missing GCS configuration.")

    if os.path.exists(MODEL_PATH):
        logging.info("Model already exists locally. Skipping download.")
        return

    logging.info(f"Downloading model from GCS bucket '{bucket_name}', blob '{blob_name}'.")
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(MODEL_PATH)
    logging.info("Model downloaded successfully.")

def load_model():
    """Load the XGBoost model from local file."""
    model = xgb.Booster()
    model.load_model(MODEL_PATH)
    logging.info("Model loaded successfully into memory.")
    return model


# ---------------------------
# App Startup Event
# ---------------------------
@app.on_event("startup")
def startup_event():
    global model
    try:
        download_model_from_gcs()  # calls your zero-param function that reads env vars
        model = load_model()
        print("Model loaded successfully.")
        logging.info("Model loaded successfully.")
    except Exception as e:
        print(f"Failed to load model during startup: {e}")
        logging.error(f"Failed to load model during startup: {e}")
        raise

# Input Schema
# ---------------------------
class SpeciesEnum(str, Enum):
    Adelie = "Adelie"
    Chinstrap = "Chinstrap"
    Gentoo = "Gentoo"


class PenguinFeatures(BaseModel):
    island: str
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    sex: str


# ---------------------------
# Prediction Endpoint
# ---------------------------
def predict(features: PenguinFeatures):
    try:
        input_df = pd.DataFrame([features.dict()])

        # Simple mapping of categorical columns to integers
        island_map = {"Torgersen": 0, "Biscoe": 1, "Dream": 2}
        sex_map = {"male": 0, "female": 1}

        input_df['island'] = input_df['island'].map(island_map)
        input_df['sex'] = input_df['sex'].map(sex_map)

        input_data = xgb.DMatrix(input_df)
        preds = model.predict(input_data)
        predicted_class = int(np.argmax(preds, axis=1)[0])

        species_map = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
        predicted_species = species_map.get(predicted_class, "Unknown")

        return {"predicted_species": predicted_species}

    except Exception as e:
        logging.error(f"Prediction failed: {str(e)}")
        return {"error": str(e)}


# ---------------------------
# Root Endpoint
# ---------------------------
@app.get("/")
def root():
    return {"message": "Penguin Classifier API is running"}

@app.get("/status")
def status():
    if model:
        return {"status": "Model loaded"}
    else:
        return {"status": "Model not loaded"}
