code = """import json
import re

with open(locals()['var_function-call-16148835938051840028'], 'r') as f:
    pub_data = json.load(f)

year_pattern = re.compile(r'\b(19|20)\d{2}\b')
all_years = set()

for record in pub_data:
    f_date = record.get('filing_date', '')
    if f_date:
        match = year_pattern.search(f_date)
        if match:
            all_years.add(int(match.group(0)))

result = {
    "years": sorted(list(all_years))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9506971857936168120': 'file_storage/function-call-9506971857936168120.json', 'var_function-call-16148835938051840028': 'file_storage/function-call-16148835938051840028.json', 'var_function-call-17364678478425837483': []}

exec(code, env_args)
