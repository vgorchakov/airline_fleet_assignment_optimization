import pandas as pd
import datetime


class BuildGraph():
    def __init__(self, flights_info_dict):
        self.flight_info_dict = flights_info_dict
        # nodes of the graph
        self.flight_list = flights_info_dict.keys()
        # edges of the graph
        self.flight_pairs = BuildGraph.prepare_feasible_flight_pairs(self.flight_info_dict)

    @staticmethod
    def prepare_feasible_flight_pairs(flight_info_dict, min_time=3600):
        # TODO: move min_time to config
        # check that there is enough time between two flights to be consecutive
        flight_gap_time = lambda pair: flight_info_dict[pair[1]]["departure_time"] - flight_info_dict[pair[0]]["arrival_time"]
        # check that the flight_one arrival airport = flight_two departure airport
        check_same_airport = lambda pair: flight_info_dict[pair[1]]["airport_from"] == flight_info_dict[pair[0]]["airport_to"]

        pairs = filter(
            lambda pair: (flight_gap_time(pair) >= min_time) and (check_same_airport(pair)),
            [(flight_i, flight_j) for flight_i in flight_info_dict.keys()
             for flight_j in flight_info_dict.keys() if flight_i != flight_j]
        )
        return {pair: flight_gap_time(pair) for pair in pairs}