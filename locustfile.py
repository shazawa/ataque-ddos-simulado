from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://challenge2024brute.com"  # Seu domínio

    @task
    def load_test(self):
        self.client.get("/")

    @task
    def submit_form(self):
        self.client.post("/", data={"field1": "value1", "field2": "value2"})

    @task
    def other_endpoint(self):
        self.client.get("/#")


# Configuração para alta carga com múltiplos usuários e frequências
class HeavyLoadUser(HttpUser):
    wait_time = between(0.001, 0.1)  # Defina o intervalo de tempo de espera entre requisições
    host = "https://challenge2024brute.com"
    
    @task
    def high_frequency_requests(self):
        self.client.get("/")  # Requisição GET na raiz
        self.client.post("/", json={"data": "high_load"})  # Requisição POST com alta carga
        self.client.get("/other-endpoint")  # Requisição GET em outro endpoint
    
    def on_start(self):
        print("Iniciando múltiplos tipos de requisições")

    @task
    def load_test_heavy(self):
        for i in range(100000000):  # Número razoável de requisições por loop
            response = self.client.get("/")
            if response.status_code != 200:
                print(f"Erro na requisição {i}: {response.status_code}")

