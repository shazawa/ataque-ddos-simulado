from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://challenge2024brute.com/:8000"  # Substitua pela URL da aplicação que você quer testar

    @task
    def load_test(self):
        self.client.get("/")
