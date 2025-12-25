code = """import json

symbols = ["AEFC", "AIN", "AIV", "AIZP", "AJRD", "AL", "AMN", "AMP", "AMT", "ARD", "ARGD", "ARLO", "ASG", "AVA", "BANC", "BBU", "BBVA", "BDXA", "BKH", "BKT", "BLD", "BNS", "BV", "BZH", "CADE", "CAE", "CAF", "CBT", "CCC", "CCZ", "CHAP", "CIA", "CMA", "CMI", "CMSA", "CNK", "COTY", "CRC", "CRM", "CRS", "CSL", "CTS", "CUBE", "CURO", "CVIA", "CVX", "CXH", "DAC", "DDS", "DDT", "DEO", "DGX", "DMB", "DTQ", "DXC", "EARN", "EBS", "EGO", "EGY", "EIG", "ELF", "EMP", "ENLC", "EPR", "EPRT", "ES", "ESRT", "ESS", "ETM", "EV", "EVT", "EXP", "FMN", "FPAC", "FSM", "GCO", "GD", "GDL", "GDV", "GEL", "GJP", "GLOB", "GLT", "GOL", "GSLD", "GTY", "GVA", "GWB", "H", "HBI", "HDB", "HEP", "HIL", "HIO", "HIX", "HLF", "HLT", "HNI", "HRB", "HTFA", "IBM", "IGR", "IHC", "IPG", "IRM", "IT", "JGH", "JHY", "JKS", "JMP", "JNPR", "KMB", "KNX", "KW", "KYN", "LB", "LDOS", "LHC"]
# 115 symbols

sq = chr(39)
dq = chr(34)

queries = []
for sym in symbols:
    q = "SELECT " + sq + sym + sq + " AS Symbol, " + \
        "SUM(CASE WHEN " + dq + "Close" + dq + " > " + dq + "Open" + dq + " THEN 1 ELSE 0 END) AS UpDays, " + \
        "SUM(CASE WHEN " + dq + "Close" + dq + " < " + dq + "Open" + dq + " THEN 1 ELSE 0 END) AS DownDays " + \
        "FROM " + dq + sym + dq + " " + \
        "WHERE " + dq + "Date" + dq + " >= " + sq + "2017-01-01" + sq + " AND " + dq + "Date" + dq + " <= " + sq + "2017-12-31" + sq
    queries.append(q)

full_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-6393703521614786747': 'file_storage/function-call-6393703521614786747.json', 'var_function-call-17168036801476034566': 234, 'var_function-call-14160190749123252694': 'file_storage/function-call-14160190749123252694.json', 'var_function-call-339975677454623462': 'file_storage/function-call-339975677454623462.json', 'var_function-call-3254594062745804831': 52477, 'var_function-call-14365546043785219338': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}

exec(code, env_args)
