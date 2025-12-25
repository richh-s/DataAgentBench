code = """import json

# Load relevant symbols
relevant_symbols = json.loads(locals()['var_function-call-17855858328423130321'])

# Construct query
queries = []
for sym in relevant_symbols:
    # Need to quote the table name just in case, though symbols are usually safe.
    # Also duckdb is case insensitive for table names usually but better be safe.
    # Note: The table names in duckdb seem to be exactly the symbol names.
    # I should put double quotes around table names.
    q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{sym}\" WHERE Date BETWEEN '2017-01-01' AND '2017-12-31'"
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-13162311836547151521': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-12422574718348653119': 'file_storage/function-call-12422574718348653119.json', 'var_function-call-7361097673943553959': 'file_storage/function-call-7361097673943553959.json', 'var_function-call-17855858328423130321': ['CMSA', 'PSXP', 'SMP', 'LDOS', 'GWB', 'LOMA', 'SRF', 'MR', 'BBVA', 'BDXA', 'MANU', 'MNE', 'CRC', 'MDLY', 'PIM', 'BLD', 'CHAP', 'VVI', 'VRT', 'SAM', 'MFO', 'LHC', 'X', 'VHI', 'HBI', 'PRSP', 'SI', 'KW', 'NJV', 'PPG', 'HLF', 'TUFN', 'AIV', 'GLT', 'IHC', 'RBC', 'CVX', 'ELF', 'CMA', 'EMP', 'FSM', 'BKT', 'TRV', 'OCFT', 'KMB', 'RES', 'MHE', 'LHX', 'AL', 'VGR', 'WOR', 'YEXT', 'PGR', 'RH', 'AVA', 'TBB', 'HTFA', 'TPH', 'PLAN', 'ESRT', 'GOL', 'DTQ', 'ROL', 'AMN', 'SFUN', 'SYX', 'DGX', 'HLT', 'EV', 'QUAD', 'GD', 'MDLX', 'SPOT', 'H', 'PNM', 'TLYS', 'NFH', 'AMP', 'USX', 'SOL', 'HIO', 'SJM', 'KNX', 'HDB', 'UIS', 'BKH', 'CRS', 'CCC', 'ORN', 'UHT', 'GLOB', 'KYN', 'EPR', 'PAG', 'BBU', 'CXH', 'DDS', 'NRUC', 'ROG', 'TWTR', 'SCU', 'DMB', 'MYD', 'CAE', 'RMT', 'DDT', 'CCZ', 'SAF', 'EVT', 'JGH', 'BANC', 'MGR', 'NXN', 'IT', 'IPG', 'ES', 'LB', 'MLI', 'TGP', 'HEP', 'CNK', 'CAF', 'RCB', 'AJRD', 'EARN', 'ORCL', 'ETM', 'SRC', 'CURO', 'AIZP', 'JNPR', 'RCI', 'HIX', 'PMT', 'PLNT', 'BV', 'MTD', 'HIL', 'ZNH', 'EPRT', 'ENLC', 'MS', 'SJT', 'BZH', 'ASG', 'MED', 'NGG', 'CIA', 'PSV', 'TDJ', 'IRM', 'IGR', 'IBM', 'EIG', 'GDV', 'FPAC', 'GCO', 'GDL', 'PFE', 'JKS', 'CUBE', 'VIV', 'GJP', 'PFSI', 'AIN', 'PKE', 'WPG', 'MKC', 'ARGD', 'EBS', 'AEFC', 'HNI', 'FMN', 'NUE', 'ORA', 'QTS', 'RPAI', 'GVA', 'NNI', 'GSLD', 'SJW', 'TTI', 'RWT', 'SAIL', 'MIY', 'CBT', 'ZTR', 'EGY', 'HRB', 'CADE', 'STG', 'CVIA', 'MGU', 'STL', 'STON', 'AMT', 'PBI', 'SITC', 'ARLO', 'RQI', 'GEL', 'SRT', 'VKQ', 'BNS', 'NNY', 'ORAN', 'SBR', 'SHAK', 'ARD', 'SSD', 'CSL', 'UTL', 'VET', 'GTY', 'JMP', 'PRTY', 'WSM', 'CRM', 'DXC', 'SLF', 'COTY', 'OEC', 'REXR', 'ESS', 'CTS', 'CMI', 'RPM', 'TNC', 'DAC', 'JHY', 'DEO', 'EGO', 'EXP', 'TCP']}

exec(code, env_args)
