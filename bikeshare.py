import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv', 
              'washington': 'washington.csv', 'dc': 'washington.csv', 'new york': 'new_york_city.csv', 'nyc': 'new_york_city.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
               
    while True:
        cities = ['chicago', 'new york city', 'nyc', 'new york', 'washington', 'dc'] 
        city = input("Which city would you like to explore: Chicago, New York City, or Washington DC?\n ").lower()
        if city not in cities:
            print('Selection Error, please choose one of the three cities. \n')
            continue
        else: 
            break
                
                # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input('For which month between January to June? or all? \n').lower()       
        if month not in months:
            print('Selection Error, please choose one of the six months or all. \n')
            continue
        else:
            break
                        

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

       
    while True:
        day_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input('For which day of the week? or all?\n').lower()
        if day not in day_of_week:
            print('Selection Error, please choose one seven days or all. \n')
            continue  
        else:
            print('Thank you! please wait while we process the data! \n')
            break   
      
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("\nWould you like to see first 5 rows of data? Please enter 'yes or 'no'\n ") # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("\nWould you like to see the next 5 rows of data? Please enter 'yes' or 'no'\n").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()  
            
            
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_dayofweek = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', popular_dayofweek)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_starts = df['Start Station'].mode()[0]
    print('Most Common Start Station:', popular_starts)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most Common End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most Frequent Combination:', combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = sum(df['Trip Duration']) 
    print('Total Travel time:', round(total_travel, 1))
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean Travel time:', round(mean_travel, 1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # TO DO: Display counts of user types
        user_type_ct = df['User Type'].value_counts()
        print('User Types:\n', user_type_ct)
        
        # TO DO: Display counts of gender
        gender_ct = df['Gender'].value_counts()
        print('Gender:\n', gender_ct)
        

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        print('Earlist year of birth:\n', int(earliest))
        most_recent = df['Birth Year'].max()
        print('Most recent year of birth:\n', int(most_recent))
        most_common = df['Birth Year'].value_counts().idxmax()
        print('Most common year of birth:\n', int(most_common))
    except KeyError:
        print('No data available for this city')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
