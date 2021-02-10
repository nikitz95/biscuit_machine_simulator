from Controller import Controller
from MachineStatus import MachineStatus
from PulseTransmitter import PulseTransmitter
from Config import Config


class StamperController(Controller):
    def __init__(self, machine_status: MachineStatus, pulse_transmitter: PulseTransmitter):
        super().__init__(machine_status, pulse_transmitter)
        self.input_pin = Config.get_config_variable('stamper_input_pin')
        self.pulse_transmitter.register_receiver(self.transmit_pulse)

    def work(self):
        return

    def transmit_pulse(self):
        self.pins.send_a_pulse(self.input_pin)
