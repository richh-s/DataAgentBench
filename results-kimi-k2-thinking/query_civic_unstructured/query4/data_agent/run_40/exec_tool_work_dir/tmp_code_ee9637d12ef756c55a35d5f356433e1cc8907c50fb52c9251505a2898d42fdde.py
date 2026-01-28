code = """import json, re

# Get the stored results - assume they're available in the execution context
# and we know their storage keys
funding_data = storage['var_functions.query_db:50']
civic_docs = storage['var_functions.query_db:72']

print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Extract Spring 2022 project names from civic documents
spring_2022_names = []

for doc in civic_docs:
    text = doc['text']
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Look backwards up to 5 lines for project name
                start_idx = max(0, i-5)
                for j in range(i-1, start_idx-1, -1):
                    candidate = lines[j].strip()
                    if candidate and len(candidate) > 15 and not candidate.startswith('('):
                        spring_2022_names.append(candidate)
                        break
                break

print("Candidate Spring 2022 projects:", len(spring_2022_names))

# Match with funding records
total_funding = 0
matched_names = set()

for fund in funding_data:
    fund_name = fund['Project_Name']
    amount = int(fund['Amount'])
    
    for project_name in spring_2022_names:
        # Match if one name is contained in the other or they share first words
        if (fund_name in project_name or project_name in fund_name):
            if fund_name not in matched_names:
                matched_names.add(fund_name)
                total_funding += amount
                break

result = {"project_count": len(matched_names), "total_funding": total_funding}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
