orders = spark.table("silver_orders")

order_items = spark.table("silver_order_items")

products = spark.table("silver_products")

customers = spark.table("silver_customers")

payments = spark.table("silver_payments")

sellers = spark.table("silver_sellers")

reviews = spark.table("silver_reviews")

category = spark.table("silver_category_translation")


sales_fact = orders.join(
    order_items,
    "order_id",
    "inner"
)

sales_fact = sales_fact.join(
    customers,
    "customer_id",
    "left"
)

sales_fact = sales_fact.join(
    products,
    "product_id",
    "left"
)

display(sales_fact)






