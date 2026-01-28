code = """import json
import re

# Load funding dataset
funding_list = storage['var_functions.query_db:50']

# Load civic documents dataset  
civic_list = storage['var_functions.query_db:72']

print('Funding records:', len(funding_list))
print('Civic documents:', len(civic_list))

# Find projects referencing Spring 2022 in civic docs
spring_2022_candidates = []

for doc in civic_list:
    txt = doc.get('text', '')
    # Check for Spring 2022 indicators
    if 'Spring 2022' in txt or '2022-Spring' in txt or re.search('2022-(03|04|05)', txt):
        lines = txt.split('\n')
        for i, line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line or re.search('2022-(03|04|05)', line):
                # Look back up to 5 lines for project name
                for j in range(i-1, max(0, i-6), -1):
                    candidate = lines[j].strip()
                    if candidate and len(candidate) > 15 and not candidate.startswith('('):
                        spring_2022_candidates.append(candidate)
                        break
                break

print('Spring 2022 candidates:', len(spring_2022_candidates))

# Match with funding records
total = 0
matched = set()

for fund in funding_list:
    fname = fund['Project_Name']
    amount = int(fund['Amount'])
    
    for proj in spring_2022_candidates:
        # Check for name match (containment)
        if fname in proj or proj in fname or any(part in fname for part in proj.split()[:2]):
            if fname not in matched:
                matched.add(fname)
                total += amount
                break

result = {"project_count": len(matched), "total_funding": total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
