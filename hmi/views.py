from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

from modbus.sensors import REGISTER_MAPPINGS

UNIT = 0x1
# Create your views here.

def index(request):
    return render(request, 'index.html')


def olorin(request):
    return render(request, 'olorin.html')


def aiwendil(request):
    return render(request, 'aiwendil.html')


def alatar(request):
    return render(request, 'alatar.html')


def curunir(request):
    return render(request, 'curunir.html')

def getSensorValues(request):
    client = ModbusClient('localhost', port=5020)
    client.connect()
    all_coils = client.read_coils(0, 5).bits
    all_registers = client.read_holding_registers(0, 8).registers
    client.close()
    return JsonResponse({
        "coils" : all_coils,
        "registers" : all_registers
    })

@csrf_exempt
def setCoil(request):
    coil_address = request.POST["coil_address"]
    coil_value = request.POST["coil_value"]
    client = ModbusClient('localhost', port=5020)
    print(f"client.write_coil({int(coil_address)}, {1 if coil_value == 'true' else 0})")
    client.write_coil(int(coil_address), 1 if coil_value == 'true' else 0)
    client.close()
    return JsonResponse({
        "status": "success"
    })