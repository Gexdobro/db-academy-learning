# Databricks notebook source
import pyspark.sql.functions as F
import pyspark.sql.types as T

# COMMAND ----------

df = spark.table("nyc_taxi_csv")

# COMMAND ----------

df_agg = df \
  .where(F.col('totalAmount').isNotNull()) \
  .groupby('month_num') \
  .agg(
     F.mean('totalAmount').alias('avg_price'), F.mean('temperature').alias('avg_temp')
  ) \
  .orderBy('month_num')

# COMMAND ----------

display(df_agg)
