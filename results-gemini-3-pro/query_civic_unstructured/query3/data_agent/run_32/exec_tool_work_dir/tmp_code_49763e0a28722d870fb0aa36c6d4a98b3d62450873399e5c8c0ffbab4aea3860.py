code = """import json
import sqlite3
import pandas as pd
import re

# Load previous results
funding_file = locals()['var_function-call-5036986330958495032']
civic_docs_file = locals()['var_function-call-5036986330958492415']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

# Combine text
full_text = '\n'.join([doc['text'] for doc in civic_docs_data])

funding_df = pd.DataFrame(funding_data)

results = []
keywords = ['emergency', 'FEMA']

lines = full_text.split('\n')

# Map lines to sections
sections = []
current_section = None
for line in lines:
    l_strip = line.strip()
    if 'Capital Improvement Projects (Design)' in l_strip:
        current_section = 'design'
    elif 'Capital Improvement Projects (Construction)' in l_strip:
        current_section = 'construction'
    elif 'Capital Improvement Projects (Not Started)' in l_strip:
        current_section = 'not started'
    sections.append(current_section)

# Search for projects
for index, row in funding_df.iterrows():
    proj_name = row['Project_Name']
    
    found_idx = -1
    # precise matching
    for i, line in enumerate(lines):
        if proj_name.lower() in line.lower():
            # Check length to avoid partial matches inside long sentences
            if len(line.strip()) < len(proj_name) + 20:
                found_idx = i
                break
    
    # Fallback: clean name
    if found_idx == -1:
        clean_name = re.sub(r'\s*\(.*?\)', '', proj_name)
        if clean_name and len(clean_name) > 5:
            for i, line in enumerate(lines):
                if clean_name.lower() in line.lower():
                    if len(line.strip()) < len(clean_name) + 20:
                        found_idx = i
                        break
    
    if found_idx != -1:
        section_status = sections[found_idx]
        
        # Extract block
        block_text = []
        for j in range(found_idx, len(lines)):
            l = lines[j].strip()
            # Stop at next section header
            if 'Capital Improvement Projects (' in l and j != found_idx:
                break
            
            # Stop at likely next project
            if j > found_idx and len(block_text) > 0:
                is_bullet = l.startswith('(cid:') or l.startswith('Updates:') or l.startswith('Project Schedule:')
                is_page = 'Page ' in l or 'Agenda Item' in l or l == ''
                if not is_bullet and not is_page:
                    # Likely new project name
                    break
            
            block_text.append(lines[j])
        
        full_block = '\n'.join(block_text)
        
        # Check relevance
        is_relevant = False
        for kw in keywords:
            if kw.lower() in proj_name.lower() or kw.lower() in full_block.lower():
                is_relevant = True
                break
        
        if is_relevant:
            final_status = section_status
            if section_status == 'construction':
                if 'completed' in full_block.lower():
                    final_status = 'completed'
                elif 'under construction' in full_block.lower():
                    final_status = 'in construction'
                else:
                    final_status = 'construction' # fallback
            
            results.append({
                'Project_Name': proj_name,
                'Funding_Source': row['Funding_Source'],
                'Amount': row['Amount'],
                'Status': final_status
            })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-11141337925117404384': ['civic_docs'], 'var_function-call-11141337925117405097': ['Funding'], 'var_function-call-3665847163097728255': 'file_storage/function-call-3665847163097728255.json', 'var_function-call-3665847163097727678': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-5036986330958495032': 'file_storage/function-call-5036986330958495032.json', 'var_function-call-5036986330958492415': 'file_storage/function-call-5036986330958492415.json'}

exec(code, env_args)
