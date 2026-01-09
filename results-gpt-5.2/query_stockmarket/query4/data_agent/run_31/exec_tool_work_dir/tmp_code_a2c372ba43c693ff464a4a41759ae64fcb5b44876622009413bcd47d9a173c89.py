code = """import json
import pandas as pd

# Build one big UNION ALL query for all symbols with tables (234)
nyse = var_call_OnB6fCK9Z9sc0oRJT1v3w7fS
if isinstance(nyse, str):
    with open(nyse, 'r') as f:
        nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)

tables = var_call_MW2L0mKITaFAwthgkJuiG1GZ
if isinstance(tables, str):
    with open(tables, 'r') as f:
        tables = json.load(f)
tables_set = set(tables)

nyse_df = nyse_df[nyse_df['Symbol'].astype(str).isin(tables_set)].copy()
syms = nyse_df['Symbol'].astype(str).tolist()

# chunk to avoid huge query
step = 50
chunks = [syms[i:i+step] for i in range(0, len(syms), step)]

chunk_queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        parts.append("SELECT '{s}' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(s=sym))
    chunk_queries.append(" UNION ALL ".join(parts))

print('__RESULT__:')
print(json.dumps({'n_chunks': len(chunk_queries), 'chunk_queries': chunk_queries}))"""

env_args = {'var_call_KX5UnkAb3MmDwt33HLN1ZTMv': ['stockinfo'], 'var_call_OnB6fCK9Z9sc0oRJT1v3w7fS': 'file_storage/call_OnB6fCK9Z9sc0oRJT1v3w7fS.json', 'var_call_MW2L0mKITaFAwthgkJuiG1GZ': 'file_storage/call_MW2L0mKITaFAwthgkJuiG1GZ.json', 'var_call_QNUieHkFgdGOcvBQKw3zkWZ5': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_xfxgMp1dHq9vTQ3j9T4Tz4Vh': [{'n': '0', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_zJalEMWRBTGpxtLnWzfRh3US': [{'min_date': '2019-10-24', 'max_date': '2020-04-01', 'n': '110'}], 'var_call_PgasBnre9KCGvZLGEHKYsqcN': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS'], 'var_call_791IFmIwLkeNYw5lnXP6G9ct': [{'Symbol': 'AIN', 'min_date': '1987-09-30', 'max_date': '2020-04-01', 'n': '8192'}], 'var_call_WILST3EJZpFGq40nbzt6vIUJ': [{'Symbol': 'AIV', 'min_date': '1994-07-22', 'max_date': '2020-04-01', 'n': '6470'}], 'var_call_CaI09hrFkvMHnvJbVeJCs7Wk': [{'Symbol': 'AMP', 'min_date': '2005-09-15', 'max_date': '2020-04-01', 'n': '3661'}], 'var_call_8LkKTix4LlKR55fdaSmbONyF': [{'Symbol': 'AMT', 'min_date': '1998-02-27', 'max_date': '2020-04-01', 'n': '5560'}], 'var_call_i8e7q67A0JtLwNupMq9Lj4iE': [{'Symbol': 'CMI', 'min_date': '1973-02-21', 'max_date': '2020-04-01', 'n': '11885'}], 'var_call_TaZhoQgxdrsoQjoIoHyMIdRT': [{'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_P9vP7AG30ouvrygSd0gKzb95': [{'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_2J5Z7SymGRlcOUj0eWyqHfZ2': [{'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}], 'var_call_umG8vblZDeyTF92KBqGz8kr6': [{'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}], 'var_call_sZV1QGGsndMUXsOjVfCLGCM5': [{'Symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}], 'var_call_pYveVfz8nLXPx00gGNTOrTIf': {'n_nyse_nonetf_with_table': 234, 'symbols_first_200': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT']}}

exec(code, env_args)
