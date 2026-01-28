code = """import json, re

# Load funding data
funding_file = open('/tmp/tmp_3z7x6gk.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load Spring 2022 documents
spring_file = open('/tmp/tmp_2z4l8jq.json', 'r')
spring_docs = json.load(spring_file)
spring_file.close()

print('Funding records:', len(funding_data))
print('Spring documents:', len(spring_docs))

# Find projects starting in Spring 2022
project_list = []
keywords = ['construction', 'advertise', 'begin']
stop_words = ['update', 'schedule', 'status', 'description']

for doc in spring_docs:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Spring' in line and '2022' in line:
            lower_line = line.lower()
            if any(kw in lower_line for kw in keywords):
                project_name = None
                for j in range(i-1, max(-1, i-15), -1):
                    prev = lines[j].strip()
                    if prev and not prev.startswith('(') and not prev.startswith('•') and len(prev) < 200:
                        if not any(sw in prev.lower() for sw in stop_words):
                            project_name = prev
                            break
                if project_name and project_name not in project_list:
                    project_list.append(project_name)

print('Spring 2022 projects:', len(project_list))

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Amount'])

# Calculate total funding
matched = 0
total_funding = 0
for proj in project_list:
    if proj in funding_lookup:
        matched += 1
        total_funding += funding_lookup[proj]
    else:
        # Try partial matching
        for funded_name, amount in funding_lookup.items():
            if proj in funded_name or funded_name in proj:
                matched += 1
                total_funding += amount
                break

print('Matched projects:', matched)
print('Total funding:', total_funding)

result = {'count': len(project_list), 'funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
