code = """import json
import pandas as pd

funding_path = locals()['var_function-call-9960923256029121607']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

docs_path = locals()['var_function-call-9960923256029120432']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_status = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if 'Capital Improvement Projects' in line:
            if '(Design)' in line:
                current_status = 'design'
            elif '(Construction)' in line:
                current_status = 'construction_section'
            elif '(Not Started)' in line:
                current_status = 'not started'
            i += 1
            continue
            
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            is_start = False
            if 'Updates:' in next_line or 'Project Description:' in next_line:
                if len(next_line) < 100:
                    is_start = True
            
            if is_start and line:
                project_name = line
                block_lines = [line, next_line]
                j = i + 2
                while j < len(lines):
                    l = lines[j].strip()
                    if 'Capital Improvement Projects' in l:
                        break
                    if j + 1 < len(lines):
                        nl = lines[j+1].strip()
                        if ('Updates:' in nl or 'Project Description:' in nl) and len(nl) < 100:
                            if l:
                                break
                    block_lines.append(l)
                    j += 1
                
                full_text = '\n'.join(block_lines)
                p_status = current_status
                if p_status == 'construction_section':
                    if 'completed' in full_text.lower() and 'construction was completed' in full_text.lower():
                        p_status = 'completed'
                    else:
                        p_status = 'construction'

                projects.append({
                    'Project_Name': project_name,
                    'text': full_text,
                    'status': p_status
                })
                i = j
                continue
        i += 1

related_projects = []
seen_names = set()

for p in projects:
    if p['Project_Name'] in seen_names:
        continue
    text_lower = p['text'].lower()
    name_lower = p['Project_Name'].lower()
    if 'emergency' in text_lower or 'fema' in text_lower or 'emergency' in name_lower or 'fema' in name_lower:
        related_projects.append(p)
        seen_names.add(p['Project_Name'])

related_df = pd.DataFrame(related_projects)

if not related_df.empty:
    related_df['Project_Name'] = related_df['Project_Name'].str.strip()
    merged_df = pd.merge(related_df, funding_df, on='Project_Name', how='left')
    result = merged_df[['Project_Name', 'Funding_Source', 'Amount', 'status']]
    result = result.fillna('N/A')
    print('__RESULT__:')
    print(result.to_json(orient='records'))
else:
    print('__RESULT__:')
    print('[]')"""

env_args = {'var_function-call-7478273444201397872': ['Funding'], 'var_function-call-7478273444201397573': ['civic_docs'], 'var_function-call-9960923256029121607': 'file_storage/function-call-9960923256029121607.json', 'var_function-call-9960923256029120432': 'file_storage/function-call-9960923256029120432.json'}

exec(code, env_args)
