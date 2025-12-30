code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-12443390616213881639'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-13902106228594848871'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

projects = []
topic_keywords = ['park', 'road', 'fema', 'fire', 'emergency warning', 'drainage', 'storm drain', 'highway', 'bridge', 'playground', 'water treatment', 'guardrail', 'emergency']

cid_marker = '(' + 'cid:190' + ')'
marker_char = chr(190)

def extract_dates(text):
    st = None
    et = None
    # Flexible date patterns
    # Regex strings without backslashes if possible, or double escaped
    # We need \s. So \\s in the string.
    
    begin_match = re.search(r'Begin [Cc]onstruction:?\s*([A-Za-z0-9\s]+)', text)
    if begin_match:
        st = begin_match.group(1).strip()
    else:
        adv_match = re.search(r'Advertise:?\s*([A-Za-z0-9\s]+)', text)
        if adv_match:
            st = adv_match.group(1).strip()
            
    comp_match = re.search(r'Complete [Cc]onstruction:?\s*([A-Za-z0-9\s]+)', text)
    if comp_match:
        et = comp_match.group(1).strip()
    
    return st, et

def get_status(section_status, text):
    if section_status == 'design':
        return 'design'
    elif section_status == 'not_started':
        return 'not started'
    elif section_status == 'construction':
        if 'completed' in text.lower() and 'notice of completion' in text.lower():
             return 'completed'
        if 'construction was completed' in text.lower():
            return 'completed'
        return 'design' 
    return 'design'

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines() # Use splitlines
    
    current_type = None
    current_section_status = None
    name_buffer = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if 'Capital Improvement Projects' in line:
            current_type = 'capital'
            if '(Design)' in line:
                current_section_status = 'design'
            elif '(Construction)' in line:
                current_section_status = 'construction'
            elif '(Not Started)' in line:
                current_section_status = 'not_started'
            i += 1
            continue
        elif 'Disaster Recovery Projects' in line:
            current_type = 'disaster'
            if '(Design)' in line:
                current_section_status = 'design'
            elif '(Construction)' in line:
                current_section_status = 'construction'
            elif '(Not Started)' in line:
                current_section_status = 'not_started'
            i += 1
            continue
            
        if line.startswith(cid_marker) or line.startswith(marker_char):
            proj_name = ' '.join([n for n in name_buffer if n]).strip()
            
            block_lines = []
            block_lines.append(line)
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                if 'Capital Improvement Projects' in next_line or 'Disaster Recovery Projects' in next_line:
                    break
                
                k = j + 1
                found_next_marker = False
                while k < len(lines):
                    if lines[k].strip():
                        if lines[k].strip().startswith(cid_marker) or lines[k].strip().startswith(marker_char):
                            found_next_marker = True
                        break
                    k += 1
                
                if found_next_marker and not (next_line.startswith(cid_marker) or next_line.startswith(marker_char)):
                    break
                
                block_lines.append(next_line)
                j += 1
            
            block_text = '\n'.join(block_lines)
            
            topics = []
            for kw in topic_keywords:
                if kw.lower() in proj_name.lower() or kw.lower() in block_text.lower():
                    topics.append(kw)
            
            status = get_status(current_section_status, block_text)
            st, et = extract_dates(block_text)
            
            if proj_name:
                projects.append({
                    'Project_Name': proj_name,
                    'topics': topics,
                    'type': current_type,
                    'status': status,
                    'st': st,
                    'et': et
                })
            
            name_buffer = []
            i = j
            continue
            
        else:
            if line:
                name_buffer.append(line)
            i += 1

relevant_projects = []
for p in projects:
    is_related = False
    if 'emergency' in p['topics'] or 'fema' in p['topics']:
        is_related = True
    if 'emergency' in p['Project_Name'].lower() or 'fema' in p['Project_Name'].lower():
        is_related = True
        
    if is_related:
        relevant_projects.append(p)

final_results = []
for p in relevant_projects:
    p_name = p['Project_Name']
    matches = df_funding[df_funding['Project_Name'].apply(lambda x: x.lower().startswith(p_name.lower()) or p_name.lower().startswith(x.lower()))]
    
    if not matches.empty:
        for _, row in matches.iterrows():
            final_results.append({
                'Project_Name': row['Project_Name'],
                'Funding_Source': row['Funding_Source'],
                'Amount': row['Amount'],
                'Status': p['status']
            })

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_function-call-6697639078713076568': ['civic_docs'], 'var_function-call-6697639078713075367': ['Funding'], 'var_function-call-4303639865338753386': 'file_storage/function-call-4303639865338753386.json', 'var_function-call-13902106228594848871': 'file_storage/function-call-13902106228594848871.json', 'var_function-call-12443390616213881639': 'file_storage/function-call-12443390616213881639.json'}

exec(code, env_args)
