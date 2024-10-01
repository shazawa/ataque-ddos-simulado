# Ataque DDoS Simulado

Este repositório contém um script em Python que utiliza **Apache JMeter** e **Locust** para realizar testes de carga em aplicações web. O objetivo é simular um ataque DDoS (Distributed Denial of Service) para avaliar a resiliência e o desempenho de servidores web sob alta carga.

## Funcionalidades

- **Apache JMeter**: Executa um teste de carga baseado em um arquivo `.jmx`, permitindo simular múltiplas requisições simultâneas a um servidor.
- **Locust**: Complementa os testes executando um script de carga em modo headless, gerando tráfego de forma controlada e escalável.

## Estrutura do Código

- `run_jmeter(jmx_file, jmeter_path)`: Função que inicia o Apache JMeter com um plano de teste especificado.
- `run_locust(locust_file)`: Função que inicia o Locust com um arquivo de configuração.
- `WebsiteUser`: Classe que define o comportamento dos usuários virtuais durante os testes de carga com Locust.
- `main()`: Função principal que coordena a execução dos testes, chamando o JMeter seguido do Locust.

## Requisitos

- Python 3.x
- Apache JMeter
- Locust

## Como Usar

1. Certifique-se de ter o JMeter e o Locust instalados em seu sistema.
2. Configure os arquivos `test_plan.jmx` e `locustfile.py` conforme necessário.
3. Execute o script Python:
   ```bash
   python ataque_ddos.py

