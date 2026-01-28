code = """import json
import os

# helper to load variable which may be a file path or a python object
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r') as f:
            return json.load(f)
    else:
        return v

vars_to_load = [
    'var_call_0aDXy2WIyW3zfIO7ZUjzfRHD',
    'var_call_BEg0jQ0E1S3xWxybYAqNRo17',
    'var_call_XjqFkzHwv5uXixX2SQQEq2Zx',
    'var_call_FDfAIcqLTmU7Kt7WGPITvm7O',
    'var_call_sryV4VMl0aL5D97v6sqIF6Dw',
    'var_call_84f6uxn9cz9jBqS8wo5qrLJM',
    'var_call_MgZqulSlKOIE7WIEzEyObIlu',
    'var_call_pKaDWyeUySXqIanp50YnJObF'
]

all_records = []
for name in vars_to_load:
    v = globals().get(name)
    if v is None:
        continue
    data = load_var(v)
    # data expected to be list of dicts
    if isinstance(data, list):
        all_records.extend(data)

# load sym_to_name mapping from the earlier stockinfo intersection result (last var in list)
sym_to_name = {}
for name in all_records:
    # if this list contains sym_to_name entry, skip
    pass
# Actually var_call_pKaDW... contains mapping; load it
mapping_var = load_var(var_call_pKaDWyeUySXqIanp50YnJObF)
# mapping_var is a dict with keys 'common_symbols', 'sym_to_name', 'n_common'
if isinstance(mapping_var, dict) and 'sym_to_name' in mapping_var:
    sym_to_name = mapping_var['sym_to_name']
else:
    sym_to_name = {}

# Process all_records to numeric
processed = []
for r in all_records:
    try:
        sym = r.get('symbol')
        up = r.get('up')
        down = r.get('down')
        # convert to float if possible
        upn = None
        downn = None
        if up is None:
            upn = None
        else:
            try:
                upn = float(up)
            except:
                upn = None
        if down is None:
            downn = None
        else:
            try:
                downn = float(down)
            except:
                downn = None
        processed.append({'symbol': sym, 'up': upn, 'down': downn})
    except Exception as e:
        continue

# Filter where up and down are not None and up>down
valid = [r for r in processed if r['up'] is not None and r['down'] is not None and r['up']>r['down']]
# compute delta
for r in valid:
    r['delta'] = r['up'] - r['down']

# sort by delta desc then by up desc
valid_sorted = sorted(valid, key=lambda x: (x['delta'], x['up']), reverse=True)

# take top 5
top5 = valid_sorted[:5]

# helper to extract company name from description
import re

def extract_name(desc):
    if not desc or not isinstance(desc, str):
        return None
    # split on common patterns
    patterns = [' is ', ' specializes', ' specializes in', ' offers ', ' provides ', ' operates ', ' is an ', ' is a ', ' is the ']
    idxs = []
    for p in patterns:
        i = desc.find(p)
        if i!=-1:
            idxs.append(i)
    if idxs:
        i = min(idxs)
        return desc[:i].strip()
    # fallback: first comma
    if ',' in desc:
        return desc.split(',')[0].strip()
    return desc

# Build final names list
final_names = []
for r in top5:
    sym = r['symbol']
    desc = sym_to_name.get(sym)
    name = extract_name(desc) if desc else None
    if not name:
        name = sym
    final_names.append(name)

# Prepare output JSON
output = final_names

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_QYmSJ4a5h1qX6ejjrb40amfT': 'file_storage/call_QYmSJ4a5h1qX6ejjrb40amfT.json', 'var_call_aQoeNw5nSqywRD7EjJP9yNGT': 'file_storage/call_aQoeNw5nSqywRD7EjJP9yNGT.json', 'var_call_pKaDWyeUySXqIanp50YnJObF': 'file_storage/call_pKaDWyeUySXqIanp50YnJObF.json', 'var_call_0aDXy2WIyW3zfIO7ZUjzfRHD': [{'symbol': 'AEFC', 'up': 'nan', 'down': 'nan'}, {'symbol': 'AIN', 'up': '143.0', 'down': '101.0'}, {'symbol': 'AIV', 'up': '118.0', 'down': '128.0'}, {'symbol': 'AIZP', 'up': 'nan', 'down': 'nan'}, {'symbol': 'AJRD', 'up': '123.0', 'down': '123.0'}, {'symbol': 'AL', 'up': '131.0', 'down': '117.0'}, {'symbol': 'AMN', 'up': '134.0', 'down': '111.0'}, {'symbol': 'AMP', 'up': '141.0', 'down': '110.0'}, {'symbol': 'AMT', 'up': '128.0', 'down': '123.0'}, {'symbol': 'ARD', 'up': '80.0', 'down': '119.0'}, {'symbol': 'ARGD', 'up': '133.0', 'down': '82.0'}, {'symbol': 'ARLO', 'up': 'nan', 'down': 'nan'}, {'symbol': 'ASG', 'up': '110.0', 'down': '110.0'}, {'symbol': 'AVA', 'up': '134.0', 'down': '112.0'}, {'symbol': 'BANC', 'up': '108.0', 'down': '119.0'}, {'symbol': 'BBU', 'up': '129.0', 'down': '120.0'}, {'symbol': 'BBVA', 'up': '126.0', 'down': '104.0'}, {'symbol': 'BDXA', 'up': '83.0', 'down': '77.0'}, {'symbol': 'BKH', 'up': '134.0', 'down': '115.0'}, {'symbol': 'BKT', 'up': '105.0', 'down': '97.0'}, {'symbol': 'BLD', 'up': '131.0', 'down': '120.0'}, {'symbol': 'BNS', 'up': '132.0', 'down': '117.0'}, {'symbol': 'BV', 'up': 'nan', 'down': 'nan'}, {'symbol': 'BZH', 'up': '127.0', 'down': '123.0'}, {'symbol': 'CADE', 'up': '88.0', 'down': '83.0'}, {'symbol': 'CAE', 'up': '122.0', 'down': '117.0'}, {'symbol': 'CAF', 'up': '131.0', 'down': '113.0'}, {'symbol': 'CBT', 'up': '128.0', 'down': '122.0'}, {'symbol': 'CCC', 'up': 'nan', 'down': 'nan'}, {'symbol': 'CCZ', 'up': '17.0', 'down': '10.0'}, {'symbol': 'CHAP', 'up': '34.0', 'down': '23.0'}], 'var_call_BEg0jQ0E1S3xWxybYAqNRo17': [{'symbol': 'CIA', 'up': '130.0', 'down': '112.0'}, {'symbol': 'CMA', 'up': '124.0', 'down': '124.0'}, {'symbol': 'CMI', 'up': '127.0', 'down': '123.0'}, {'symbol': 'CMSA', 'up': 'nan', 'down': 'nan'}, {'symbol': 'CNK', 'up': '128.0', 'down': '122.0'}, {'symbol': 'COTY', 'up': '124.0', 'down': '123.0'}, {'symbol': 'CRC', 'up': '121.0', 'down': '128.0'}, {'symbol': 'CRM', 'up': '137.0', 'down': '113.0'}, {'symbol': 'CRS', 'up': '121.0', 'down': '128.0'}, {'symbol': 'CSL', 'up': '131.0', 'down': '119.0'}, {'symbol': 'CTS', 'up': '113.0', 'down': '122.0'}, {'symbol': 'CUBE', 'up': '133.0', 'down': '113.0'}, {'symbol': 'CURO', 'up': '9.0', 'down': '7.0'}, {'symbol': 'CVIA', 'up': 'nan', 'down': 'nan'}, {'symbol': 'CVX', 'up': '118.0', 'down': '132.0'}, {'symbol': 'CXH', 'up': '126.0', 'down': '91.0'}, {'symbol': 'DAC', 'up': '66.0', 'down': '115.0'}, {'symbol': 'DDS', 'up': '128.0', 'down': '123.0'}, {'symbol': 'DDT', 'up': '118.0', 'down': '119.0'}], 'var_call_XjqFkzHwv5uXixX2SQQEq2Zx': [{'symbol': 'DEO', 'up': '131.0', 'down': '120.0'}, {'symbol': 'DGX', 'up': '129.0', 'down': '121.0'}, {'symbol': 'DMB', 'up': '132.0', 'down': '95.0'}, {'symbol': 'DTQ', 'up': '139.0', 'down': '98.0'}, {'symbol': 'DXC', 'up': '133.0', 'down': '116.0'}, {'symbol': 'EARN', 'up': '114.0', 'down': '124.0'}, {'symbol': 'EBS', 'up': '133.0', 'down': '115.0'}, {'symbol': 'EGO', 'up': '108.0', 'down': '123.0'}, {'symbol': 'EGY', 'up': '100.0', 'down': '128.0'}, {'symbol': 'EIG', 'up': '125.0', 'down': '116.0'}], 'var_call_FDfAIcqLTmU7Kt7WGPITvm7O': [{'symbol': 'ELF', 'up': '121.0', 'down': '129.0'}, {'symbol': 'EMP', 'up': '74.0', 'down': '100.0'}, {'symbol': 'ENLC', 'up': '107.0', 'down': '124.0'}, {'symbol': 'EPR', 'up': '132.0', 'down': '117.0'}, {'symbol': 'EPRT', 'up': 'nan', 'down': 'nan'}, {'symbol': 'ES', 'up': '132.0', 'down': '117.0'}, {'symbol': 'ESRT', 'up': '124.0', 'down': '125.0'}, {'symbol': 'ESS', 'up': '128.0', 'down': '123.0'}, {'symbol': 'ETM', 'up': '97.0', 'down': '140.0'}], 'var_call_sryV4VMl0aL5D97v6sqIF6Dw': [{'symbol': 'EV', 'up': '139.0', 'down': '112.0'}, {'symbol': 'EVT', 'up': '131.0', 'down': '109.0'}, {'symbol': 'EXP', 'up': '127.0', 'down': '124.0'}, {'symbol': 'FMN', 'up': '119.0', 'down': '106.0'}, {'symbol': 'FPAC', 'up': 'nan', 'down': 'nan'}, {'symbol': 'FSM', 'up': '113.0', 'down': '132.0'}, {'symbol': 'GCO', 'up': '119.0', 'down': '126.0'}, {'symbol': 'GD', 'up': '134.0', 'down': '117.0'}], 'var_call_84f6uxn9cz9jBqS8wo5qrLJM': [{'symbol': 'GDL', 'up': '122.0', 'down': '97.0'}, {'symbol': 'GDV', 'up': '126.0', 'down': '110.0'}, {'symbol': 'GEL', 'up': '103.0', 'down': '144.0'}, {'symbol': 'GJP', 'up': '25.0', 'down': '23.0'}, {'symbol': 'GLOB', 'up': '126.0', 'down': '123.0'}, {'symbol': 'GLT', 'up': '117.0', 'down': '130.0'}], 'var_call_MgZqulSlKOIE7WIEzEyObIlu': [{'symbol': 'GOL', 'up': '116.0', 'down': '133.0'}, {'symbol': 'GSLD', 'up': 'nan', 'down': 'nan'}, {'symbol': 'GTY', 'up': '143.0', 'down': '104.0'}, {'symbol': 'GVA', 'up': '120.0', 'down': '131.0'}, {'symbol': 'GWB', 'up': '119.0', 'down': '130.0'}, {'symbol': 'H', 'up': '135.0', 'down': '115.0'}]}

exec(code, env_args)
