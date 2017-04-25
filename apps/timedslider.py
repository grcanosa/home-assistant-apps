#!/usr/bin/python3

import appdaemon.appapi as appapi



class TimedSlider(appapi.AppDaemon)
    def initialize(self):
        self.check_conf()
        if self.valid:
            self.handles = []
            self.step = self.get_state(self.args["slider"], "step")
            self.max_val = self.get_state(self.args["slider"], "max")
            self.min_val = self.get_state(self.args["slider"], "min")
            self.unit = self.get_state(self.args["slider"], "unit")
            self.step_multiplier = 1 # default is seconds
            if self.unit == "sec":
                self.step_multiplier = 1;
            elif self.unit == "min":
                self.step_multiplier = 60;
            elif self.unit == "hour":
                self.step_multiplier = 3600;
            self.step_seconds = int(self.step) * self.step_multiplier
            self.handles.append(self.listen_state(self.state_change, self.args["slider"]))

    def check_conf(self):
        self.valid = True
        if "slider" not in self.args or
            "sensor" not in self.args or
            "boolean" not in self.args or
            "onoff" not in self.args:
            self.valid = False


    def state_change(self,new):
        if int(new) == 0:
            self.turn_off(self.args["onoff"])
        else:
            self.turn_on(self.args["onoff")
            step_time
            self.run_in(self.change_slider_state,self.step_seconds,old_state = new)

    def change_slider_state(self,old_state):
        new_state = int(old_state)-int(self.step)
        self.set_state(self.args["slider"],state=str(new_state));
