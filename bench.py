import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(2, 4)

    @task
    def normal(self):
        self.client.get("/function/nodeinfo")

    @task
    def policy(self):
        self.client.get("/function/nodeinfo?policy=test")

