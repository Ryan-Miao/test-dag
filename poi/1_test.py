
"""
Generated by airflow console
fileName:  poi/1_test.py
date    :  2019-09-20 11:54:00
"""


from airflow import DAG
from datetime import datetime

default_args = {
    'owner': 'est',
    'depends_on_past': False,
    'start_date': datetime(2019, 09, 18),
}

dag = DAG(
    '1_test',
    description='test',
    default_args=default_args,
    schedule_interval="est")


from airflow.operators.bash_operator import BashOperator






sdfsdf = BashOperator(
    task_id='sdfsdf',
    bash_command='aaaaa',
    dag=dag)


t1>>t2