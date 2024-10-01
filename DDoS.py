# Ataque-DDoS
import subprocess
import time
from locust import HttpUser, task, between

def run_jmeter(jmx_file, jmeter_path="path_to_jmeter"):
    print("Iniciando Apache JMeter...")
    
    command = f"{jmeter_path}/bin/jmeter -n -t {jmx_file} -l jmeter_results.jtl"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print("Teste JMeter concluído com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o JMeter: {e}")

def run_locust(locust_file):
    print("Iniciando Locust...")
    
    command = f"locust -f {locust_file} --headless -u 10 -r 1 --run-time 1m"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print("Teste Locust concluído com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o Locust: {e}")

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  

    @task
    def load_test(self):
        self.client.get("/")

def main():
    jmx_file = "test_plan.jmx"  
    locust_file = "locustfile.py"  
    
    run_jmeter(jmx_file)
    
    time.sleep(5)
    
    run_locust(locust_file)

if __name__ == "__main__":
    main()
