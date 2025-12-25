code = """import json, pandas as pd
from pathlib import Path

files = {
 'AIN': var_call_F74imMIte3y5l7kbmOOSEwOq,
 'AIV': var_call_rNLwCH7aUi35CHPlogPYIwXE,
 'AJRD': var_call_dL5tU4xSyMjZss7jSYZFa3kK,
 'AL': var_call_6kWXy5SSxGr8eWTm69pQOVk5,
 'AMN': var_call_B5j5QfPMOzzZNuR5du59kMew,
 'AMP': var_call_g4D3qNvzw08vOq2MkRAihikK,
 'AMT': var_call_0uzHLUFUcl3QpDTIsVtEZW3c,
 'ARD': var_call_T8UKmzh8FAtJD4vgbW2xYEJH
}

stats = []
for sym, path in files.items():
    df = pd.read_json(path)
    df['Open'] = df['Open'].astype(float)
    df['Close'] = df['Close'].astype(float)
    up = (df['Close'] > df['Open']).sum()
    down = (df['Close'] < df['Open']).sum()
    stats.append({'Symbol': sym, 'up_days': int(up), 'down_days': int(down)})

res = json.dumps(stats)
print('__RESULT__:')
print(res)"""

env_args = {'var_call_fxnkv82rBl8tiSErzAmdokTp': 'file_storage/call_fxnkv82rBl8tiSErzAmdokTp.json', 'var_call_Kxfl8JHTJpmGvmbIlfmgsbfq': 'file_storage/call_Kxfl8JHTJpmGvmbIlfmgsbfq.json', 'var_call_Xqamx7gM9JsW2Ki5SZuPH4ln': {'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT']}, 'var_call_baAMzZksomDIrqYrTVlXhm6n': [], 'var_call_F74imMIte3y5l7kbmOOSEwOq': 'file_storage/call_F74imMIte3y5l7kbmOOSEwOq.json', 'var_call_rNLwCH7aUi35CHPlogPYIwXE': 'file_storage/call_rNLwCH7aUi35CHPlogPYIwXE.json', 'var_call_YdQyVfbJOnyFLuYteyJMVyJH': [], 'var_call_dL5tU4xSyMjZss7jSYZFa3kK': 'file_storage/call_dL5tU4xSyMjZss7jSYZFa3kK.json', 'var_call_6kWXy5SSxGr8eWTm69pQOVk5': 'file_storage/call_6kWXy5SSxGr8eWTm69pQOVk5.json', 'var_call_B5j5QfPMOzzZNuR5du59kMew': 'file_storage/call_B5j5QfPMOzzZNuR5du59kMew.json', 'var_call_g4D3qNvzw08vOq2MkRAihikK': 'file_storage/call_g4D3qNvzw08vOq2MkRAihikK.json', 'var_call_0uzHLUFUcl3QpDTIsVtEZW3c': 'file_storage/call_0uzHLUFUcl3QpDTIsVtEZW3c.json', 'var_call_T8UKmzh8FAtJD4vgbW2xYEJH': 'file_storage/call_T8UKmzh8FAtJD4vgbW2xYEJH.json'}

exec(code, env_args)
