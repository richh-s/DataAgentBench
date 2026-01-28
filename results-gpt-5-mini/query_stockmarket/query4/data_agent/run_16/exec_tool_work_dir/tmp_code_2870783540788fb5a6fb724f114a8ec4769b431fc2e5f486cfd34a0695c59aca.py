code = """import json, os, math
# Collect all variables in the exec environment that start with var_call_
collected = []
for name, val in globals().items():
    if name.startswith('var_call_'):
        # val may be a path to a json file (string) or the actual data (list/dict)
        try:
            if isinstance(val, str) and os.path.exists(val):
                with open(val, 'r') as f:
                    data = json.load(f)
            else:
                data = val
        except Exception:
            continue
        # data may be a list of records or a dict
        if isinstance(data, list):
            collected.append(data)
        elif isinstance(data, dict):
            collected.append([data])

# Flatten collected lists
records = []
for lst in collected:
    for rec in lst:
        # We're interested in records with 'symbol' key from query_db results
        if isinstance(rec, dict) and 'symbol' in rec:
            records.append(rec)

# Normalize up/down to numbers, skip if nan or missing
norm = []
for r in records:
    s = r.get('symbol')
    try:
        up = r.get('up_days')
        down = r.get('down_days')
        if up is None or down is None:
            continue
        # up/down may be strings like "143.0" or "nan"
        if isinstance(up, str):
            if up.lower() == 'nan':
                continue
            up = float(up)
        if isinstance(down, str):
            if down.lower() == 'nan':
                continue
            down = float(down)
        up = float(up); down = float(down)
    except Exception:
        continue
    norm.append({'symbol': s, 'up_days': int(up), 'down_days': int(down)})

# Aggregate by symbol (in case duplicates)
agg = {}
for r in norm:
    s = r['symbol']
    if s not in agg:
        agg[s] = {'up_days': 0, 'down_days': 0}
    agg[s]['up_days'] += r['up_days']
    agg[s]['down_days'] += r['down_days']

rows = [{'symbol': s, 'up_days': v['up_days'], 'down_days': v['down_days']} for s,v in agg.items()]
# Filter where up_days > down_days
rows = [r for r in rows if r['up_days'] > r['down_days']]
# Sort by up_days desc
rows.sort(key=lambda x: x['up_days'], reverse=True)

top5 = rows[:5]

# Load company descriptions from stockinfo file
stockinfo = []
try:
    if isinstance(var_call_nELGdyvPXxMt9K3rUNiloF4h, str) and os.path.exists(var_call_nELGdyvPXxMt9K3rUNiloF4h):
        with open(var_call_nELGdyvPXxMt9K3rUNiloF4h, 'r') as f:
            stockinfo = json.load(f)
    else:
        stockinfo = var_call_nELGdyvPXxMt9K3rUNiloF4h
except Exception:
    stockinfo = []

sym_to_name = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo}

result_names = []
for r in top5:
    name = sym_to_name.get(r['symbol'], '')
    # If company description contains full name at start, try to extract the company name (before first ' is ' or ' specializes' or ' offers')
    comp = name
    if comp:
        for sep in [' specializes', ' offers', ' is ', ' provides', ' operates', ' that ']:
            if sep in comp:
                comp = comp.split(sep)[0]
                break
        comp = comp.strip(', ')
    result_names.append(comp if comp else r['symbol'])

print('__RESULT__:')
print(json.dumps(result_names))"""

env_args = {'var_call_nELGdyvPXxMt9K3rUNiloF4h': 'file_storage/call_nELGdyvPXxMt9K3rUNiloF4h.json', 'var_call_OxR5V4zYOQmYrDGwhBhWPqi7': 'file_storage/call_OxR5V4zYOQmYrDGwhBhWPqi7.json', 'var_call_LhZBRkhnWZtgcltCUmMOfIF7': {'n_info': 234, 'n_tables': 2753}, 'var_call_I8BXF6ocEYErU0wbgzxnZ8PI': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_sJkSQjBDdEVdp2mz4oBpuVjA': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_7Da31yJlqiCoC913zF9FKbdr': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_CpYnAOikgytjg2QRlEHkZk3i': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_YtxMsxnk7OqBOGJospNL42pO': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_SlESxmdL7cXtjbYzvx3oRKqY': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_t43Y3mDMlfNT50FxY1xkx0PA': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_n6xxQ2u18cIzf4cANk1ZkhDL': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_NCw3KRilMpJgqfK4Ty3EYYLj': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_9ElumbpFfkOFpK0EaJsl9CLq': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_ydJRnzMJiBMXT1ZyQ2HxrPMI': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}], 'var_call_cUxWmhZY2DlBa6l1NNyTLJPx': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}], 'var_call_ueYBJrvSxCfAkT9B427T6duV': [{'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_NDgUT47imLWO7vLL90KiDaif': [{'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}], 'var_call_PP0XRxku5F5m14bxijiBK0I3': [{'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_call_JH2zsGvazdSVDo7pHutOcLlJ': [{'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}], 'var_call_IUwldIqCkVn7pjzYXorVaywh': [{'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}], 'var_call_UDhL3RgrEzksWB8QO5jF7nh2': [{'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}], 'var_call_QSj4f0B4yhLKgEJcHfl7nrXi': [{'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}], 'var_call_xp7CY0228jJQq5Smuh2tnsnS': [{'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}], 'var_call_2Aze8fAUSKLbKmTbGFnFJf94': [{'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}], 'var_call_nZGKH5mwCJRoDbtCMb7Vnc2z': [{'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}], 'var_call_qTMSky0Qe16MbhcMltY6uq5v': [{'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}], 'var_call_nEwxpMFKE2RqVIcf1e8x0krY': [{'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_VPj17zKBUKnlWikL0oEuhH9V': [{'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_E4YbvWYUKsx9funbxaTSJHyQ': [{'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}], 'var_call_IcTs8U1mq9xUlm3rs6vTXYK6': [{'symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}], 'var_call_PY9ppjW1LOQubr78jNVnHY9B': [{'symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}], 'var_call_kgBM30ouMhBZktGzmIbC9sPT': [{'symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}], 'var_call_nS58XXTyLlAuDIXM36sVXCCX': [{'symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_j5byZdVZvL4waf42yhacVMDK': [{'symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}], 'var_call_uv4Z8qFYq3qGnY89DCKnYHly': [{'symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}], 'var_call_qfmAnLEw9elTivoPIA4JV1yt': [{'symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}], 'var_call_qif6jYmPD09wCLdpY4hBsGcN': [{'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}], 'var_call_zXxb26vNhyZtzWv1uaRb063G': [{'symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_DYJSPTj6csO3uaqKArdBunYb': [{'symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_DXehVpnShHmZ8hBkwDoojrRo': [{'symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}]}

exec(code, env_args)
