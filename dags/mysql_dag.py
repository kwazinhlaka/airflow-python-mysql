from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import mysql_task  # Import your task

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_mysql_task():
    mysql_task.connect_to_db()

with DAG(
    dag_id='mysql_connection_dag',
    default_args=default_args,
    description='A simple DAG to connect to MySQL using Python',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    connect_to_mysql = PythonOperator(
        task_id='connect_to_mysql',
        python_callable=run_mysql_task
    )
