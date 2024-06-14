# Databricks notebook source
def mount_containers(storagename,containername):
    #Get secrets from key vault
    client_id_key=dbutils.secrets.get(scope='formula1-scope',key='client-id-key')
    tenant_id_key=dbutils.secrets.get(scope='formula1-scope',key='tenant-id-key')
    client_secret_key=dbutils.secrets.get(scope='formula1-scope',key='client-secret-key')

    #Configuration details
    configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id_key,
          "fs.azure.account.oauth2.client.secret": client_secret_key,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id_key}/oauth2/token"}
    
    #Check if container already mounted
    if any(mount.mountPoint == f"/mnt/{storagename}/{containername}" for mount in dbutils.fs.mounts()):
        dbutils.fs.unmount(f"/mnt/{storagename}/{containername}")

    #Mount Container
    dbutils.fs.mount(
    source = f"abfss://{containername}@{storagename}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storagename}/{containername}",
    extra_configs = configs)

    #display
    display(dbutils.fs.mounts())

# COMMAND ----------

mount_containers("dbnisformula1dl","raw")

# COMMAND ----------

mount_containers('dbnisformula1dl', 'processed')

# COMMAND ----------

mount_containers('dbnisformula1dl', 'presentation')