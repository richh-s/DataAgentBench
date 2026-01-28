code = """import json, math, re
# Collect all query results stored in variables whose names start with var_call_
records = []
for name, val in list(globals().items()):
    if name.startswith('var_call_') and isinstance(val, list):
        # each val is likely a list of dicts from query_db
        if len(val) > 0 and isinstance(val[0], dict) and 'symbol' in val[0]:
            for rec in val:
                records.append(rec)
# Deduplicate by symbol keeping the first occurrence
by_symbol = {}
for r in records:
    sym = r.get('symbol')
    if sym in by_symbol:
        continue
    up = r.get('up_days')
    down = r.get('down_days')
    # convert to float where possible
    try:
        up_f = float(up)
        down_f = float(down)
    except Exception:
        up_f = None
        down_f = None
    by_symbol[sym] = {'symbol': sym, 'up_days': up_f, 'down_days': down_f}

# Filter symbols with valid counts and up_days > down_days
valid = [v for v in by_symbol.values() if v['up_days'] is not None and v['down_days'] is not None and not math.isnan(v['up_days']) and not math.isnan(v['down_days']) and v['up_days']>v['down_days']]
# Sort by up_days desc
valid_sorted = sorted(valid, key=lambda x: x['up_days'], reverse=True)
top5 = valid_sorted[:5]

# Load stockinfo records to map symbol to company description
stockinfo_path = var_call_toOPi0d7uHXqBrFdsJsgbaoj
with open(stockinfo_path, 'r') as f:
    stockinfo = json.load(f)
info_map = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo}

# Heuristic to extract company name from description
def extract_name(desc):
    if not desc or not isinstance(desc, str):
        return desc
    # Split on common delimiters
    parts = re.split(r'\b(is an?|specializes in|specializes|offers|provides|operates|is part of|is a|,|which|that)\b', desc, flags=re.IGNORECASE)
    name = parts[0].strip()
    return name

result_names = []
for t in top5:
    sym = t['symbol']
    desc = info_map.get(sym, '')
    name = extract_name(desc)
    # fallback to symbol if name empty
    if not name:
        name = sym
    result_names.append(name)

# Prepare output: list of names
print("__RESULT__:")
print(json.dumps(result_names))"""

env_args = {'var_call_toOPi0d7uHXqBrFdsJsgbaoj': 'file_storage/call_toOPi0d7uHXqBrFdsJsgbaoj.json', 'var_call_GpOTNLhRBgAGsYnqs4hCCifR': 'file_storage/call_GpOTNLhRBgAGsYnqs4hCCifR.json', 'var_call_AGG3nKxoD9uV9SoaZIqBrNFD': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_A8rTIWkFFPQ2L6eAL19bezPl': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_Uqtfp9aMc17rVzciWvpFeTjd': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_SzHkdDybDMRWr8jNVgaVeG2A': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_khgln6mE6lqO5dsZEohhKpLS': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_PscpSL3hh7xoLtq0cQ91jMt2': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_sjBQQMgLHRFDcBkyGsPboTqX': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'var_call_hTQ62S10TdBZhRpMk9tHtbc1': 234, 'var_call_9feXomUF9wvowqQC6LPQr7V8': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_TfpyDn8Eg4IS6lVp6AD8tYKy': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_X5NYhOpwbECO2qyX8steIjwW': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_N5J66Ew0ywU3meiBaKq37vCY': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_HxOvOUoAae0FtUwZ2PwOGaQc': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_bpdGJsaHu31btj47rZMIyB7X': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_pUYF16n6xfx93CPYTjot5hG4': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_QIlbpKBOTfC5kMB7LFQeGWLN': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_fKCJeAePGLJfvSEZgKC3EUF5': [{'symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_k7Jc0E2hTIwWNrwLSqQ896oo': [{'symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}], 'var_call_EiEvbHVXN9UlNmCVN3ZqbIQQ': [{'symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}], 'var_call_3vmqcmcAsNXw4ObRbjoPaosX': [{'symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_We1YFOPFrAVpFW5zsUf2F3oY': [{'symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}], 'var_call_hVtllDk1WdsRV8wYTtYNOZ84': [{'symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}], 'var_call_XF1CuEfVhNCwGCKlXJ9QJb4X': [{'symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}], 'var_call_47UpDIgG8DwKRVsk72qmqgbC': [{'symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}], 'var_call_x36dubH91dcUWedi7HXdz0vs': [{'symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}], 'var_call_aG6eRH5yIuhryZvwBNUMNtr9': [{'symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}], 'var_call_KJOCWb1a8DKQmMa2uU9lnE67': [{'symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}], 'var_call_nY3QYwuhZKqhLSTKRX88mNef': [{'symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}], 'var_call_4eEnizX2o3DqTI3rG4J2MhoG': [{'symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}], 'var_call_GcH1J13AdlIFLY8Cemy6YM9i': [{'symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}], 'var_call_Wx9C762JXkc2d86ChG2CwhCY': [{'symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_C4NgSG4fNUXEWD5WJl27D9wA': [{'symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_4O1E2gKhkwg7D2f7JMK6NKuU': [{'symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}], 'var_call_CbvndpUPS5uAjsZ9Yyu9uvps': [{'symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}], 'var_call_kSg1IBWy06l0jpbHpYjBZpHt': [{'symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}], 'var_call_g1xQuumET8tgEf620ZT58WyX': [{'symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}], 'var_call_pAd262PlQYeMl7ZCHF0nDbg4': [{'symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_iewSQAANKiK7VaVFuVBk7kEn': [{'symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}], 'var_call_nVn6joe4Kd1Dd0J7njruWlcv': [{'symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}], 'var_call_5S8zzQzQlrjIja8khFc4vPdg': [{'symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}], 'var_call_oAj6Pz1IaB4ibjpFpAyZO1pg': [{'symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}], 'var_call_5B2PWbNBnZHKMmWOScoTEPkV': [{'symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_URF7vR8atijdok50wqj0ro2W': [{'symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_fPAIUPwnwx0f6MX3rzh4Vd6F': [{'symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}], 'var_call_ZOKDXerCd2Nkl44TqQzw0tku': [{'symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}], 'var_call_yKUVAyZZyPaX5gIdtFEuLQ3n': [{'symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}], 'var_call_bwcqBQiEL35WfWEuYXl4X2Pd': [{'symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}], 'var_call_sudBNaY5oI3dPfa1kwpM6w0N': [{'symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}], 'var_call_59T7IcrCzbexZuhX1wtYeyOV': [{'symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}], 'var_call_cFJu5pgAhd91YIZuupkFBI2E': [{'symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}], 'var_call_Y2rNUiZjLXfgnGgVSmBEw5N5': [{'symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}], 'var_call_ZFh5WsaMgjE5QckLbx9lL9EC': [{'symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}], 'var_call_KOHvZfwD8DQfUskwXYawqV8y': [{'symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_A9VOJZGXHz0IjYrrqJ4naMzE': [{'symbol': 'CVX', 'up_days': '118.0', 'down_days': '132.0'}], 'var_call_FYvKrHsL8INE7JCg87jS0w5g': [{'symbol': 'CXH', 'up_days': '126.0', 'down_days': '91.0'}], 'var_call_a14X4YPjAUhSAH0xkUEwIuSO': [{'symbol': 'DAC', 'up_days': '66.0', 'down_days': '115.0'}], 'var_call_mZABnP7nyWbDF35tY3Lfkg1V': [{'symbol': 'DDS', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_uAs3EHb9L4brjL8OoYcRQMHY': [{'symbol': 'DDT', 'up_days': '118.0', 'down_days': '119.0'}]}

exec(code, env_args)
