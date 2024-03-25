'''
Simple Ping testcase using pyATS.
'''

from pyats import aetest, topology


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
        in the destinations tuple.
        '''
        # WRITE YOUR PING TEST HERE

    @aetest.cleanup
    def disconnect(self, testbed):
        '''
        Cleanup after the ping test by disconnecting from all testbed devices.
        '''
        testbed.disconnect()

def make_ping_test(testbed_path:str, destinations:tuple)->tuple:
    '''
    Function to make the ping test. This function calls aetest.main to run the PingTestcase.
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
