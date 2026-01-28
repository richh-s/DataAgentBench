code = """import json

# Get the list of NYSE Arca ETFs
result_key1 = 'var_functions.query_db:0'
result_file_1 = locals()[result_key1]

with open(result_file_1, 'r') as f:
    etf_list = json.load(f)

nyse_arca_etfs = [etf['Symbol'] for etf in etf_list]

print('__RESULT__:')
print(json.dumps({
    'total_etfs_to_check': len(nyse_arca_etfs),
    'first_five_etfs': nyse_arca_etfs[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:10': {'total_nyse_arca_etfs': 1435, 'etfs_with_price_data': 1435, 'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': [{'Date': '2015-07-20', 'Adj Close': '193.3121490478516'}, {'Date': '2015-07-17', 'Adj Close': '193.212158203125'}, {'Date': '2015-05-21', 'Adj Close': '193.1998443603516'}, {'Date': '2015-07-16', 'Adj Close': '193.0484619140625'}, {'Date': '2015-11-03', 'Adj Close': '192.8638153076172'}, {'Date': '2015-05-18', 'Adj Close': '192.83792114257807'}, {'Date': '2015-06-23', 'Adj Close': '192.8120574951172'}, {'Date': '2015-05-19', 'Adj Close': '192.77456665039065'}, {'Date': '2015-05-22', 'Adj Close': '192.73838806152344'}, {'Date': '2015-06-22', 'Adj Close': '192.67564392089844'}], 'var_functions.query_db:16': [{'Date': '2015-01-22', 'Adj Close': '125.2300033569336'}, {'Date': '2015-01-27', 'Adj Close': '124.4000015258789'}, {'Date': '2015-01-21', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-23', 'Adj Close': '124.2300033569336'}, {'Date': '2015-01-20', 'Adj Close': '124.1999969482422'}]}

exec(code, env_args)
