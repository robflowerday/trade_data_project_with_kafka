import json
from random import random

from kafka import KafkaProducer

from timestamp_utils import get_date_from_timestamp, incremented_timestamp


if __name__ == "__main__":

    producer = KafkaProducer(bootstrap_servers="localhost:29092")

    instrument_id_list = [
        "b2h34jbv5k2j3h4v5uo23y4vg52uk3jy4v5k23",
        "5oui26bo425iy6v24uoy62v45ou",
        "5b2345hbv63kj4hv63jkgcv6k3hyc56k3h4g5",
        "45huv623u457v23j4h7v34l56bl345",
        "n45li63hb457liy2hbv45lkhb24kb6",
    ]

    timestamp = "2012-01-01 00:00:00 UTC"

    for i in range(300000):

        for instrument_id in instrument_id_list:

            payload = {
                    "tradedate": get_date_from_timestamp(timestamp),
                    "instrument_id": instrument_id,
                    "when_timestamp": timestamp,
                    "gamma": random() / 3,
                    "vega": random() * 100 - 50,
                    "theta": random() * 200 - 100,
            }

            producer.send(
                topic="valuedata",
                value=json.dumps(payload).encode("utf-8"),
            )

            timestamp = incremented_timestamp(timestamp)
