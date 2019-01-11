from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 1, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("random-fail", default_args=default_args, schedule_interval=timedelta(1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(task_id="task1", bash_command="echo task1", dag=dag)

t2 = BashOperator(task_id="task2", bash_command="rnd=$RANDOM; echo $rnd; if [ $rnd -lt 20000 ]; then exit 1; fi", retries=0, dag=dag)

t3 = BashOperator(task_id="task3", bash_command="echo task3", dag=dag)

t1 >> t2
t2 >> t3
