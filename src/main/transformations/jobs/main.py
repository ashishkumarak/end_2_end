
from resources.dev import config
from src.main.utility.encrypt_decrypt import *
from src.main.utility.s3_client_object import *
from src.main.utility.logging_config import *
from src.main.utility.my_sql_session import *



####################### Get S3 Client ####################

aws_access_key = config.aws_access_key
# aws_access_key = "your_encrypted_access_key"
aws_secret_key = config.aws_secret_key

s3_client_provider = S3ClientProvider(decrypt(aws_access_key), decrypt(aws_secret_key))
s3_client = s3_client_provider.get_client()

# Now you can use s3_client for your S3 operations
response = s3_client.list_buckets()
print(response)
logger.info("List of Buckets: %s", response['Buckets'])

################################ second day -------------------------------------------------

# check if local directory has already a file
# if file is there then check if the same file is present in the staging area
# with status as A. If so then don't delete and try to re-run
# Else give an error and not process the next file

csv_files = [file for file in os.listdir(config.local_directory) if file.endswith(".csv")]
connection = get_mysql_connection()
cursor = connection.cursor()

total_csv_files = []
if csv_files:
    for file in csv_files:
        total_csv_files.append(file)
    statement = f"""
                select distinct file_name from
                ashish.product_staging_table
                where file_name in ({str(total_csv_files)[1:-1]}) and status='I'
               """

    # statement = f"select distinct file_name from " \
    #               {config.db_name}.{config.table_name}  ## give like this in production level
    #             f"youtube_project.product_staging_table " \
    #             f"where file_name in ({str(total_csv_files)[1:-1]}) and status='I' "

    logger.info(f"dynamically statement created: {statement} ")
    cursor.execute(statement)
    data = cursor.fetchall()
    if data:
        logger.info("Your last run was failed please check")
    else:
        logger.info("No record match")

else:
        logger.info("Last run was successful!!!")

########################## third day --------------------------------------------------------



