from psycopg2 import connect

from sql_queries import create_trades_table, create_valuedata_table


if __name__ == "__main__":

    connection = connect(
        dbname="postgres",
        user="postgres",
        password="password",
        port=5431,
        host="localhost",
    )

    with connection.cursor() as cursor:

        cursor.execute(create_trades_table)
        cursor.execute(create_valuedata_table)

        connection.commit()
