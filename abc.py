# Databricks notebook source
import pandas as pd

# COMMAND ----------

all_args = dbutils.notebook.entry_point.getCurrentBindings()
 
print(all_args)

# COMMAND ----------

para = dbutils.widgets.get('parameter_1')

# COMMAND ----------

print(para)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Haha
