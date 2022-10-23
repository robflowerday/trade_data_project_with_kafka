import json

from kafka import KafkaConsumer
from psycopg2 import connect

from sql_queries import insert_into_trades


if __name__ == "__main__":

    connection = connect(
        dbname="postgres",
        user="postgres",
        password="password",
        port=5431,
        host="localhost",
    )

    consumer = KafkaConsumer("trades", bootstrap_servers="localhost:29092")

    print("Trades topic consumer, listening...")

    with connection.cursor() as cursor:
        while True:
            for message in consumer:
                trades_row = json.loads(message.value.decode())
                print(trades_row)
                trades_insert_statement = insert_into_trades.format(
                    tradedate=f"'{trades_row['tradedate']}'",
                    event_timestamp=f"'{trades_row['event_timestamp']}'",
                    instrument_id=f"'{trades_row['instrument_id']}'",
                )
                cursor.execute(trades_insert_statement)
                connection.commit()
