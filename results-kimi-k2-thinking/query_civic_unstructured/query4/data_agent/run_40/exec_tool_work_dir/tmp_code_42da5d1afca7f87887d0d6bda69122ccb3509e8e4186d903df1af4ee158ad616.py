code = """import json
import re

# Access data from the execution environment context
# Try to get it from locals() or globals()
funding_key = 'var_functions.query_db:50'
civic_key = 'var_functions.query_db:72'

data_dict = locals()
if funding_key in data_dict:
    funding_list = data_dict[funding_key]
else:
    funding_list = globals()[funding_key]

if civic_key in data_dict:
    civic_list = data_dict[civic_key]
else:
    civic_list = globals()[civic_key]

print('Funding records:', len(funding_list))
print('Civic documents:', len(civic_list))

# Extract Spring 2022 project names from civic documents
spring_2022_candidates = []
for doc in civic_list:
    txt = doc.get('text', '')
    if 'Spring 2022' in txt or '2022-Spring' in txt:
        lines = txt.split('\n')
        for i, line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Look backwards for project name
                for j in range(i-1, max(0, i-6), -1):
                    candidate = lines[j].strip()
                    if candidate and len(candidate) > 15 and not candidate.startswith('('):
                        spring_2022_candidates.append(candidate)
                        break
                break

print('Spring 2022 candidates:', len(spring_2022_candidates))

# Match with funding
total = 0
matched_fund_names = set()

for fund in funding_list:
    fname = fund['Project_Name']
    amount = int(fund['Amount'])
    
    for proj in spring_2022_candidates:
        # Check containment
        if fname in proj or proj in fname:
            if fname not in matched_fund_names:
                matched_fund_names.add(fname)
                total += amount
                break

result = {"project_count": len(matched_fund_names), "total_funding": total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
