code = """import json, re, sys

# Read funding file
funding_content = open('/tmp/tmp_3z7x6gk.json', 'r').read()
funding_data = json.loads(funding_content)

# Read spring docs file
spring_content = open('/tmp/tmp_2z4l8jq.json', 'r').read()
spring_docs = json.loads(spring_content)

print('Funding:', len(funding_data))
print('Spring docs:', len(spring_docs))

# Extract Spring 2022 projects
project_names = []
for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Spring' in line and '2022' in line:
            low_line = line.lower()
            if 'construction' in low_line or 'advertise' in low_line:
                # Find project name
                name = None
                for j in range(i-1, max(-1, i-10), -1):
                    prev = lines[j].strip()
                    if prev and not prev.startswith('(') and not prev.startswith('•'):
                        if len(prev) < 200:
                            check_bad = prev.lower().find('update') < 0 and prev.lower().find('schedule') < 0
                            if check_bad:
                                name = prev
                                break
                if name and name not in project_names:
                    project_names.append(name)

print('Spring 2022 projects found:', len(project_names))
for p in project_names:
    print('- ' + p)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Amount'])

# Calculate total funding
total_funding = 0
matched_count = 0
for proj in project_names:
    if proj in funding_lookup:
        total_funding += funding_lookup[proj]
        matched_count += 1
    else:
        # Try partial match
        for funded_name, amount in funding_lookup.items():
            if proj.find(funded_name) >= 0 or funded_name.find(proj) >= 0:
                total_funding += amount
                matched_count += 1
                break

print('Matched projects:', matched_count)
print('Total funding:', total_funding)

result = {'project_count': len(project_names), 'total_funding': total_funding}

sys.stdout.write('__RESULT__:\n')
sys.stdout.write(json.dumps(result))
sys.stdout.flush()"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:60': [{'count': '2', 'total': '83000'}]}

exec(code, env_args)
