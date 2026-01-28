code = """import json
# Collect query_db result variables
vars_to_check = [
    'var_call_zcTqC92HXZUXXAY2SgSemlTr', 'var_call_zedbo0f2DM2ccUJYLnurVj4p', 'var_call_s7dMOlIQUA69Nrt3DhXSBN8x', 'var_call_N56cHYFaUkg7pMBINhbyC6nE', 'var_call_dH0l397Bt6CrPJUQSwmgoWqv',
    'var_call_ndrOeKJMjZvgzagzChHwCVBo', 'var_call_0YDZssOfhDephqpqsaSWvSff', 'var_call_Wdi1dzC1mcCf8n6MhhZ5YVeL', 'var_call_Azfx4tgELYIW4D04LLcOFqtq', 'var_call_ghxADPajZYKUd8TH3t78lWu1',
    'var_call_Q8n9juM4g1ZMfOJ12E25ht00', 'var_call_8aClZvkdZjMVwT8CvIDWXkip', 'var_call_J0Go5DWzvrqZ956ZpbEr6GAr', 'var_call_u7sTIXJSG54MMXKhP6syZgT3', 'var_call_alhkPoRII4kOZ2K0rPH7bihR',
    'var_call_povb9pqChuetaPVbwvhqwJ6A', 'var_call_OXfWVjTFFCN3nnqePSYJjitu', 'var_call_JoPDydSMKnA4NFUch6dQYKzy', 'var_call_Wb5PTqs9hJsKulwesXWQMIsZ', 'var_call_Vz8ZYalZWfABrp3yclYqzvIi'
]

all_records = []
for varname in vars_to_check:
    if varname in globals():
        data = globals()[varname]
        # data is likely a list of dicts
        if isinstance(data, list):
            for rec in data:
                all_records.append(rec)
# Also include any earlier single results if present
if 'var_call_zcTqC92HXZUXXAY2SgSemlTr' not in globals():
    pass

# Parse records
parsed = []
for r in all_records:
    try:
        sym = r.get('symbol')
        up = r.get('up_days')
        down = r.get('down_days')
        # convert to float if possible
        if up is None or down is None:
            continue
        if isinstance(up, str):
            if up.lower() == 'nan':
                continue
            upf = float(up)
        else:
            upf = float(up)
        if isinstance(down, str):
            if down.lower() == 'nan':
                continue
            downf = float(down)
        else:
            downf = float(down)
        parsed.append({'symbol': sym, 'up_days': int(upf), 'down_days': int(downf)})
    except Exception:
        continue

# Filter up_days > down_days
filtered = [p for p in parsed if p['up_days'] > p['down_days']]
# Sort by up_days desc then symbol
filtered.sort(key=lambda x: (-x['up_days'], x['symbol']))
top5 = filtered[:5]

# Load stockinfo to map symbol to company description
stockinfo_path = var_call_rO65WOPZ1O5Fp8eHGX8wzg5z
with open(stockinfo_path, 'r') as f:
    stockinfo = json.load(f)
# build mapping
sym_to_name = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}

# Prepare final names for top5
final_names = []
for rec in top5:
    name = sym_to_name.get(rec['symbol'], rec['symbol'])
    final_names.append(name)

print("__RESULT__:")
print(json.dumps(final_names))"""

env_args = {'var_call_rO65WOPZ1O5Fp8eHGX8wzg5z': 'file_storage/call_rO65WOPZ1O5Fp8eHGX8wzg5z.json', 'var_call_HmVfyD2JszwBVczi5l8yvuWA': 'file_storage/call_HmVfyD2JszwBVczi5l8yvuWA.json', 'var_call_204C8i9PAPcEmpTUIu9kmxwP': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_sFwvc5IZOFL4Mr5DVTyyq8pd': {'count': 234}, 'var_call_zcTqC92HXZUXXAY2SgSemlTr': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_zedbo0f2DM2ccUJYLnurVj4p': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_s7dMOlIQUA69Nrt3DhXSBN8x': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_N56cHYFaUkg7pMBINhbyC6nE': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_dH0l397Bt6CrPJUQSwmgoWqv': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_ndrOeKJMjZvgzagzChHwCVBo': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_0YDZssOfhDephqpqsaSWvSff': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_Wdi1dzC1mcCf8n6MhhZ5YVeL': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_Azfx4tgELYIW4D04LLcOFqtq': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_ghxADPajZYKUd8TH3t78lWu1': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}], 'var_call_Q8n9juM4g1ZMfOJ12E25ht00': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}], 'var_call_8aClZvkdZjMVwT8CvIDWXkip': [{'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_J0Go5DWzvrqZ956ZpbEr6GAr': [{'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}], 'var_call_u7sTIXJSG54MMXKhP6syZgT3': [{'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_call_alhkPoRII4kOZ2K0rPH7bihR': [{'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}], 'var_call_povb9pqChuetaPVbwvhqwJ6A': [{'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}], 'var_call_OXfWVjTFFCN3nnqePSYJjitu': [{'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}], 'var_call_JoPDydSMKnA4NFUch6dQYKzy': [{'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}], 'var_call_Wb5PTqs9hJsKulwesXWQMIsZ': [{'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}], 'var_call_Vz8ZYalZWfABrp3yclYqzvIi': [{'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}]}

exec(code, env_args)
