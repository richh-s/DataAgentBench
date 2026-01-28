code = """import json

# Check the actual data
patent_file = locals()['var_functions.query_db:2']
cpc_file = locals()['var_functions.query_db:3']

with open(cpc_file, 'r') as f:
    cpc_level5_data = json.load(f)

with open(patent_file, 'r') as f:
    patent_data = json.load(f)

# Sample some CPC symbols and patent CPC codes
cpc_symbols_sample = [item['symbol'] for item in cpc_level5_data[:20]]

patent_cpc_samples = []
for i, record in enumerate(patent_data[:50]):
    cpc_str = record.get('cpc', '')
    if cpc_str:
        try:
            import ast
            cpc_list = ast.literal_eval(cpc_str)
            for entry in cpc_list:
                if isinstance(entry, dict) and 'code' in entry:
                    patent_cpc_samples.append(entry['code'])
        except:
            pass

# Check years available
import re
years = set()
for record in patent_data:
    pub_date = record.get('publication_date', '')
    if pub_date:
        match = re.search(r'(\d{4})', str(pub_date))
        if match:
            years.add(int(match.group(1)))

result = {
    "cpc_symbols_sample": cpc_symbols_sample,
    "patent_cpc_samples": list(set(patent_cpc_samples))[:30],
    "available_years": sorted(list(years))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:18': []}

exec(code, env_args)
