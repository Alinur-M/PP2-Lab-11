import psycopg2
from config import load_config

def get_paginacia(limit, offset):
    config = load_config()
    sql = """    SELECT c.first_name, c.last_name, p.phone_number
    FROM contacts c
    JOIN phone_numbers p ON c.id = p.contact_id
    ORDER BY c.id
    LIMIT %s OFFSET %s"""
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (limit,offset))
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == "__main__":
    l = input("введите limit")
    off = input("введите offset")
    get_paginacia(l,off)