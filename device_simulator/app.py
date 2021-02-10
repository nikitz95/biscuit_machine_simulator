import os

from machine_devices import Extruder, Motor, Oven, Stamper, Switch
from DeviceManager import DeviceManager
from Config import Config

if __name__ == "__main__":
    # Configuring
    print('Configuring...')
    Config.set_config_variable('redis_host', os.getenv('REDIS_HOST', 'redis'))
    Config.set_config_variable('redis_port', os.getenv('REDIS_PORT', 6379))
    Config.set_config_variable('redis_db', os.getenv('REDIS_DB', 0))
    Config.set_config_variable('extruder_input_pin', os.getenv('EXTRUDER_INPUT_PIN', 1))
    Config.set_config_variable('extruder_output_pin', os.getenv('EXTRUDER_OUTPUT_PIN', 2))
    Config.set_config_variable('stamper_input_pin', os.getenv('STAMPER_INPUT_PIN', 3))
    Config.set_config_variable('stamper_output_pin', os.getenv('STAMPER_OUTPUT_PIN', 4))
    Config.set_config_variable('switch_input_pin', os.getenv('SWITCH_INPUT_PIN', 5))
    Config.set_config_variable('switch_output_pin', os.getenv('SWITCH_OUTPUT_PIN', 6))
    Config.set_config_variable('motor_input_pin', os.getenv('MOTOR_INPUT_PIN', 7))
    Config.set_config_variable('motor_output_pin', os.getenv('MOTOR_OUTPUT_PIN', 8))
    Config.set_config_variable('motor_revolution_time', os.getenv('MOTOR_REVOLUTION_TIME', 5))
    Config.set_config_variable('oven_input_pin', os.getenv('OVEN_INPUT_PIN', 9))
    Config.set_config_variable('oven_output_pin', os.getenv('OVEN_OUTPUT_PIN', 10))
    Config.set_config_variable('oven_heating_degrees_per_sec', os.getenv('OVEN_HEATING_DEGREES_PER_SEC', 3))
    Config.set_config_variable('oven_cooling_degrees_per_sec', os.getenv('OVEN_COOLING_DEGREES_PER_SEC', 1))
    Config.set_config_variable('oven_room_temperature', os.getenv('OVEN_ROOM_TEMPERATURE', 23))

    # Setup the machine components
    print('Setting up the devices...')
    extruder = Extruder.Extruder(input_pin=Config.get_config_variable('extruder_input_pin'),
                                 output_pin=Config.get_config_variable('extruder_output_pin'))
    stamper = Stamper.Stamper(input_pin=Config.get_config_variable('stamper_input_pin'),
                              output_pin=Config.get_config_variable('stamper_output_pin'))
    switch = Switch.Switch(input_pin=Config.get_config_variable('switch_input_pin'),
                           output_pin=Config.get_config_variable('switch_output_pin'))
    motor = Motor.Motor(input_pin=Config.get_config_variable('motor_input_pin'),
                        output_pin=Config.get_config_variable('motor_output_pin'),
                        revolution_time=Config.get_config_variable('motor_revolution_time'))
    oven = Oven.Oven(input_pin=Config.get_config_variable('oven_input_pin'),
                     output_pin=Config.get_config_variable('oven_output_pin'),
                     heating_degrees_per_sec=Config.get_config_variable('oven_heating_degrees_per_sec'),
                     cooling_degrees_per_sec=Config.get_config_variable('oven_cooling_degrees_per_sec'),
                     room_temperature=Config.get_config_variable('oven_room_temperature'))

    # Registering the machine components
    device_manager = DeviceManager()
    device_manager.register_device(extruder)
    device_manager.register_device(stamper)
    device_manager.register_device(switch)
    device_manager.register_device(motor)
    device_manager.register_device(oven)

    # Start the machine components
    print('Starting the devices...')
    device_manager.start_devices()
