from locust import HttpUser, task, between
import json

class PenguinApiUser(HttpUser):
    wait_time = between(1, 3)  # wait 1 to 3 seconds between tasks

    @task
    def predict(self):
        payload = {
            "island": "Biscoe",
            "bill_length_mm": 45.5,
            "bill_depth_mm": 14.3,
            "flipper_length_mm": 220,
            "body_mass_g": 4500,
            "sex": "male"
        }
        headers = {"Content-Type": "application/json"}

        self.client.post("/predict", data=json.dumps(payload), headers=headers)
