code = """import json
import re

# Load data
funding_path = locals()['var_function-call-12062815889619764856']
civic_docs_path = locals()['var_function-call-9916471758806846480']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

projects = {} 

def is_disaster_text(text):
    keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster', 'Recovery', 'Woolsey Fire']
    return any(k.upper() in text.upper() for k in keywords)

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section_disaster = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if 'Disaster Recovery Projects' in line:
            current_section_disaster = True
        elif 'Capital Improvement Projects' in line:
            current_section_disaster = False
            
        is_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if 'Updates:' in next_line or 'Project Description:' in next_line:
                is_project = True
        
        if is_project and line and len(line) > 3 and 'Agenda' not in line and 'Page' not in line:
            p_name = line.strip()
            
            j = i + 1
            block_lines = []
            while j < len(lines):
                next_l = lines[j].strip()
                
                if j + 1 < len(lines):
                    nn_l = lines[j+1].strip()
                    if ('Updates:' in nn_l or 'Project Description:' in nn_l) and next_l and len(next_l) > 3:
                        break
                
                if 'Capital Improvement Projects' in next_l or 'Disaster Recovery Projects' in next_l:
                    break
                
                block_lines.append(next_l)
                j += 1
            
            block_text = '\n'.join(block_lines)
            
            is_disaster = current_section_disaster or is_disaster_text(p_name) or is_disaster_text(block_text)
            
            start_date_2022 = False
            
            # Using simple string find instead of regex for simplicity to avoid escape hell
            # We want 'Begin Construction' ... '2022'
            # Or 'Start Date' ... '2022'
            lower_text = block_text.lower()
            if 'begin construction' in lower_text:
                idx = lower_text.find('begin construction')
                snippet = lower_text[idx:idx+50]
                if '2022' in snippet:
                    start_date_2022 = True
            if 'start date' in lower_text:
                idx = lower_text.find('start date')
                snippet = lower_text[idx:idx+50]
                if '2022' in snippet:
                    start_date_2022 = True
            if 'construction started' in lower_text:
                idx = lower_text.find('construction started')
                snippet = lower_text[idx:idx+50]
                if '2022' in snippet:
                    start_date_2022 = True

            if p_name not in projects:
                projects[p_name] = {'is_disaster': False, 'start_2022': False}
            
            if is_disaster:
                projects[p_name]['is_disaster'] = True
            if start_date_2022:
                projects[p_name]['start_2022'] = True
            
            i = j - 1
        i += 1

total_amount = 0
matched_details = []

for f in funding_data:
    fname = f['Project_Name']
    amount = float(f['Amount']) if f['Amount'] else 0
    
    match_found = False
    
    if fname in projects:
        p = projects[fname]
        if p['is_disaster'] and p['start_2022']:
            total_amount += amount
            match_found = True
            matched_details.append(fname)
            
    if not match_found:
        for p_name, p_info in projects.items():
            if p_name in fname and len(p_name) > 10 and p_info['is_disaster'] and p_info['start_2022']:
                 if fname.startswith(p_name):
                     total_amount += amount
                     matched_details.append(fname)
                     match_found = True
                     break

print('__RESULT__:')
print(json.dumps({'total_amount': total_amount, 'matched_projects': matched_details}))"""

env_args = {'var_function-call-1624468200300741529': ['Funding'], 'var_function-call-1624468200300743390': ['civic_docs'], 'var_function-call-12062815889619764856': 'file_storage/function-call-12062815889619764856.json', 'var_function-call-12062815889619765571': 'file_storage/function-call-12062815889619765571.json', 'var_function-call-9916471758806846480': 'file_storage/function-call-9916471758806846480.json'}

exec(code, env_args)
