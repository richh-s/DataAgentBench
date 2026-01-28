code = """import json, re

# Load data from files
funding = json.load(open('/tmp/tmp_hb9f3fdk.json', 'r'))
civic_docs = json.load(open('/tmp/tmp_cdv8r04p.json', 'r'))

# Create funding lookup
funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Extract projects from documents
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find pattern: Project Name (status) followed by details
    pattern = r'([A-Z].*?)\(([A-Za-z\s]+)\)[\s\S]*?topic:\s*(.*?)[\s\S]*?type:\s*(.*?)[\s\S]*?st:\s*(.*?)[\s\S]*?et:\s*(.*?)\n'
    matches = re.finditer(pattern, text, re.MULTILINE)
    
    for match in matches:
        name = match.group(1).strip()
        status = match.group(2).strip().lower()
        topic = match.group(3).strip()
        type_val = match.group(4).strip()
        st = match.group(5).strip()
        et = match.group(6).strip()
        
        all_projects.append({
            'name': name,
            'topic': topic,
            'type': type_val,
            'status': status,
            'st': st,
            'et': et
        })

# Find disaster projects starting in 2022
disaster_2022 = []
fema_pattern = re.compile(r'\((FEMA|CalJPIA|CalOES)\s*Project\)', re.IGNORECASE)

for proj in all_projects:
    if '2022' in proj['st']:
        if proj['type'] == 'disaster' or fema_pattern.search(proj['name']):
            disaster_2022.append(proj)

# Remove duplicate projects by name
unique_projects = {}
for proj in disaster_2022:
    if proj['name'] not in unique_projects:
        unique_projects[proj['name']] = proj

# Calculate total funding
total_funding = 0
funded_list = []
for proj in unique_projects.values():
    if proj['name'] in funding_dict:
        amount = funding_dict[proj['name']]
        total_funding += amount
        funded_list.append({'name': proj['name'], 'amount': amount})

# Output results
result = {
    'total_funding_2022_disaster_projects': total_funding,
    'number_of_projects': len(funded_list),
    'projects': funded_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
