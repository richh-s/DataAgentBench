code = """import json
import math

# Get all NYSE Arca ETF symbols
nyse_arca_data = locals()['var_functions.query_db:0']
if isinstance(nyse_arca_data, str):
    with open(nyse_arca_data, 'r') as f:
        nyse_arca_data = json.load(f)

symbols = [item['Symbol'] for item in nyse_arca_data]

# Create batches for processing (20 ETFs per batch)
batch_size = 20
batches = [symbols[i:i+batch_size] for i in range(0, len(symbols), batch_size)]

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols), 
    'batch_count': len(batches),
    'batch_size': batch_size
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.list_db:11': 'file_storage/functions.list_db:11.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY'], 'var_functions.query_db:20': [{'max_adj_close': '193.3121490478516'}], 'var_functions.query_db:24': [{'Symbol': 'GLD', 'max_adj_close': '125.2300033569336'}, {'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}, {'Symbol': 'AGG', 'max_adj_close': '98.26229858398438'}, {'Symbol': 'SPY', 'max_adj_close': '193.3121490478516'}, {'Symbol': 'IVV', 'max_adj_close': '193.5270538330078'}], 'var_functions.query_db:26': [{'Symbol': 'SSO', 'max_adj_close': '66.95523071289062'}, {'Symbol': 'UPRO', 'max_adj_close': '24.036970138549805'}, {'Symbol': 'TMF', 'max_adj_close': '27.289674758911133'}, {'Symbol': 'TLT', 'max_adj_close': '121.58584594726562'}, {'Symbol': 'QQQ', 'max_adj_close': '110.42893981933594'}], 'var_functions.execute_python:28': {'total_symbols': 1435, 'batch_count': 72, 'batches': [['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], ['AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY']]}, 'var_functions.query_db:30': [{'Symbol': 'GLD', 'max_adj_close': '125.2300033569336'}, {'Symbol': 'DIA', 'max_adj_close': '163.6190185546875'}, {'Symbol': 'AGG', 'max_adj_close': '98.26229858398438'}, {'Symbol': 'SPY', 'max_adj_close': '193.3121490478516'}, {'Symbol': 'IVV', 'max_adj_close': '193.5270538330078'}, {'Symbol': 'BIL', 'max_adj_close': '87.24989318847656'}, {'Symbol': 'BKLN', 'max_adj_close': '19.62266731262207'}, {'Symbol': 'HYG', 'max_adj_close': '70.25736999511719'}, {'Symbol': 'SHV', 'max_adj_close': '104.59674072265624'}, {'Symbol': 'VEU', 'max_adj_close': '44.92586135864258'}, {'Symbol': 'EFA', 'max_adj_close': '59.14651870727539'}, {'Symbol': 'IWF', 'max_adj_close': '97.2972412109375'}, {'Symbol': 'IWD', 'max_adj_close': '93.8613052368164'}, {'Symbol': 'IWB', 'max_adj_close': '108.6298828125'}, {'Symbol': 'IYW', 'max_adj_close': '106.93596649169922'}, {'Symbol': 'IYF', 'max_adj_close': '86.10455322265625'}, {'Symbol': 'IYM', 'max_adj_close': '79.51802825927734'}, {'Symbol': 'IYR', 'max_adj_close': '68.42395782470703'}, {'Symbol': 'IYH', 'max_adj_close': '152.538330078125'}, {'Symbol': 'IYK', 'max_adj_close': '99.7577896118164'}]}

exec(code, env_args)
