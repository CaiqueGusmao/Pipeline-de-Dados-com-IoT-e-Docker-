#  Pipeline de Dados com IoT e Docker

Este projeto constrói um pipeline de dados para leitura, processamento e visualização de informações de temperatura geradas por dispositivos IoT. Utiliza Python para ingestão e análise, PostgreSQL como banco de dados, Docker para orquestração e Streamlit para visualização interativa via dashboard.

---

##  Objetivos

- Processar dados de temperatura vindos de sensores IoT.
- Armazenar os dados em um banco PostgreSQL usando Docker.
- Visualizar informações relevantes com gráficos interativos.
- Garantir o versionamento do projeto com Git e GitHub.

---

##  Estrutura do Projeto

```bash
iot-pipeline/
├── temperature_readings.csv           # Base de dados original
├── pipeline.py                        # Script para ingestão dos dados
├── dashboard.py                       # Dashboard interativo com Streamlit
├── requirements.txt                   # Bibliotecas necessárias
└── README.md                          # Este arquivo
```

---

##  Requisitos

- Python 3.10+
- Docker
- Git
- Conta no Kaggle (para baixar o dataset original)

## Tecnologias Utilizadas

- **Python** (Manipulação de dados e integração com o banco)
- **PostgreSQL** (Armazenamento e processamento dos dados)
- **SQLAlchemy** (ORM para interagir com o banco de dados)
- **Pandas** (Leitura e tratamento de arquivos CSV)
- **Streamlit** (Criação do dashboard interativo)
- **Plotly** (Visualização gráfica dos dados)

---

##  Instalação das Bibliotecas

Crie um ambiente virtual e execute:

```bash
pip install -r requirements.txt
```

Conteúdo do `requirements.txt`:

```
pandas
sqlalchemy
psycopg2-binary
streamlit
plotly
```

---

## Configuração do Banco com Docker

Execute no terminal:

```bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha  -p 5432:5432  -d postgres
```


---

##  Executar o Pipeline de Dados

Rode o script de ingestão:

```bash
python pipeline.py
```

Este script:

- Lê o arquivo `temperature_readings.csv`
- Conecta ao PostgreSQL via SQLAlchemy
- Cria a tabela e insere os dados

---

##  Views SQL no PostgreSQL

Execute no banco as seguintes views:

```sql
-- Média de temperatura por Ambiente
Uso: Permite visualizar a média de temperatura para ambientes internos e externos.

CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id;


-- Leituras por hora
Uso: Permite acompanhar as variações de temperatura de uma forma mais detalhada ao longo das horas.

CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM timestamp) AS hora, COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora;

-- Temperaturas por dia
Uso: Permite acompanhar as variações extremas de temperatura ao longo do dia.

CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(timestamp) AS data,
       MAX(temperature) AS temp_max,
       MIN(temperature) AS temp_min
FROM temperature_readings
GROUP BY data;
```

---

##  Executar o Dashboard

Inicie com:

```bash
streamlit run dashboard.py
```

Funcionalidades:

-  Gráfico de barras: Média de temperatura por Ambiente
-  Gráfico de linha: Leituras por hora do dia
-  Gráfico comparativo: Temperaturas máximas e mínimas por dia

---

##  Insights Obtidos

- Dispositivos com maior e menor temperatura média
- Horários com maior volume de leituras
- Variações de temperatura por dia
- Identificação de padrões climáticos ou possíveis falhas em sensores

---

##  Licença e Autoria

Desenvolvido por **Caique** com foco em integração de tecnologias de IoT, dados e visualização.  
Este projeto é de uso educacional e pode ser expandido para soluções reais.

```   ## Screenhots

<img width="569" height="378" alt="image" src="https://github.com/user-attachments/assets/06742ae4-8333-4ed1-87fa-0b9e62572f21" />


<img width="584" height="294" alt="image" src="https://github.com/user-attachments/assets/d1b2a4f6-2a25-4381-8cac-ed733a733dce" />


<img width="608" height="374" alt="image" src="https://github.com/user-attachments/assets/8cbda1ca-54e7-4b5c-ab57-3d318b5bb347" />
