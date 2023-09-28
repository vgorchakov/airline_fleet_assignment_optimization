from data_preprocessing import DataPreprocess
from schedule_visualizer import VisualizeSchedule
from graph import BuildGraph
from optimizer.model import ModelBuild
import pandas as pd
import pyomo.environ as pe
import json

def run_pipeline():
    print('Start Data Preprocessing')
    dp = DataPreprocess()
    #one_day_flights_df = pd.read_csv('data/day_flights.csv')
    #flight_info_dict = DataPreprocess.construct_graph_input(one_day_flights_df)
    print('Start Building Graph')
    gr = BuildGraph(dp.flight_info_dict)
    print('Start Model Solving')
    m = ModelBuild(gr.flight_list, gr.flight_pairs_dict, gr.incoming_nodes, gr.outgoing_nodes)
    # store model output
    with open("model_output.json", "w") as file:
        json.dump(m.solved_model.model_variable_values, file)

    VisualizeSchedule(m.solved_model, dp.flight_info_dict)


if __name__ == "__main__":
    run_pipeline()