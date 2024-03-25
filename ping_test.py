'''
Simple example of a Ping testcase using pyATS.

Copyright (c) 2024 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
'''

from pyats import aetest, topology

__copyright__ = "Copyright (c) 2024 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

class PingTestcase(aetest.Testcase):
    '''
    Simple Testcase for checking connectivity from the network devices.
    '''
    @aetest.setup
    def connect(self, testbed):
        '''
        Setup task: connect to all devices in the testbed and define that the
        test function "ping" should be repeated for each device in the testbed.
        '''
        testbed.connect(log_stdout=False)
        aetest.loop.mark(self.ping, device=testbed)


    @aetest.test
    def ping(self, steps, device, destinations):
        '''
        Simple ping test: using pyats API "ping", try pinging each of the IP addresses
        in the destinations tuple. If the ping is successful, the test step is marked passed,
        but if the ping is unsuccesful, the step is marked as failed.
        test_results dictionary is used to collect a summary of the results to be further used
        in for example sending the end result to Webex space.
        '''
        for destination in destinations:
            with steps.start(
                f"Checking Ping from {device.hostname} to {destination}", continue_=True
                ) as step:
                try:
                    device.ping(destination)
                except:
                    step.failed(f'Ping {destination} from device {device.hostname} unsuccessful')
                else:
                    step.passed(f'Ping {destination} from device {device.hostname} successful')

    @aetest.cleanup
    def disconnect(self, testbed):
        '''
        Cleanup after the ping test by disconnecting from all testbed devices.
        '''
        testbed.disconnect()

def make_ping_test(testbed_path:str, destinations:tuple)->tuple:
    '''
    Function to make the ping test. This function calls aetest.main to run the PingTestcase. The
    aetest.main returns the result of the full test including all the testcases. This means that
    even if only one section of one testcase fails, the full test have failed.

    As in the final step of the workshop this function will be called from another module (main.py),
    it is required to define the actual target of the aetest with the argument "testable". When
    calling the make_ping_test from another Python module, the value of __name__ will be the name
    of this module: ping_test. This way aetest will know that from wherever we run the script,
    the test details are located in the module called ping_test.
    This is an optional argument and you would not need it if running directly this file with
        python ping_test.py
    as the default value of the testable is "__main__".
    '''
    testbed = topology.loader.load(testbed_path)
    ping_test = aetest.main(
                            testable=__name__,
                            testbed=testbed,
                            destinations=destinations,
                        )

if __name__ == "__main__":
    my_testbed = "testbed.yaml"
    my_destinations = ('198.18.18.101', '198.18.6.1')
    my_ping_test = make_ping_test(my_testbed, my_destinations)
