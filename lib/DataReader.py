from lib import ConfigReader

# defining Customers schema
def get_customers_schema():
    schema = "customer_id int, customer_fname string, customer_lname string, username string, password string, address string, city string, state string, pincode string"
    return schema

# creating Customers Dataframe
def read_customers(spark, env):
    conf = ConfigReader.get_app_conf(env)
    customers_file_path = conf["customers.file.path"]
    return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(get_customers_schema()) \
    .load(customers_file_path)

# defining orders schema
def get_orders_schema():
    schema = "order_id int, order_date string, customer_id int, order_status string"
    return schema

# creating orders Dataframe
def read_orders(spark, env):
    conf = ConfigReader.get_app_conf(env)
    orders_file_path = conf["orders.file.path"]
    return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(get_orders_schema()) \
    .load(orders_file_path)