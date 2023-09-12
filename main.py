from data_preprocessing import DataPreprocess
from graph import BuildGraph
from optimizer.model import ModelBuild

def run_pipeline():
    print('Start Data Preprocessing')
    dp = DataPreprocess()
    print('Start Building Graph')
    gr = BuildGraph(dp.flight_info_dict)
    print('Start Model Solving>')
    m = ModelBuild(gr.flight_list, gr.flight_pairs_dict, gr.incoming_nodes, gr.outgoing_nodes)
    print(m.solved_model.is_flight_pair_chosen_var)
    print(m.solved_model.OBJ)

if __name__ == "__main__":
    run_pipeline()