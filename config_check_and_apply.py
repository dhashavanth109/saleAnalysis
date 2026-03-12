# Databricks notebook source
# MAGIC %sql
# MAGIC use catalog ecommerce;

# COMMAND ----------

# MAGIC %sql 
# MAGIC drop table if exists bronze.customers_bronze

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS bronze.customers_bronze (
# MAGIC     customer_id STRING,
# MAGIC     customer_name STRING,
# MAGIC     email STRING,
# MAGIC     phone STRING,
# MAGIC     address STRING,
# MAGIC     segment STRING,
# MAGIC     country STRING,
# MAGIC     city STRING,
# MAGIC     state STRING,
# MAGIC     postal_code STRING,
# MAGIC     region STRING,
# MAGIC     
# MAGIC     -- Audit Columns
# MAGIC     ingestion_timestamp TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC )
# MAGIC USING DELTA

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.customers_silver (
# MAGIC     customer_id STRING NOT NULL,
# MAGIC     customer_name STRING,
# MAGIC     email STRING,
# MAGIC     phone STRING,
# MAGIC     address STRING,
# MAGIC     segment STRING,
# MAGIC     country STRING,
# MAGIC     city STRING,
# MAGIC     state STRING,
# MAGIC     postal_code STRING,
# MAGIC     region STRING,
# MAGIC
# MAGIC     -- Change detection
# MAGIC     record_hash STRING NOT NULL,
# MAGIC
# MAGIC     -- SCD Type 2 columns
# MAGIC     effective_start_date TIMESTAMP NOT NULL,
# MAGIC     effective_end_date TIMESTAMP NOT NULL,
# MAGIC     is_current BOOLEAN NOT NULL,
# MAGIC
# MAGIC     -- Audit columns
# MAGIC     created_date TIMESTAMP NOT NULL,
# MAGIC     updated_date TIMESTAMP NOT NULL,
# MAGIC     batch_id INTEGER,
# MAGIC     source_file_name STRING
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS error.customers_bronze_error (
# MAGIC     customer_id STRING,
# MAGIC     customer_name STRING,
# MAGIC     email STRING,
# MAGIC     phone STRING,
# MAGIC     address STRING,
# MAGIC     segment STRING,
# MAGIC     country STRING,
# MAGIC     city STRING,
# MAGIC     state STRING,
# MAGIC     postal_code STRING,
# MAGIC     region STRING,
# MAGIC
# MAGIC     error_code STRING NOT NULL,
# MAGIC     error_description STRING NOT NULL,
# MAGIC     error_timestamp TIMESTAMP NOT NULL,
# MAGIC     ingestion_timestamp TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC
# MAGIC )
# MAGIC USING DELTA;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS error.customers_silver_error (
# MAGIC     customer_id STRING,
# MAGIC     customer_name STRING,
# MAGIC     email STRING,
# MAGIC     phone STRING,
# MAGIC     address STRING,
# MAGIC     segment STRING,
# MAGIC     country STRING,
# MAGIC     city STRING,
# MAGIC     state STRING,
# MAGIC     postal_code STRING,
# MAGIC     region STRING,
# MAGIC
# MAGIC     error_code STRING NOT NULL,
# MAGIC     error_description STRING NOT NULL,
# MAGIC     error_timestamp TIMESTAMP NOT NULL,
# MAGIC     pipeline_run_id STRING,
# MAGIC     created_at TIMESTAMP NOT NULL,
# MAGIC     batch_id INTEGER,
# MAGIC     source_file_name STRING
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS bronze.product_bronze (
# MAGIC     product_id STRING,
# MAGIC     category STRING,
# MAGIC     sub_category STRING,
# MAGIC     product_name STRING,
# MAGIC     state STRING,
# MAGIC     price_per_product DECIMAL(10,2),
# MAGIC
# MAGIC     -- Audit columns
# MAGIC     ingestion_timestamp TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS silver.product_silver (
# MAGIC     product_id STRING,
# MAGIC     category STRING,
# MAGIC     sub_category STRING,
# MAGIC     product_name STRING,
# MAGIC     state STRING,
# MAGIC     price_per_product DECIMAL(10,2),
# MAGIC
# MAGIC     -- Change detection
# MAGIC     record_hash STRING,
# MAGIC
# MAGIC     -- SCD Type 2 columns
# MAGIC     effective_start_date TIMESTAMP,
# MAGIC     effective_end_date TIMESTAMP,
# MAGIC     is_current BOOLEAN,
# MAGIC
# MAGIC     -- Audit columns
# MAGIC     created_date TIMESTAMP,
# MAGIC     updated_date TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS error.product_bronze_error (
# MAGIC     product_id STRING,
# MAGIC     category STRING,
# MAGIC     sub_category STRING,
# MAGIC     product_name STRING,
# MAGIC     state STRING,
# MAGIC     price_per_product DECIMAL(10,2),
# MAGIC
# MAGIC     error_code STRING,
# MAGIC     error_description STRING,
# MAGIC
# MAGIC     ingestion_timestamp TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS error.product_silver_error (
# MAGIC     product_id STRING,
# MAGIC     category STRING,
# MAGIC     sub_category STRING,
# MAGIC     product_name STRING,
# MAGIC     state STRING,
# MAGIC     price_per_product DECIMAL(10,2),
# MAGIC
# MAGIC     error_code STRING,
# MAGIC     error_description STRING,
# MAGIC
# MAGIC     error_timestamp TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS bronze.orders_bronze (
# MAGIC     row_id STRING,
# MAGIC     order_id STRING,
# MAGIC     order_date DATE,
# MAGIC     ship_date DATE,
# MAGIC     ship_mode STRING,
# MAGIC     customer_id STRING,
# MAGIC     product_id STRING,
# MAGIC     quantity INT,
# MAGIC     price DECIMAL(10,2),
# MAGIC     discount DECIMAL(5,2),
# MAGIC     profit DECIMAL(10,2),
# MAGIC
# MAGIC     -- Audit columns
# MAGIC     ingestion_timestamp TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC )
# MAGIC USING DELTA

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS silver.orders_silver (
# MAGIC     row_id STRING,
# MAGIC     order_id STRING,
# MAGIC     order_date DATE,
# MAGIC     ship_date DATE,
# MAGIC     ship_mode STRING,
# MAGIC     customer_id STRING,
# MAGIC     product_id STRING,
# MAGIC     quantity INT,
# MAGIC     price DECIMAL(10,2),
# MAGIC     discount DECIMAL(5,2),
# MAGIC     profit DECIMAL(10,2),
# MAGIC
# MAGIC     -- Change detection
# MAGIC     record_hash STRING,
# MAGIC
# MAGIC     -- SCD Type 2 columns
# MAGIC     effective_start_date TIMESTAMP,
# MAGIC     effective_end_date TIMESTAMP,
# MAGIC     is_current BOOLEAN,
# MAGIC
# MAGIC     -- Audit columns
# MAGIC     created_date TIMESTAMP NOT NULL,
# MAGIC     updated_date TIMESTAMP NOT NULL,
# MAGIC     batch_id INTEGER,
# MAGIC     source_file_name STRING
# MAGIC
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS error.orders_bronze_error (
# MAGIC     row_id STRING,
# MAGIC     order_id STRING,
# MAGIC     order_date DATE,
# MAGIC     ship_date DATE,
# MAGIC     ship_mode STRING,
# MAGIC     customer_id STRING,
# MAGIC     product_id STRING,
# MAGIC     quantity INT,
# MAGIC     price DECIMAL(10,2),
# MAGIC     discount DECIMAL(5,2),
# MAGIC     profit DECIMAL(10,2),
# MAGIC
# MAGIC     error_code STRING NOT NULL,
# MAGIC     error_description STRING NOT NULL,
# MAGIC     error_timestamp TIMESTAMP NOT NULL,
# MAGIC     ingestion_timestamp TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS error.orders_silver_error (
# MAGIC     row_id STRING,
# MAGIC     order_id STRING,
# MAGIC     order_date DATE,
# MAGIC     ship_date DATE,
# MAGIC     ship_mode STRING,
# MAGIC     customer_id STRING,
# MAGIC     product_id STRING,
# MAGIC     quantity INT,
# MAGIC     price DECIMAL(10,2),
# MAGIC     discount DECIMAL(5,2),
# MAGIC     profit DECIMAL(10,2),
# MAGIC
# MAGIC     error_code STRING NOT NULL,
# MAGIC     error_description STRING NOT NULL,
# MAGIC     error_timestamp TIMESTAMP NOT NULL,
# MAGIC     pipeline_run_id STRING,
# MAGIC     created_at TIMESTAMP NOT NULL,
# MAGIC     batch_id INTEGER,
# MAGIC     source_file_name STRING
# MAGIC
# MAGIC )
# MAGIC USING DELTA
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG ecommerce;
# MAGIC USE SCHEMA gold

# COMMAND ----------

# MAGIC %sql DROP TABLE IF EXISTS gold.gold_sales_summary

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists gold.gold_sales_summary

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS gold.gold_sales_summary (
# MAGIC
# MAGIC     year INT,
# MAGIC     product_category STRING,
# MAGIC     product_sub_category STRING,
# MAGIC     customer STRING,
# MAGIC     transaction_amount DECIMAL(12,2),
# MAGIC
# MAGIC     -- Audit Columns
# MAGIC     created_at TIMESTAMP,
# MAGIC     updated_at TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC
# MAGIC )
# MAGIC USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS gold.gold_sales_summary (
# MAGIC
# MAGIC     year INT,
# MAGIC     product_category STRING,
# MAGIC     product_sub_category STRING,
# MAGIC     customer STRING,
# MAGIC     transaction_amount DECIMAL(12,2),
# MAGIC
# MAGIC     -- Audit Columns
# MAGIC     created_at TIMESTAMP,
# MAGIC     updated_at TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC )
# MAGIC USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS gold_sales_summary_error (
# MAGIC
# MAGIC     year INT,
# MAGIC     product_category STRING,
# MAGIC     product_sub_category STRING,
# MAGIC     customer STRING,
# MAGIC     transaction_amount STRING,
# MAGIC
# MAGIC     error_code STRING,
# MAGIC     error_description STRING,
# MAGIC
# MAGIC     error_record_timestamp TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     batch_id INTEGER
# MAGIC     )
# MAGIC USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG ecommerce;
# MAGIC USE SCHEMA silver;

# COMMAND ----------

# MAGIC %sql DROP TABLE IF EXISTS  batch_table

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS batch_table (
# MAGIC     batch_id INT,
# MAGIC     batch_start_date TIMESTAMP,
# MAGIC     batch_end_date TIMESTAMP,
# MAGIC     source_file_name STRING,
# MAGIC     record_count INT,
# MAGIC     source_schema STRING,
# MAGIC     source_table STRING,
# MAGIC     target_schema STRING,
# MAGIC     target_table STRING,
# MAGIC     batch_status STRING,
# MAGIC     created_date TIMESTAMP,
# MAGIC     updated_date TIMESTAMP
# MAGIC )
# MAGIC USING DELTA;