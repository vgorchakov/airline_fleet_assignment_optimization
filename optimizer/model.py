import pyomo.environ as pe
import pyomo.opt as popt
from pyomo.environ import *
from optimizer.sets import SetsBuilder
from optimizer.variables import VariablesBuilder
from optimizer.constraints import ConstraintsBuilder
from optimizer.objective import ObjectiveBuilder


class ModelBuild:
    def __init__(self, flight_list, flight_pairs_dict, incoming_nodes, outgoing_nodes):
        self.flight_list = flight_list
        self.flight_pairs_dict = flight_pairs_dict
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes
        self.build_model(flight_list, flight_pairs_dict, incoming_nodes, outgoing_nodes)
        self.solved_model = self.solve_model(self.m)
        # store model output
        model_variable_values = {}
        for var in self.solved_model.component_objects(Var, active=True):
            model_variable_values[var.name] = {}
            for index in var:
                if pe.value(var[index]) != 0:
                    model_variable_values[var.name][str(index)] = pe.value(var[index])
        self.solved_model.model_variable_values = model_variable_values

    def build_model(self, flight_list, flight_pairs_dict, incoming_nodes, outgoing_nodes):
        self.m = pe.ConcreteModel()
        SetsBuilder(self.m, flight_list, flight_pairs_dict)
        VariablesBuilder(self.m)
        # ParametersBuilder(self.m)
        ConstraintsBuilder(self.m, incoming_nodes, outgoing_nodes)
        ObjectiveBuilder(self.m)

    @staticmethod
    def solve_model(m):
        # Solve model
        solver = popt.SolverFactory("cbc")
        model_instance = m.create_instance()
        solver.solve(
            model_instance,
            # tee=True,
            # keepfiles=True,
            # logfile="model_logfile",
            # report_timing=True,
            # symbolic_solver_labels=True
        )
        return model_instance

