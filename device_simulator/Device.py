import time

from PinEmulator import PinEmulator
from Config import Config


class Device:
    def __init__(self, input_pin=None, output_pin=None, wait_interval=0.1):
        self.wait_interval = wait_interval
        self.pins = PinEmulator(redis_host=Config.get_config_variable('redis_host'),
                                redis_port=Config.get_config_variable('redis_port'),
                                redis_db=Config.get_config_variable('redis_db'))

        self.input_pin = input_pin
        self.output_pin = output_pin

    def run(self):
        self.initialize_initial_input_and_output_values()

        while True:
            self.device_run_logic()

            time.sleep(self.wait_interval)

    def device_run_logic(self):
        raise NotImplementedError()

    def initialize_initial_input_and_output_values(self):
        raise NotImplementedError()
