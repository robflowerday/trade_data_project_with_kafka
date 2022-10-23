import json
from random import randint, random, choice

from kafka import KafkaProducer

from timestamp_utils import get_date_from_timestamp, incremented_timestamp


def get_random_instrument_id():
    instrument_id_list = [
        "b2h34jbv5k2j3h4v5uo23y4vg52uk3jy4v5k23",
        "5oui26bo425iy6v24uoy62v45ou",
        "5b2345hbv63kj4hv63jkgcv6k3hyc56k3h4g5",
        "45huv623u457v23j4h7v34l56bl345",
        "n45li63hb457liy2hbv45lkhb24kb6",
    ]
    return choice(instrument_id_list)


if __name__ == "__main__":

    producer = KafkaProducer(bootstrap_servers="localhost:29092")

    timestamp = "2012-01-01 00:00:00 UTC"

    for i in range(100000):

        payload = {
            "tradedate": get_date_from_timestamp(timestamp),
            "event_timestamp": timestamp,
            "instrument_id": get_random_instrument_id(),
        }

        producer.send(
            topic="trades",
            value=json.dumps(payload).encode("utf-8"),
        )

        num_seconds = round(random() * 100, 4)
        timestamp = incremented_timestamp(timestamp, num_seconds)
