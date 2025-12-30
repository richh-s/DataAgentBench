code = """import json
import pandas as pd
import re

# Load data
funding_path = locals()['var_function-call-11668788458618260347']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

civic_path = locals()['var_function-call-11668788458618261250']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

projects_found = []

def get_start_date(text_block):
    # flexible search for start date
    # Look for Begin Construction line
    for line in text_block.split('\n'):
        if 'Begin Construction' in line or 'Begin construction' in line:
            parts = line.split(':')
            if len(parts) > 1:
                return parts[1].strip()
    return None

def is_spring_2022(date_str):
    if not date_str:
        return False
    ds = date_str.lower()
    if 'spring 2022' in ds or 'spring, 2022' in ds:
        return True
    if '2022' in ds:
        if 'spring' in ds:
            return True
        if any(m in ds for m in ['march', 'april', 'may']):
            return True
        # Check simple date formats like 3/2022 or 2022-03
        # Avoid backslashes in regex if problematic, use simple replace
        ds_clean = ds.replace('-', '/').replace('.', '/')
        if '03/2022' in ds_clean or '04/2022' in ds_clean or '05/2022' in ds_clean:
            return True
        if '2022/03' in ds_clean or '2022/04' in ds_clean or '2022/05' in ds_clean:
            return True
    return False

for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_project = None
    current_block = []
    
    # scan lines
    for i, line in enumerate(lines):
        line_s = line.strip()
        # check for project header markers
        is_header = False
        if 'Updates:' in line_s and len(line_s) < 30:
            is_header = True
        elif 'Project Description:' in line_s and len(line_s) < 30:
            is_header = True
            
        if is_header:
            # save previous project if exists
            if current_project and current_block:
                full_block = '\n'.join(current_block)
                st = get_start_date(full_block)
                if is_spring_2022(st):
                    projects_found.append({'Project_Name': current_project, 'st': st})
            
            # Start new project
            # The project name is likely the previous non-empty line
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                current_project = lines[j].strip()
                current_block = []
        else:
            if current_project:
                current_block.append(line)

    # capture last project
    if current_project and current_block:
        full_block = '\n'.join(current_block)
        st = get_start_date(full_block)
        if is_spring_2022(st):
            projects_found.append({'Project_Name': current_project, 'st': st})

df_res = pd.DataFrame(projects_found)

# Join
final_res = pd.merge(df_funding, df_res, on='Project_Name')

print("__RESULT__:")
print(json.dumps({
    "count": len(final_res),
    "total_funding": int(final_res['Amount'].sum()),
    "details": final_res[['Project_Name', 'st']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-5073457582333833681': ['civic_docs'], 'var_function-call-5073457582333837024': ['Funding'], 'var_function-call-11668788458618260347': 'file_storage/function-call-11668788458618260347.json', 'var_function-call-11668788458618261250': 'file_storage/function-call-11668788458618261250.json'}

exec(code, env_args)
