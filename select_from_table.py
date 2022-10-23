from psycopg2 import connect

from sql_queries import output_query


if __name__ == "__main__":

    connection = connect(
        dbname="postgres",
        user="postgres",
        password="password",
        port=5431,
        host="localhost",
    )

    with connection.cursor() as cursor:

        cursor.execute(output_query)
        result = cursor.fetchall()

        print(result)
