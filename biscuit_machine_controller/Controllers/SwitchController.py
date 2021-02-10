from Controller import Controller
from MachineStatus import MachineStatus
from PulseTransmitter import PulseTransmitter
from Config import Config


class SwitchController(Controller):
    def __init__(self, machine_status: MachineStatus, pulse_transmitter: PulseTransmitter):
        super().__init__(machine_status, pulse_transmitter)
        self.input_pin = Config.get_config_variable('switch_input_pin')
        self.output_pin = Config.get_config_variable('switch_output_pin')

    def work(self):
        if self.machine_status.machine_status != self.pins.digital_read(self.output_pin):
            self.pins.digital_write(self.input_pin, self.machine_status.machine_status)
