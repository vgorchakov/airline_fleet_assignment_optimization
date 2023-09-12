import pyomo.environ as pe

class ObjectiveBuilder():
    def __init__(self, m):
        self.build_objective(m)

    def build_obj_rule(self, m):
        return pe.summation(m.is_source_flight_var)

    def build_objective(self, m):
        m.OBJ = pe.Objective(rule=self.build_obj_rule)

