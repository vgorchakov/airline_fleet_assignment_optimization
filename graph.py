import pandas as pd
import datetime


class BuildGraph():
    def __init__(self, flights_info_dict):
        self.flight_info_dict = flights_info_dict
        # nodes of the graph
        self.flight_list = list(flights_info_dict.keys())
        # edges of the graph
        self.flight_pairs_dict = BuildGraph.build_feasible_flight_pairs(self.flight_info_dict)
        self.incoming_nodes, self.outgoing_nodes = BuildGraph.build_incoming_outgoing_edges(self.flight_list,
                                                                                            self.flight_pairs_dict)

    @staticmethod
    def build_feasible_flight_pairs(flight_info_dict, min_time=3600):
        """
        Build dictionary with keys as feasible pairs of flights and values as timedelta between flights of each pair
        """
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

    @staticmethod
    def build_incoming_outgoing_edges(flight_list, flight_pairs_dict):
        """
        For each flight build incoming and outgoing edges and return lists of corresponding nodes
        """
        incoming_nodes = {flight: [] for flight in flight_list}
        outgoing_nodes = {flight: [] for flight in flight_list}
        for f1, f2 in flight_pairs_dict.keys():
            incoming_nodes[f2].append(f1)
            outgoing_nodes[f1].append(f2)
        return incoming_nodes, outgoing_nodes
