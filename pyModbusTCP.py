from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils

import time

c = ModbusClient(host='172.25.50.115', port=502, unit_id=100, auto_open=True)

try:
# Check if the connection is established
    c.open()
    while True:
        list = c.read_holding_registers(841,1)
        vals = utils.get_list_2comp(list, 16)
        for val in vals:
            result = int(val)
            print(result/10)
        time.sleep(1)

finally:
    # The `auto_close` parameter handles closing, but this ensures it
    c.close()
