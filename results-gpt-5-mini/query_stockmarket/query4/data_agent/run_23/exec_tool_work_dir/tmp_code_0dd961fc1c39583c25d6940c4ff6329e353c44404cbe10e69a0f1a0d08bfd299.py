code = """import json, os, math
# Collect all var_call_ variables
gv = globals()
var_keys = [k for k in gv.keys() if k.startswith('var_call_')]
records = []
for k in var_keys:
    v = gv[k]
    # If v is a string that is a path to a json file
    if isinstance(v, str) and os.path.exists(v) and v.endswith('.json'):
        try:
            with open(v, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            continue
    else:
        data = v
    # If data is a string that contains JSON
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception:
            # skip non-json strings
            continue
    # Now if data is a list of dicts, look for symbol/up_count/down_count
    if isinstance(data, list):
        for item in data:
            if not isinstance(item, dict):
                continue
            if 'symbol' in item and ('up_count' in item or 'up' in item):
                # normalize keys
                up = item.get('up_count', item.get('up'))
                down = item.get('down_count', item.get('down'))
                sym = item.get('symbol')
                records.append({'symbol': sym, 'up_count': up, 'down_count': down})

# Load stockinfo mapping (company descriptions). The original stockinfo query result file path is in var_call_WZq9wz2apZmrEaTu4pYKgPLZ
stockinfo = []
path_var = 'var_call_WZq9wz2apZmrEaTu4pYKgPLZ'
if path_var in gv:
    path = gv[path_var]
    if isinstance(path, str) and os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            stockinfo = json.load(f)

sym_to_name = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    name = rec.get('Company Description')
    if sym and name:
        sym_to_name[sym] = name

# Process records: convert counts to numbers, filter out NaNs
clean = []
for r in records:
    sym = r['symbol']
    try:
        up = float(r['up_count'])
    except Exception:
        up = None
    try:
        down = float(r['down_count'])
    except Exception:
        down = None
    if up is None or down is None:
        continue
    if math.isnan(up) or math.isnan(down):
        continue
    if up > down:
        clean.append({'symbol': sym, 'up_count': int(up), 'down_count': int(down)})

# Sort by up_count desc
clean_sorted = sorted(clean, key=lambda x: x['up_count'], reverse=True)
# Take top 5
top5 = clean_sorted[:5]
# Map to company names
result = []
for item in top5:
    sym = item['symbol']
    name = sym_to_name.get(sym, None)
    if name is None:
        name = sym
    result.append({'symbol': sym, 'company_name': name, 'up_count': item['up_count'], 'down_count': item['down_count']})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WZq9wz2apZmrEaTu4pYKgPLZ': 'file_storage/call_WZq9wz2apZmrEaTu4pYKgPLZ.json', 'var_call_yscC6NObrqvHfKXNY6uFGAve': 'file_storage/call_yscC6NObrqvHfKXNY6uFGAve.json', 'var_call_GmXJSp3LJH2xZqpXzfizISmF': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_SUEkX8TQT7At7KZg8ppKR4qI': {'count': 234, 'first_10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_VQYJbxgj7u8yPorluwmW0wQR': [{'symbol': 'AEFC', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_mldPwG0lvYzd8UkaWXx2hkiF': [{'symbol': 'AIN', 'up_count': '143.0', 'down_count': '101.0'}], 'var_call_v2UBceTZb3lW5050k3ZQZB2J': [{'symbol': 'AIV', 'up_count': '118.0', 'down_count': '128.0'}], 'var_call_Q09Esqd8yYJ67od4sM3adbWv': [{'symbol': 'AIZP', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_lUSIkAr9n3OzIpCy3zulrmiV': [{'symbol': 'AJRD', 'up_count': '123.0', 'down_count': '123.0'}], 'var_call_PQEFwZLDtHEBqyid26YbfRlk': [{'symbol': 'AL', 'up_count': '131.0', 'down_count': '117.0'}], 'var_call_EYQZHTPlplytdKTqi0EmFrzQ': [{'symbol': 'AMN', 'up_count': '134.0', 'down_count': '111.0'}], 'var_call_I5FUlkOKRs4eFBZgS1Od63OM': [{'symbol': 'AMP', 'up_count': '141.0', 'down_count': '110.0'}], 'var_call_l3IhWMndSTyWiiU2vAaR52Hg': [{'symbol': 'AMT', 'up_count': '128.0', 'down_count': '123.0'}], 'var_call_hdMyVeszRD79vT3MFQx5iXwM': [{'symbol': 'ARD', 'up_count': '80.0', 'down_count': '119.0'}], 'var_call_STcHZQwZeYab0X4Bj4U7uQ1M': [{'symbol': 'ARGD', 'up_count': '133.0', 'down_count': '82.0'}], 'var_call_5ZlQNumCOrv5wjm6KjgyS0c6': [{'symbol': 'ARLO', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_gFZAHTZR8aBxwCYwc7ZMG8Nk': [{'symbol': 'ASG', 'up_count': '110.0', 'down_count': '110.0'}], 'var_call_dzEGXgNSFKacGB8wjBtic9rH': [{'symbol': 'AVA', 'up_count': '134.0', 'down_count': '112.0'}], 'var_call_PThAmpUCuxOxZUYBVIesbR3O': [{'symbol': 'BANC', 'up_count': '108.0', 'down_count': '119.0'}], 'var_call_FOeoVGAHJxU3WnG5VaWysEhX': [{'symbol': 'BBU', 'up_count': '129.0', 'down_count': '120.0'}], 'var_call_gq8mubQmmeeSpbkiOwUiKNyj': [{'symbol': 'BBVA', 'up_count': '126.0', 'down_count': '104.0'}], 'var_call_biCKvRXww0fmKS0yKvKk6dBz': [{'symbol': 'BDXA', 'up_count': '83.0', 'down_count': '77.0'}], 'var_call_P88fJJS7bVOlKqhShwFetkbR': [{'symbol': 'BKH', 'up_count': '134.0', 'down_count': '115.0'}], 'var_call_skZeJfCQu3gMSukHuJsG35wZ': [{'symbol': 'BKT', 'up_count': '105.0', 'down_count': '97.0'}], 'var_call_qyUcARjuyMw9fPoXXsjslTH0': [{'symbol': 'BLD', 'up_count': '131.0', 'down_count': '120.0'}], 'var_call_w9yfy1pmm44t9jt9UETJnunR': [{'symbol': 'BNS', 'up_count': '132.0', 'down_count': '117.0'}], 'var_call_HsQlwa1VuHByseTQREEbnYEF': [{'symbol': 'BV', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_zUdnNb4b1wdE39qPiNV5CNOl': [{'symbol': 'BZH', 'up_count': '127.0', 'down_count': '123.0'}], 'var_call_TW2Y3UGYpV2lsYnsHG9q13jS': [{'symbol': 'CADE', 'up_count': '88.0', 'down_count': '83.0'}], 'var_call_m91RjNF9AH7EqtXkg3aBbKgc': [{'symbol': 'CAE', 'up_count': '122.0', 'down_count': '117.0'}], 'var_call_wF7D8ZBBlgVvnDhyJrSxD12M': [{'symbol': 'CAF', 'up_count': '131.0', 'down_count': '113.0'}], 'var_call_uvmSafk9m2DDTofJE5tPytZv': [{'symbol': 'CBT', 'up_count': '128.0', 'down_count': '122.0'}], 'var_call_VzelTF0n7cdnbMAJsE8RGL0b': [{'symbol': 'CCC', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_EWOplLUbQAXptfBiSET9Ovef': [{'symbol': 'CCZ', 'up_count': '17.0', 'down_count': '10.0'}], 'var_call_e5hGH57KQyTTCrKy2LyGBl0D': [{'symbol': 'CHAP', 'up_count': '34.0', 'down_count': '23.0'}], 'var_call_chQFVAvhy3ZV4ukqmF1TVvxt': [{'symbol': 'CIA', 'up_count': '130.0', 'down_count': '112.0'}], 'var_call_OLV9bSm8jAMdWVsTZpCDwFnX': [{'symbol': 'CMA', 'up_count': '124.0', 'down_count': '124.0'}], 'var_call_hQK08tjJe8YCDL6Uk5sVIuzh': [{'symbol': 'CMI', 'up_count': '127.0', 'down_count': '123.0'}], 'var_call_PdLK0a2ZmXNlhU50KCHA95XY': [{'symbol': 'CMSA', 'up_count': 'nan', 'down_count': 'nan'}], 'var_call_pxW8oGmh66uA4VHbYbd1ElhZ': [{'symbol': 'CNK', 'up_count': '128.0', 'down_count': '122.0'}], 'var_call_4tP4rRXGk1VdhQsPBLp1G4dv': [{'symbol': 'COTY', 'up_count': '124.0', 'down_count': '123.0'}], 'var_call_M8cVKCy1KLq98jgGSikjW9Ey': [{'symbol': 'CRC', 'up_count': '121.0', 'down_count': '128.0'}], 'var_call_1n6UuQdwaNhBeSdX2wGXILvC': [{'symbol': 'CRM', 'up_count': '137.0', 'down_count': '113.0'}]}

exec(code, env_args)
