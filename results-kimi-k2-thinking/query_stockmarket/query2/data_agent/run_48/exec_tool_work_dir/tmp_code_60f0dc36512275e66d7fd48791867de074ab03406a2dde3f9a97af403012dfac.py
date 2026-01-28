code = """import json

# First, let's get all the data we need
nyse_file = locals()['var_functions.query_db:30']
trade_file = locals()['var_functions.list_db:16']

with open(nyse_file, 'r') as f:
    symbols_data = json.load(f)
nyse_arca_etfs = [item['Symbol'] for item in symbols_data]

with open(trade_file, 'r') as f:
    all_tables = json.load(f)

# Create a comprehensive sampling strategy based on:
# 1. ETF categories that are more likely to have high prices
# 2. Historical knowledge of ETF price ranges
# 3. Focus on ETFs that existed before 2015

sampling_strategy = {
    'bond_etfs': [],
    'commodity_etfs': [],
    'currency_etfs': [],
    'leveraged_etfs': [],
    'index_etfs': [],
    'other_etfs': []
}

# Categorize ETFs based on symbol patterns
for etf in nyse_arca_etfs:
    if len(etf) == 3:  # 3-letter symbols are often older, established ETFs
        if any(x in etf for x in ['B', 'L', 'T', 'S']):  # Bond indicators
            sampling_strategy['bond_etfs'].append(etf)
        elif any(x in etf for x in ['G', 'S', 'O', 'U']):  # Commodity indicators  
            sampling_strategy['commodity_etfs'].append(etf)
        elif any(x in etf for x in ['F', 'X']):  # Currency indicators
            sampling_strategy['currency_etfs'].append(etf)
        elif etf.isupper() and not any(c.isdigit() for c in etf):  # Regular equity ETFs
            sampling_strategy['index_etfs'].append(etf)
        else:
            sampling_strategy['other_etfs'].append(etf)
    else:
        # Longer symbols - often newer or specialty ETFs
        if any(prefix in etf for prefix in ['TLT', 'EDV', 'GLD', 'SLV', 'IAU', 'HYG', 'LQD']):
            if 'TLT' in etf or 'EDV' in etf:
                sampling_strategy['bond_etfs'].append(etf)
            elif 'GLD' in etf or 'SLV' in etf or 'IAU' in etf:
                sampling_strategy['commodity_etfs'].append(etf)
            elif 'HYG' in etf or 'LQD' in etf:
                sampling_strategy['bond_etfs'].append(etf)
        else:
            sampling_strategy['other_etfs'].append(etf)

# Let's refine to check actual candidates that existed pre-2015
high_prob_candidates = [
    # Treasury/Bond ETFs - these can have high unit values
    'TLT', 'EDV', 'TLO', 'VGIT', 'VGLT', 'IGLB', 'SPTL', 'SCHR',
    
    # Some older commodity ETFs
    'GLD', 'IAU', 'SLV', 'USO', 'UNG', 
    
    # Currency ETFs (some trade at high values)
    'FXE', 'FXY', 'FXF', 'UUP', 'UDN',
    
    # Large index ETFs (pre-split)
    'SPY', 'DIA', 'QQQ', 'MDY', 'IVV', 'VOO',
    
    # Bond/Fixed Income
    'HYG', 'LQD', 'MUB', 'BKLN', 'BIL', 'SHV', 'SHY',
    
    # Some specialty ETFs
    'PFF', 'XLU', 'VNQ', 'IYR'
]

# Filter to only valid NYSE Arca ETFs and existing tables
table_set = set(all_tables)
valid_candidates = []

for candidate in high_prob_candidates:
    if candidate in nyse_arca_etfs and candidate in table_set:
        valid_candidates.append(candidate)

print('__RESULT__:')
print(json.dumps({
    'total_strategy': {k: len(v) for k, v in sampling_strategy.items()},
    'total_nyse_arca': len(nyse_arca_etfs),
    'valid_test_candidates': len(valid_candidates),
    'test_candidates': valid_candidates
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.query_db:8': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}, {'table_name': 'ABEQ'}, {'table_name': 'ABMD'}, {'table_name': 'ACAD'}, {'table_name': 'ACES'}, {'table_name': 'ACIO'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'count': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:14': {'total_symbols': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:16': 'file_storage/functions.list_db:16.json', 'var_functions.execute_python:18': {'total_nyse_arca_etfs': 1435, 'total_trade_tables': 2753, 'common_etfs': 1435, 'sample_common': ['LRNZ', 'NETL', 'DRN', 'IHI', 'JKK', 'IWL', 'CHAD', 'VAW', 'HSCZ', 'JHCS', 'RSP', 'ELD', 'IXN', 'TLEH', 'EUM', 'SILJ', 'TMF', 'SPYX', 'IYW', 'FLAX']}, 'var_functions.execute_python:20': {'total_nyse_arca_etfs': 1435, 'first_20_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [{'Adj Close': '193.3121490478516'}, {'Adj Close': '193.212158203125'}, {'Adj Close': '193.1998443603516'}, {'Adj Close': '193.0484619140625'}, {'Adj Close': '192.8638153076172'}, {'Adj Close': '192.83792114257807'}, {'Adj Close': '192.8120574951172'}, {'Adj Close': '192.77456665039065'}, {'Adj Close': '192.73838806152344'}, {'Adj Close': '192.67564392089844'}], 'var_functions.query_db:26': [{'Symbol': 'DIA', 'max_close': '163.6190185546875'}, {'Symbol': 'SSO', 'max_close': '66.95523071289062'}, {'Symbol': 'GLD', 'max_close': '125.2300033569336'}, {'Symbol': 'QQQ', 'max_close': '110.42893981933594'}, {'Symbol': 'IWM', 'max_close': '120.37349700927734'}], 'var_functions.query_db:28': [{'max_close': '125.2300033569336'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_etfs': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:36': ['GLD', 'SLV', 'IAU', 'GDX', 'GDXJ', 'SSO', 'UPRO', 'TQQQ', 'QLD', 'DDM', 'MVV', 'SAA', 'DUST', 'NUGT', 'JNUG', 'JDST', 'BOIL', 'KOLD', 'UGL', 'GLL', 'DGP', 'DZZ', 'AGQ', 'ZSL', 'SPY', 'QQQ', 'DIA', 'IWM', 'MDY', 'TLT', 'VGLT', 'EDV', 'TMF'], 'var_functions.execute_python:38': {'nyse_arca_total': 1435, 'sample_filtered': ['GLD', 'SLV', 'IAU', 'GDX', 'GDXJ', 'SSO', 'UPRO', 'QLD', 'DDM', 'MVV', 'SAA', 'DUST', 'NUGT', 'JNUG', 'JDST', 'BOIL', 'KOLD', 'UGL', 'GLL', 'AGQ', 'SPY', 'DIA', 'IWM', 'EDV', 'TMF']}, 'var_functions.query_db:40': [{'Date': '2015-01-22', 'Adj Close': '51.709999084472656'}, {'Date': '2015-01-23', 'Adj Close': '51.18000030517578'}, {'Date': '2015-01-21', 'Adj Close': '50.470001220703125'}, {'Date': '2015-01-27', 'Adj Close': '50.08000183105469'}, {'Date': '2015-01-28', 'Adj Close': '49.45000076293945'}], 'var_functions.query_db:42': [{'Symbol': 'TQQQ', 'max_close': '21.189502716064453'}, {'Symbol': 'UPRO', 'max_close': '24.036970138549805'}, {'Symbol': 'SPXL', 'max_close': '22.93797874450684'}, {'Symbol': 'TECL', 'max_close': '40.2764892578125'}, {'Symbol': 'SOXL', 'max_close': '39.06019592285156'}], 'var_functions.execute_python:44': {'test_count': 26, 'candidates': ['BKF', 'EMLP', 'AMLP', 'FXE', 'FXY', 'FXF', 'USO', 'UNG', 'BNO', 'BIL', 'IVV', 'VOO', 'SPLG', 'VEA', 'EFA', 'HYG', 'LQD', 'SCHD', 'VYM', 'XLF', 'XLU', 'XLY', 'GLD', 'IAU', 'TLT', 'EDV']}, 'var_functions.query_db:46': [{'Symbol': 'IVV', 'max_close': '193.5270538330078'}, {'Symbol': 'SLV', 'max_close': '17.610000610351562'}, {'Symbol': 'VOO', 'max_close': '177.17626953125'}, {'Symbol': 'GLD', 'max_close': '125.2300033569336'}, {'Symbol': 'TLT', 'max_close': '121.58584594726562'}, {'Symbol': 'BIL', 'max_close': '87.24989318847656'}, {'Symbol': 'EDV', 'max_close': '117.01538848876952'}, {'Symbol': 'IAU', 'max_close': '12.619999885559082'}, {'Symbol': 'HYG', 'max_close': '70.25736999511719'}, {'Symbol': 'LQD', 'max_close': '104.0085906982422'}], 'var_functions.query_db:48': [{'max_close': '104.59674072265624'}], 'var_functions.query_db:50': [{'max_close': '24.44536590576172'}], 'var_functions.execute_python:52': {'total_in_stockinfo': 1435, 'total_trade_tables': 2753, 'valid_etfs': 1435}, 'var_functions.query_db:54': [{'max_close': '117.01538848876952'}], 'var_functions.execute_python:58': {'nyse_arca_etfs': 1435, 'valid_etfs': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:60': 'file_storage/functions.execute_python:60.json'}

exec(code, env_args)
