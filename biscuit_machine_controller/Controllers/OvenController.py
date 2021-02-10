from Controller import Controller
from MachineStatus import MachineStatus
from PulseTransmitter import PulseTransmitter
from Config import Config


class OvenController(Controller):
    def __init__(self, machine_status: MachineStatus, pulse_transmitter: PulseTransmitter):
        super().__init__(machine_status, pulse_transmitter)
        self.input_pin = Config.get_config_variable('oven_input_pin')
        self.output_pin = Config.get_config_variable('oven_output_pin')

    def work(self):
        if self.machine_status.machine_status == 'On' or self.machine_status.machine_status == 'Pause':
            self._keep_warm()
        else:
            if self.pins.digital_read(self.input_pin) == 'On':
                self.pins.digital_write(self.input_pin, 'Off')
                self.machine_status.oven_status = 'Off'

    def _get_temperature(self):
        temp = int(float(self.pins.digital_read(self.output_pin)))
        print(temp)
        return temp

    def _turn_oven_on(self):
        self.pins.digital_write(self.input_pin, 'On')

    def _turn_oven_off(self):
        self.pins.digital_write(self.input_pin, 'Off')

    def _keep_warm(self):
        oven_temperature = self._get_temperature()
        if oven_temperature <= 220:
            if self.machine_status.oven_status == 'Off':
                self._turn_oven_on()
                self.machine_status.oven_status = 'On'
                self.machine_status.working_temperature = False
        elif oven_temperature >= 240:
            if self.machine_status.oven_status == 'On':
                self._turn_oven_off()
                self.machine_status.oven_status = 'Off'
                self.machine_status.working_temperature = False
        else:
            self.machine_status.working_temperature = True
