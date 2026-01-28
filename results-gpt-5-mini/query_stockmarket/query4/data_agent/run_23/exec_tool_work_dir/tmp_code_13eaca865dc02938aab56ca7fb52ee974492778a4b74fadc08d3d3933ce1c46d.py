code = """import json
p1 = var_call_WZq9wz2apZmrEaTu4pYKgPLZ
p2 = var_call_yscC6NObrqvHfKXNY6uFGAve

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

stockinfo = load_json(p1)
trade_tables = load_json(p2)

symbols_stockinfo = [rec['Symbol'] for rec in stockinfo]
symbols = sorted(list(set(symbols_stockinfo).intersection(set(trade_tables))))

frags = []
for s in symbols:
    frag = ("SELECT '{sym}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_count, "
            "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_count FROM \"{sym}\" "
            "WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'").format(sym=s)
    frags.append(frag)

sql = "\nUNION ALL\n".join(frags)
final_sql = "SELECT symbol, up_count, down_count FROM (\n" + sql + "\n) AS t WHERE up_count>down_count ORDER BY up_count DESC LIMIT 5;"

print("__RESULT__:")
print(json.dumps(final_sql))"""

env_args = {'var_call_WZq9wz2apZmrEaTu4pYKgPLZ': 'file_storage/call_WZq9wz2apZmrEaTu4pYKgPLZ.json', 'var_call_yscC6NObrqvHfKXNY6uFGAve': 'file_storage/call_yscC6NObrqvHfKXNY6uFGAve.json', 'var_call_GmXJSp3LJH2xZqpXzfizISmF': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}

exec(code, env_args)
