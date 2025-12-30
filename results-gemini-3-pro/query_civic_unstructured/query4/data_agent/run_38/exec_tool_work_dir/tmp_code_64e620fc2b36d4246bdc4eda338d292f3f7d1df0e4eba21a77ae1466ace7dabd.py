code = """import json
import pandas as pd

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

def get_start_date(lines_list):
    # flexible search for start date
    # Look for Begin Construction line
    for line in lines_list:
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
        if 'march' in ds or 'april' in ds or 'may' in ds:
            return True
        if '03/2022' in ds or '04/2022' in ds or '05/2022' in ds:
            return True
        if '2022-03' in ds or '2022-04' in ds or '2022-05' in ds:
            return True
    return False

for doc in civic_docs:
    lines = doc['text'].splitlines()
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
                st = get_start_date(current_block)
                if is_spring_2022(st):
                    projects_found.append({'Project_Name': current_project, 'st': st})
            
            # Start new project
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
        st = get_start_date(current_block)
        if is_spring_2022(st):
            projects_found.append({'Project_Name': current_project, 'st': st})

df_res = pd.DataFrame(projects_found)

# Join
if not df_res.empty:
    final_res = pd.merge(df_funding, df_res, on='Project_Name')
    count = len(final_res)
    total_funding = int(final_res['Amount'].sum())
    
    print('__RESULT__:')
    print(json.dumps({
        'count': count,
        'total_funding': total_funding,
        'projects': final_res['Project_Name'].tolist()
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'count': 0,
        'total_funding': 0
    }))"""

env_args = {'var_function-call-5073457582333833681': ['civic_docs'], 'var_function-call-5073457582333837024': ['Funding'], 'var_function-call-11668788458618260347': 'file_storage/function-call-11668788458618260347.json', 'var_function-call-11668788458618261250': 'file_storage/function-call-11668788458618261250.json'}

exec(code, env_args)
