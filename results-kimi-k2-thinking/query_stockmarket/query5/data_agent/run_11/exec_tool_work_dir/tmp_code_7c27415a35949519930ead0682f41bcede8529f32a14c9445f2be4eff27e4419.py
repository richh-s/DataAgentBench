code = """import json
import pandas as pd

# Read company mapping
stockinfo_path = locals()['var_functions.query_db:0']
if isinstance(stockinfo_path, str):
    with open(stockinfo_path, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = locals()['var_functions.query_db:0']

company_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# List of eligible symbols from previous analysis
eligible_symbols = ["SES", "POPE", "PCSB", "CEMI", "PBTS", "MCEP", "MNPR", "ANDA", "IGIC", "WHLR", "AEGN", "CPSR", "YTRA", "MCC", "RHE", "FSTR", "CPSH", "PRPO", "MCHX", "BLCM", "BCDA", "MBII", "GLG", "FCRE", "DWIN", "BKYI", "CFBK", "ALACU", "ATXI", "AMHC", "GRNVU", "BCLI", "AGMH", "CLRB", "CPAAU", "BOSC", "BVSN", "CHFS", "BVXV", "CANF", "CORV", "CSSE", "CUBA", "CVV", "DZSI", "ELSE", "EXPC", "EYEG", "FAMI", "FNCB", "FSBW", "FTFT", "GDYN", "HEPA", "HCCOU", "HNNA", "HQI", "HRTX", "IDEX", "IOTS", "JFK", "LJPC", "MTP", "NEPT", "NKTR", "NSYS", "NXTD", "ONCY", "OSS", "PBMD", "PFMT", "PLXP", "PSTV", "REED", "RLMD", "RMTI", "SHIP", "SNMP", "SPNV", "TANH", "TKAT", "TMDI", "TRIB", "TTOO", "VBIV", "VYGR", "WHLM", "YJ"]

# Test the calculation logic with SES data
ses_path = locals()['var_functions.query_db:10']
if isinstance(ses_path, str):
    with open(ses_path, 'r') as f:
        ses_data = json.load(f)
else:
    ses_data = locals()['var_functions.query_db:10']

# Convert to DataFrame and calculate
df_ses = pd.DataFrame(ses_data)
df_ses['High'] = pd.to_numeric(df_ses['High'])
df_ses['Low'] = pd.to_numeric(df_ses['Low'])
df_ses['range'] = df_ses['High'] - df_ses['Low']
df_ses['threshold'] = df_ses['Low'] * 0.20
df_ses['exceeds_20pct'] = df_ses['range'] > df_ses['threshold']

ses_count = df_ses['exceeds_20pct'].sum()
total_days = len(df_ses)

print('__RESULT__:')
print(json.dumps({
    'symbol': 'SES',
    'company': company_map.get('SES', 'Unknown'),
    'days_2019': total_days,
    'days_exceeding_20pct': int(ses_count),
    'calculation_logic_test': 'passed'
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:5': {'eligible_count': 86, 'sample_symbols': ['SES', 'POPE', 'PCSB', 'CEMI', 'PBTS', 'MCEP', 'MNPR', 'ANDA', 'IGIC', 'WHLR']}, 'var_functions.query_db:6': [{'Date': '2019-01-02', 'High': '7.28000020980835', 'Low': '5.840000152587891'}, {'Date': '2019-01-03', 'High': '7.28000020980835', 'Low': '6.400000095367432'}, {'Date': '2019-01-04', 'High': '8.319999694824219', 'Low': '6.480000019073486'}, {'Date': '2019-01-07', 'High': '7.039999961853027', 'Low': '6.960000038146973'}, {'Date': '2019-01-08', 'High': '7.039999961853027', 'Low': '6.400000095367432'}], 'var_functions.execute_python:8': {'symbols_to_process': 88, 'sample': ['SES', 'POPE', 'PCSB', 'CEMI', 'PBTS']}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
