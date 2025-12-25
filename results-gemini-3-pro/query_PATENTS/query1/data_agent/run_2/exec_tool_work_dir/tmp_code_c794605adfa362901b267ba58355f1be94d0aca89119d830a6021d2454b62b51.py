code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-7542188176596272141'], 'r') as f:
    pub_data = json.load(f)

years = []
year_pattern = re.compile(r'\b(19|20)\d{2}\b')

for entry in pub_data:
    f_date = entry.get('filing_date')
    if f_date:
        match = year_pattern.search(f_date)
        if match:
            years.append(int(match.group(0)))

if years:
    print("__RESULT__:")
    print(json.dumps({
        "min_year": min(years),
        "max_year": max(years),
        "count": len(years)
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"error": "No years found"}))"""

env_args = {'var_function-call-18438039698466275985': [{'symbol': 'A01H'}, {'symbol': 'A01F'}, {'symbol': 'A01C'}, {'symbol': 'A01G'}, {'symbol': 'A23J'}, {'symbol': 'A01N'}, {'symbol': 'A01P'}, {'symbol': 'A01D'}, {'symbol': 'A01L'}, {'symbol': 'A01K'}], 'var_function-call-11425610840667422492': 'file_storage/function-call-11425610840667422492.json', 'var_function-call-15261515319027993325': [{'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-3988956739634739314': [{'symbol': 'A01H', 'level': '5.0'}], 'var_function-call-16646390810544569620': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}], 'var_function-call-3646825604830857458': 'file_storage/function-call-3646825604830857458.json', 'var_function-call-7247946529193589936': [{'COUNT(*)': '277813'}], 'var_function-call-7542188176596272141': 'file_storage/function-call-7542188176596272141.json', 'var_function-call-2924045124924059341': []}

exec(code, env_args)
