code = """import json
import os

# Get NYSE Arca ETFs list
nyse_arca_etfs_file = locals().get('var_functions.query_db:0')

nyse_arca_etfs = []
if isinstance(nyse_arca_etfs_file, str) and os.path.exists(nyse_arca_etfs_file):
    with open(nyse_arca_etfs_file, 'r') as f:
        nyse_arca_etfs = [item['Symbol'] for item in json.load(f)]
elif isinstance(nyse_arca_etfs_file, list):
    nyse_arca_etfs = [item['Symbol'] for item in nyse_arca_etfs_file]

# We'll process tickers in batches to check prices
def get_tickers_exceeding_200(limit=200):
    """Get first batch of tickers to check"""
    return nyse_arca_etfs[:limit]

high_price_etfs = []
tested = 0
batch_size = 50

# We'll build a query for multiple tickers
# For now, let's return a batch to test the approach
first_batch = nyse_arca_etfs[:batch_size]

print('__RESULT__:')
print(json.dumps({
    'batch_size': batch_size,
    'first_batch': first_batch,
    'total_remaining': len(nyse_arca_etfs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'tickers_count': 1435, 'first_10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.list_db:9': 'file_storage/functions.list_db:9.json', 'var_functions.execute_python:8': {'nyse_arca_etfs_count': 1435, 'all_tickers_count': 2753, 'etf_intersection_count': 1435, 'first_10_intersection': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:10': [{'Date': '2015-01-02', 'Adj Close': '35.3997688293457'}, {'Date': '2015-01-05', 'Adj Close': '34.96500015258789'}, {'Date': '2015-01-06', 'Adj Close': '34.6751594543457'}, {'Date': '2015-01-07', 'Adj Close': '34.6751594543457'}, {'Date': '2015-01-08', 'Adj Close': '35.21620559692383'}], 'var_functions.execute_python:12': {'tickers_to_check': 1435, 'example_tickers': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.query_db:14': [{'Date': '2015-01-30', 'Adj Close': '98.26229858398438'}, {'Date': '2015-02-02', 'Adj Close': '98.25880432128906'}, {'Date': '2015-04-17', 'Adj Close': '98.14436340332033'}], 'var_functions.execute_python:16': {'total_etfs': 1435, 'status': 'Ready to check prices'}, 'var_functions.execute_python:18': {'total_etfs': 1435, 'number_of_batches': 72, 'batch_size': 20, 'first_two_batches': [['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], ['AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY']]}, 'var_functions.query_db:20': [{'max_price': '125.2300033569336'}], 'var_functions.execute_python:22': {'test_candidates': ['SPY', 'QQQ', 'DIA', 'IVV', 'VTI', 'GLD']}, 'var_functions.query_db:24': [{'max_price': '193.3121490478516'}], 'var_functions.execute_python:26': {'tickers_to_test': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX'], 'count': 100, 'status': 'Ready to query prices for 2015'}}

exec(code, env_args)
