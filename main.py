from data_preprocessing import DataPreprocess
from graph import BuildGraph
from graph_viz import build_graph_vizualization

def run_pipeline():
    print('Start Data Preprocessing')
    dp = DataPreprocess()
    print('Start Building Graph')
    gr = BuildGraph(dp.flight_info_dict)
    print('Start Graph Vizualization')
    build_graph_vizualization(gr.flight_list, gr.flight_pairs)

if __name__ == "__main__":
    run_pipeline()