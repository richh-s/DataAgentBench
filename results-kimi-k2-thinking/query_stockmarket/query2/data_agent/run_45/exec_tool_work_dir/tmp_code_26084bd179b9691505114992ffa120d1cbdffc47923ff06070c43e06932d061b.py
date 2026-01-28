code = """import json
import sqlite3
import os

# Read the list of NYSE Arca ETFs
etfs_file_path = locals()['var_functions.query_db:22']
with open(etfs_file_path, 'r') as f:
    etfs_data = json.load(f)

nyse_arca_etfs = [etf['Symbol'] for etf in etfs_data]

# Get company descriptions
stockinfo_file_path = locals()['var_functions.query_db:18']
with open(stockinfo_file_path, 'r') as f:
    stockinfo_data = json.load(f)

description_map = {etf['Symbol']: etf.get('Company Description', 'N/A') for etf in stockinfo_data}

# Check high-price candidates first (more likely to exceed $200)
high_price_candidates = ['DIA', 'SPY', 'IVV', 'VOO', 'QQQ', 'IWV', 'VTI', 'RSP', 'XLY', 'XLF', 'XLU']
candidates_to_check = [etf for etf in high_price_candidates if etf in nyse_arca_etfs]

# Add some other likely candidates based on index/fund type
other_candidates = ['IVW', 'IWD', 'IWF', 'IWN', 'IWO', 'IJH', 'IJR', 'IJT', 'IJS', 'IJJ']
candidates_to_check.extend([etf for etf in other_candidates if etf in nyse_arca_etfs and etf not in candidates_to_check])

# Since we've already checked major ones and they didn't hit $200,
# let's be more systematic but efficient
print(f"Total NYSE Arca ETFs: {len(nyse_arca_etfs)}")
print(f"Checking {len(candidates_to_check)} high-potential candidates first")

# Save data for next steps
print('__RESULT__:')
print(json.dumps({
    'total_etfs': len(nyse_arca_etfs),
    'candidates': candidates_to_check,
    'candidate_count': len(candidates_to_check)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': {'etf_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'total_count': 1435}, 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': {'nyse_arca_etfs': 1435, 'total_tables': 2753, 'available_etfs': 1435, 'sample_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [], 'var_functions.query_db:26': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}, {'Date': '2015-01-30', 'Adj Close': '123.4499969482422'}, {'Date': '2015-01-28', 'Adj Close': '123.41999816894533'}, {'Date': '2015-01-26', 'Adj Close': '122.98999786376952'}, {'Date': '2015-01-16', 'Adj Close': '122.5199966430664'}, {'Date': '2015-02-02', 'Adj Close': '122.41999816894533'}], 'var_functions.query_db:28': [], 'var_functions.query_db:30': [{'min("Adj Close")': '170.28823852539062', 'max("Adj Close")': '193.3121490478516'}], 'var_functions.query_db:32': [], 'var_functions.execute_python:34': {'candidates': ['DIA', 'SPY', 'IVV', 'VOO', 'IWV', 'VTI', 'RSP', 'XLY', 'XLF', 'XLU'], 'total_etfs': 1435}, 'var_functions.execute_python:36': {'total_etfs': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'descriptions': {'AAAU': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.', 'AADR': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies.", 'ABEQ': 'Absolute Core Strategy ETF is an investment fund designed to offer a diversified portfolio, focusing on strategic asset allocation to optimize returns for investors.', 'ACSG': 'Xtrackers MSCI ACWI ex USA ESG Leaders Equity ETF offers investors an opportunity to engage with international companies that are recognized for their strong environmental, social, and governance practices, excluding those based in the USA.', 'ACWF': 'iShares Edge MSCI Multifactor Global ETF is an investment fund that provides exposure to a diversified portfolio of stocks worldwide, utilizing a multifactor approach to enhance returns and manage risk.'}}, 'var_functions.query_db:38': [{'Date': '2015-12-01', 'Adj Close': '110.42893981933594'}, {'Date': '2015-12-04', 'Adj Close': '110.40975952148438'}, {'Date': '2015-11-04', 'Adj Close': '110.29467010498048'}, {'Date': '2015-11-03', 'Adj Close': '110.2851104736328'}, {'Date': '2015-11-06', 'Adj Close': '110.07412719726562'}, {'Date': '2015-11-05', 'Adj Close': '109.99744415283205'}, {'Date': '2015-12-29', 'Adj Close': '109.9390106201172'}, {'Date': '2015-12-08', 'Adj Close': '109.92070770263672'}, {'Date': '2015-12-07', 'Adj Close': '109.9111099243164'}, {'Date': '2015-11-02', 'Adj Close': '109.90152740478516'}], 'var_functions.query_db:40': [{'max_price': '163.6190185546875'}]}

exec(code, env_args)
