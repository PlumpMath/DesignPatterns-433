from __future__ import print_function
import time
import random
__author__ = 'Taylor'

class Engine(object):
    def __init__(self):
        self._choke = False

    @property
    def choke(self):
        return self._choke

    @choke.setter
    def choke(self, value):
        print('Engine Choke - {state}'.format(state='ON' if value else 'OFF'))
        self._choke = value


class EngineStarter(object):
    def __init__(self):
        self._relayState = False

    def activateRelay(self):
        print('Engine Starter - Activating Relay')
        self._relayState = True

    def deactivateRelay(self):
        print('Engine Starter - Deactivating Relay')
        self._relayState = False


class EngineControlUnit(object):
    def __init__(self):
        self._engine = Engine()
        self._engineStarter = EngineStarter()
        self._on = False

    def keyOn(self):
        print('------ Key ON ------')
        print('ECU - Electronics Enabled')
        self._on = True
        self._engineStarter.deactivateRelay()
        self._engine.choke = False

    def keyStart(self):
        print('----- Key START -----')
        self._engine.choke = True
        self._engineStarter.activateRelay()

    def keyOff(self):
        print('---- Key OFF ----')
        print('ECU - Electronics Disabled')
        self._on = False

if __name__ == '__main__':
    ecu = EngineControlUnit()
    print('Human - Turning Key to On position')
    ecu.keyOn()
    print('Human - Starting Car')
    ecu.keyStart()
    print('Human - Waiting for car to start')
    for i in range(random.randrange(4, 8, 1)):
        time.sleep(0.25)
        print('.', end='')
    print()
    print('Human - Notices the car is started')
    ecu.keyOn()
