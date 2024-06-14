# Databricks notebook source
dbutils.secrets.list(scope='formula1-scope')

# COMMAND ----------

client_id_key=dbutils.secrets.get(scope='formula1-scope',key='client-id-key')
tenant_id_key=dbutils.secrets.get(scope='formula1-scope',key='tenant-id-key')
client_secret_key=dbutils.secrets.get(scope='formula1-scope',key='client-secret-key')

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id_key,
          "fs.azure.account.oauth2.client.secret": client_secret_key,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id_key}/oauth2/token"}

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://demo@dbnisformula1dl.dfs.core.windows.net/",
  mount_point = "/mnt/dbnisformula1dl/demo",
  extra_configs = configs)

# COMMAND ----------

display(dbutils.fs.ls("/mnt/dbnisformula1dl/demo"))

# COMMAND ----------

display(spark.read.csv("dbfs:/mnt/dbnisformula1dl/demo/circuits.csv"))

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

dbutils.fs.unmount('/mnt/formula1dl/demo')