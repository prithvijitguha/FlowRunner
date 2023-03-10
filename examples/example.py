# -*- coding: utf-8 -*-
from flowrunner import BaseFlow, end, start, step


class ExampleFlow(BaseFlow):
    @start
    @step(next=["method2", "method3"])
    def method1(self):
        self.a = 1

    @step(next=["method4"])
    def method2(self):
        self.a += 1

    @step(next=["method4"])
    def method3(self):
        self.a += 2

    @end
    @step
    def method4(self):
        self.a += 3
        print(self.a)
