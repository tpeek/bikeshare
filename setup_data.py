# coding: utf-8
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import datetime
stations = pd.read_table('stations.tsv')
usage = pd.read_table('usage_2012.tsv')
weather = pd.read_table('daily_weather.tsv')


def change_seasons():
    weather.loc[weather["season_code"] == 1, "season_desc"] = 'Winter'
    weather.loc[weather["season_code"] == 2, "season_desc"] = 'Spring'
    weather.loc[weather["season_code"] == 3, "season_desc"] = 'Summer'
    weather.loc[weather["season_code"] == 4, "season_desc"] = 'Fall'


def convert_dates():
    for i in weather.index:
        weather.ix[i, 'date'] = datetime.datetime.strptime(
            str(weather.ix[i, 'date']), "%Y-%m-%d").date()


def add_months():
    for i in weather.index:
        weather.ix[i, 'month'] = weather.ix[i, 'date'].month

if __name__ == "__main__":
    change_seasons()
    convert_dates()
    add_months()