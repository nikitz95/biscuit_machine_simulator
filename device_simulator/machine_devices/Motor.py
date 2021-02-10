from time import time

from Device import Device


class Motor(Device):
    def __init__(self, input_pin, output_pin, revolution_time):
        super().__init__(input_pin, output_pin)

        self.pulse_count = 0
        self.current_status = 'Off'
        self.revolution_time = revolution_time
        self.last_revolution_start = None

    def initialize_initial_input_and_output_values(self):
        self.pins.digital_write(self.input_pin, self.current_status)
        self.pins.digital_write(self.output_pin, '0')

    def device_run_logic(self):
        pin_value = self.pins.digital_read(self.input_pin)

        if pin_value != self.current_status:
            if pin_value == 'On':
                print('Staring up the motor...')
                self.current_status = 'On'
                self.last_revolution_start = time()
            else:
                print('Stopping the motor...')
                self.current_status = 'Off'
                self.last_revolution_start = None

        # Should send pulse
        if self.current_status == 'On' and time() - self.last_revolution_start > self.revolution_time:
            self.last_revolution_start = time()

            print('Sending a pulse...')
            self.pins.send_a_pulse(self.output_pin)
