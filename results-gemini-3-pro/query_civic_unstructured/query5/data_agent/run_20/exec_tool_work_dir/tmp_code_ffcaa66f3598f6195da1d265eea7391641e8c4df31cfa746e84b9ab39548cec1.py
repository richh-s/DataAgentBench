code = """import json
import pandas as pd
import re

funding_file = locals()['var_function-call-5321786749699906543']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

docs_file = locals()['var_function-call-13929900393569377328']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

projects = {} 

def check_disaster(text_context):
    keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster Recovery']
    for k in keywords:
        if k.lower() in text_context.lower():
            return True
    return False

# Regex using single quotes to avoid JSON escaping issues with double quotes
# We use \\ for backslashes. In regex, \s is whitespace.
start_patterns = [
    r'Begin Construction:?\s*([A-Za-z]+\s*\d{4})',
    r'Construction Start:?\s*([A-Za-z]+\s*\d{4})',
    r'Start Date:?\s*([A-Za-z]+\s*\d{4})'
]

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    current_section = ''
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        if 'Capital Improvement Projects' in line or 'Disaster Recovery Projects' in line:
            if 'Disaster' in line:
                current_section = 'Disaster'
            elif 'Capital' in line:
                current_section = 'Capital'
                
        is_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # (cid:190) check. The preview showed (cid:190).
            if next_line.startswith('(cid:190)') and ('Updates' in next_line or 'Description' in next_line or 'Status' in next_line):
                is_project = True
        
        if not is_project and i + 2 < len(lines) and not lines[i+1].strip():
            next_next_line = lines[i+2].strip()
            if next_next_line.startswith('(cid:190)') and ('Updates' in next_next_line or 'Description' in next_next_line or 'Status' in next_next_line):
                is_project = True
        
        if is_project:
            p_name = line.strip()
            
            is_dis = False
            if current_section == 'Disaster':
                is_dis = True
            if check_disaster(p_name):
                is_dis = True
            
            started_2022 = False
            block_text = ''
            for j in range(i+1, min(i+50, len(lines))):
                subline = lines[j].strip()
                block_text += subline + ' '
            
            for pat in start_patterns:
                match = re.search(pat, block_text, re.IGNORECASE)
                if match:
                    date_str = match.group(1)
                    if '2022' in date_str:
                        started_2022 = True
            
            if not started_2022:
                if 'Begin Construction: Fall 2022' in block_text or \
                   'Begin Construction: Spring 2022' in block_text or \
                   'Begin Construction: Summer 2022' in block_text or \
                   'Begin Construction: Winter 2022' in block_text:
                    started_2022 = True

            if p_name not in projects:
                projects[p_name] = {'is_disaster': is_dis, 'started_2022': started_2022}
            else:
                if is_dis: projects[p_name]['is_disaster'] = True
                if started_2022: projects[p_name]['started_2022'] = True

target_projects = []
for name, info in projects.items():
    if info['is_disaster'] and info['started_2022']:
        target_projects.append(name)

total_funding = 0
matched_details = []
funding_dict = {}

for idx, row in df_funding.iterrows():
    orig = row['Project_Name']
    norm = orig.strip().lower()
    amt = int(row['Amount'])
    if norm in funding_dict:
        funding_dict[norm] += amt
    else:
        funding_dict[norm] = amt

for tp in target_projects:
    tp_norm = tp.strip().lower()
    
    match_found = False
    if tp_norm in funding_dict:
        total_funding += funding_dict[tp_norm]
        matched_details.append((tp, funding_dict[tp_norm]))
        match_found = True
    
    if not match_found:
        for fnorm in funding_dict:
            if fnorm.startswith(tp_norm):
                 total_funding += funding_dict[fnorm]
                 matched_details.append((fnorm, funding_dict[fnorm]))
                 match_found = True
        
    if not match_found:
        for fnorm in funding_dict:
            if tp_norm.startswith(fnorm):
                 total_funding += funding_dict[fnorm]
                 matched_details.append((fnorm, funding_dict[fnorm]))
                 match_found = True
                 break 

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding, 'projects': matched_details}))"""

env_args = {'var_function-call-1518905300948613366': ['Funding'], 'var_function-call-1518905300948614017': ['civic_docs'], 'var_function-call-5321786749699906543': 'file_storage/function-call-5321786749699906543.json', 'var_function-call-5321786749699905058': 'file_storage/function-call-5321786749699905058.json', 'var_function-call-130987581307727602': 'file_storage/function-call-130987581307727602.json', 'var_function-call-13929900393569377328': 'file_storage/function-call-13929900393569377328.json'}

exec(code, env_args)
