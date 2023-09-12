import pyomo.environ as pe

class SetsBuilder():
    def __init__(self, m, flight_list, flight_pairs_dict):
        self.m = m
        self.flight_list = flight_list
        self.flight_pairs = flight_pairs_dict
        self.build_all_sets(flight_list, flight_pairs_dict)

    def build_all_sets(self, flight_list, flight_pairs_dict):
        self.build_all_flights_nodes_set(self.m, flight_list)
        self.build_all_flights_pairs_edges_set(self.m, flight_pairs_dict)

    @staticmethod
    def build_all_flights_nodes_set(m, flight_list):
        m.flights_nodes_set = pe.Set(initialize=flight_list, dimen=1)

    @staticmethod
    def build_all_flights_pairs_edges_set(m, flight_pairs_dict):
        m.flights_edges_set = pe.Set(initialize=flight_pairs_dict.keys(), dimen=2)
