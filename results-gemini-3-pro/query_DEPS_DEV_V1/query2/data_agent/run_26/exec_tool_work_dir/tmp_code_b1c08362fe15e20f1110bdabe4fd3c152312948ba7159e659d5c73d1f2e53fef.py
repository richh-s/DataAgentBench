code = """import json
import re
import pandas as pd

# Files
file_pkg = locals()['var_function-call-6938159831684507998']
file_proj_info = locals()['var_function-call-7253653177288570155']
file_mapping = locals()['var_function-call-4671920378434493390']

# 1. Parse Project Info
with open(file_proj_info, 'r') as f:
    proj_info_data = json.load(f)

proj_forks = {}
name_patterns = [
    r"The project is hosted on GitHub under the name ([^,]+),",
    r"The GitHub project named ([^ ]+) currently",
    r"The project named ([^ ]+) is hosted on GitHub",
    r"The project named ([^ ]+) on GitHub",
    r"The GitHub project ([^ ]+) currently",
    r"The project ([^ ]+) is hosted on GitHub",
    r"The project ([^ ]+) is hosted on GITHUB",
    r"The project ([^ ]+) on GitHub"
]
fork_patterns = [
    r"and ([0-9,]+) forks",
    r"forks count of ([0-9,]+)",
    r"and has been forked ([0-9,]+) times",
    r"and a forks count of ([0-9,]+)"
]

for entry in proj_info_data:
    text = entry['Project_Information']
    name = None
    forks = 0
    
    # Name
    for p in name_patterns:
        m = re.search(p, text)
        if m:
            name = m.group(1).strip()
            if name.endswith(',') or name.endswith('.'):
                name = name[:-1]
            break
            
    # Forks
    for p in fork_patterns:
        m = re.search(p, text)
        if m:
            f_str = m.group(1).replace(',', '')
            forks = int(f_str)
            break
    
    if name:
        proj_forks[name] = forks

# 2. Load Mappings
with open(file_mapping, 'r') as f:
    mapping_data = json.load(f)
df_map = pd.DataFrame(mapping_data)

# 3. Load Candidates
with open(file_pkg, 'r') as f:
    pkg_data = json.load(f)

candidates = []
for p in pkg_data:
    # Filter
    try:
        lics = json.loads(p['Licenses'])
        # Check if MIT is in the list
        if 'MIT' not in lics:
            continue
    except:
        continue
        
    # VersionInfo
    try:
        vinfo = json.loads(p['VersionInfo'])
        if not vinfo.get('IsRelease', False):
            continue
    except:
        continue
        
    candidates.append({'Name': p['Name'], 'Version': p['Version']})

df_candidates = pd.DataFrame(candidates)

# 4. Merge
if not df_candidates.empty and not df_map.empty:
    df_merged = pd.merge(df_candidates, df_map, on=['Name', 'Version'], how='inner')
    
    # 5. Map Forks
    unique_projects = df_merged['ProjectName'].unique()
    
    results = []
    for proj in unique_projects:
        if proj in proj_forks:
            results.append({'Project': proj, 'Forks': proj_forks[proj]})
    
    # 6. Sort
    results.sort(key=lambda x: x['Forks'], reverse=True)
    
    # 7. Top 5
    top_5 = [r['Project'] for r in results[:5]]
    
    print("__RESULT__:")
    print(json.dumps(top_5))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-10352811860558582149': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'Licenses': '[]', 'Description': 'Template for npm package library configured to be used with CI/CD', 'Homepage': 'None', 'OSSFuzz': 'nan'}], 'var_function-call-12554035315876686551': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-12554035315876685994': [{'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'Licenses': '[\n  "EUPL-1.2"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}'}], 'var_function-call-6938159831684507998': 'file_storage/function-call-6938159831684507998.json', 'var_function-call-14508441577688866252': [{'count_star()': '597602'}], 'var_function-call-14508441577688862885': [{'count_star()': '770'}], 'var_function-call-7253653177288570155': 'file_storage/function-call-7253653177288570155.json', 'var_function-call-16967882764331233460': 'file_storage/function-call-16967882764331233460.json', 'var_function-call-4671920378434493390': 'file_storage/function-call-4671920378434493390.json'}

exec(code, env_args)
