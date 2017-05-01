#!/usr/bin/python3

import appdaemon.appapi as appapi



class TimedSlider(appapi.AppDaemon):
    def initialize(self):
        self.check_conf()
        if self.valid:
            self.handles = []
            self.run_in_h = []
            self.step = self.get_state(self.args["slider"], "step")
            self.max_val = self.get_state(self.args["slider"], "max")
            self.min_val = self.get_state(self.args["slider"], "min")
            self.unit = self.get_state(self.args["slider"], "unit_of_measurement")
            #print(self)
            self.step_multiplier = 60 # default is minutes
            if self.unit == "sec":
                self.step_multiplier = 1;
            elif self.unit == "min":
                self.step_multiplier = 60;
            elif self.unit == "hour":
                self.step_multiplier = 3600;
            #self.step_multiplier = 1
            self.step_seconds = float(self.step) * self.step_multiplier
            self.handles.append(self.listen_state(self.state_change, self.args["slider"]))

    def check_conf(self):
        self.valid = True
        if "slider" not in self.args or "onoff" not in self.args:
            self.valid = False


    def state_change(self, entity, attribute, old, new, kwargs):
        self.notify("State has been changed to "+str(new),name="grcanosabot")
        if float(new) == 0:
            self.turn_off(self.args["onoff"])
        else:
            self.turn_on(self.args["onoff"])
            for h in self.run_in_h:
                self.cancel_timer(h)
            self.run_in_h = []
            self.run_in_h.append(self.run_in(self.change_slider_state,self.step_seconds,old_state = new))

    def change_slider_state(self,kwargs):
        new_state = float(kwargs["old_state"])-float(self.step)
        self.set_state(self.args["slider"],state=str(new_state));
        self.notify("Changing state to "+str(new_state),name="grcanosabot")
