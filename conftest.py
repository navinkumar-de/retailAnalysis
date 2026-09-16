import pytest
from lib.Utils import get_spark_session

@pytest.fixture
# def spark():
#     return get_spark_session("LOCAL")
def spark():
    "Creates Spark Session and After Test cases run it will destroy the session"
    spark_session = get_spark_session("LOCAL")
    yield spark_session
    spark_session.stop()

@pytest.fixture
def expected_results(spark):
    "Gives the Expected Results for Aggregation operation"
    results_schema = "state string, count int"
    return spark.read.format("csv").schema(results_schema).load("data/test_results/state_aggregate.csv")