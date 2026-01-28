code = """import json
symbols = json.loads(var_call_ptXhpFZ8BINMPs4Fg32qM4rU)['symbols']
chunks = [symbols[i:i+25] for i in range(0, len(symbols), 25)]
queries = []
for chunk in chunks:
    parts = []
    for sym in chunk:
        sym_esc = sym.replace('"','""')
        parts.append("SELECT '{}' AS symbol, \"Open\" AS open, \"Close\" AS close FROM \"{}\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" < '2018-01-01'".format(sym_esc, sym_esc))
    union_sql = " UNION ALL ".join(parts)
    q = (
        "WITH all_rows AS (" + union_sql + ") "
        + "SELECT symbol, "
        + "SUM(CASE WHEN close > open THEN 1 ELSE 0 END) AS up_days, "
        + "SUM(CASE WHEN close < open THEN 1 ELSE 0 END) AS down_days "
        + "FROM all_rows GROUP BY symbol"
    )
    queries.append(q)
print('__RESULT__:')
print(json.dumps({'n_chunks': len(chunks), 'queries': queries}))"""

env_args = {'var_call_QTlIzelgD7c9YCeCM1DsmgUt': 'file_storage/call_QTlIzelgD7c9YCeCM1DsmgUt.json', 'var_call_AceQkdmru6bj7QFVvVXiKhbC': 'file_storage/call_AceQkdmru6bj7QFVvVXiKhbC.json', 'var_call_ptXhpFZ8BINMPs4Fg32qM4rU': {'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'n_symbols': 234}, 'var_call_K4j5SnBNfZsmlZK9Whv71wF6': [{'symbol': 'IBM', 'up_days': '111.0', 'down_days': '136.0'}]}

exec(code, env_args)
