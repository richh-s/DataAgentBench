code = """import json

# Read funding file
path_fund = locals()['var_function-call-5247396609485473632']
with open(path_fund, 'r') as f:
    funding_list = json.load(f)

# Filter > 50000
valid_funding_names = set()
for x in funding_list:
    try:
        if float(x['Amount']) > 50000:
            valid_funding_names.add(x['Project_Name'].strip().lower())
    except:
        pass

# Read docs file
path_docs = locals()['var_function-call-633765740054289148']
with open(path_docs, 'r') as f:
    doc_list = json.load(f)

found_projects = set()

for d in doc_list:
    txt = d['text']
    lines = txt.split('\n')
    
    in_design_section = False
    
    for ln in lines:
        ln_clean = ln.strip().lower()
        if not ln_clean:
            continue
        
        # Check markers
        if "capital improvement projects (design)" in ln_clean:
            in_design_section = True
            continue
        
        # Check for other sections to exit design section
        if "capital improvement projects (construction)" in ln_clean:
            in_design_section = False
            continue
        if "capital improvement projects (not started)" in ln_clean:
            in_design_section = False
            continue
        if "disaster recovery projects" in ln_clean:
            in_design_section = False
            continue
            
        if in_design_section:
            # Check if line is a project name
            if ln_clean in valid_funding_names:
                found_projects.add(ln_clean)

result_list = list(found_projects)
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-5247396609485473632': 'file_storage/function-call-5247396609485473632.json', 'var_function-call-633765740054289148': 'file_storage/function-call-633765740054289148.json'}

exec(code, env_args)
