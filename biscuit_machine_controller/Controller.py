from PinEmulator import PinEmulator
from MachineStatus import MachineStatus
from PulseTransmitter import PulseTransmitter
from Config import Config


class Controller:
    def __init__(self, machine_status: MachineStatus, pulse_transmitter: PulseTransmitter):
        self.pins = PinEmulator(redis_host=Config.get_config_variable('redis_host'),
                                redis_port=Config.get_config_variable('redis_port'),
                                redis_db=Config.get_config_variable('redis_db'))
        self.machine_status = machine_status
        self.pulse_transmitter = pulse_transmitter

    def work(self):
        raise NotImplementedError()
