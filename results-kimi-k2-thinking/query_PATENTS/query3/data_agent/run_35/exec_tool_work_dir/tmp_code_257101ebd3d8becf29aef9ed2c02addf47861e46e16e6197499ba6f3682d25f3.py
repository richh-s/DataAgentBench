code = """import json

data_key = 'var_functions.query_db:2'
if data_key in locals():
    data = locals()[data_key]
    print('Number of UNIV CALIFORNIA patents:', len(data))
    
    if len(data) > 0:
        print('\nFirst record structure:')
        print('Keys:', list(data[0].keys()))
        print('\nPatents_info:', data[0]['Patents_info'])
        print('\nCitation preview:', str(data[0]['citation'])[:150])
        print('\nCPC preview:', str(data[0]['cpc'])[:150])
    
    print('\n__RESULT__:')
    print('Data loaded successfully - {} records'.format(len(data)))
else:
    print('Data not found in locals()')
    print('Available keys:', [k for k in locals().keys() if 'query' in k])
    
    print('\n__RESULT__:')
    print('Key not found')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
