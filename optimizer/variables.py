import pyomo.environ as pe

class VariablesBuilder:
    def __init__(self, m):
        self.m = m
        self.build_all_variables()

    def build_all_variables(self):
        self.build_is_flight_pair_chosen_var()
        self.build_is_source_flight_var()
        self.build_is_sink_flight_var()

    def build_is_flight_pair_chosen_var(self):
        self.m.is_flight_pair_chosen_var = pe.Var(self.m.flights_edges_set, domain=pe.Boolean, initialize=0)

    def build_is_source_flight_var(self):
        """
        Boolean variable. Equal to 1, if unassigned fleet starts schedule from this flight
        """
        self.m.is_source_flight_var = pe.Var(self.m.flights_nodes_set, domain=pe.Boolean, initialize=0)

    def build_is_sink_flight_var(self):
        """
        Boolean variable. Equal to 1, if unassigned fleet finish schedule from this flight
        """
        self.m.is_sink_flight_var = pe.Var(self.m.flights_nodes_set, domain=pe.Boolean, initialize=0)