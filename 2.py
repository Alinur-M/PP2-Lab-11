import psycopg2
from config import load_config
def call_insert_procedure(first_name, last_name, phone_number):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_data(%s,%s,%s)",(first_name, last_name, phone_number))
                conn.commit()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)

first_name = input("введи имя:")
last_name = input("введи фамилия:")
phone_number = input("введи номер:")




call_insert_procedure(first_name, last_name,phone_number)