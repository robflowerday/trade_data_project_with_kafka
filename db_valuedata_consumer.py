import json

from kafka import KafkaConsumer
from psycopg2 import connect

from sql_queries import insert_into_valuedata


if __name__ == "__main__":

    connection = connect(
        dbname="postgres",
        user="postgres",
        password="password",
        port=5431,
        host="localhost",
    )

    consumer = KafkaConsumer("valuedata", bootstrap_servers="localhost:29092")

    print("Trades topic consumer, listening...")

    with connection.cursor() as cursor:
        while True:
            for message in consumer:
                valuedata_row = json.loads(message.value.decode())
                print(valuedata_row)
                valuedata_insert_statement = insert_into_valuedata.format(
                    tradedate=f"'{valuedata_row['tradedate']}'",
                    instrument_id=f"'{valuedata_row['instrument_id']}'",
                    when_timestamp=f"'{valuedata_row['when_timestamp']}'",
                    gamma=valuedata_row['gamma'],
                    vega=valuedata_row['vega'],
                    theta=valuedata_row['theta'],
                )
                cursor.execute(valuedata_insert_statement)
                connection.commit()
