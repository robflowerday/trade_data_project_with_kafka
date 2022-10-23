# trade_data_project_with_kafka

This repository aims to solve the same tasks as my
https://github.com/robflowerday/trade_data_project_with_kafka
repository, for details of the main task please see
the above repositories README.md file.

I have extended my code to show how kafka could be
introduced into the system. Without a suitable API, I
have randomised the times and values of data entries
into the trades table. In order to create this data, I
have created some custom functions to manipulate
timestamps. As this is not code that would be put into
production I have not ensured these functions are correct
in the sense that they do not handle leap years, or the
month of Feburary correctly on regular years. That said,
I have included unittests for these functions which help
to ensure their basic functionality works to a sufficient
level to allow the code to run.

This program will not populate all dates, it only deals
with the first 300000 seconds and as such after 3 and a
half days, when the select query specified in task 2 is
used, None values will be returned.

To run the program perform the following:
- Ensure Docker and Docker Compose are installed.
- git clone https://github.com/robflowerday/trade_data_project_with_kafka.git
- cd trade_data_project
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- docker-compose up -d
- Create the database and tables
  - python create_tables.py
- Start the kafka consumers
  - python db_valuedata_consumer.py
  - python db_trades_consumer
- Start the kafka producers
  - python trades_producer.py
  - python value_data_producer.py
- When you wish to see results of the query specified
  in task 2, run:
  - python select_from_table.py

As the data we are using is unrealistic and sometimes
produced out of order (with the trades data potentially
being created before the value data), the results may
not be entirely appropriate. This was intended as a
proof of concept rather than code suitable for production.
