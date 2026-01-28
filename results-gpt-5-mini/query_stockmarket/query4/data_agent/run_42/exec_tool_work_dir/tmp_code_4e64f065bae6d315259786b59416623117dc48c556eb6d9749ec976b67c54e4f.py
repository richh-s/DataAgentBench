code = """import json, math
# Collect all var_call_* variables
gl = globals()
vars_keys = [k for k in gl.keys() if k.startswith('var_call_')]
records = []
for k in vars_keys:
    v = gl[k]
    # if v is a string pointing to json file
    if isinstance(v, str) and v.endswith('.json'):
        try:
            with open(v, 'r') as f:
                v = json.load(f)
        except Exception:
            pass
    # if v is a string that contains JSON list, try to parse
    if isinstance(v, str):
        try:
            parsed = json.loads(v)
            v = parsed
        except Exception:
            pass
    # if v is a list of dicts, collect any dicts with symbol/up/down
    if isinstance(v, list):
        for item in v:
            if isinstance(item, dict) and 'symbol' in item and ('up' in item or 'down' in item):
                records.append(item)

# Deduplicate by symbol, prefer numeric up values
by_sym = {}
for r in records:
    sym = r.get('symbol')
    up = r.get('up')
    down = r.get('down')
    # Convert strings like '143.0' or numbers or 'nan'
    def to_num(x):
        if x is None:
            return None
        if isinstance(x, (int, float)):
            return float(x)
        if isinstance(x, str):
            if x.lower()=='nan':
                return None
            try:
                return float(x)
            except:
                return None
        return None
    upn = to_num(up)
    downn = to_num(down)
    existing = by_sym.get(sym)
    # prefer record with numeric up
    if existing is None:
        by_sym[sym] = {'symbol': sym, 'up': upn, 'down': downn}
    else:
        if existing['up'] is None and upn is not None:
            by_sym[sym] = {'symbol': sym, 'up': upn, 'down': downn}

# Filter where up>down
filtered = [v for v in by_sym.values() if v['up'] is not None and v['down'] is not None and v['up']>v['down']]
# Sort by up descending
filtered_sorted = sorted(filtered, key=lambda x: x['up'], reverse=True)
Top5 = filtered_sorted[:5]

# Load stockinfo to map symbol to Company Description
stockinfo = None
if 'var_call_BgwYg1HfC2uTmILKaMuNl1Kc' in gl:
    si = gl['var_call_BgwYg1HfC2uTmILKaMuNl1Kc']
    if isinstance(si, str) and si.endswith('.json'):
        with open(si,'r') as f:
            stockinfo = json.load(f)
    else:
        try:
            stockinfo = si
        except:
            stockinfo = None
# build map
sym_to_name = {}
if isinstance(stockinfo, list):
    for row in stockinfo:
        sym = row.get('Symbol')
        desc = row.get('Company Description')
        sym_to_name[sym] = desc

# Prepare final result: list of company names
result_names = []
for item in Top5:
    sym = item['symbol']
    name = sym_to_name.get(sym, None)
    if name is None:
        name = sym
    result_names.append({'symbol': sym, 'company': name, 'up': item['up'], 'down': item['down']})

print('__RESULT__:')
print(json.dumps(result_names))"""

env_args = {'var_call_BgwYg1HfC2uTmILKaMuNl1Kc': 'file_storage/call_BgwYg1HfC2uTmILKaMuNl1Kc.json', 'var_call_J5nXUxgsJFd2mFEKbycrZPRG': 'file_storage/call_J5nXUxgsJFd2mFEKbycrZPRG.json', 'var_call_hohOiQU7f8uJF8P2C11PqePk': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_qYmU3wDHqCtqe6EtmPDT1nSS': [{'symbol': 'AEFC', 'up': 'nan', 'down': 'nan'}], 'var_call_HcToTQKNtJvuuTJraZ9FWiyZ': [{'symbol': 'AIN', 'up': '143.0', 'down': '101.0'}], 'var_call_8O1qyMpcac8s3oXY1p6kCz2u': [{'symbol': 'AIV', 'up': '118.0', 'down': '128.0'}], 'var_call_jZZmYhXJefUcm3N3qYZJuBeS': [{'symbol': 'AIZP', 'up': 'nan', 'down': 'nan'}], 'var_call_EZPMlRn2VQuy4BytrcSrgUFq': [{'symbol': 'AJRD', 'up': '123.0', 'down': '123.0'}], 'var_call_0ZxXX0IYJOuHelykk8k1Voa9': [{'symbol': 'AL', 'up': '131.0', 'down': '117.0'}], 'var_call_sTxxwLFeXVcaJaanvleJCnNf': [{'symbol': 'AMN', 'up': '134.0', 'down': '111.0'}], 'var_call_Ce1Ifl17gDae2OCtibA6BOcA': [{'symbol': 'AMP', 'up': '141.0', 'down': '110.0'}], 'var_call_FCxanfWCyC2LgvK3fJrCpwo8': [{'symbol': 'AMT', 'up': '128.0', 'down': '123.0'}], 'var_call_hGAxETJBtDP8N9lCCCHdhgEP': [{'symbol': 'ARD', 'up': '80.0', 'down': '119.0'}], 'var_call_thdjypsMjv8yWDnKPFrs31qc': [{'symbol': 'ARGD', 'up': '133.0', 'down': '82.0'}], 'var_call_9xJANCsnJFKXgB9ULqdN9xwW': [{'symbol': 'ARLO', 'up': 'nan', 'down': 'nan'}], 'var_call_AiUX6n5eWpFpNhLrl0ZAUJm2': [{'symbol': 'ASG', 'up': '110.0', 'down': '110.0'}], 'var_call_hTfj9abgaYOMnbgby6VUtocH': [{'symbol': 'AVA', 'up': '134.0', 'down': '112.0'}], 'var_call_J4HAU40ZogCDTIeDPSGitzgN': [{'symbol': 'BANC', 'up': '108.0', 'down': '119.0'}], 'var_call_KkuLhwCV3q7md6sXLSDRQUKO': [{'symbol': 'BBU', 'up': '129.0', 'down': '120.0'}], 'var_call_zdEyY0eB50vtVpzUlr98UEqr': [{'symbol': 'BBVA', 'up': '126.0', 'down': '104.0'}], 'var_call_tRV69Uf1UW0661bCoFF43GE0': [{'symbol': 'BDXA', 'up': '83.0', 'down': '77.0'}], 'var_call_Kd8uzWcySn8JJnLGrag5uCnk': [{'symbol': 'BKH', 'up': '134.0', 'down': '115.0'}], 'var_call_yB7Up3E8pRCTyBUzolRE09GA': [{'symbol': 'BKT', 'up': '105.0', 'down': '97.0'}], 'var_call_oZLtRxDRAFvSsKkXyTjvr0NT': [{'symbol': 'BLD', 'up': '131.0', 'down': '120.0'}], 'var_call_fHglgp9VuWdyVpOqyReGGq32': [{'symbol': 'BNS', 'up': '132.0', 'down': '117.0'}], 'var_call_jNZhcq1EIOsFb5lPFJr4WZNB': [{'symbol': 'BV', 'up': 'nan', 'down': 'nan'}], 'var_call_wesf9xCFiU0tIGTiUqXUlbJ0': [{'symbol': 'BZH', 'up': '127.0', 'down': '123.0'}], 'var_call_Ykxbcy3lxQTm1V7YCKvj6Jsv': [{'symbol': 'CADE', 'up': '88.0', 'down': '83.0'}], 'var_call_TEITavtZLO2Bcpt9fykivRYi': [{'symbol': 'CAE', 'up': '122.0', 'down': '117.0'}], 'var_call_4BFNmNiFTZJMQ46oa3yUsaNb': [{'symbol': 'CAF', 'up': '131.0', 'down': '113.0'}], 'var_call_HJRIN5t3OJeSdGb82CdSifkN': [{'symbol': 'CBT', 'up': '128.0', 'down': '122.0'}], 'var_call_mlaDCgLVcvd4FGbhEC324VgX': [{'symbol': 'CCC', 'up': 'nan', 'down': 'nan'}], 'var_call_tgHhcmbA1sX5qlZOIJ6qD8di': [{'symbol': 'CCZ', 'up': '17.0', 'down': '10.0'}], 'var_call_lJKcZFQnWCUc8RE90QiKDCaF': [{'symbol': 'CHAP', 'up': '34.0', 'down': '23.0'}], 'var_call_NFVAs6eb1DJ3Jkww5YxD7aoy': [{'symbol': 'CIA', 'up': '130.0', 'down': '112.0'}], 'var_call_72o9XXfzkFZ5rHBEK0h1lYe5': [{'symbol': 'CMA', 'up': '124.0', 'down': '124.0'}], 'var_call_DWYuyxRK42ix1bapTd4jk2Cf': [{'symbol': 'CMI', 'up': '127.0', 'down': '123.0'}], 'var_call_ugPTbWnDJN39fRcAn4tyPeW6': [{'symbol': 'CMSA', 'up': 'nan', 'down': 'nan'}], 'var_call_u4ZOdb02Y5IYqbrgutQrIWDF': [{'symbol': 'CNK', 'up': '128.0', 'down': '122.0'}]}

exec(code, env_args)
