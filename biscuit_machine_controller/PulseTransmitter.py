class PulseTransmitter:
    def __init__(self):
        self.receivers = []

    def register_receiver(self, receiver_func):
        self.receivers.append(receiver_func)

    def transmit_pulse(self):
        for receiver in self.receivers:
            receiver()
