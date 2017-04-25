#!/usr/bin/python3

import appdaemon.appapi as appapi



class TimedSlider(appapi.AppDaemon)
    def initialize(self):
        self.slider = self.args["input_slider"]
        self.sensor = self.args["sensor"]
        self.active = self.args["input_boolean"]
        self.step = self.get_state(entity = self.slider_name, attribute = "step")
        self.max_val = self.get_state(entity = self.slider_name, attribute = "max")
        self.min_val = self.get_state(entity = self.slider_name, attribute = "min")
        self.unit = self.get_state(entity = self.slider_name, attribute = "unit")
        self.listen_state(self.state_change, self.args["switch"], new="on")

    def state_change(self,)
