#TODO: import all necessary packages and functions

import time
import datetime
import re
from collections import Counter
from colorama import Fore

#Filenames

chicago = 'chicago.csv'
new_york = 'new_york_city.csv'
washington = 'washington.csv'

month_list = ("January", "February", "March", "April", "May", "June")
day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago(use input: chicago), New York(use input: new_york),'
                 ' or Washington(use input: washington)?\n')

    return city.lower()
    # TODO: handle raw input and complete function


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    # TODO: handle raw input and complete function

    time_period = input('\nWould you like to filter the data by month name '
                        '("January", "February", "March", "April", "May", "June"), by day name'
                        '("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"), or not at'
                        ' all? Type "none" for no time filter.\n')

    if (time_period == "none") or (time_period.title() in month_list) or (time_period.title() in day_list):
        return time_period.title()
    else:
        print("Please check the input!")


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')

    if month.title() != "January" or "February" or "March" or "April" or "May" or "June":
        print("Pl check the month name")
    else:
        return month.title()

    # TODO: handle raw input and complete function


# originally month parameter is passed to get_day function
def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')

    if day.title() != "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday" or "Saturday" or 'Sunday':
        print("Please check the day name")
    else:
        return day.title()
    # TODO: handle raw input and complete function


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?

    Args:
        "city_file" is to fetch csv data of city by passing city name chicago, new_york or washington
        "time_duration" is a parameter to filter the csv data for a given month or day; it is expected to use the function
         with "none" time_duration, but logic is in place to use other filters as well.
    Returns:
        the function prints most popular month for the given time period.
    '''
    # TODO: complete function

    filtered_list_popular_month = time_period_filtered_list(city_file, time_period)

    start_time_pattern_1 = r"^\d+\-01\-\d+"
    start_time_pattern_2 = r"^\d+\-02\-\d+"
    start_time_pattern_3 = r"^\d+\-03\-\d+"
    start_time_pattern_4 = r"^\d+\-04\-\d+"
    start_time_pattern_5 = r"^\d+\-05\-\d+"
    start_time_pattern_6 = r"^\d+\-06\-\d+"

    count1, count2, count3, count4, count5, count6 = 0, 0, 0, 0, 0, 0

    for line in filtered_list_popular_month:
        if re.findall(start_time_pattern_1, line): count1 += 1
        elif re.findall(start_time_pattern_2, line): count2 += 1
        elif re.findall(start_time_pattern_3, line): count3 += 1
        elif re.findall(start_time_pattern_4, line): count4 += 1
        elif re.findall(start_time_pattern_5, line): count5 += 1
        elif re.findall(start_time_pattern_6, line): count6 += 1

    stats = [count1, count2, count3, count4, count5, count6]
    position = stats.index(max(stats)) + 1

    print(Fore.BLUE + "Most Popular Month: Maximum Start_Time Instances in time period filter"
                      " {}are in month {}, {} times".format(time_period, month_list[position-1], max(stats)))


def time_period_filtered_list(city_file, time_period):
    filtered_list = list()
    try:
        city_data = list(open(globals()[city_file], "r"))

        if time_period in month_list:
            search_pattern = re.compile("^\d+-0" + str(month_list.index(time_period) + 1) + "-\d+")
            for line in city_data[1:]:
                if re.findall(search_pattern, line):
                    filtered_list.append(line)
        elif time_period in day_list:
            start_time_pattern = r"^\d+\-\d+\-\d+"
            for line in city_data[1:]:
                start_time = re.findall(start_time_pattern, line)
                if day_list[datetime.datetime.strptime(start_time[0], "%Y-%m-%d").weekday()] == time_period:
                    filtered_list.append(line)
        elif time_period == "none":
            filtered_list = city_data[1:]
        else:
            print("time_period criteria not satisfied...")
    except IOError:
        print("please check the file path")
    return filtered_list


def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
     Args:
        "city_file" is to fetch csv data of city by passing city name chicago, new_york or washington
        "time_duration" is a parameter to filter the csv data for a given month or day.
    Returns:
        the function prints most popular day for the given time period.
    '''
    # TODO: complete function

    filtered_list_popular_day = time_period_filtered_list(city_file, time_period)

    count1, count2, count3, count4, count5, count6, count7 = 0, 0, 0, 0, 0, 0, 0

    for line in filtered_list_popular_day:
        start_time = line.split(",")[0].split()[0]
        try:
            if day_list[datetime.datetime.strptime(start_time, "%Y-%m-%d").weekday()] == "Monday": count1 += 1
            elif day_list[datetime.datetime.strptime(start_time, "%Y-%m-%d").weekday()] == "Tuesday": count2 += 1
            elif day_list[datetime.datetime.strptime(start_time, "%Y-%m-%d").weekday()] == "Wednesday": count3 += 1
            elif day_list[datetime.datetime.strptime(start_time, "%Y-%m-%d").weekday()] == "Thursday": count4 += 1
            elif day_list[datetime.datetime.strptime(start_time, "%Y-%m-%d").weekday()] == "Friday": count5 += 1
            elif day_list[datetime.datetime.strptime(start_time, "%Y-%m-%d").weekday()] == "Saturday": count6 += 1
            elif day_list[datetime.datetime.strptime(start_time, "%Y-%m-%d").weekday()] == "Sunday": count7 += 1
        except ValueError:
            continue
    count_stats = [count1, count2, count3, count4, count5, count6, count7]

    day_name = day_list[count_stats.index(max(count_stats))]

    print(Fore.CYAN + "Most Popular Day: Maximum Start_Time Instances are on {} with {} count".
          format(day_name, max(count_stats)))


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
     Args:
        "city_file" is to fetch csv data of city by passing city name chicago, new_york or washington
        "time_duration" is a parameter to filter the csv data for a given month or day.
    Returns:
        the function prints most popular hour for the given time period.
    '''
    # TODO: complete function

    time_list = list()
    filtered_list_popular_hour = time_period_filtered_list(city_file, time_period)
    for line in filtered_list_popular_hour:
        start_time_pattern = r"\s\d+\:\d+\:\d+"
        start_time_find = re.findall(start_time_pattern, line)
        time_list.append((start_time_find[0].strip()).split(":")[0])

    start_time_popularity = Counter(time_list)

    print(Fore.GREEN + "Most popular start time Hour is: {} Hrs, used {} times".
          format(start_time_popularity.most_common()[0][0], start_time_popularity.most_common()[0][1]))


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?

     Args:
        "city_file" is to fetch csv data of city by passing city name chicago, new_york or washington
        "time_duration" is a parameter to filter the csv data for a given month or day.
    Returns:
        the function prints total and average trip duration for the given time period.
    '''
    # TODO: complete function

    filtered_list_trip_duration = time_period_filtered_list(city_file, time_period)

    trip_duration_sum = 0
    date_format = "%Y-%m-%d %H:%M:%S"

    for line in filtered_list_trip_duration:
        start_time_string = line.split(",")[0]
        end_time_string = line.split(",")[1]
        start_time_datetime = datetime.datetime.strptime(start_time_string, date_format)
        end_time_datetime = datetime.datetime.strptime(end_time_string, date_format)
        one_trip_duration = end_time_datetime - start_time_datetime
        trip_duration_sum += one_trip_duration.seconds

    trip_duration_avg = trip_duration_sum / (len(filtered_list_trip_duration) - 1)

    d, h, m, s = seconds_to_readable_time(trip_duration_sum)
    trip_duration_sum_detailed = "%d days %d hours %02d minutes %02d seconds" % (d, h, m, s)
    d, h, m, s = seconds_to_readable_time(trip_duration_avg)
    trip_duration_avg_detailed = "%d days %d hours %02d minutes %02d seconds" % (d, h, m, s)

    print(Fore.LIGHTRED_EX + "Total trip duration is: {} and Average trip duration is {} ".
          format(trip_duration_sum_detailed, trip_duration_avg_detailed))


def seconds_to_readable_time(trip_duration_sum):
    m, s = divmod(trip_duration_sum, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return d, h, m, s


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
     Args:
        "city_file" is to fetch csv data of city by passing city name chicago, new_york or washington
        "time_duration" is a parameter to filter the csv data for a given month or day.
    Returns:
        the function prints most popular start and end stations for the given time period.
    '''
    # TODO: complete function

    filtered_list_popular_stations = time_period_filtered_list(city_file, time_period)

    start_station_list = list()
    end_station_list = list()

    for line in filtered_list_popular_stations:
        start_station = line.split(",")[3]
        start_station_list.append(start_station)
        end_station = line.split(",")[4]
        end_station_list.append(end_station)

    start_station_popularity = Counter(start_station_list)
    end_station_popularity = Counter(end_station_list)

    print(Fore.LIGHTYELLOW_EX + "Most popular start and end stations are: {} with {} times usage and"
                                " {} with {} times usage".
          format(start_station_popularity.most_common()[0][0], start_station_popularity.most_common()[0][1],
                 end_station_popularity.most_common()[0][0], end_station_popularity.most_common()[0][1]))


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
     Args:
        "city_file" is to fetch csv data of city by passing city name chicago, new_york or washington
        "time_duration" is a parameter to filter the csv data for a given month or day.
    Returns:
        the function prints most popular trip(pair of start and end station) for the given time period.

    '''
    # TODO: complete function

    filtered_list_popular_stations = time_period_filtered_list(city_file, time_period)

    start_station_list = list()
    end_station_list = list()

    for line in filtered_list_popular_stations:
        start_station = line.split(",")[3]
        end_station = line.split(",")[4]
        start_station_list.append(start_station)
        end_station_list.append(end_station)

    trip_list = zip(start_station_list, end_station_list)
    trip_popularity = Counter(trip_list)

    print(Fore.BLUE + "Most popular trip is between stations: {} and {}, used {} times".
          format(trip_popularity.most_common()[0][0][0], trip_popularity.most_common()[0][0][1],
                 trip_popularity.most_common()[0][1]))


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?

     Args:
        "city_file" is to fetch csv data of city by passing city name chicago, new_york or washington
        "time_duration" is a parameter to filter the csv data for a given month or day.
    Returns:
        the function prints different users with their count

    '''
    # TODO: complete function

    filtered_list_users = time_period_filtered_list(city_file, time_period)

    user_type_list = list()

    for line in filtered_list_users:
        user_type = line.split(",")[5]
        user_type_list.append(user_type)

    user_type_counts = Counter(user_type_list)

    print(Fore.CYAN + "{} Users are: {} and {} Users are: {}"
          .format(user_type_counts.most_common()[0][0],
                  user_type_counts.most_common()[0][1], user_type_counts.most_common()[1][0],
                  user_type_counts.most_common()[1][1]))


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
     Args:
        "city_file" is to fetch csv data of city by passing city name chicago, new_york or washington
        "time_duration" is a parameter to filter the csv data for a given month or day.
    Returns:
        the function prints genders of users with count
    '''
    # TODO: complete function
    filtered_list_gender = time_period_filtered_list(city_file, time_period)

    user_gender_list = list()

    for line in filtered_list_gender:
        user_gender = line.split(",")[6]
        user_gender_list.append(user_gender)
    user_gender_counts = Counter(user_gender_list)

    print(Fore.LIGHTRED_EX + "{} Users are: {} and {} Users are: {}"
          .format(user_gender_counts.most_common()[0][0],
                  user_gender_counts.most_common()[0][1], user_gender_counts.most_common()[2][0],
                  user_gender_counts.most_common()[2][1]))


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?

     Args:
        "city_file" is to fetch csv data of city by passing city name chicago, new_york or washington
        "time_duration" is a parameter to filter the csv data for a given month or day.
    Returns:
        the function prints oldest and recent user's birth year and also most popular birth year

    '''
    # TODO: complete function

    filtered_list_birth_years = time_period_filtered_list(city_file, time_period)

    user_birth_year_list = list()
    for line in filtered_list_birth_years:
        try:
            user_birth = float(line.split(",")[7])
        except ValueError:
            continue
        user_birth_year_list.append(user_birth)

    user_birth_counts = Counter(user_birth_year_list)

    min_year = min(user_birth_year_list)
    max_year = max(user_birth_year_list)
    occ_min, occ_max = "", ""
    for year, occ in user_birth_counts.items():
        if year == min_year:
            occ_min = occ
        elif year == max_year:
            occ_max = occ

    print_string = "Most Popular Birth year {} Born Users are: {}" \
                   "\nOldest user birth year is: {} with {} occurrences," \
                   "\nYoungest user birth year is {} with {} occurrences ".\
        format(user_birth_counts.most_common()[0][0], user_birth_counts.most_common()[0][1],
               min_year, occ_min, max_year, occ_max)
    print(Fore.GREEN + print_string)


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        the function print 5 lines with every "yes". exits when entered "no"
    '''
    # TODO: handle raw input and complete function

    city_name = input("Which city data you would like to view? type chicago or new_york_city or washington")
    city_data = list(open(globals()[city_name], "r"))

    x = 1
    y = 6

    while x <= len(city_data):
        display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')

        if display.lower() == "yes":
            for line in city_data[x:y]:
                print(line)
            x = y
            y += 5
        elif display.lower() == "no":
            break


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''

    # Filter by city (Chicago, New York, Washington)
    city_file = get_city()

    # Filter by time period (month, day, none)

    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == "none":
        start_time = time.time()
        #TODO: call popular_month function and print the results
        popular_month(city_file, time_period)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if (time_period == 'none') or (time_period in month_list) or (time_period in day_list):
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        popular_day(city_file, time_period)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_hour(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    gender(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    birth_years(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
    statistics()
