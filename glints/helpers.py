import collections
from datetime import datetime

days = ["Mon","Tues","Weds","Thurs","Fri","Sat","Sun"]

weekdays = {"Mon":1,"Tues":2,"Weds":3,"Thurs":4,"Fri":5,"Sat":6,"Sun":7}

def get_time(time_string):
    time_list = time_string.split('-')
    new_time_list = []
    for x in time_list:
        try:
            in_time = datetime.strptime(x, "%I:%M%p")
            out_time = datetime.strftime(in_time, "%H:%M")
        except:
            in_time = datetime.strptime(x, "%I%p")
            out_time = datetime.strftime(in_time, "%H:%M")
        new_time_list.append(out_time)
    return new_time_list


def get_time_list(time_string):
    # get 24hr format list from : "2:30pm-8pm"
    time_list = time_string.split('-')
    new_time_list = []
    for x in time_list:
        try:
            in_time = datetime.strptime(x, "%I:%M%p")
            out_time = datetime.strftime(in_time, "%H:%M")
        except:
            in_time = datetime.strptime(x, "%I%p")
            out_time = datetime.strftime(in_time, "%H:%M")
        new_time_list.append(out_time)
    return new_time_list


def get_day_time_dict(string):
  # get_date_time from a str like : "Mon, Thurs, Fri, 2:30 pm - 8 pm"
  sentence = string
  new_sen = sentence.replace(" ", "")
  temp = new_sen.split(',')
  for day in days:
    if day in temp[-1]:
      abc = temp[-1].split(day)
      time_string = abc[-1]
      time_list = get_time_list(time_string)
      temp.pop()
      temp.append(f"{day}")
      day_time_dict = dict.fromkeys(temp, time_list)
      break
  return day_time_dict


def get_schedule(string):
    full_day_time_list = string.split('/')
    super_dict = dict()
    for daytime_str in full_day_time_list:
        day_time_dict = get_day_time_dict(daytime_str)
        for k, v in day_time_dict.items():
            super_dict[k] = v
    return super_dict