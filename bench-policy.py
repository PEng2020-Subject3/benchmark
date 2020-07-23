import random
import json
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(2, 4)
    sensors = ["smart", "lambo", "angela merte"]
    headers = {'content-type': 'text/plain'}

    @task
    def function_call(self):
        payload = {"sensor_ID": random.choice(self.sensors), "function": "genPerformanceScore"}
        self.client.get("/function/performance-scores?policy=gdpr", headers=self.headers, data=json.dumps(payload))
