code = """import json
import re

# Read funding data
with open('/tmp/tmp_3z7x6gk.json', 'r') as f:
    funding_data = json.load(f)

# Read spring 2022 documents
with open('/tmp/tmp_2z4l8jq.json', 'r') as f:
    spring_docs = json.load(f)

print('Funding records loaded:', len(funding_data))
print('Spring documents loaded:', len(spring_docs))

# Find Spring 2022 projects
project_names = []
for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        # Look for Spring 2022 with construction/advertisement context
        if 'Spring' in line and '2022' in line:
            lower_line = line.lower()
            if 'construction' in lower_line or 'advertise' in lower_line or 'begin' in lower_line:
                # Find project name by looking backward
                for j in range(i-1, max(-1, i-15), -1):
                    prev_line = lines[j].strip()
                    if prev_line and not prev_line.startswith('(') and not prev_line.startswith('•'):
                        # Avoid header words
                        bad_words = ['update', 'schedule', 'status', 'description', 'project', 'begin construction', 'advertise', 'complete design']
                        has_bad_word = any(word in prev_line.lower() for word in bad_words)
                        if not has_bad_word and len(prev_line) < 200:
                            if prev_line not in project_names:
                                project_names.append(prev_line)
                            break

print('Unique Spring 2022 projects found:', len(project_names))
for proj in sorted(project_names):
    print('- ' + proj)

# Match with funding
funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding_data}

total_funding = 0
matched_projects = []
for proj in project_names:
    if proj in funding_dict:
        amount = funding_dict[proj]
        total_funding += amount
        matched_projects.append(proj)
    else:
        # Partial match
        for funded_name, amount in funding_dict.items():
            if proj in funded_name or funded_name in proj:
                total_funding += amount
                matched_projects.append(proj + ' (matched to: ' + funded_name + ')')
                break

print('Matched projects:', len(matched_projects))
print('Total funding:', total_funding)

result = {
    'spring_2022_project_count': len(project_names),
    'matched_projects': len(matched_projects),
    'total_funding': total_funding,
    'project_list': project_names[:20]  # First 20 projects
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.list_db:16': ['civic_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
