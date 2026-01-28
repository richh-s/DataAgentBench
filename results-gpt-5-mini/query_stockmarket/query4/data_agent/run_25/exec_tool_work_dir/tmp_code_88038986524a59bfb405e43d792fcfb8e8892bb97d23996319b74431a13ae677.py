code = """import json
# load query results and stockinfo
with open(var_call_xtVadWw6ZKGMR5c9wljZo8gU, 'r') as f:
    trade_stats = json.load(f)
with open(var_call_Siv61kM1ZxxjZL6JwTXRBBKD, 'r') as f:
    stockinfo = json.load(f)

# build symbol -> company description map
desc_map = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}

# helper to parse up/down days
records = []
for rec in trade_stats:
    sym = rec.get('symbol')
    up = rec.get('up_days')
    down = rec.get('down_days')
    try:
        upf = float(up)
        downf = float(down)
    except:
        continue
    if upf > downf:
        # get company name from description
        desc = desc_map.get(sym, '')
        name = desc
        # extract likely company name before verbs/clauses
        low = desc.lower()
        patterns = [' is part', ' is a ', ' is an ', ' is ', ' specializes', ' specializes in', ' offers', ' provides', ' operates', ' is headquartered', ' is ', ' a leading', ' a provider', ' that ']
        idxs = [low.find(p) for p in patterns if low.find(p) != -1]
        if idxs:
            cut = min(idxs)
            name = desc[:cut].strip()
        else:
            # fallback to before first period or comma
            p1 = desc.find('.')
            p2 = desc.find(',')
            cuts = [i for i in [p1,p2] if i!=-1]
            if cuts:
                name = desc[:min(cuts)].strip()
            else:
                name = desc.strip()
        records.append({'symbol': sym, 'up_days': upf, 'down_days': downf, 'name': name})

# sort by up_days desc, then by up-down difference
records_sorted = sorted(records, key=lambda r: (r['up_days'], r['up_days']-r['down_days']), reverse=True)
Top5 = [r['name'] for r in records_sorted[:5]]

import json
print("__RESULT__:")
print(json.dumps(Top5))"""

env_args = {'var_call_Siv61kM1ZxxjZL6JwTXRBBKD': 'file_storage/call_Siv61kM1ZxxjZL6JwTXRBBKD.json', 'var_call_o5pJhfiSiYi7fwlfUC1c4YWm': 'file_storage/call_o5pJhfiSiYi7fwlfUC1c4YWm.json', 'var_call_9xaGF9WRrBHvfjILvKrFAMhh': {'count_stockinfo_symbols': 234, 'count_intersection': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_call_xtVadWw6ZKGMR5c9wljZo8gU': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}, {'symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}, {'symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}, {'symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}, {'symbol': 'CXH', 'up_days': '126.0', 'down_days': '91.0'}, {'symbol': 'DAC', 'up_days': '66.0', 'down_days': '115.0'}, {'symbol': 'DDS', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'DDT', 'up_days': '118.0', 'down_days': '119.0'}, {'symbol': 'DEO', 'up_days': '131.0', 'down_days': '120.0'}, {'symbol': 'DGX', 'up_days': '129.0', 'down_days': '121.0'}, {'symbol': 'DMB', 'up_days': '132.0', 'down_days': '95.0'}, {'symbol': 'DTQ', 'up_days': '139.0', 'down_days': '98.0'}, {'symbol': 'DXC', 'up_days': '133.0', 'down_days': '116.0'}, {'symbol': 'EARN', 'up_days': '114.0', 'down_days': '124.0'}, {'symbol': 'EBS', 'up_days': '133.0', 'down_days': '115.0'}, {'symbol': 'EGO', 'up_days': '108.0', 'down_days': '123.0'}, {'symbol': 'EGY', 'up_days': '100.0', 'down_days': '128.0'}, {'symbol': 'EIG', 'up_days': '125.0', 'down_days': '116.0'}, {'symbol': 'ELF', 'up_days': '121.0', 'down_days': '129.0'}, {'symbol': 'EMP', 'up_days': '74.0', 'down_days': '100.0'}, {'symbol': 'ENLC', 'up_days': '107.0', 'down_days': '124.0'}, {'symbol': 'EPR', 'up_days': '132.0', 'down_days': '117.0'}, {'symbol': 'EPRT', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'ES', 'up_days': '132.0', 'down_days': '117.0'}, {'symbol': 'ESRT', 'up_days': '124.0', 'down_days': '125.0'}, {'symbol': 'ESS', 'up_days': '128.0', 'down_days': '123.0'}, {'symbol': 'ETM', 'up_days': '97.0', 'down_days': '140.0'}, {'symbol': 'EV', 'up_days': '139.0', 'down_days': '112.0'}, {'symbol': 'EVT', 'up_days': '131.0', 'down_days': '109.0'}, {'symbol': 'EXP', 'up_days': '127.0', 'down_days': '124.0'}, {'symbol': 'FMN', 'up_days': '119.0', 'down_days': '106.0'}, {'symbol': 'FPAC', 'up_days': 'nan', 'down_days': 'nan'}, {'symbol': 'FSM', 'up_days': '113.0', 'down_days': '132.0'}, {'symbol': 'GCO', 'up_days': '119.0', 'down_days': '126.0'}, {'symbol': 'GD', 'up_days': '134.0', 'down_days': '117.0'}, {'symbol': 'GDL', 'up_days': '122.0', 'down_days': '97.0'}]}

exec(code, env_args)
