code = """import json
import pandas as pd

ema_results = json.loads(locals()['var_function-call-11028652032211112393'])
cpc_codes_to_query = [item['cpc_group_level_4'] for item in ema_results]
unique_cpc_codes = list(set(cpc_codes_to_query))

print('__RESULT__:')
print(json.dumps(unique_cpc_codes))"""

env_args = {'var_function-call-10273422858072318649': 'file_storage/function-call-10273422858072318649.json', 'var_function-call-11028652032211112393': [{'cpc_group_level_4': 'A43B', 'filing_year': 2016, 'ema': 0.5}, {'cpc_group_level_4': 'A61B', 'filing_year': 2016, 'ema': 0.2}, {'cpc_group_level_4': 'A61F', 'filing_year': 2016, 'ema': 0.6}, {'cpc_group_level_4': 'A61L', 'filing_year': 2016, 'ema': 0.2}, {'cpc_group_level_4': 'B23K', 'filing_year': 2015, 'ema': 0.1}, {'cpc_group_level_4': 'B41F', 'filing_year': 2007, 'ema': 3.0}, {'cpc_group_level_4': 'B60K', 'filing_year': 2013, 'ema': 0.1}, {'cpc_group_level_4': 'B60N', 'filing_year': 2009, 'ema': 0.3}, {'cpc_group_level_4': 'B60R', 'filing_year': 2018, 'ema': 0.1}, {'cpc_group_level_4': 'B60W', 'filing_year': 2013, 'ema': 0.1}, {'cpc_group_level_4': 'B64D', 'filing_year': 2018, 'ema': 0.1}, {'cpc_group_level_4': 'E02F', 'filing_year': 2012, 'ema': 0.5}, {'cpc_group_level_4': 'F01D', 'filing_year': 2018, 'ema': 0.2}, {'cpc_group_level_4': 'F02N', 'filing_year': 2013, 'ema': 0.7}, {'cpc_group_level_4': 'F04D', 'filing_year': 2018, 'ema': 0.1}, {'cpc_group_level_4': 'F05D', 'filing_year': 2018, 'ema': 0.2}, {'cpc_group_level_4': 'F16F', 'filing_year': 2018, 'ema': 0.1}, {'cpc_group_level_4': 'F41H', 'filing_year': 2012, 'ema': 0.2}, {'cpc_group_level_4': 'F42B', 'filing_year': 2012, 'ema': 0.2}, {'cpc_group_level_4': 'G01D', 'filing_year': 2015, 'ema': 0.1}, {'cpc_group_level_4': 'G01M', 'filing_year': 2018, 'ema': 0.4}, {'cpc_group_level_4': 'G01N', 'filing_year': 2018, 'ema': 0.181}, {'cpc_group_level_4': 'G02B', 'filing_year': 2018, 'ema': 0.8}, {'cpc_group_level_4': 'H01R', 'filing_year': 2018, 'ema': 0.6}, {'cpc_group_level_4': 'H02J', 'filing_year': 2009, 'ema': 0.6}, {'cpc_group_level_4': 'H03L', 'filing_year': 2015, 'ema': 0.6}, {'cpc_group_level_4': 'H04L', 'filing_year': 2015, 'ema': 0.2}, {'cpc_group_level_4': 'Y02T', 'filing_year': 2013, 'ema': 0.2}]}

exec(code, env_args)
