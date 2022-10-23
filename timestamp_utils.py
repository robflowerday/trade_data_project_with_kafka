def get_date_from_timestamp(timestamp):
    year = timestamp[:4]
    month = timestamp[5:7]
    day = timestamp[8:10]

    return f"{year}{month}{day}"


def get_timestamp(year, month, day, hour, minute, second):
    year = str(year).zfill(4)
    month = str(month).zfill(2)
    day = str(day).zfill(2)
    hour = str(hour).zfill(2)
    minute = str(minute).zfill(2)
    second = str(second).zfill(2)

    timestamp = f"{year}-{month}-{day} {hour}:{minute}:{second} UTC"

    return timestamp


def incremented_timestamp(timestamp, number_of_seconds=1):
    print(timestamp)
    year = int(timestamp[:4])
    month = int(timestamp[5:7])
    day = int(timestamp[8:10])
    hour = int(timestamp[11:13])
    minute = int(timestamp[14:16])
    second = int(timestamp[17:19])

    if len(timestamp) > 25:
        second = float(timestamp[17:25])

    second += number_of_seconds

    while second >= 60:
        second -= 60
        minute += 1

    while minute >= 60:
        minute -= 60
        hour += 1

    while hour >= 24:
        hour -= 24
        day += 1

    while month in [10, 4, 3, 11] and day > 30 or day > 31:
        day -= 24
        month += 1

    while month > 12:
        month -= 12
        year += 1

    if isinstance(second, float):
        second = str(round(second, 5)).zfill(8)
    else:
        second = str(second).zfill(2)

    return get_timestamp(year, month, day, hour, minute, second)
