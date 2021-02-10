from time import time

from Device import Device


class Oven(Device):
    def __init__(self, input_pin, output_pin, heating_degrees_per_sec, cooling_degrees_per_sec, room_temperature):
        super().__init__(input_pin, output_pin)

        self.heating_degrees_per_sec = heating_degrees_per_sec
        self.cooling_degrees_per_sec = cooling_degrees_per_sec
        self.room_temperature = room_temperature
        self.temperature = room_temperature
        self.last_temperature_update = time()
        self.oven_status = 'Off'

    def initialize_initial_input_and_output_values(self):
        self.pins.digital_write(self.input_pin, self.oven_status)
        self.pins.digital_write(self.output_pin, str(self.temperature))

    def device_run_logic(self):
        # Calculate temperature
        self._calculate_temperature()

        # Update status
        input_pin_value = self.pins.digital_read(self.input_pin)
        if self.oven_status != input_pin_value:
            self.oven_status = input_pin_value
            if self.oven_status == 'On':
                print('Turning on the oven...')
            else:
                print('Turning off the oven...')

        # Update temperature on output pin
        self.pins.digital_write(self.output_pin, str(self.temperature))

    def _calculate_temperature(self):
        update_time = time()
        if self.oven_status == 'On':
            self.temperature += self.heating_degrees_per_sec * (update_time - self.last_temperature_update)
        else:
            new_temp = self.temperature - self.cooling_degrees_per_sec * (update_time - self.last_temperature_update)
            if new_temp > self.room_temperature:
                self.temperature = new_temp
            else:
                self.temperature = self.room_temperature

        self.last_temperature_update = update_time
