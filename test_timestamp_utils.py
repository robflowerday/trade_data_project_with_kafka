import unittest

from timestamp_utils import (
    get_date_from_timestamp,
    get_timestamp,
    incremented_timestamp,
)


class TestGetDateFromTimestamp(unittest.TestCase):

    def test_get_date_from_when_timestamp(self):

        timestamp = "2022-04-29 00:01:23 UTC"
        calculated_result = get_date_from_timestamp(timestamp)

        expected_result = "20220429"

        self.assertEqual(calculated_result, expected_result)

    def test_get_date_from_event_timestamp(self):

        timestamp = "2022-04-29 00:01:23.123457 UTC"
        calculated_result = get_date_from_timestamp(timestamp)

        expected_result = "20220429"

        self.assertEqual(calculated_result, expected_result)


class TestGetTimestamp(unittest.TestCase):

    def test_get_timestamp(self):

        year = 2022
        month = 11
        day = 5
        hour = 2
        minute = 8
        second = 10

        calculated_result = get_timestamp(
            year,
            month,
            day,
            hour,
            minute,
            second,
        )

        expected_result = "2022-11-05 02:08:10 UTC"

        self.assertEqual(calculated_result, expected_result)


class TestIncrementedTimestamp(unittest.TestCase):

    def test_incremented_when_timestamp_1_second(self):

        initial_timestamp = "2022-11-05 02:08:10 UTC"
        calculated_result = incremented_timestamp(initial_timestamp)
        expected_result = "2022-11-05 02:08:11 UTC"
        self.assertEqual(calculated_result, expected_result)

    def test_incremented_when_timestamp_13_second(self):

        initial_timestamp = "2022-11-05 02:08:10 UTC"
        calculated_result = incremented_timestamp(initial_timestamp, 13)
        expected_result = "2022-11-05 02:08:23 UTC"
        self.assertEqual(calculated_result, expected_result)

    def test_incremented_when_timestamp_1_second_on_day_change(self):

        initial_timestamp = "2022-11-05 23:59:59 UTC"
        calculated_result = incremented_timestamp(initial_timestamp)
        expected_result = "2022-11-06 00:00:00 UTC"
        self.assertEqual(calculated_result, expected_result)

    def test_incremented_event_timestamp_1_second(self):

        initial_timestamp = "2022-11-05 02:08:10.12345 UTC"
        calculated_result = incremented_timestamp(initial_timestamp)
        expected_result = "2022-11-05 02:08:11.12345 UTC"
        self.assertEqual(calculated_result, expected_result)

    def test_incremented_event_timestamp_13_second(self):

        initial_timestamp = "2022-11-05 02:08:10.12345 UTC"
        calculated_result = incremented_timestamp(initial_timestamp, 13)
        expected_result = "2022-11-05 02:08:23.12345 UTC"
        self.assertEqual(expected_result, calculated_result)

    def test_incremented_event_timestamp_1_second_on_day_change(self):

        initial_timestamp = "2022-11-05 23:59:59.12345 UTC"
        calculated_result = incremented_timestamp(initial_timestamp)
        expected_result = "2022-11-06 00:00:00.12345 UTC"
        self.assertEqual(calculated_result, expected_result)
