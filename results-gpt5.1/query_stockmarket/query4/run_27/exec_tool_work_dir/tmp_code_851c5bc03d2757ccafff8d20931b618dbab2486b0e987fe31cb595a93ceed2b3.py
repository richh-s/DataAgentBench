code = """import json, pandas as pd

stats = pd.DataFrame(var_call_T8Gb23BP7vAdWlxpJ1MLHP2h)
meta = pd.read_json(var_call_Kxfl8JHTJpmGvmbIlfmgsbfq)

filtered = stats[stats['up_days'] > stats['down_days']]
merged = filtered.merge(meta, on='Symbol')[['Symbol','Company Description','up_days','down_days']]
merged = merged.sort_values('up_days', ascending=False).head(5)

ans = []
for _, row in merged.iterrows():
    ans.append({'Symbol': row['Symbol'], 'Name': row['Company Description']})

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_fxnkv82rBl8tiSErzAmdokTp': 'file_storage/call_fxnkv82rBl8tiSErzAmdokTp.json', 'var_call_Kxfl8JHTJpmGvmbIlfmgsbfq': 'file_storage/call_Kxfl8JHTJpmGvmbIlfmgsbfq.json', 'var_call_Xqamx7gM9JsW2Ki5SZuPH4ln': {'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT']}, 'var_call_baAMzZksomDIrqYrTVlXhm6n': [], 'var_call_F74imMIte3y5l7kbmOOSEwOq': 'file_storage/call_F74imMIte3y5l7kbmOOSEwOq.json', 'var_call_rNLwCH7aUi35CHPlogPYIwXE': 'file_storage/call_rNLwCH7aUi35CHPlogPYIwXE.json', 'var_call_YdQyVfbJOnyFLuYteyJMVyJH': [], 'var_call_dL5tU4xSyMjZss7jSYZFa3kK': 'file_storage/call_dL5tU4xSyMjZss7jSYZFa3kK.json', 'var_call_6kWXy5SSxGr8eWTm69pQOVk5': 'file_storage/call_6kWXy5SSxGr8eWTm69pQOVk5.json', 'var_call_B5j5QfPMOzzZNuR5du59kMew': 'file_storage/call_B5j5QfPMOzzZNuR5du59kMew.json', 'var_call_g4D3qNvzw08vOq2MkRAihikK': 'file_storage/call_g4D3qNvzw08vOq2MkRAihikK.json', 'var_call_0uzHLUFUcl3QpDTIsVtEZW3c': 'file_storage/call_0uzHLUFUcl3QpDTIsVtEZW3c.json', 'var_call_T8UKmzh8FAtJD4vgbW2xYEJH': 'file_storage/call_T8UKmzh8FAtJD4vgbW2xYEJH.json', 'var_call_T8Gb23BP7vAdWlxpJ1MLHP2h': [{'Symbol': 'AIN', 'up_days': 143, 'down_days': 101}, {'Symbol': 'AIV', 'up_days': 118, 'down_days': 128}, {'Symbol': 'AJRD', 'up_days': 123, 'down_days': 123}, {'Symbol': 'AL', 'up_days': 131, 'down_days': 117}, {'Symbol': 'AMN', 'up_days': 134, 'down_days': 111}, {'Symbol': 'AMP', 'up_days': 141, 'down_days': 110}, {'Symbol': 'AMT', 'up_days': 128, 'down_days': 123}, {'Symbol': 'ARD', 'up_days': 80, 'down_days': 119}]}

exec(code, env_args)
