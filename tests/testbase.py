# This function defines the common test fixture for Panda3D.

import unittest

class PandaTestCase(unittest.TestCase):
    def setUp(self):
        from panda3d.core import ClockObject
        self.__global_clock = ClockObject.get_global_clock()

        self.__global_clock.set_mode(ClockObject.M_non_real_time)

        self.__tick_function = None
        self.setTickStep(0.01)

    def setTickFunction(self, func):
        self.__tick_function = func

    def setTickStep(self, dt):
        self.__global_clock.set_dt(dt)

    def wait(self, delay):
        stop = self.__global_clock.get_frame_time() + delay
        while self.__global_clock.get_frame_time() < stop:
            self.__global_clock.tick()
