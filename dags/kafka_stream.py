from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 3 ,10,00),

}
def get_data():
    import requests
    data = requests.get('https://randomuser.me/api/')
    print(data.json())

def stream_data():
    import json
    
'''with DAG('user_automation',default_args=default_args,
         schedule_interval='@daily',catchup=False) as dag:
    
    streaming_task = PythonOperator(
        task_id='streaming_data_from_api',
        python_callable=stream_data,
        )'''
stream_data()

