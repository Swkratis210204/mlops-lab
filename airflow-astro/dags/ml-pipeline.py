from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def preprocess_data():
    print("Preprocess data")


def train_model():
    print("Training Model")


def evaluate_model():
    print("Evaluate Model")


with DAG(
    dag_id="ml_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule="@weekly",
    catchup=False,
) as dag:

    preprocess = PythonOperator(
        task_id="preprocess_task",
        python_callable=preprocess_data,
    )

    train = PythonOperator(
        task_id="train_task",
        python_callable=train_model,
    )

    evaluate = PythonOperator(
        task_id="evaluate_task",
        python_callable=evaluate_model,
    )

    preprocess >> train >> evaluate