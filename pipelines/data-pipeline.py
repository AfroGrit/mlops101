import kfp
from kfp import dsl


@dsl.pipeline(name="mlops101-pipeline")
def data_pipeline():
    spark_task = dsl.ContainerOp(
        name="spark-job1", image="afrogrit/mlops101-spark-job1:latest", arguments=[]
    )
