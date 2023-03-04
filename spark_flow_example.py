from flowrunner.runner.flow import BaseFlow
from flowrunner.core.decorators import step, start, end

import pandas as pd

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


class PySparkFlowExample(BaseFlow):
    # read from sample data
    @start
    @step(next="union_data")
    def read_data(self):
        self.sample_data = spark.createDataFrame(pd.read_csv("./sample_data.csv"))

    # union two dataframes
    @step(next="show_df")
    def union_data(self):
        copy_df = self.sample_data.alias('copy_df')
        self.final_df = copy_df.union(self.sample_data)
    # display the dataframes
    @end
    @step
    def show_df(self):
        print(self.final_df.show())

PySparkFlowExample().run_flow()