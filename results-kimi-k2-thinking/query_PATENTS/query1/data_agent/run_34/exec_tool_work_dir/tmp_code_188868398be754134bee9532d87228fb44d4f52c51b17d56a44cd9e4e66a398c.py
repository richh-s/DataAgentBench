code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC data
cpc_var = locals()['var_functions.query_db:66']
level5_var = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_var)) if isinstance(cpc_var, str) and '.json' in cpc_var else cpc_var
level5_data = json.load(open(level5_var)) if isinstance(level5_var, str) and '.json' in level5_var else level5_var

level5_symbols = set([item['symbol'] for item in level5_data])

# Parse CPC records
code_year_counts = {}
for row in cpc_data:
    pub_date = row.get('publication_date', '')
    year = None
    if pub_date:
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
        except:
            continue
    
    cpc_str = row.get('cpc', '')
    if cpc_str:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                code = item.get('code', '')
                if code and len(code) >= 4:
                    level5_code = code[:4]
                    if level5_code in level5_symbols:
                        key = (level5_code, year)
                        code_year_counts[key] = code_year_counts.get(key, 0) + 1
        except:
            pass

# Calculate EMA for each code
codes_2022 = []
for code in level5_symbols:
    code_counts = {}
    for (c, y), count in code_year_counts.items():
        if c == code:
            code_counts[y] = count
    
    if len(code_counts) >= 3:
        years = sorted(code_counts.keys())
        counts = [code_counts[y] for y in years]
        ema = pd.Series(counts).ewm(alpha=0.2, adjust=False).mean()
        best_year = years[ema.idxmax()]
        if best_year == 2022:
            codes_2022.append(code)

result = json.dumps(sorted(codes_2022))
output = '__RESULT__:' + str(result)
print(output)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': [], 'var_functions.execute_python:86': []}

exec(code, env_args)
