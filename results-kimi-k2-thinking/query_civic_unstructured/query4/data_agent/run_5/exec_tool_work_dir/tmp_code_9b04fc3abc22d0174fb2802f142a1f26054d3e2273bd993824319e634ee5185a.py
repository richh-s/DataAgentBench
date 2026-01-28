code = """import json

# Load data from temp files
civic_docs = json.load(open('/tmp/tmp3.json'))
funding_data = json.load(open('/tmp/tmp4.json'))

# Build simple funding map: project name -> total amount
funding_totals = {}
for rec in funding_data:
    name = rec['Project_Name']
    amt = int(rec['Amount'])
    funding_totals[name] = funding_totals.get(name, 0) + amt

print('Loaded', len(civic_docs), 'civic docs and', len(funding_data), 'funding records')

# Simple approach: look for projects with 2022 and match
spring_2022_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'Spring' in text:
        # Parse lines to find project name
        lines = text.split('\n')
        for i in range(1, len(lines)):
            prev = lines[i-1].strip()
            curr = lines[i].strip()
            if '2022' in curr and 'Spring' in curr and len(prev) > 15:
                spring_2022_projects.append(prev)

# Remove duplicates
unique_projects = list(dict.fromkeys(spring_2022_projects))

# Match with funding
total_funding = 0
matched = []
for proj in unique_projects:
    if proj in funding_totals:
        total_funding += funding_totals[proj]
        matched.append({'name': proj, 'funding': funding_totals[proj]})

result = {'count': len(matched), 'total_funding': total_funding}
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json'}

exec(code, env_args)
