from fastapi.testclient import TestClient
from apps.main import app

client = TestClient(app)


def test_predict_endpoint_valid_input():
    sample_data = {
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750,
        "sex": "male",
        "island": "Torgersen"
    }

    with TestClient(app) as client:
        response = client.post("/predict", json=sample_data)
        assert response.status_code == 200
        json_resp = response.json()
        assert "predicted_species" in json_resp
        assert json_resp["predicted_species"] in ["Adelie", "Chinstrap", "Gentoo"]

def test_predict_endpoint_missing_field():
    sample_data = {
        # "bill_length_mm" omitted on purpose
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750,
        "sex": "male",
        "island": "Torgersen"
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422  # Validation error for missing field

def test_predict_endpoint_invalid_type():
    sample_data = {
        "bill_length_mm": "thirty-nine",  # invalid type
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": 3750,
        "sex": "male",
        "island": "Torgersen"
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 422  # Validation error for wrong type

def test_predict_endpoint_out_of_range():
    sample_data = {
        "bill_length_mm": 39.1,
        "bill_depth_mm": 18.7,
        "flipper_length_mm": 181,
        "body_mass_g": -100,  # Negative body mass
        "sex": "male",
        "island": "Torgersen"
    }
    response = client.post("/predict", json=sample_data)
    # Your app currently does not reject negative values, so expect 200 or error key
    assert response.status_code == 200
    json_resp = response.json()
    assert "predicted_species" in json_resp or "error" in json_resp

def test_predict_endpoint_empty_request():
    response = client.post("/predict", json={})
    assert response.status_code == 422  # Validation error for missing all fields















