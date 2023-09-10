import pandas as pd
import datetime

class DataPreprocess():
    def __init__(self):
        self.one_day_flights_df = None
        self.preprocess_data()
        self.construct_graph_input()

    def preprocess_data(self):
        flights_data = pd.read_csv('data/azul_airline_flights.csv')
        flights_data['Departure_Date_Day'] = pd.to_datetime(flights_data['Scheduled.Departure']).dt.date
        flights_data['Departure_Date'] = pd.to_datetime(flights_data['Scheduled.Departure']).dt.date
        # take one day with maximum number of flights
        day_max_number_flights = flights_data.groupby('Departure_Date_Day').size().idxmax()
        one_day_flights_df = flights_data[flights_data['Departure_Date'] == day_max_number_flights]
        one_day_flights_df = one_day_flights_df[
            ['Airline', 'Scheduled.Departure', 'Scheduled.Arrival', 'Airport.From', 'Airport.To',
             'Longitude.To', 'Latitude.To', 'Longitude.From', 'Latitude.From']]
        one_day_flights_df = one_day_flights_df.loc[
            one_day_flights_df['Scheduled.Departure'].notna() & one_day_flights_df['Scheduled.Arrival'].notna()]
        one_day_flights_df['Scheduled.Departure'] = pd.to_datetime(one_day_flights_df['Scheduled.Departure'])
        one_day_flights_df['Scheduled.Arrival'] = pd.to_datetime(one_day_flights_df['Scheduled.Arrival'])
        day_max_number_flights = pd.to_datetime(day_max_number_flights)
        one_day_flights_df['departure_time'] = (
                    one_day_flights_df['Scheduled.Departure'] - day_max_number_flights).dt.total_seconds().astype(int)
        one_day_flights_df['arrival_time'] = (
                    one_day_flights_df['Scheduled.Arrival'] - day_max_number_flights).dt.total_seconds().astype(int)
        one_day_flights_df = one_day_flights_df[['Airport.From', 'Airport.To', 'departure_time', 'arrival_time',
                                                 'Longitude.To', 'Latitude.To', 'Longitude.From', 'Latitude.From']]
        one_day_flights_df.to_csv('data/day_flights.csv')
        return one_day_flights_df

    def construct_graph_input(self):
        pass