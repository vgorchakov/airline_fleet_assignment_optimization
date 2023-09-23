import pyomo.environ as pe


class SetsBuilder():
    def __init__(self, m, flight_list, flight_pairs_dict):
        self.m = m
        self.flight_list = flight_list
        self.flight_pairs_dict = flight_pairs_dict
        self.build_all_sets()

    def build_all_sets(self):
        self.build_all_flights_nodes_set()
        self.build_all_flights_pairs_edges_set()

    def build_all_flights_nodes_set(self):
        self.m.flights_nodes_set = pe.Set(initialize=self.flight_list, dimen=1)

    def build_all_flights_pairs_edges_set(self):
        self.m.flights_edges_set = pe.Set(initialize=list(self.flight_pairs_dict.keys()), dimen=2)