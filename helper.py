
import json
from datetime import datetime, timedelta, date
import dateutil.parser as dp


'''
Write data to a json file.
'''
def write_data_to_file(filename,data):
    path = '../results/' + filename
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


'''
Creates epoch start and end timestamps and a timespan in seconds 
for a given number of days.
'''
def days_to_timeformats(start_days, end_days):

    today = get_today_minus_x_day(start_days, string=False)
    end_epoch = iso_to_epoch_timestamp(today)

    days_ago_x = get_today_minus_x_day(int(end_days), string=False)
    start_epoch = iso_to_epoch_timestamp(days_ago_x)

    timespanc_sec = end_epoch - start_epoch

    return end_epoch, start_epoch, timespanc_sec


'''
Returns the current date - x days as string or datetime object
'''
def get_today_minus_x_day(delta, frmt='%Y-%m-%d %H:%M:%S', string=True):
    date = datetime.now() - timedelta(delta)
    if string:
        return date.strftime(frmt)
    return date


'''
Translated a iso timestamp to an epoch timestamp
'''
def iso_to_epoch_timestamp(timestamp):

    #parsed_timestamp = dp.parse(timestamp)
    timestamp_in_seconds = timestamp.timestamp()
    return timestamp_in_seconds