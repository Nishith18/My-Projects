# Databricks notebook source
dbutils.secrets.list(scope='formula1-scope')

# COMMAND ----------

client_id_key=dbutils.secrets.get(scope='formula1-scope',key='client-id-key')
tenant_id_key=dbutils.secrets.get(scope='formula1-scope',key='tenant-id-key')
client_secret_key=dbutils.secrets.get(scope='formula1-scope',key='client-secret-key')

# COMMAND ----------


spark.conf.set("fs.azure.account.auth.type.dbnisformula1dl.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.dbnisformula1dl.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.dbnisformula1dl.dfs.core.windows.net", client_id_key)
spark.conf.set("fs.azure.account.oauth2.client.secret.dbnisformula1dl.dfs.core.windows.net", client_secret_key)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.dbnisformula1dl.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id_key}/oauth2/token")

# COMMAND ----------

dbutils.fs.ls("abfss://demo@dbnisformula1dl.dfs.core.windows.net")

# COMMAND ----------

display(spark.read.csv("abfss://demo@dbnisformula1dl.dfs.core.windows.net/circuits.csv"))