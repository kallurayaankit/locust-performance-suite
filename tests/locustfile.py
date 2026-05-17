from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # wait 1-2 seconds between tasks

    @task(3)  # 3 times more likely to run this task
    def fast_endpoint(self):
        self.client.get("/fast")

    @task(1)
    def slow_endpoint(self):
        self.client.get("/slow")