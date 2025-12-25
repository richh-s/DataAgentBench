code = """import json
import pandas as pd

top_indices_returns = json.loads(locals()['var_function-call-17924491885778729575'])

index_to_country = {
    'IXIC': 'United States',
    '399001.SZ': 'China',
    'GDAXI': 'Germany',
    'TWII': 'Taiwan',
    'NSEI': 'India'
}

formatted_results = []
for item in top_indices_returns:
    index_symbol = item['Index']
    country = index_to_country.get(index_symbol, 'Unknown')
    formatted_results.append({'Index': index_symbol, 'Country': country, 'Return': item['Return']})

print('__RESULT__:')
print(json.dumps(formatted_results))"""

env_args = {'var_function-call-14095839042875052654': 'file_storage/function-call-14095839042875052654.json', 'var_function-call-17924491885778729575': [{'Index': 'IXIC', 'Return': 3.786263717408535}, {'Index': '399001.SZ', 'Return': 1.347928823154433}, {'Index': 'GDAXI', 'Return': 1.3201203421480523}, {'Index': 'TWII', 'Return': 1.317355739060972}, {'Index': 'NSEI', 'Return': 1.2123905368580012}]}

exec(code, env_args)
