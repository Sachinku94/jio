import os
from dotenv import load_dotenv
import pymysql

load_dotenv()  # Load variables from .env

db_password = os.getenv('DB_PASSWORD')
db_username=os.getenv('DB_USER')
db_host=os.getenv('DB_HOST')
dv_db=os.getenv('DATABASE')
dv_port=int(os.getenv('DB_PORT'))

conn = pymysql.connect(
    host=db_host,
    user=db_username,
    password=db_password,
    database=dv_db,
    port=dv_port
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM development.term_all_leads where mobile='9845985498';")
result=cursor.fetchone()[1]
print(result)
print("MySQL version:", result )
conn.close()

