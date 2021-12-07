import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please choose the name of the city to analyze.\nHint: Must be chicago, new york city or washington: ').lower()
        if city in CITY_DATA:
            break


    # get user input for month (all, january, february, ... , june)
    month = input('Please choose the month to analyze.\nHint: Must be "all" or between january to june: ').lower()
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please choose the day of the week to analyze.\nHint: Must be "all" or between monday to sunday: ').lower()
            

    print('-'*40)
    return city, month, day


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
    #loading the city data
    df = pd.read_csv(CITY_DATA[city])

    #converting the 'Start Time' column in CITY_DATA to 'Date_Time'
    df['Start_Time'] = pd.to_datetime(df['Start Time'])


    #creating month, week_day and hour column
    df["month"] = df["Start_Time"].dt.month_name().str.lower()
    df["week_day"] = df["Start_Time"].dt.day_name().str.lower()
    df["hour"] = df["Start_Time"].dt.hour


    #filtering the month to analyse
    if month != 'all':
        df = df.loc[df["month"] == month]


    #filtering the week_day to analyse
    if day != 'all':
        df = df.loc[df["week_day"] == day]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df["month"].mode()[0]
    print('Most Popular Travel Month: ' + str(popular_month))

    # display the most common day of week
    popular_day = df["week_day"].mode()[0]
    print('Most Popular Travel Week Day: ' + str(popular_day))

    # display the most common start hour
    popular_hour = df["hour"].mode()[0]
    print('Most Popular Travel Hour: ' + str(popular_hour))

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ' + str(popular_start_station))


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: ' + str(popular_end_station))

    # display most frequent combination of start station and end station trip
    df['combine_station'] = df['Start Station'] + df['End Station']
    frequent_station = df['combine_station'].mode()[0]
    print('Most Popular Start and End Station: ' + str(frequent_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Number of Trip Duration: ' + str(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Total Mean of Trip Duration: ' + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    subscribers = df['User Type'].count()
    print('Total Number of Customers: ' + str(subscribers))

    #Display counts of gender
    # The try statement is for the washington city not to output error since it doesn't have Gender Column
    try:
        gender_count = df['Gender'].count()
        print('Total Number Of Genders: ' + str(gender_count))
    except:
        print("Sorry, there's no data for 'Gender' in washington city")

    # Display earliest, most recent, and most common year of birth
    # The try statement is for the washington city not to output error since it doesn't have Birth Year Column
    try:
        recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year: ' + str(recent_birth_year))

        earliest_birth_year = df['Birth Year'].min()
        print('The Earliest Birth Year: ' + str(earliest_birth_year))

        popular_birth_year = df['Birth Year'].mode()[0]
        print('The Most Popular Birth Year: ' + str(popular_birth_year))
    except:
        print("Sorry, we have no data for 'Birth Year' in washington city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Display of raw data upon request by the users
    raw_data = input('Would you like to see the 5 rows of each city raw data? Enter \'Yes\' or \'No\': ').lower()
    start = 0
    end = 5
    while raw_data == 'yes':
        print(df.iloc[start:end])
        start += 5
        end += 5
        raw_data = input('Would you like to see more data? Enter \'Yes\' or \'No\': ').lower()
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
