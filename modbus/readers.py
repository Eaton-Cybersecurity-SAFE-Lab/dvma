from pymodbus.version import version
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusServerContext
from pymodbus.datastore.database import SqlSlaveContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer
import random
from dam.models import DamSensor


def update_register(a):
    context = a[0]
    readfunction = 0x03
    slave_id = 0x01  # slave address
    count = 50
    rand_addr = random.randint(0, 65000)
    values = context[slave_id].getValues(readfunction, rand_addr, count)
    djangoSensor = DamSensor.objects.get(sensor_name="sensor_1")
    djangoSensor.sensor_value = str(values)
    djangoSensor.save()

