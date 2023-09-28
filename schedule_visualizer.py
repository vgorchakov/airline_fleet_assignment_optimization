import pyomo.environ as pe
import plotly.express as px
import pandas as pd
import datetime
from datetime import timedelta

class VisualizeSchedule():
    def __init__(self, solved_model, flight_info_dict):
        self.solved_model = solved_model
        self.build_schedule_plot(flight_info_dict)

    @staticmethod
    def find_one_fleet_schedule(sourcing_flight, sink_flights, flight_consecutive_pair):
        one_fleet_schedule = [sourcing_flight]
        current_flight = sourcing_flight
        while current_flight not in sink_flights:
            next_flight = flight_consecutive_pair[current_flight]
            one_fleet_schedule += [next_flight]
            current_flight = next_flight
        return one_fleet_schedule

    @staticmethod
    def add_one_fleet_schedule(fleets_schedule_list, one_fleet_schedule, flight_info_dict, fleet_index):
        for flight in one_fleet_schedule:
            flight_dict = flight_info_dict[flight]
            dep_time = datetime.datetime(2016, 3, 15, 00, 00) + timedelta(seconds=flight_dict['departure_time'])
            arr_time = datetime.datetime(2016, 3, 15, 00, 00) + timedelta(seconds=flight_dict['arrival_time'])
            fleets_schedule_list += [dict(Task=f'Fleet_{fleet_index}', Departure=dep_time,
                                          Arrival=arr_time, Flight_index=flight, From=flight_dict['airport_from'],
                                          To=flight_dict['airport_to'])]
        return fleets_schedule_list

    def build_schedule_plot(self, flight_info_dict):
        sourcing_flights = [index for index in self.solved_model.is_source_flight_var
                            if pe.value(self.solved_model.is_source_flight_var[index]) == 1]
        sink_flights = [index for index in self.solved_model.is_sink_flight_var
                        if pe.value(self.solved_model.is_sink_flight_var[index]) == 1]
        flight_consecutive_pair = {}
        for index in self.solved_model.is_flight_pair_chosen_var:
            flight_consecutive_pair[index[0]] = index[1]
        fleets_schedule_list = []
        for fleet_index, sourcing_flight in enumerate(sourcing_flights):
            one_fleet_schedule = VisualizeSchedule.find_one_fleet_schedule(sourcing_flight, sink_flights, flight_consecutive_pair)
            fleets_schedule_list = VisualizeSchedule.add_one_fleet_schedule(fleets_schedule_list, one_fleet_schedule,
                                                                            flight_info_dict, fleet_index)

        fig = px.timeline(pd.DataFrame(fleets_schedule_list), x_start='Departure', x_end='Arrival', y='Task', color='Task',
                          text='Flight_index', hover_data=['From', 'To', 'Departure', 'Arrival'],
                          title='Fleet Schedule Timetable')
        fig.update_traces(textposition='inside')
        fig.update_layout(autosize=False, width=1400, height=9000)
        fig.write_html("plots/fleet_schedule_vizualization.html")

