code = """import json

# Load data
with open('var_function-call-5363402596982368323.json') as f:
    funding_data = json.load(f)

with open('var_function-call-5363402596982368440.json') as f:
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
    start_marker = "capital improvement projects (design)"
    start_idx = text_lower.find(start_marker)
    
    if start_idx == -1:
        return found
    
    next_markers = [
        "capital improvement projects (construction)",
        "capital improvement projects (not started)",
        "disaster recovery projects"
    ]
    
    end_idx = len(text)
    for mk in next_markers:
        idx = text_lower.find(mk, start_idx + len(start_marker))
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx + len(start_marker):end_idx]
    
    lines = section_text.split('\n')
    for i, line in enumerate(lines):
        sline = line.strip()
        if not sline:
            continue
            
        # Check next non-empty line for "Updates:"
        for j in range(i+1, len(lines)):
            nline = lines[j].strip()
            if not nline:
                continue
            
            if "Updates:" in nline or "Project Description:" in nline:
                # Valid project
                if "Page" not in sline and "Agenda Item" not in sline:
                    found.add(sline)
            break
            
    return found

all_extracted = set()
for doc in docs_data:
    all_extracted.update(extract_projects(doc['text']))

matched = all_extracted.intersection(funded_projects)

# Debug printing
print("Extracted:", list(all_extracted))
print("Matched:", list(matched))

print("__RESULT__:")
print(json.dumps(len(matched)))"""

env_args = {'var_function-call-5363402596982368323': 'file_storage/function-call-5363402596982368323.json', 'var_function-call-5363402596982368440': 'file_storage/function-call-5363402596982368440.json'}

exec(code, env_args)
