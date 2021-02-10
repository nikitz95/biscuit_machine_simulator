import threading
import time
import os

from flask import Flask, Response

from Controllers.ExtruderController import ExtruderController
from Controllers.StamperController import StamperController
from Controllers.MotorController import MotorController
from Controllers.OvenController import OvenController
from Controllers.SwitchController import SwitchController
from MachineStatus import MachineStatus
from PulseTransmitter import PulseTransmitter
from Config import Config


app = Flask(__name__)


@app.route('/start')
def start():
    machine_status.machine_status = 'On'
    return Response(status=200)


@app.route('/pause')
def pause():
    machine_status.machine_status = 'Pause'
    return Response(status=200)


@app.route('/stop')
def stop():
    machine_status.machine_status = 'Off'
    return Response(status=200)


def control_the_machine():
    while True:
        time.sleep(0.5)
        for c in controllers:
            c.work()


if __name__ == '__main__':
    # Configuration
    Config.set_config_variable('app_host', os.getenv('APP_HOST', 'localhost'))
    Config.set_config_variable('app_port', os.getenv('APP_PORT', 5000))
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
    Config.set_config_variable('oven_input_pin', os.getenv('OVEN_INPUT_PIN', 9))
    Config.set_config_variable('oven_output_pin', os.getenv('OVEN_OUTPUT_PIN', 10))

    # Setup
    machine_status = MachineStatus()
    pulse_transmitter = PulseTransmitter()
    controllers = [
        OvenController(machine_status, pulse_transmitter),
        MotorController(machine_status, pulse_transmitter),
        ExtruderController(machine_status, pulse_transmitter),
        StamperController(machine_status, pulse_transmitter),
        SwitchController(machine_status, pulse_transmitter)]


    # Start
    threads = list()
    thread = threading.Thread(target=control_the_machine, args=(), daemon=True)
    threads.append(thread)
    thread.start()

    thread = threading.Thread(target=app.run, kwargs={'host': Config.get_config_variable('app_host'), 'port': Config.get_config_variable('app_port')}, daemon=True)
    threads.append(thread)
    thread.start()

    for index, thread in enumerate(threads):
        thread.join()
