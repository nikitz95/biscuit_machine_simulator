import redis
import threading


class PinEmulator:
    def __init__(self, redis_host, redis_port, redis_db):
        self.r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, charset="utf-8", decode_responses=True)

    def digital_write(self, pin, input_val):
        self.r.set(pin, input_val)

    def digital_read(self, pin):
        return self.r.get(pin)

    def send_a_pulse(self, pin):
        self.digital_write(pin, '1')

        # Hold HIGH state for 0.5 sec and return to LOW state
        threading.Timer(0.5, self.digital_write, [pin, '0']).start()
        return
