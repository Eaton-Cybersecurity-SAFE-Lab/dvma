import random

from pymodbus.version import version
from pymodbus.server.sync import StartTcpServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

import logging

from modbus.sensors import generateDVMAModbusSlaveContext

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def run_server():
    store = generateDVMAModbusSlaveContext()

    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'RIT Safe Lab'
    identity.ProductCode = 'RS'
    identity.VendorUrl = 'https://github.com/rit-cybersecurity-safe-lab/dvma'
    identity.ProductName = 'Damn Vulnerable Modbus Application'
    identity.ModelName = 'DVMA'
    identity.MajorMinorRevision = version.short()

    StartTcpServer(context, identity=identity, address=("", 5020))


if __name__ == "__main__":
    run_server()
