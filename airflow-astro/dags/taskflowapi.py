from datetime import datetime
from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id="math_sequence_dag_with_taskflow",
    start_date=datetime(2024, 1, 1),
    schedule="@once",
    catchup=False,
) as dag:

    @task
    def start_number():
        val = 10
        print(f"Starting number: {val}")
        return val

    @task
    def add_five(current_value):
        new_value = current_value + 5
        print(f"Added 5: {new_value}")
        return new_value

    @task
    def multiply_by_two(current_value):
        new_value = current_value * 2
        print(f"Multiplied by 2: {new_value}")
        return new_value

    @task
    def subtract_three(current_value):
        new_value = current_value - 3
        print(f"Subtracted 3: {new_value}")
        return new_value

    @task
    def square_number(current_value):
        new_value = current_value ** 2
        print(f"Final value (squared): {new_value}")
        return new_value

    start = start_number()
    added = add_five(start)
    multiplied = multiply_by_two(added)
    subtracted = subtract_three(multiplied)
    square_value=square_number(subtracted)