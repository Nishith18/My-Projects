# Databricks notebook source
display(dbutils.fs.ls('/'))

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/FileStore/tables/circuits.csv'))

# COMMAND ----------

display(spark.read.csv('/FileStore/tables/circuits.csv'))

# COMMAND ----------

databases = spark.sql
databases.show()

# COMMAND ----------

