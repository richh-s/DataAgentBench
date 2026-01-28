code = """import json

# Load funding data
with open(locals()['var_function-call-14381109173196317470'], 'r') as f:
    funding_data = json.load(f)

# Create a set of high funding project names (Amount > 50000 is already filtered in SQL, but let's be safe and store names)
high_funding_projects = {item['Project_Name'].strip() for item in funding_data}

# Load civic docs
with open(locals()['var_function-call-3599675758928509690'], 'r') as f:
    civic_docs = json.load(f)

# Extract projects in "Capital Improvement Projects (Design)" status
# We look for the section and then check lines against high_funding_projects
found_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            continue
        elif "Capital Improvement Projects" in line and "(Design)" not in line:
            # Move to next section (Construction or Not Started)
            in_design_section = False
        elif "Disaster Recovery Projects" in line:
            in_design_section = False
            
        if in_design_section:
            # Check if line matches a funded project
            # Exact match check
            if line in high_funding_projects:
                found_projects.add(line)
            else:
                # Try checking if line is contained in project name or vice versa?
                # The hint says names match.
                # Let's also check for "Project Name" being a substring of the line, just in case of formatting chars.
                # But 'Birdview Avenue Improvements' is clean.
                # Let's stick to exact match first.
                pass

print("__RESULT__:")
print(len(found_projects))"""

env_args = {'var_function-call-14381109173196317470': 'file_storage/function-call-14381109173196317470.json', 'var_function-call-14381109173196319441': 'file_storage/function-call-14381109173196319441.json', 'var_function-call-3599675758928509690': 'file_storage/function-call-3599675758928509690.json'}

exec(code, env_args)
