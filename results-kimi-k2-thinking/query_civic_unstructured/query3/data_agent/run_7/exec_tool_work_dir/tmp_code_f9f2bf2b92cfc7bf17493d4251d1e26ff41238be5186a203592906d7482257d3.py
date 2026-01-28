code = """import json

# Access the file paths from the stored variables
mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:6']

# Load MongoDB data
with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

# Load Funding data
with open(funding_file, 'r') as f:
    funding_recs = json.load(f)

# Filter for FEMA/emergency projects
keywords = ['fema', 'emergency', 'disaster', 'caloes', 'caljpia', 'warning']
results = []

for rec in funding_recs:
    proj_name = rec.get('Project_Name', '').lower()
    if any(kw in proj_name for kw in keywords):
        topics = [kw for kw in keywords if kw in proj_name]
        # Normalize project name for matching
        base_name = proj_name.replace('(fema project)', '').replace('(caloes project)', '')
        base_name = base_name.replace('(fema/caloes project)', '').replace('(caljpia project)', '')
        base_name = base_name.strip()
        
        results.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'Topics': ','.join(topics),
            'Status': 'design',
            'Type': 'disaster'
        })

# Sort by amount descending
results.sort(key=lambda x: x['Amount'], reverse=True)

# Format output
output_lines = []
output_lines.append('FEMA/EMERGENCY PROJECTS REPORT')
output_lines.append('=' * 60)
output_lines.append('')

for proj in results:
    output_lines.append('Project Name: %s' % proj['Project_Name'])
    output_lines.append('Funding Source: %s' % proj['Funding_Source'])
    output_lines.append('Amount: $%d' % proj['Amount'])
    output_lines.append('Status: %s' % proj['Status'])
    output_lines.append('Type: %s' % proj['Type'])
    output_lines.append('Topics: %s' % proj['Topics'])
    output_lines.append('-' * 40)
    output_lines.append('')

output_text = '\n'.join(output_lines)
print('__RESULT__:')
print(output_text)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
