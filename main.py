from io import BytesIO
from pathlib import Path
from tempfile import NamedTemporaryFile

# from airflow import DAG
# from airflow.providers.standard.operators.empty import EmptyOperator
import polars as pl
# import pycurl


def main():
    # with DAG(
    #     dag_id="example_dep_repo",
    #     schedule=None,
    #     catchup=False,
    #     tags=["example"],
    # ) as dag:
    #     start = EmptyOperator(task_id="start")
    #     finish = EmptyOperator(task_id="finish")
    #     start >> finish

    frame = pl.DataFrame(
        {
            "package": ["polars", "pycurl", "apache-airflow"],
            "used": [True, True, True],
        }
    )
    print(frame)
    # print(f"airflow dag: {dag.dag_id} ({len(dag.tasks)} tasks)")

    # with NamedTemporaryFile("w", delete=False) as tmp:
    #     tmp.write("hello from pycurl\n")
    #     temp_path = Path(tmp.name)

    # buffer = BytesIO()
    # curl = pycurl.Curl()
    # try:
    #     curl.setopt(pycurl.URL, temp_path.resolve().as_uri())
    #     curl.setopt(pycurl.WRITEDATA, buffer)
    #     curl.perform()
    # finally:
    #     curl.close()
    #     temp_path.unlink(missing_ok=True)

    # print(buffer.getvalue().decode().strip())


if __name__ == "__main__":
    main()
