code = """# Approach: Check likely candidates systematically
# 1. Get volatility-related ETFs from NYSE Arca
# 2. Check 3x leveraged ETFs that could reach $200
# 3. Sample high-value ETFs

import json

# Load all NYSE Arca ETFs
result_key1 = 'var_functions.query_db:0'
result_file_1 = locals()[result_key1]

with open(result_file_1, 'r') as f:
    etf_list = json.load(f)

# Filter ETFs by symbol patterns that might be high-priced
potential_high_values = []
vix_etfs = []
leveraged_etfs = []

for etf in etf_list:
    symbol = etf['Symbol']
    
    # VIX/volatility ETFs
    if any(x in symbol for x in ['VIX', 'VXX', 'UVXY', 'TVIX', 'SVXY', 'VIXY', 'VIXM']):
        vix_etfs.append(symbol)
    
    # Leveraged ETFs (2x/3x)
    if any(symbol.startswith(x) for x in ['UPRO', 'TQQQ', 'SQQQ', 'TNA', 'TZA', 'FAS', 'FAZ']):
        leveraged_etfs.append(symbol)
    
    # High-value sectors (gold, bonds, etc.)
    if symbol in ['GLD', 'IAU', 'TLT', 'IEF', 'MUB', 'AGG']:
        potential_high_values.append(symbol)

print('__RESULT__:')
print(json.dumps({
    'vix_etfs': vix_etfs,
    'leveraged_etfs': leveraged_etfs,
    'potential_high_values': potential_high_values,
    'total_likely_candidates': len(vix_etfs) + len(leveraged_etfs) + len(potential_high_values)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:10': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}, {'Date': '2015-05-18', 'Adj Close': '192.83792114257807'}, {'Date': '2015-06-23', 'Adj Close': '192.8120574951172'}, {'Date': '2015-05-19', 'Adj Close': '192.77456665039065'}, {'Date': '2015-05-22', 'Adj Close': '192.73838806152344'}, {'Date': '2015-06-22', 'Adj Close': '192.67564392089844'}], 'var_functions.query_db:16': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}], 'var_functions.execute_python:20': {'total_etfs_to_check': 1435, 'first_five_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:22': [{'max_close': '110.42893981933594'}], 'var_functions.query_db:24': [{'max_close': '24.036970138549805'}], 'var_functions.query_db:26': [{'max_close': '163.6190185546875'}], 'var_functions.query_db:28': [], 'var_functions.execute_python:30': {'status': 'Starting check for 1435 ETFs'}, 'var_functions.query_db:32': [{'max_close': '193.5270538330078'}], 'var_functions.query_db:34': [{'max_close': '21.189502716064453'}], 'var_functions.query_db:36': [{'max_close': '41.19669723510742'}], 'var_functions.query_db:38': [{'max_close': '52.82048416137695'}], 'var_functions.execute_python:36': 'file_storage/functions.execute_python:36.json', 'var_functions.execute_python:42': {'message': 'Created list of 1435 NYSE Arca ETFs to check', 'sample': [{'symbol': 'AAAU', 'description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'symbol': 'AADR', 'description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'symbol': 'ABEQ', 'description': 'Absolute Core Strategy ETF is an investment fund designed to offer a diversified portfolio, focusing on strategic asset allocation to optimize returns for investors.'}]}, 'var_functions.query_db:44': [{'max_close': '193.3121490478516', 'min_close': '170.28823852539062', 'avg_close': '187.21235711233956'}], 'var_functions.query_db:46': [{'max_close': '66.95523071289062'}], 'var_functions.query_db:48': [{'max_close': '125.2300033569336'}], 'var_functions.query_db:50': [{'max_close': '116.41609191894533'}], 'var_functions.query_db:52': [{'max_close': '24.133516311645508'}], 'var_functions.query_db:54': [{'max_close': '22.93797874450684'}], 'var_functions.query_db:56': [{'max_close': '39.58057403564453'}], 'var_functions.query_db:58': [{'count': '252'}], 'var_functions.query_db:60': [{'max_close': '507.2368774414063'}], 'var_functions.execute_python:62': {'SQQQ_in_nyse_arca': False, 'checked_against_total': 1435}, 'var_functions.execute_python:64': {'total_nyse_arca_etfs': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:66': [{'max_close': '87.24989318847656'}], 'var_functions.query_db:68': [{'max_close': '507.2368774414063'}], 'var_functions.query_db:70': [{'max_close': '99.8505401611328'}], 'var_functions.query_db:72': [{'Symbol': 'UVXY'}, {'Symbol': 'VIXY'}], 'var_functions.query_db:74': [{'max_close': '81500.0'}], 'var_functions.query_db:76': [{'max_close': '491.0'}], 'var_functions.query_db:78': [{'max_close': '194.8000030517578'}], 'var_functions.execute_python:80': {'batch_1_size': 200, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX', 'CLIX', 'CLTL', 'CMBS', 'CMDY', 'CMF', 'CN', 'CNBS', 'CNRG', 'CNXT', 'COM', 'COMB', 'COPX', 'CORN', 'CORP', 'CPER', 'CPI', 'CQQQ', 'CRAK', 'CRBN', 'CROP', 'CSD', 'CURE', 'CUT', 'CVY', 'CWB', 'CWEB', 'CWI', 'CWS', 'CYB', 'CZA', 'DBA', 'DBAW', 'DBB', 'DBC', 'DBE', 'DBEF', 'DBEH', 'DBEM', 'DBEU', 'DBEZ', 'DBGR', 'DBJP', 'DBLV', 'DBMF', 'DBO', 'DBP', 'DBS', 'DBV', 'DDG', 'DDM', 'DEEF', 'DEF', 'DEM', 'DES', 'DEUS', 'DEW', 'DFE', 'DFEN', 'DFJ', 'DGL', 'DGRO', 'DGS', 'DGT', 'DHS', 'DIA', 'DIAL', 'DIET', 'DIG', 'DIM', 'DIV', 'DIVA', 'DIVO', 'DIVY', 'DJCB', 'DJD', 'DLBR', 'DLN', 'DLS', 'DMDV', 'DMRE', 'DMRI', 'DMRL', 'DMRM', 'DMRS', 'DNL', 'DOG', 'DOGS', 'DOL', 'DON', 'DOO', 'DPST', 'DRIP', 'DRN', 'DRV', 'DRW', 'DSI', 'DSTL', 'DTD', 'DTH', 'DTN']}}

exec(code, env_args)
