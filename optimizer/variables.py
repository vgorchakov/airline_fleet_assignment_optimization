import pyomo.environ as pe

class VariablesBuilder:
    def __init__(self, m):
        self.m = VariablesBuilder.build_all_variables(m)

    @staticmethod
    def build_all_variables(m):
        m = VariablesBuilder.build_is_flight_pair_chosen_var(m)
        m = VariablesBuilder.build_is_source_flight_var(m)
        m = VariablesBuilder.build_is_sink_flight_var(m)
        return m

    @staticmethod
    def build_is_flight_pair_chosen_var(m):
        m.is_flight_pair_chosen_var = pe.Var(m.flights_edges_set, domain=pe.Boolean, initialize=0)
        return m

    @staticmethod
    def build_is_source_flight_var(m):
        """
        Boolean variable. Equal to 1, if unassigned fleet starts schedule from this flight
        """
        m.is_source_flight_var = pe.Var(m.flights_nodes_set, domain=pe.Boolean, initialize=0)
        return m

    @staticmethod
    def build_is_sink_flight_var(m):
        """
        Boolean variable. Equal to 1, if unassigned fleet finish schedule from this flight
        """
        m.is_sink_flight_var = pe.Var(m.flights_nodes_set, domain=pe.Boolean, initialize=0)
        return m