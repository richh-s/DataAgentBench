code = """import json, re

# Load data from files
with open('/tmp/tmp_3z7x6gk.json', 'r') as f:
    funding_data = json.load(f)

with open('/tmp/tmp_2z4l8jq.json', 'r') as f:
    spring_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Spring documents:', len(spring_docs))

# Find projects that started in Spring 2022
spring_projects = []

for doc in spring_docs:
    text = doc['text']
    # Look for Spring 2022 patterns
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if 'Spring' in line and '2022' in line:
                # Check if this is a construction/advertise line
                if any(kw in line.lower() for kw in ['begin construction', 'construction', 'advertise', 'start']):
                    # Look backward for project name
                    for j in range(i-1, max(-1, i-15), -1):
                        prev = lines[j].strip()
                        if prev and not prev.startswith('(') and not prev.startswith('•') and len(prev) < 200:
                            # Skip lines that contain common header words
                            if not any(word in prev.lower() for word in ['update', 'schedule', 'status', 'description']):
                                spring_projects.append(prev)
                                break

# Get unique project names
unique_projects = list(set(spring_projects))
print('\nUnique Spring 2022 projects:', len(unique_projects))
for proj in sorted(unique_projects):
    print('- ' + proj)

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name']] = int(item['Amount'])

# Match projects with funding
matched_count = 0
total_funding = 0
for proj in unique_projects:
    if proj in funding_lookup:
        matched_count += 1
        total_funding += funding_lookup[proj]
    else:
        # Try partial match
        for funded_proj, amount in funding_lookup.items():
            if proj in funded_proj or funded_proj in proj:
                matched_count += 1
                total_funding += amount
                break

print('\nMatched projects:', matched_count)
print('Total funding:', total_funding)

result = {
    'spring_2022_project_count': len(unique_projects),
    'total_funding': total_funding
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
