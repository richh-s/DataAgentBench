code = """import json
import pandas as pd
import re

civic_docs = json.load(open('var_function-call-445312601869862601'))
funding_data = json.load(open('var_function-call-445312601869864330'))

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

text_content = ''
for doc in civic_docs:
    text_content += doc.get('text', '') + ' '

project_names = df_funding['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

found_projects = []
for pname in project_names:
    pattern = re.escape(pname)
    for match in re.finditer(pattern, text_content, re.IGNORECASE):
        found_projects.append({
            'name': pname,
            'start': match.start(),
            'end': match.end()
        })

found_projects.sort(key=lambda x: (x['start'], -x['end']))

cleaned_projects = []
last_end = -1
for p in found_projects:
    if p['start'] >= last_end:
        cleaned_projects.append(p)
        last_end = p['end']

completed_2022_projects = set()

for i, p in enumerate(cleaned_projects):
    pname = p['name']
    start_pos = p['end']
    if i < len(cleaned_projects) - 1:
        end_pos = cleaned_projects[i+1]['start']
    else:
        end_pos = start_pos + 2000
    
    chunk = text_content[start_pos:end_pos]
    chunk_norm = ' '.join(chunk.split())
    
    # Check for completed in 2022
    # Regex: (completed|complete construction|construction complete) ... (Month) ... 2022
    pattern_str = r"(completed|complete construction|construction complete|construction was completed)\D{0,60}(january|february|march|april|may|june|july|august|september|october|november|december)\D{0,10}2022"
    
    if re.search(pattern_str, chunk_norm, re.IGNORECASE):
        completed_2022_projects.add(pname)

park_projects = []
for pname in completed_2022_projects:
    lower = pname.lower()
    if 'park' in lower or 'playground' in lower or 'recreation' in lower:
        park_projects.append(pname)

total = 0
matched_df = df_funding[df_funding['Project_Name'].isin(park_projects)]
total = matched_df['Amount'].sum()

print('__RESULT__:')
print(json.dumps({'projects': park_projects, 'total_funding': total, 'details': matched_df.to_dict(orient='records')}))"""

env_args = {'var_function-call-18426906873258029198': ['civic_docs'], 'var_function-call-18426906873258031577': ['Funding'], 'var_function-call-8821001174791641027': 'file_storage/function-call-8821001174791641027.json', 'var_function-call-8821001174791641856': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-445312601869862601': 'file_storage/function-call-445312601869862601.json', 'var_function-call-445312601869864330': 'file_storage/function-call-445312601869864330.json'}

exec(code, env_args)
