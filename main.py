
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt






def CleanUpWeather(file_path):
    """
    Get weather data by hours and return weekly data
    :param file_path: CSV file path
    :return: DataFrame of weekly weather in Los Angeles, San Diego and Las Vegas
    """

    # read csv data
    df = pd.read_csv(file_path)
    df = df[['datetime','Los Angeles', 'San Diego', 'Las Vegas']]

    # convert to date feature
    df['datetime'] = pd.to_datetime(df['datetime'])
    # extract years months and weeks from the date features
    df['year']= df['datetime'].dt.year
    df['month']= df['datetime'].dt.month
    df['week_of_year'] = df['datetime'].dt.week
    # take data only between years 2012-2015
    df = df.loc[(df['year'] >= 2012) & (df['year'] <= 2015)]
    # solve a specific case when the last days of one year counts in the 'week_of_year' of the next year
    df.loc[(df['month'] == 12) & (df['week_of_year'] == 1) , 'year'] += 1
    df.drop(columns=['month'], inplace=True )
    # calculate the average temperature of every week
    return df.groupby(['year','week_of_year']).mean()


if __name__ == '__main__':


    # test
    temperature = CleanUpWeather(r'data\weather\temperature.csv')
    print(temperature)
    temperature.to_csv(r'data\weather\temp.csv')


