orders = spark.table("silver_orders")

order_items = spark.table("silver_order_items")

products = spark.table("silver_products")

customers = spark.table("silver_customers")

#payments = spark.table("silver_payments")

sellers = spark.table("silver_sellers")

reviews = spark.table("silver_reviews")

category = spark.table("silver_category")


sales_fact = orders.join(
     order_items,
    on="order_id",
    how="inner"
)

#display(sales_fact)
#Join Products
sales_fact = sales_fact.join(
    products,
    on="product_id",
    how="left"
)

display(sales_fact.limit(20))
#Join Customers
sales_fact = sales_fact.join(
    customers,
    on="customer_id",
    how="left"
)

display(sales_fact.limit(20))

sales_fact.write \
.format("delta") \
.option("overwriteSchema","true") \
.mode("overwrite") \
.saveAsTable("gold_sales_fact")







