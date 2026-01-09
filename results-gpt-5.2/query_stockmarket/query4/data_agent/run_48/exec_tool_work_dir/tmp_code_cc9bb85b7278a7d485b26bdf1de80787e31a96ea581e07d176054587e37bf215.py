code = """import json
symbols = json.loads(var_call_ptXhpFZ8BINMPs4Fg32qM4rU)['symbols']

# Build a UNION ALL query over all symbols for 2017
parts = []
for sym in symbols:
    # Escape double quotes by doubling (not expected here)
    sym_esc = sym.replace('"','""')
    parts.append(
        f"SELECT '{sym_esc}' AS symbol, \"Open\" AS open, \"Close\" AS close FROM \"{sym_esc}\" WHERE \"Date\" >= '2017-01-01' AND \"Date\" < '2018-01-01'"
    )

union_sql = "\nUNION ALL\n".join(parts)
final_sql = (
    "WITH all_rows AS (\n" + union_sql + "\n)\n"
    "SELECT symbol,\n"
    "  SUM(CASE WHEN close > open THEN 1 ELSE 0 END) AS up_days,\n"
    "  SUM(CASE WHEN close < open THEN 1 ELSE 0 END) AS down_days\n"
    "FROM all_rows\n"
    "GROUP BY symbol\n"
    "HAVING up_days > down_days\n"
    "ORDER BY (up_days - down_days) DESC, up_days DESC, symbol ASC\n"
    "LIMIT 5;"
)

print('__RESULT__:')
print(json.dumps({'sql': final_sql}))"""

env_args = {'var_call_QTlIzelgD7c9YCeCM1DsmgUt': 'file_storage/call_QTlIzelgD7c9YCeCM1DsmgUt.json', 'var_call_AceQkdmru6bj7QFVvVXiKhbC': 'file_storage/call_AceQkdmru6bj7QFVvVXiKhbC.json', 'var_call_ptXhpFZ8BINMPs4Fg32qM4rU': {'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'n_symbols': 234}}

exec(code, env_args)
