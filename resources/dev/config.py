import os

from dotenv import dotenv_values  ## for loading secrets keys

####### Get a dictionary of .env variables ############
conf=dotenv_values()

## Put details in .env file
key = conf.get('key')
iv = conf.get('iv')
salt = conf.get('salt')

#####  AWS Access And Secret key
# Put details in .env file

aws_access_key = conf.get('aws_access_key')
# aws_access_key = "your_encrypted_access_key"
aws_secret_key = conf.get('aws_secret_key')
#aws_secret_key = "your_encrypted_secret_key"


bucket_name = "aws-bucket-ak"
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


#Database credential
# MySQL database connection properties

mySql_password= conf.get('mySql_password')
database_name = "ashish"

url = f"jdbc:mysql://localhost:3306/{database_name}"
properties = {
    "user": "root",
    "password": mySql_password,
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

#Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id","store_id","product_name","sales_date","sales_person_id","price","quantity","total_cost"]


# File Download location
local_directory = "C:\\Users\\Ashish Kumar AK\\PycharmProjects\\local_files\\file_from_s3\\"
customer_data_mart_local_file = "C:\\Users\\Ashish Kumar AK\\PycharmProjects\\local_files\\customer_data_mart\\"
sales_team_data_mart_local_file = "C:\\Users\\Ashish Kumar AK\\PycharmProjects\\local_files\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "C:\\Users\\Ashish Kumar AK\\PycharmProjects\\local_files\\sales_partition_data\\"
error_folder_path_local = "C:\\Users\\Ashish Kumar AK\\PycharmProjects\\local_files\\error_files\\"

