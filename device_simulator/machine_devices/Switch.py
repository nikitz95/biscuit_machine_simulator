from Device import Device


class Switch(Device):
    def __init__(self, input_pin, output_pin):
        super().__init__(input_pin, output_pin)
        self.current_status = 'Off'

    def initialize_initial_input_and_output_values(self):
        self.pins.digital_write(self.input_pin, self.current_status)
        self.pins.digital_write(self.output_pin, self.current_status)

    def device_run_logic(self):
        pin_value = self.pins.digital_read(self.input_pin)

        if pin_value and pin_value != self.current_status:
            self.pins.digital_write(self.output_pin, pin_value)
            if pin_value == 'Off':
                self.current_status = 'Off'
                print('Switch Off...')
            if pin_value == 'Pause':
                self.current_status = 'Pause'
                print('Switch Pause...')
            if pin_value == 'On':
                self.current_status = 'On'
                print('Switch On...')
