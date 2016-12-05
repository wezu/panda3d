#!/usr/bin/env python
import unittest
from .. import testbase

class TestClockObject(testbase.PandaTestCase):
    # Please keep tests sorted alphabetically!
    def test_wait(self):
        """This tests the test fixture more than anything:

            self.wait() can be used to advance the local clock forward.
        """

        from panda3d.core import ClockObject
        clock = ClockObject.get_global_clock()

        ft = clock.get_frame_time()
        self.wait(1.0)
        self.assertGreaterEqual(clock.get_frame_time(), ft+1.0)

if __name__ == '__main__':
    unittest.main()
