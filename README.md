﻿
# Sales Incentive and Coupon Generator System

Welcome to the show.

This endeavor aims to provide you with insights into the functioning of projects within a real-time environment.

The code has been meticulously crafted with careful consideration for various aspects.It not only nurtures your coding skills but also imparts a comprehensive comprehension of project structures.

## Aim

- Give the dynamically coupon code to those customers whose total_sales decreases.
- Give the 1% incentive of total_sales by sales_person per month to the Top performer (sales_person).

## Project Overview
- Production level project
- Encryption and Decryption
- Logging 
- S3 boto3 AWS
- Data mart and ETL concepts
- Spark, Pycharm, MySQL
- You can upgrade this project by using CI/CD pipeline, Airflow
- You can generate data as per your choice ( separately run the .py files present at `src\test` dir)

```plaintext
Project structure:-

end_2_end\
|
|   .env
|   .gitignore
|   README.md
|      
+---.idea
|   |   .gitignore
|   |   end_2_end.iml
|           
+---docs
|       architecture.png
|       database_schema_drawio.png
|       end2end_project_final_op_20240821_132415.mp4
|       
+---resources
|   +---dev
|   |   |   config.py
|   |   |   requirements.txt
|   |           
|   +---sql_scripts
|           table_scripts.sql
|           
+---src
|   +---main
|   |   +---delete
|   |   |   |   local_file_delete.py   
|   |   |           
|   |   +---download
|   |   |   |   aws_file_download.py
|   |   |           
|   |   +---move
|   |   |   |   move_files.py
|   |   |           
|   |   +---read
|   |   |   |   aws_read.py
|   |   |   |   database_read.py
|   |   |           
|   |   +---transformations
|   |   |   \---jobs
|   |   |       |   customer_mart_sql_transform_write.py
|   |   |       |   dimension_tables_join.py
|   |   |       |   main.py
|   |   |       |   sales_mart_sql_transform_write.py
|   |   |               
|   |   +---upload
|   |   |   |   upload_to_s3.py
|   |   |           
|   |   +---utility
|   |   |   |   encrypt_decrypt.py
|   |   |   |   logging_config.py
|   |   |   |   my_sql_session.py
|   |   |   |   s3_client_object.py
|   |   |   |   spark_session.py
|   |   |           
|   |   \---write
|   |       |   database_write.py
|   |       |   parquet_writer.py
|   |               
|   \---test
|       |    extra_column_csv_generated_data.py
|       |    generate_csv_data.py
|       |    less_column_csv_generated_data.py
|       |    sales_data_upload_s3.py
|       |    test.py

```
- If you want the above tree structure of your project then first complete your project then go to the `root` dir of your project and open the Cmd terminal

``` 
tree /f /a > tree.txt
 ```

## Project Architecture
- Here first we download the data in the local machine from the s3 bucket of AWS.
- S3 boto SDK has been used to connect with s3 bucket only access through a programmatic way using Access & Secret keys.
- Spark has been used for transformations to get enriched data.
- Processed data pushed to AWS/SQL using Datamart concepts.
- Doing some analysis on enriched data then store in Sql for reporting tool.

![Architecture](https://github.com/ashishkumarak/end_2_end/blob/3068c0aa1d86748e3ffc7620addd061e2eb08d67/docs/architecture.png)

## Database Entity Relationship (ER) Diagram
Let's understand the data.
- Fact table:- sales table present in s3 bucket.
- Dimension tables:-  customer , store , product and sales team tables.
Doing transformations on fact and dimensions table then we get enriched data.

![(ER) Diagram](https://github.com/ashishkumarak/end_2_end/blob/3068c0aa1d86748e3ffc7620addd061e2eb08d67/docs/database_schema_drawio.png)


## Resources requirement

Let's Start with the requirement to complete the projects:-

1. You should have a laptop with a minimum of 4 GB of RAM, an i3 processor , and above ( Better to have 8GB with an i5 processor ).
2. Local setup of Spark. This is tricky so keep all things intact to work properly and download Java, Python.
3. PyCharm installed in the system.
4. MySQL Server, Shell and Workbench should also be installed to the system and the Mysql connector jar file also used.
5. A GitHub account is good to have but not necessary.
6. You should have AWS account.
7. Understanding of Spark, Sql and Python is required.
8. If you are using Windows OS for Spark then you should have winutils.exe, hadoop.dll file also. You can download it from this GitHub account. [--Click here--](https://github.com/cdarlint/winutils)

#### --What versions did I use in my project ?
 - Pycharm Community Edition 2024.1.5
 - MySQL installer 8.0.39 
 - Mysql connector jar file 9.0.0
 - Spark 3.5.1
 - Python 3.11.9
 - Java 1.8
 - Winutils (hadoop-3.3.6)
 - AWS account

## How to Use the Project

To run the program in Pycharm:-

1. Open the Pycharm editor.
2. Upload or pull the project from GitHub.
3. Open the terminal from the bottom pane.
4. Create a virtual environment in the `root` dir of your project and activate it. Let's say you have venv as a virtual environment then use the command in the terminal for activation

```
 .\venv\Scripts\activate
 ```

5. Now install some packages in your virtual environment using the command in the terminal from the `root` dir

```
pip install -r .\resources\dev\requirements.txt
```
- To see the version of packages installed in your virtual environment then use
```
pip list
```
- In my case , the versions of the packages are :-
```
>pip list
Package                Version
---------------------- -----------
boto3                  1.34.158
botocore               1.34.158
colorama               0.4.6
findspark              2.0.1
jmespath               1.0.1
loguru                 0.7.2
mysql-connector-python 9.0.0
pip                    23.2.1
py4j                   0.10.9.7
pycryptodome           3.20.0
pycryptodomex          3.20.0
pyspark                3.5.1
python-dateutil        2.9.0.post0
python-dotenv          1.0.1
s3transfer             0.10.2
setuptools             68.2.0
six                    1.16.0
urllib3                2.2.2
wheel                  0.41.2
win32-setctime         1.1.0
```

6. You will have to create a user on AWS also and assign s3 full access and provide a secret key and access key to the config file present at `resources\dev\config.py`
- You will need to add the following environment variables to your `.env` file for not exposing your AWS access and secret keys , MySQL password also. In my project, I have used the Encryption and Decryption functions present in the `src\main\utility\encrypt_decrypt.py` file.

`aws_access_key` 

`aws_secret_key` 

`mySql_password` 

For extra safety put the Keys in encrypted form in the `.env` file by using the `encrypt function.`


- In the AWS s3 bucket you should have to create some `dir` in your bucket like
```
customer_data_mart
sales_data_mart
sales_data
sales_data_error
sales_data_processed
```
- First, create some data files so run separately .py files of `src\test` dir and give a local path in each file where you want to save these CSV files.
```
extra_column_csv_generated_data.py
generate_csv_data.py
less_column_csv_generated_data.py
```

- Now your s3 bucket is empty so upload the above CSV files or any other extension files by running the `src\test\sales_data_upload_s3.py` file then your files uploaded to the `sales_data` dir of your s3 bucket.
- Files are downloaded locally in your machine so create some `dir` at any location as you want but give correct paths in the `config.py` file.
```
file_from_s3
customer_data_mart
sales_team_data_mart
sales_partition_data
error_files
```
- So carefully give correct paths in the`resources\dev\config.py` file.

7. Create all tables in your MySQL database, just copy and paste all queries from the`resources\sql_scripts\table_scripts.sql` file.

8. When you have correctly done all things then go to `main.py` present at `src\main\transformations\jobs\main.py`

9. Now it's time to run `main.py` from the green play button on the top right-hand side. If everything works as expected then enjoy, else re-try.

10. If you get stuck in the project then don't hesitate , feel free to ask. 

#### -- Output of my project 
Sample video of my project's result. If video is not playing and bad quality issue then you can download from `docs\end2end_project_final_op_20240821_132415.mp4`

![sample video](https://github.com/user-attachments/assets/a3174cf1-bfb0-4311-8ce8-c8ce30da53ca)


## Results
Doing all analysis on enriched data :-

- Give the dynamically coupon code to those customers whose total_sales decreases.

![customers_data_mart](https://github.com/ashishkumarak/end_2_end/blob/3068c0aa1d86748e3ffc7620addd061e2eb08d67/docs/customers_data_mart.JPG)


- Give the 1% incentive of total_sales by sales_person per month to the Top performer (sales_person).

![sales_team_data_mart](https://github.com/ashishkumarak/end_2_end/blob/3068c0aa1d86748e3ffc7620addd061e2eb08d67/docs/sales_team_data_mart.JPG)


### Thank you

