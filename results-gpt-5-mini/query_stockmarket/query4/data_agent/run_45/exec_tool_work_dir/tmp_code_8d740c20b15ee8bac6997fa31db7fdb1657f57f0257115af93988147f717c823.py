code = """import json
# load variables from storage
p_info = var_call_F7ARdSLa3CfMEqYQoQGvzIcb
p_tables = var_call_hVRnygUyYYarq6fpaeURlABC
with open(p_info,'r') as f:
    info = json.load(f)
symbols = [rec['Symbol'] for rec in info]
# filter to those present in stocktrade (var_call_hVR... is the present list)
present = p_tables
# Build union SQL safely
parts = []
for s in present:
    part = (
        "SELECT '" + s.replace("'","''") + "' as symbol, "+
        "SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) as up_count, "+
        "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) as down_count "+
        "FROM \"" + s + "\" "+
        "WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'"
    )
    parts.append(part)
union_sql = ' UNION ALL '.join(parts)
final_sql = 'SELECT symbol, up_count, down_count FROM (' + union_sql + ") as t WHERE up_count>down_count ORDER BY up_count DESC LIMIT 5;"
print('__RESULT__:')
print(json.dumps(final_sql))"""

env_args = {'var_call_F7ARdSLa3CfMEqYQoQGvzIcb': 'file_storage/call_F7ARdSLa3CfMEqYQoQGvzIcb.json', 'var_call_nRCOIQTKtx4ukCguggXBETaj': 'file_storage/call_nRCOIQTKtx4ukCguggXBETaj.json', 'var_call_iiVxyEpARj5wqd3glSsWLWmq': {'symbols_in_stockinfo': 234, 'tables_in_stocktrade': 2753}, 'var_call_cV4zh4nKX1ldk88sDJmyrQHs': {'symbols_present_count': 234, 'sample_present': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_call_hVRnygUyYYarq6fpaeURlABC': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}

exec(code, env_args)
