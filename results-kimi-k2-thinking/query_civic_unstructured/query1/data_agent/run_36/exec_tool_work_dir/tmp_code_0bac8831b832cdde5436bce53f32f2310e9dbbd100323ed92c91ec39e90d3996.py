code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic docs
civic_file = var_functions.query_db:28
with open(civic_file) as f:
    civic_docs = json.load(f)

# Get funding > $50,000
high_funding = []
for record in funding_data:
    if record.get('Amount'):
        try:
            amount = int(record['Amount'])
            if amount > 50000:
                high_funding.append(record)
        except:
            pass

print('High funding count:', len(high_funding))

# Extract capital design projects from civic docs
design_project_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    design_start = text.lower().find('projects (design)')
    if design_start < 0:
        design_start = text.lower().find('design)\n')
        
    if design_start >= 0:
        section = text[design_start:design_start+3000]
        section_lower = section.lower()
        
        end_markers = ['projects (construction)', 'disaster recovery', 'projects (not started)']
        end_pos = len(section)
        for marker in end_markers:
            pos = section_lower.find(marker)
            if pos > 0 and pos < end_pos:
                end_pos = pos
                
        design_section = section[:end_pos]
        lines = design_section.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 6:
                continue
                
            lower_line = line.lower()
            if any(exclude in lower_line for exclude in ['capital improvement', 'design', 'updates:', 'project schedule', 'subject:', 'recommended']):
                continue
                
            if line in ['•', '●', '■', '□']:
                continue
                
            if i + 1 < len(lines):
                next_line = lines[i + 1].lower()
                if 'updates:' in next_line or 'project schedule' in next_line or next_line.startswith('('):
                    clean_name = line.lstrip('0123456789.-• ')
                    if len(clean_name) > 8:
                        design_project_names.append(clean_name)

print('Design projects found:', len(design_project_names))

# Match projects
matched_count = 0
unique_matches = set()

for design_name in design_project_names:
    design_lower = design_name.lower()
    for fund in high_funding:
        fund_name = fund['Project_Name'].lower()
        
        if design_lower in fund_name or fund_name in design_lower:
            unique_matches.add(design_name)
            break

matched_count = len(unique_matches)
print('Matched projects:', matched_count)

result = {'capital_design_projects_with_funding_greater_than_50k': matched_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
