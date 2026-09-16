# import pytest
import pytest
from lib.Utils import get_spark_session
from lib.DataReader import read_customers, read_orders
from lib.DataManipulation import filter_closed_orders, count_orders_state, filter_orders_generic
from lib.ConfigReader import get_app_conf

# to reduce redudant code like spark Session creation code. Mo dularise we push this code to conftest.py
# @pytest.fixture
# def spark():
#     return get_spark_session("LOCAL")


# code before the fixure
# def test_read_customers_df():
#     spark = get_spark_session("LOCAL")
#     customers_count = read_customers(spark,"LOCAL").count()
#     assert customers_count == 12435

@pytest.mark.skip()
def test_read_customers_df(spark):
    customers_count = read_customers(spark,"LOCAL").count()
    assert customers_count == 12435

@pytest.mark.skip()
def test_read_orders_df(spark):
    orders_count = read_orders(spark,"LOCAL").count()
    assert orders_count == 68884

@pytest.mark.skip()
def test_filtered_orders_df(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_orders_count = filter_closed_orders(orders_df).count()
    assert filtered_orders_count == 7556

@pytest.mark.skip()
def test_read_app_config():
    config = get_app_conf("LOCAL")
    assert config["orders.file.path"] == "data/orders.csv"

@pytest.mark.skip()
def test_count_orders_statewise(spark,expected_results):
    actual_results = count_orders_state(read_customers(spark, "LOCAL"))
    assert actual_results.collect() == expected_results.collect()

@pytest.mark.skip()
def test_closed_count(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_orders_count = filter_closed_orders(orders_df).count()
    assert filtered_orders_count == 7556

@pytest.mark.parametrize(
        "status, count",
        [
            ("CLOSED",7556),
            ("PENDING_PAYMENT", 15030),
            ("COMPLETE",22900)
        ]
)
def test_filter_orders_gerenric(spark, status, count):
    orders_df = read_orders(spark,"LOCAL")
    filtered_orders_count = filter_orders_generic(orders_df,status).count()
    assert filtered_orders_count == count
