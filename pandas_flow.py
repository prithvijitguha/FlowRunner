from flowrunner.runner.flow import BaseFlow
from flowrunner.core.decorators import step, start, end

import pandas as pd


class PandasFlowExample(BaseFlow):
    # read from sample data
    @start
    @step(next="union_data")
    def read_data(self):
        self.sample_data = pd.read_csv("./sample_data.csv")

    # union two dataframes
    @step(next="show_df")
    def union_data(self):
        copy_data = self.sample_data.copy()
        self.final_df = copy_data.append(self.sample_data)
    # display the dataframes
    @end
    @step
    def show_df(self):
        print(self.final_df)

PandasFlowExample().run_flow()