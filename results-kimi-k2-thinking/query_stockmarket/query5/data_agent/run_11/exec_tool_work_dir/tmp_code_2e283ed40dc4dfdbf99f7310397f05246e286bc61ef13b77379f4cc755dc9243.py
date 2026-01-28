code = """import json
import pandas as pd

# Read previous results
stockinfo_path = locals()['var_functions.query_db:0']
if isinstance(stockinfo_path, str):
    with open(stockinfo_path, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = locals()['var_functions.query_db:0']

# Create symbol -> company name mapping
company_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# Read eligible symbols from previous calculation
eligible_symbols = ["SES", "POPE", "PCSB", "CEMI", "PBTS", "MCEP", "MNPR", "ANDA", "IGIC", "WHLR", "AEGN", "CPSR", "YTRA", "MCC", "RHE", "FSTR", "CPSH", "PRPO", "MCHX", "BLCM", "BCDA", "MBII", "GLG", "FCRE", "DWIN", "BKYI", "CFBK", "ALACU", "ATXI", "AMHC", "GRNVU", "BCLI", "AGMH", "CLRB", "CPAAU", "BOSC", "BVSN", "CHFS", "BVXV", "CANF", "CORV", "CSSE", "CUBA", "CVV", "DZSI", "ELSE", "EXPC", "EYEG", "FAMI", "FNCB", "FSBW", "FTFT", "GDYN", "HEPA", "HCCOU", "HNNA", "HQI", "HRTX", "IDEX", "IOTS", "JFK", "LJPC", "MTP", "NEPT", "NKTR", "NSYS", "NXTD", "ONCY", "OSS", "PBMD", "PFMT", "PLXP", "PSTV", "REED", "RLMD", "RMTI", "SHIP", "SNMP", "SPNV", "TANH", "TKAT", "TMDI", "TRIB", "TTOO", "VBIV", "VYGR", "WHLM", "YJ"]

print('__RESULT__:')
print(json.dumps({'symbols_to_process': len(eligible_symbols), 'sample': eligible_symbols[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:5': {'eligible_count': 86, 'sample_symbols': ['SES', 'POPE', 'PCSB', 'CEMI', 'PBTS', 'MCEP', 'MNPR', 'ANDA', 'IGIC', 'WHLR']}, 'var_functions.query_db:6': [{'Date': '2019-01-02', 'High': '7.28000020980835', 'Low': '5.840000152587891'}, {'Date': '2019-01-03', 'High': '7.28000020980835', 'Low': '6.400000095367432'}, {'Date': '2019-01-04', 'High': '8.319999694824219', 'Low': '6.480000019073486'}, {'Date': '2019-01-07', 'High': '7.039999961853027', 'Low': '6.960000038146973'}, {'Date': '2019-01-08', 'High': '7.039999961853027', 'Low': '6.400000095367432'}]}

exec(code, env_args)
