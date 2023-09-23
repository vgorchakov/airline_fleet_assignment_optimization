import pyomo.environ as pe

class ConstraintsBuilder():
    def __init__(self, m, incoming_nodes, outgoing_nodes):
        self.m = m
        self.build_all_constraints(incoming_nodes, outgoing_nodes)

    def build_all_constraints(self, incoming_nodes, outgoing_nodes):
        self.build_one_incoming_edge_constr(incoming_nodes)
        self.build_one_outgoing_edge_constr(outgoing_nodes)

    def build_one_incoming_edge_constr(self, incoming_nodes):
        """
        Each flight is either source flight (first flight of schedule) or has a incoming node (previous flight)
        """
        def _one_incoming_edge_rule(m, f):
            return (m.is_source_flight_var[f] + sum(m.is_flight_pair_chosen_var[(f1, f)] for f1 in incoming_nodes[f])) == 1
        self.m.one_incoming_edge_constr = pe.Constraint(self.m.flights_nodes_set, rule=_one_incoming_edge_rule)


    def build_one_outgoing_edge_constr(self, outgoing_nodes):
        """
        Each flight is either sink flight (last flight of schedule) or has a outgoing node (next flight)
        """
        def _one_outgoing_edge_rule(m, f):
            return (m.is_source_flight_var[f] + sum(m.is_flight_pair_chosen_var[(f, f1)] for f1 in outgoing_nodes[f])) == 1
        self.m.one_outgoing_edge_constr = pe.Constraint(self.m.flights_nodes_set, rule=_one_outgoing_edge_rule)