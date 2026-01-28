code = """import json

# Load funding data
with open(locals()['var_function-call-5247396609485473632'], 'r') as f:
    funding_data = json.load(f)

# Filter funding data > 50000 and create a set of names
funded_projects = {}
for item in funding_data:
    try:
        amount = float(item['Amount'])
        if amount > 50000:
            name = item['Project_Name'].strip()
            funded_projects[name.lower()] = name # Store original name if needed, or just use lower
    except:
        pass

# Load civic docs
with open(locals()['var_function-call-633765740054289148'], 'r') as f:
    docs = json.load(f)

# Set to store matched project names (original mixed case from funding dict to avoid duplicates properly)
matched_projects = set()

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None # 'design', 'other'
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        lower_line = line_clean.lower()
        
        # Identify Sections
        if "capital improvement projects (design)" in lower_line:
            current_status = 'design'
            continue
        elif "capital improvement projects" in lower_line and "design" not in lower_line:
            # Any other CIP section (Construction, Not Started)
            current_status = 'other'
            continue
        elif "disaster recovery projects" in lower_line:
            current_status = 'other' # Assuming we only want Capital projects in Design
            continue
            
        # If in Design section, check for project matches
        if current_status == 'design':
            # Check against funded projects
            # The line should strictly match or be very close.
            # The prompt says names match.
            if lower_line in funded_projects:
                matched_projects.add(funded_projects[lower_line])

print("__RESULT__:")
print(json.dumps(list(matched_projects)))"""

env_args = {'var_function-call-5247396609485473632': 'file_storage/function-call-5247396609485473632.json', 'var_function-call-633765740054289148': 'file_storage/function-call-633765740054289148.json'}

exec(code, env_args)
