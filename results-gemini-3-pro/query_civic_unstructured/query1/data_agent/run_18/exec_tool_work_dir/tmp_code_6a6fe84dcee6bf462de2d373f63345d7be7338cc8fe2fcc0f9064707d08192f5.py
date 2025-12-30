code = """import json

# Get filenames from locals
funding_file = locals()['var_function-call-5363402596982368323']
docs_file = locals()['var_function-call-5363402596982368440']

# Load data
with open(funding_file) as f:
    funding_data = json.load(f)

with open(docs_file) as f:
    docs_data = json.load(f)

# Process funding
funded_projects = set()
for item in funding_data:
    try:
        if float(item['Amount']) > 50000:
            funded_projects.add(item['Project_Name'].strip())
    except:
        pass

def extract_projects(text):
    found = set()
    text_lower = text.lower()
    start_marker = 'capital improvement projects (design)'
    start_idx = text_lower.find(start_marker)
    
    if start_idx == -1:
        return found
    
    next_markers = [
        'capital improvement projects (construction)',
        'capital improvement projects (not started)',
        'disaster recovery projects'
    ]
    
    end_idx = len(text)
    for mk in next_markers:
        idx = text_lower.find(mk, start_idx + len(start_marker))
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx + len(start_marker):end_idx]
    
    # split by newline
    lines = section_text.split(chr(10))
    for i in range(len(lines)):
        sline = lines[i].strip()
        if not sline:
            continue
            
        # Check next non-empty
        for j in range(i+1, len(lines)):
            nline = lines[j].strip()
            if not nline:
                continue
            
            if 'Updates:' in nline or 'Project Description:' in nline:
                if 'Page' not in sline and 'Agenda Item' not in sline:
                    found.add(sline)
            break
            
    return found

all_extracted = set()
for doc in docs_data:
    all_extracted.update(extract_projects(doc['text']))

matched = all_extracted.intersection(funded_projects)

print('__RESULT__:')
print(json.dumps(len(matched)))"""

env_args = {'var_function-call-5363402596982368323': 'file_storage/function-call-5363402596982368323.json', 'var_function-call-5363402596982368440': 'file_storage/function-call-5363402596982368440.json'}

exec(code, env_args)
