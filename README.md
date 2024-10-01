# Ataque DDoS Simulado

Este repositório contém um script em Python que utiliza  **Locust** para realizar testes de carga em aplicações web. O objetivo é simular um ataque DDoS (Distributed Denial of Service) para avaliar a resiliência e o desempenho de servidores web sob alta carga.

## Funcionalidades

- **Locust**: Complementa os testes executando um script de carga em modo headless, gerando tráfego de forma controlada e escalável.

## Estrutura do Código

- `run_locust(locust_file)`: Função que inicia o Locust com um arquivo de configuração.
- `WebsiteUser`: Classe que define o comportamento dos usuários virtuais durante os testes de carga com Locust.

## Requisitos

- Python 3.x
- Locust

## Como Usar

1. Certifique-se de ter o Locust instalados em seu sistema.
2. Configure os arquivos `locustfile.py` conforme necessário.
3. Execute o script Python:
   ```bash
   locust -f locustfile.py --headless -u 1000 -r 100 --run-time 10m

