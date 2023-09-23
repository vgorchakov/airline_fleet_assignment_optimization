
class VisualizeSchedule():
    def __init__(self, solved_model):
        self.solved_model = solved_model
        self.build_schedule_plot()

    def build_schedule_plot(self):
        print(self.solved_model.is_source_flight_var)
        print(self.solved_model.is_flight_pair_chosen_var)