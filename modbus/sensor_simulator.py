from random import randint
import signal
import time

from pymodbus.client.sync import ModbusTcpClient as ModbusClient


def writeRandomSensorValues(client: ModbusClient):
    client.connect()
    client.write_registers(0, [randint(0, 255) for _ in range(8)])


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill_now = True


if __name__ == '__main__':
    killer = GracefulKiller()
    client = ModbusClient('localhost', port=5020)
    while not killer.kill_now:
        time.sleep(3)
        writeRandomSensorValues(client)
    print("Modbus disconnect")
    client.close()
