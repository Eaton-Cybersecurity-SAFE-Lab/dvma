from pymodbus.datastore import ModbusSlaveContext, ModbusSequentialDataBlock
from random import randint

REGISTER_MAPPINGS = {
    "olorin": {
        "dashboard_register_address": 0,
        "coils": [
            {
                "name": "toggle_switch_1",
                "register_address": 0
            },
            {
                "name": "toggle_switch_2",
                "register_address": 1
            },
            {
                "name": "toggle_switch_3",
                "register_address": 2
            },
            {
                "name": "control_point_1",
                "register_address": 3
            },
            {
                "name": "control_point_2",
                "register_address": 4
            }
        ],
        "holding_registers": [
            {
                "name": "knob_1",
                "register_address": 1
            },
            {
                "name": "knob_2",
                "register_address": 2
            },
            {
                "name": "knob_3",
                "register_address": 3
            },
            {
                "name": "knob_4",
                "register_address": 4
            },
            {
                "name": "range_1",
                "register_address": 5
            },
        ]
    },
    "aiwendil": {
        "dashboard_register_address": 6,
    },
    "alatar": {
        "dashboard_register_address": 7,
    },
    "curunir": {
        "dashboard_register_address": 8,
    }
}


def generateDVMAModbusSlaveContext() -> ModbusSlaveContext:
    return ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [randint(0, 1) for _ in range(6)]),
        co=ModbusSequentialDataBlock(0, [randint(0, 1) for _ in range(6)]),
        hr=ModbusSequentialDataBlock(0, [randint(0, 255) for _ in range(9)]),
        ir=ModbusSequentialDataBlock(0, [randint(0, 255) for _ in range(9)]))
