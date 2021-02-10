import threading

from Device import Device


class DeviceManager:
    def __init__(self):
        self.devices = []

    def register_device(self, device: Device):
        self.devices.append(device)

    def start_devices(self):
        threads = list()
        for device in self.devices:
            thread = threading.Thread(target=device.run, args=(), daemon=True)
            threads.append(thread)
            thread.start()
