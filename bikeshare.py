import time
import pandas as pd
import numpy as np
import os


CITY_DATA = {'Chicago': 'chicago.csv',
             'NYC': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def getMonth(argument):
    """
        Defines a dictionary for Month lookup.

        Returns : 
            (str) Name of the month
    """
    month_dict = {
        0: "All",
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_dict.get(argument, "Invalid month")


def getCity(argument):
    """
        Defines a dictionary for City lookup.

        Returns : 
            (str) Name of the city
    """
    city_dict = {
        1: "Chicago",
        2: "NYC",
        3: "Washington"
    }
    return city_dict.get(argument, "Invalid City")


def getDay(argument):
    """
        Defines a dictionary for Day of the week lookup.

        Returns : 
            (str) Name of the day of the week
    """
    city_day = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
        0: "All"
    }
    return city_day.get(argument, "Invalid Day")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city_flag = "y"
    month_flag = "y"
    day_flag = "y"

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Let's make your input easier, and associate numbers with the cities. Enter : ")
    print("1 = Chicago (The Windy City)")
    print("2 = NYC (The Big Apple)")
    print("3 = Washington (Chocolate City)")

    while city_flag == 'y':
        try:
            city_num = int(input("Enter City : "))
            if(city_num > 0 and city_num < 4):
                city = getCity(city_num)
                print()
                print(" >>>>>> You chose to get bike share details for : ",
                      city, "<<<<<<")
                city_flag = "n"
            else:
                print("Wrong Input ! Please try again ..")
        except Exception:
            print("Wrong Input ! Please try again ..")
        finally:
            print('*'*80)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*'*80)
    print("Now lets get your next input ...")
    print('*'*80)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("You chose : ")
    print("CITY = ", city)
    print()

    print("Let's make your input easier, and associate numbers with months. Enter : ")
    print("1 = January, 2 = February, 3 = March, 4 = April, 5 = May, 6 = June")
    print("7 = July, 8 = August, 9 = September, 10 = October, 11 = November, 12 = December")
    print("0 = To get data for all months")

    while month_flag == 'y':
        try:
            month_num = int(input("Enter Month : "))
            if(month_num > 0 and month_num < 13):
                month = getMonth(month_num)
                print()
                print(">>>>>> You chose to get details for : ", month, " <<<<<<")
                month_flag = "n"
            elif (month_num == 0):
                print()
                month = getMonth(month_num)
                print(">>>>>> You chose to get details for all months <<<<<<")
                month_flag = "n"
            else:
                print("Wrong Input ! Please try again ..")
        except Exception:
            print("Wrong Input ! Please try again ..")
        finally:
            print('*'*80)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*'*80)
    print("Now lets get your next input ...")
    print('*'*80)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while day_flag == 'y':
        print("You chose : ")
        print("CITY = ", city)
        print("MONTH = ", month)
        print()
        print("Enter : ")
        print("0 = To get data for all days")
        print("1 = Monday, 2= Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 7 = Sunday")

        try:
            day_num = int(input("Enter Day : "))
            if ((month_num == 0) and (day_num > 0 and day_num < 8)):
                day = getDay(day_num)
                print()
                print(">>>>>> You chose to get details for ",
                      day, " for all the months <<<<<<")
                day_flag = "n"
            elif ((month_num == 0) and (day_num == 0)):
                day = getDay(day_num)
                print()
                print(
                    ">>>>>> You chose to get details for all days for all the months <<<<<<")
                day_flag = "n"
            elif (day_num == 0):
                day = getDay(day_num)
                print()
                print(
                    ">>>>>> You chose to get details for all days for the month of", month, "<<<<<<")
                day_flag = "n"
            elif ((day_num > 0 and day_num < 8)):
                day = getDay(day_num)
                print()
                print(">>>>>> You chose to get details for",
                      day, "for the month of", month, "<<<<<<")
                day_flag = "n"
            else:
                print("Wrong Input ! Please try again ..")
        except Exception:
            print("Wrong Input ! Please try again ..")
        finally:

            print('*'*80)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*'*80)
    return city, month_num, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 0:
        df = df[df['month'] == month]

    if day != "All":
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    try:
        start_time = time.time()

        # TO DO: display the most common month
        common_month = df['month'].mode()[0]
        print("The most common bike sharing month is", getMonth(common_month))

        # TO DO: display the most common day of week
        common_day_of_week = df['day'].mode()[0]
        print("The most common bike sharing day of the week is", common_day_of_week)

        # TO DO: display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        common_hour = df['hour'].mode()[0]
        print("The most common start hour for bike sharing is", common_hour)

        print("\nThis took %s seconds." % (time.time() - start_time))
    except Exception:
        print("Oops ! Something went wrong in calculating time stats.")
        print("Or possibly no data is available.")
    finally:
        print('*'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    try:
        start_time = time.time()

        # TO DO: display most commonly used start station
        common_start_stn = df['Start Station'].mode()[0]
        print("Commonly used Start Station for bikeshare is", common_start_stn)

        # TO DO: display most commonly used end station
        common_end_stn = df['End Station'].mode()[0]
        print("Commonly used End Station for bikeshare is", common_end_stn)

        # TO DO: display most frequent combination of start station and end station trip
        df['combination'] = df['Start Station'] + ' --> ' + df['End Station']
        common_bikeshare_route = df['combination'].mode()[0]
        print("Commonly used Route for bikeshare is", common_bikeshare_route)

        print("\nThis took %s seconds." % (time.time() - start_time))
    except Exception:
        print("Oops ! Something went wrong in calculating station stats.")
        print("Or possibly no data is available.")
    finally:
        print('*'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    try:
        start_time = time.time()

        # TO DO: display total travel time
        total_travel = df['Trip Duration'].sum()
        print("Total travel time in this timeframe is", total_travel)
        print()

        # TO DO: display mean travel time
        mean_travel = df['Trip Duration'].mean()
        print("Mean of the travel time in this timeframe is", mean_travel)
        print()

        print("\nThis took %s seconds." % (time.time() - start_time))
    except Exception:
        print("Oops ! Something went wrong in calculating duration stats.")
        print("Or possibly no data is available.")
    finally:
        print('*'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    try:
        start_time = time.time()

        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print()
        print("The stats for types of users are :")
        print(user_types)

        # TO DO: Display counts of gender
        if 'Gender' in df:
            gender = df['Gender'].value_counts()
            print()
            print("The stats for gender demographics of users are :")
            print(gender)
        else:
            print("No gender data available. Sorry !")

        # TO DO: Display earliest, most recent, and most common year of birth

        if 'Birth Year' in df:
            earliest = df['Birth Year'].min()
            print()
            print("Earliest birth year in the data available :", earliest)
            recent = df['Birth Year'].max()
            print()
            print("Recent birth year in the data available :", recent)
            common_birth = df['Birth Year'].mode()[0]
            print()
            print("Common birth year in the data available :", common_birth)
        else:
            print()
            print("No birth year data available. Sorry !")

        print("\nThis took %s seconds." % (time.time() - start_time))
    except Exception:
        print("Oops ! Something went wrong in calculating time stats.")
        print("Or possibly no data is available.")
    finally:
        print('*'*80)


def raw_data(df):
    """Displays raw data on bikeshare users."""

    start_df = 0
    end_df = 5
    getData = input("Input Yes if you want to see the raw data? : ").lower()

    if getData == 'yes':
        while end_df <= df.shape[0] - 1:

            print(df.iloc[start_df:end_df, :])
            start_df += 5
            end_df += 5

            
            end_display = input("Input Yes to continue : ").lower()
            if end_display != 'yes':
                break
    
    print('*'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print("You chose : ")
        print("CITY = ", city)
        print("MONTH = ", getMonth(month))
        print("DAY OF WEEK = ", day)
        print()

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
