code = """import json
import duckdb

# Read NYSE Arca ETF symbols
arca_file = locals()['var_functions.query_db:0']
with open(arca_file, 'r') as f:
    arca_data = json.load(f)

symbols = [item['Symbol'] for item in arca_data]

# Connect to database
conn = duckdb.connect('/mnt/data/stocktrade_database.duckdb')

result = []
errors = 0

for i, symbol in enumerate(symbols):
    try:
        q = "SELECT MAX(\"Adj Close\") as max_adj FROM \"" + symbol + "\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
        row = conn.execute(q).fetchone()
        if row and row[0] is not None and float(row[0]) > 200:
            result.append({'symbol': symbol, 'max_price': round(float(row[0]), 2)})
    except:
        errors += 1

conn.close()

result.sort(key=lambda x: x['max_price'], reverse=True)

output = {
    'total_etfs': len(symbols),
    'errors': errors,
    'over_200': result,
    'count_over_200': len(result)
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:10': {'arca_etf_count': 1435, 'available_in_trade_db': 1435, 'first_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': {'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:18': [], 'var_functions.query_db:22': [{'Date': '2015-12-31', 'Adj Close': '37.5300407409668'}, {'Date': '2015-12-30', 'Adj Close': '37.87096405029297'}, {'Date': '2015-12-29', 'Adj Close': '38.065765380859375'}, {'Date': '2015-12-28', 'Adj Close': '37.403419494628906'}, {'Date': '2015-12-24', 'Adj Close': '37.98784637451172'}, {'Date': '2015-12-23', 'Adj Close': '37.865116119384766'}, {'Date': '2015-12-22', 'Adj Close': '37.54372787475586'}, {'Date': '2015-12-21', 'Adj Close': '36.73539733886719'}, {'Date': '2015-12-18', 'Adj Close': '37.183387756347656'}, {'Date': '2015-12-17', 'Adj Close': '37.29051208496094'}], 'var_functions.execute_python:24': {'total_symbols_to_check': 1435, 'message': 'Ready to check which ETFs had Adj Close > 200 in 2015'}, 'var_functions.query_db:26': [], 'var_functions.query_db:28': [{'max_close': '193.3121490478516', 'min_close': '170.28823852539062'}], 'var_functions.query_db:30': [{'Adj Close': '101.45999908447266', 'Close': '101.45999908447266'}], 'var_functions.query_db:32': [{'max_adj_close': '125.2300033569336'}], 'var_functions.execute_python:34': {'total_arca_etfs': 1435, 'checking_subset': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:38': {'checking_symbols': ['AGG', 'AGQ', 'BIBL', 'BIZD', 'BNDC', 'BOUT', 'CHIC', 'CHIL', 'CPER', 'DBEF', 'DBLV', 'DBS', 'DGS', 'DHS', 'DIA', 'DMDV', 'DOO', 'DRIP', 'DTH', 'DWM', 'DWX', 'EELV', 'EEM', 'EFA', 'EMLP', 'EUO', 'EZJ', 'FCG', 'FDLO', 'FDM', 'FITE', 'FLTW', 'FNI', 'FXB', 'FXE', 'FXH', 'FXP', 'GBDV', 'GBIL', 'GBUY', 'GDXJ', 'GLD', 'GLIF', 'GMAN', 'GRES', 'HAWX', 'HYG', 'HYLV', 'HYS', 'IAK', 'IAU', 'IBDQ', 'IBMJ', 'IGM', 'IIGD', 'IVW', 'IWC', 'IWM', 'IXSE', 'JHMM', 'JKE', 'JMIN', 'JVAL', 'KCNY', 'KGRN', 'KOL', 'LABD', 'LQD', 'LRGF', 'LRNZ', 'MXDU', 'OUSM', 'OVS', 'PACA', 'PSP', 'PWB', 'QAI', 'QED', 'QQQ', 'RXL', 'SGDM', 'SHYG', 'SLV', 'SMEZ', 'SOXL', 'SPDN', 'SPHQ', 'SPMO', 'SPVU', 'SPXL', 'SPY', 'SSPY', 'TECL', 'TFI', 'TLT', 'TPYP', 'TQQQ', 'TYBS', 'UDOW', 'UPRO', 'URA', 'UTRN', 'VBK', 'VBND', 'VEGN', 'VEU', 'VIXY', 'VO', 'VOOG', 'VXX', 'WBIG', 'XBI', 'XLF', 'XMVM', 'XOUT', 'XSMO', 'ZHOK'], 'count': 117}, 'var_functions.query_db:42': [{'max_adj_close': '21.189502716064453'}], 'var_functions.query_db:44': [{'max_adj_close': '22.93797874450684'}], 'var_functions.query_db:50': [{'max("Adj Close")': '98.26229858398438'}], 'var_functions.query_db:54': [{'max_price': '12.619999885559082'}]}

exec(code, env_args)
