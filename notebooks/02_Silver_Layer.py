customers_df = spark.table("bronze_customers")
orders_df = spark.table("bronze_orders")
products_df = spark.table("bronze_products")
order_items_df = spark.table("bronze_order_items")
#payments_df = spark.table("bronze_payments")
reviews_df = spark.table("bronze_reviews")
sellers_df = spark.table("bronze_sellers")
category_df = spark.table("bronze_category_translation")


spark.sql("DROP TABLE IF EXISTS silver_orders")
spark.sql("DROP TABLE IF EXISTS silver_products")
spark.sql("DROP TABLE IF EXISTS silver_category")
# Remove Duplicates

customers_clean = customers_df.dropDuplicates()
orders_clean = orders_df.dropDuplicates()
products_clean = products_df.dropDuplicates()
order_items_clean = order_items_df.dropDuplicates()
#payments_clean = payments_df.dropDuplicates()
reviews_clean = reviews_df.dropDuplicates()
sellers_clean = sellers_df.dropDuplicates()
category_clean = category_df.dropDuplicates()


# Create Silver Tables

customers_clean.write.format("delta").mode("overwrite").saveAsTable("silver_customers")

orders_clean.write.format("delta").mode("overwrite").saveAsTable("silver_orders")

products_clean.write.format("delta").mode("overwrite").saveAsTable("silver_products")

order_items_clean.write.format("delta").mode("overwrite").saveAsTable("silver_order_items")

#payments_clean.write.format("delta").mode("overwrite").saveAsTable("silver_payments")

reviews_clean.write.format("delta").mode("overwrite").saveAsTable("silver_reviews")

sellers_clean.write.format("delta").mode("overwrite").saveAsTable("silver_sellers")

category_clean.write.format("delta").mode("overwrite").saveAsTable("silver_category")
