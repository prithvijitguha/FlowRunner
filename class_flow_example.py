from flowrunner.decorators import step, start, end
from flowrunner.core.graph import BaseFlow
from dataclasses import dataclass

class FlowExample(BaseFlow):
    @start
    @step(next=['middle_func', 'another_middle_func'])
    def first_func(self):
        """This function is the start of our workflow
        where we extract 3 dataframes"""
        x = 2
        self.data_store['first_func'] = x
        print("first_func output", x)

    @step(next='model_func')
    def middle_func(self):
        """This function is the middle where we
        filter + transform stuff"""
        value_from_first = self.data_store['first_func']
        self.data_store['middle_func'] = value_from_first * 3
        print("middle_func output", self.data_store['middle_func'])



    @step(next='model_func')
    def another_middle_func(self):
        """This function is the middle where we
        filter + transform stuff"""

        value_from_first = self.data_store['first_func']
        self.data_store['another_middle_func'] = value_from_first
        print("another_middle_func output", value_from_first)

    @step(next='end_func')
    def model_func(self):
        """This function does model training"""
        y = self.data_store['middle_func']
        x = self.data_store['another_middle_func']
        print("model_func output", x)
        print("model_func output", y)



    @end
    @step
    def end_func(self):
        """This function is the end where
        we write data into a table"""
        final_value = self.data_store['model_func']
        print("end_func output", final_value)


