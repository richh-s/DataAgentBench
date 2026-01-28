code = """import json
# Load stockinfo data
data = var_call_5N4V5FdonW2WifZLdnA3VVie
if isinstance(data, str):
    with open(data, 'r') as f:
        stockinfo = json.load(f)
else:
    stockinfo = data

top5 = var_call_iwFyOgFOPCxeG79BpEtC4EFe
if isinstance(top5, str):
    top5 = json.loads(top5)

# Build symbol -> company description map
sym2desc = {r['Symbol']: r.get('Company Description','') for r in stockinfo}

# delimiters to split description and extract company name
delims = [' is part of', ' is an investment', ' is an', ' is ', ' specializes in', ' specializes', ' offers', ' provides', ' operates as', ' operates', ' excels', ' focuses on', ' serving', ' that', ' which']

def extract_name(desc):
    if not desc:
        return ''
    low = desc
    idx = None
    delim_found = None
    for d in delims:
        i = low.find(d)
        if i!=-1:
            if idx is None or i<idx:
                idx = i
                delim_found = d
    if idx is None:
        # fallback: take up to first comma
        i = low.find(',')
        if i!=-1:
            name = low[:i]
        else:
            name = low
    else:
        name = low[:idx]
    name = name.strip()
    # remove trailing punctuation
    name = name.rstrip(' ,.')
    return name

result_names = []
for row in top5:
    sym = row['symbol']
    desc = sym2desc.get(sym, '')
    name = extract_name(desc)
    # If name empty, fallback to symbol
    if not name:
        name = sym
    result_names.append(name)

# Print result as JSON array string
print("__RESULT__:")
print(json.dumps(result_names))"""

env_args = {'var_call_5N4V5FdonW2WifZLdnA3VVie': 'file_storage/call_5N4V5FdonW2WifZLdnA3VVie.json', 'var_call_UB3oQqZ1cT5ORMSgMqW8glAZ': 'file_storage/call_UB3oQqZ1cT5ORMSgMqW8glAZ.json', 'var_call_Iq04oUPiShz0A6N9yWxA1YWt': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'var_call_Rt7J0YvCXuFjUus4Sy1wjAHM': {'count': 234}, 'var_call_1R9xGgnnG7aqKUz4kOk53Ueu': [{'symbol': 'AEFC', 'up': 'nan', 'down': 'nan'}], 'var_call_iTR9LfqAJ0sKjXhxpgeAon5B': [{'symbol': 'AIN', 'up': '143.0', 'down': '101.0'}], 'var_call_KWqRK8eFYDB9oMVwqBCYRqNO': [{'symbol': 'AIV', 'up': '118.0', 'down': '128.0'}], 'var_call_VB6W3zhJsxy004y70jwoAMJO': [{'symbol': 'AIZP', 'up': 'nan', 'down': 'nan'}], 'var_call_ThBvP9UTHrTKQQPoNpsmsf75': [{'symbol': 'AJRD', 'up': '123.0', 'down': '123.0'}], 'var_call_JruAnrtok9zYDdfkVBVgGz0i': [{'symbol': 'AL', 'up': '131.0', 'down': '117.0'}], 'var_call_hEKsqNVCgMQsDzU5uSFR7mEd': [{'symbol': 'AMN', 'up': '134.0', 'down': '111.0'}], 'var_call_mt4bt9fnYRdHzjIx22RVEO4N': [{'symbol': 'AMP', 'up': '141.0', 'down': '110.0'}], 'var_call_ea5dNRsu9RpcLElutqRYuhnm': [{'symbol': 'AMT', 'up': '128.0', 'down': '123.0'}], 'var_call_vRkek1uOwbIYDwZKpPEvWAwl': [{'symbol': 'ARD', 'up': '80.0', 'down': '119.0'}], 'var_call_chKCsfKG6NWMqA1SLFQTDndW': [{'symbol': 'ARGD', 'up': '133.0', 'down': '82.0'}], 'var_call_DFATxBDS14sZtxRcvqx1sGh3': [{'symbol': 'ARLO', 'up': 'nan', 'down': 'nan'}], 'var_call_BxpUPgRD8Q1rilWxWovjFcaT': [{'symbol': 'ASG', 'up': '110.0', 'down': '110.0'}], 'var_call_hMtATwwbYt4qVCuEm0fYTmnU': [{'symbol': 'AVA', 'up': '134.0', 'down': '112.0'}], 'var_call_oY0kJqmaMB08oyjUwd9nzQx1': [{'symbol': 'BANC', 'up': '108.0', 'down': '119.0'}], 'var_call_8m1mQyqYzg33TvrIdSs8tHzw': [{'symbol': 'BBU', 'up': '129.0', 'down': '120.0'}], 'var_call_EkoxAGSpNkx95o2OzkqqpMuu': [{'symbol': 'BBVA', 'up': '126.0', 'down': '104.0'}], 'var_call_QHJdmgkijZMNy6MRzZzV7K9D': [{'symbol': 'BDXA', 'up': '83.0', 'down': '77.0'}], 'var_call_WxhCszGv7XIz1uQggnSweVBZ': [{'symbol': 'BKH', 'up': '134.0', 'down': '115.0'}], 'var_call_PVW1LcZYBEIaaPU7xPuNwF4d': [{'symbol': 'BKT', 'up': '105.0', 'down': '97.0'}], 'var_call_vPs9q3IxvSoeBmEY56ztHlmF': [{'symbol': 'BLD', 'up': '131.0', 'down': '120.0'}], 'var_call_RcRYWNanqekkhFTkHkA9NlKQ': [{'symbol': 'BNS', 'up': '132.0', 'down': '117.0'}], 'var_call_tXlREz14P69Z9N96L3HFwC8J': [{'symbol': 'BV', 'up': 'nan', 'down': 'nan'}], 'var_call_jpmfnKpoHT1IteqkLCnasKG7': [{'symbol': 'BZH', 'up': '127.0', 'down': '123.0'}], 'var_call_LXRVdAAQVxHB2jq3azfASAQo': [{'symbol': 'CADE', 'up': '88.0', 'down': '83.0'}], 'var_call_iwFyOgFOPCxeG79BpEtC4EFe': [{'symbol': 'AIN', 'up': '143.0', 'down': '101.0'}, {'symbol': 'AMP', 'up': '141.0', 'down': '110.0'}, {'symbol': 'AMN', 'up': '134.0', 'down': '111.0'}, {'symbol': 'BKH', 'up': '134.0', 'down': '115.0'}, {'symbol': 'AVA', 'up': '134.0', 'down': '112.0'}]}

exec(code, env_args)
