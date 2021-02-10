from Device import Device


class Extruder(Device):
    def __init__(self, input_pin, output_pin):
        super().__init__(input_pin, output_pin)
        self.pulse_count = 0
        self.pulse_detected = False

    def initialize_initial_input_and_output_values(self):
        self.pins.digital_write(self.input_pin, '0')

    def device_run_logic(self):
        pin_value = self.pins.digital_read(self.input_pin)

        if not self.pulse_detected and pin_value == '1':
            print('Pulse detected. Extruding... ')
            self.pulse_count += 1
            self.pulse_detected = True
        if pin_value == '0':
            self.pulse_detected = False
