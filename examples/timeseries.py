#!/usr/bin/env python

from evgen.core import SessionTemplate, EventGroup, GenericEventTemplate
from evgen.writers import ConsoleWriter
from random import uniform

#Random time series generator example

#creating custom event template
class TemperatureEventTemplate(GenericEventTemplate):
    def __init__(self, *args, **kwargs):
        GenericEventTemplate.__init__(self, *args, **kwargs)
        self.set_attribute('Temp', self.get_temp)

    def get_temp(self):
        return round(uniform(18, 34), 4)


#generating event group policies - 10 events will be generated in total
eg = EventGroup()
eg.add_event(TemperatureEventTemplate(writer=ConsoleWriter()), probability=1,delay=1000, delay_random=0.5)
eg.set_repeat_policy(min=10, max=10)

session = SessionTemplate()
session.add_event_group(eg)
session.generate()