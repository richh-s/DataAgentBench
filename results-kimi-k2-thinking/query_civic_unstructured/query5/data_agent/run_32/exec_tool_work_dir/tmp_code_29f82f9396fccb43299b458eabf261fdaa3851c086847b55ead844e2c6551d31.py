code = """import json
import re

# Load data
data1 = open('/tmp/tmp_hb9f3fdk.json', 'r').read()
funding = json.loads(data1)
data2 = open('/tmp/tmp_cdv8r04p.json', 'r').read()
civic_docs = json.loads(data2)

# Build funding lookup
funding_lookup = {}
for item in funding:
    funding_lookup[item['Project_Name']] = int(item['Amount'])

# Extract projects from documents
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line and i + 4 < len(lines):
            if '(' in line and ')' in line:
                # Split project name and status
                open_paren = line.rindex('(')
                close_paren = line.rindex(')')
                name = line[:open_paren].strip()
                status = line[open_paren+1:close_paren].strip().lower()
                
                # Check following lines for details
                topic_line = lines[i+1].strip()
                type_line = lines[i+2].strip()
                st_line = lines[i+3].strip()
                et_line = lines[i+4].strip()
                
                if 'topic:' in topic_line and 'type:' in type_line and 'st:' in st_line and 'et:' in et_line:
                    topic = topic_line.split(':', 1)[1].strip()
                    type_val = type_line.split(':', 1)[1].strip()
                    st = st_line.split(':', 1)[1].strip()
                    et = et_line.split(':', 1)[1].strip()
                    
                    all_projects.append({
                        'name': name,
                        'topic': topic,
                        'type': type_val,
                        'status': status,
                        'st': st,
                        'et': et
                    })
        i += 1

# Filter for 2022 disaster projects
disaster_2022 = []
fema_pattern = re.compile(r'\((FEMA|CalJPIA|CalOES)\s*Project\)', re.IGNORECASE)

for proj in all_projects:
    if '2022' in proj['st']:
        if proj['type'] == 'disaster' or fema_pattern.search(proj['name']):
            disaster_2022.append(proj)

# Remove duplicates by name
seen_names = set()
filtered_projects = []
for proj in disaster_2022:
    if proj['name'] not in seen_names:
        seen_names.add(proj['name'])
        filtered_projects.append(proj)

# Calculate total funding
total_funding = 0
matched = []
for proj in filtered_projects:
    if proj['name'] in funding_lookup:
        amount = funding_lookup[proj['name']]
        total_funding += amount
        matched.append({'project_name': proj['name'], 'amount': amount})

result = {
    'total_funding_2022_disaster': total_funding,
    'count': len(matched),
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
