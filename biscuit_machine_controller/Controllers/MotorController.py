from Controller import Controller
from MachineStatus import MachineStatus
from PulseTransmitter import PulseTransmitter
from Config import Config


class MotorController(Controller):
    def __init__(self, machine_status: MachineStatus, pulse_transmitter: PulseTransmitter):
        super().__init__(machine_status, pulse_transmitter)
        self.input_pin = Config.get_config_variable('motor_input_pin')
        self.output_pin = Config.get_config_variable('motor_output_pin')
        self.pulse_detected = False
        self.turn_off_command = False
        self.revolutions_count_after_turn_off_command = 0

    def work(self):
        if self.machine_status.machine_status == 'On':
            if self.turn_off_command:
                self.turn_off_command = False
                self.revolutions_count_after_turn_off_command = 0

            if self.machine_status.motor_status == 'Off' and self.machine_status.working_temperature:
                self.pins.digital_write(self.input_pin, 'On')
                self.machine_status.motor_status = 'On'
        else:
            self.turn_off_command = True

        # Turn off motor after certain revolutions have passed - making sure no biscuits are left on the belt
        if self.turn_off_command and self.machine_status.motor_status == 'On' and self.revolutions_count_after_turn_off_command >= self.machine_status.conveyor_belt_max_biscuits:
            self.pins.digital_write(self.input_pin, 'Off')
            self.machine_status.motor_status = 'Off'

        # Checking for pulse and transmitting it
        if not self.pulse_detected and self.pins.digital_read(self.output_pin) == '1':
            self.pulse_detected = True
            if self.turn_off_command:
                self.revolutions_count_after_turn_off_command += 1
            else:
                self.pulse_transmitter.transmit_pulse()

        if self.pins.digital_read(self.output_pin) == '0':
            self.pulse_detected = False
