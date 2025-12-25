code = """import json

# Load stock trade results
with open(locals()['var_function-call-5604540155825833582'], 'r') as f:
    trade_data = json.load(f)

# Load stock info to map names
with open(locals()['var_function-call-12422574718348653119'], 'r') as f:
    stock_info_list = json.load(f)

# Create a map from Symbol to Company Description
sym_to_name = {item['Symbol']: item['Company Description'] for item in stock_info_list}

# Process trade data
candidates = []
for row in trade_data:
    try:
        if row['Up'] == 'nan' or row['Down'] == 'nan' or row['Up'] is None or row['Down'] is None:
            continue
        up = float(row['Up'])
        down = float(row['Down'])
        
        if up > down:
            candidates.append({
                'Symbol': row['Sym'],
                'Up': int(up),
                'Down': int(down),
                'Diff': int(up - down),
                'Name': sym_to_name.get(row['Sym'], "Unknown")
            })
    except ValueError:
        continue

# Sort by Up days descending, then Diff descending
candidates.sort(key=lambda x: (x['Up'], x['Diff']), reverse=True)

top_5 = candidates[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-13162311836547151521': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-12422574718348653119': 'file_storage/function-call-12422574718348653119.json', 'var_function-call-7361097673943553959': 'file_storage/function-call-7361097673943553959.json', 'var_function-call-17855858328423130321': ['CMSA', 'PSXP', 'SMP', 'LDOS', 'GWB', 'LOMA', 'SRF', 'MR', 'BBVA', 'BDXA', 'MANU', 'MNE', 'CRC', 'MDLY', 'PIM', 'BLD', 'CHAP', 'VVI', 'VRT', 'SAM', 'MFO', 'LHC', 'X', 'VHI', 'HBI', 'PRSP', 'SI', 'KW', 'NJV', 'PPG', 'HLF', 'TUFN', 'AIV', 'GLT', 'IHC', 'RBC', 'CVX', 'ELF', 'CMA', 'EMP', 'FSM', 'BKT', 'TRV', 'OCFT', 'KMB', 'RES', 'MHE', 'LHX', 'AL', 'VGR', 'WOR', 'YEXT', 'PGR', 'RH', 'AVA', 'TBB', 'HTFA', 'TPH', 'PLAN', 'ESRT', 'GOL', 'DTQ', 'ROL', 'AMN', 'SFUN', 'SYX', 'DGX', 'HLT', 'EV', 'QUAD', 'GD', 'MDLX', 'SPOT', 'H', 'PNM', 'TLYS', 'NFH', 'AMP', 'USX', 'SOL', 'HIO', 'SJM', 'KNX', 'HDB', 'UIS', 'BKH', 'CRS', 'CCC', 'ORN', 'UHT', 'GLOB', 'KYN', 'EPR', 'PAG', 'BBU', 'CXH', 'DDS', 'NRUC', 'ROG', 'TWTR', 'SCU', 'DMB', 'MYD', 'CAE', 'RMT', 'DDT', 'CCZ', 'SAF', 'EVT', 'JGH', 'BANC', 'MGR', 'NXN', 'IT', 'IPG', 'ES', 'LB', 'MLI', 'TGP', 'HEP', 'CNK', 'CAF', 'RCB', 'AJRD', 'EARN', 'ORCL', 'ETM', 'SRC', 'CURO', 'AIZP', 'JNPR', 'RCI', 'HIX', 'PMT', 'PLNT', 'BV', 'MTD', 'HIL', 'ZNH', 'EPRT', 'ENLC', 'MS', 'SJT', 'BZH', 'ASG', 'MED', 'NGG', 'CIA', 'PSV', 'TDJ', 'IRM', 'IGR', 'IBM', 'EIG', 'GDV', 'FPAC', 'GCO', 'GDL', 'PFE', 'JKS', 'CUBE', 'VIV', 'GJP', 'PFSI', 'AIN', 'PKE', 'WPG', 'MKC', 'ARGD', 'EBS', 'AEFC', 'HNI', 'FMN', 'NUE', 'ORA', 'QTS', 'RPAI', 'GVA', 'NNI', 'GSLD', 'SJW', 'TTI', 'RWT', 'SAIL', 'MIY', 'CBT', 'ZTR', 'EGY', 'HRB', 'CADE', 'STG', 'CVIA', 'MGU', 'STL', 'STON', 'AMT', 'PBI', 'SITC', 'ARLO', 'RQI', 'GEL', 'SRT', 'VKQ', 'BNS', 'NNY', 'ORAN', 'SBR', 'SHAK', 'ARD', 'SSD', 'CSL', 'UTL', 'VET', 'GTY', 'JMP', 'PRTY', 'WSM', 'CRM', 'DXC', 'SLF', 'COTY', 'OEC', 'REXR', 'ESS', 'CTS', 'CMI', 'RPM', 'TNC', 'DAC', 'JHY', 'DEO', 'EGO', 'EXP', 'TCP'], 'var_function-call-7505108791445030801': 'file_storage/function-call-7505108791445030801.json', 'var_function-call-5604540155825833582': 'file_storage/function-call-5604540155825833582.json'}

exec(code, env_args)
