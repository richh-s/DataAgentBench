code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_function-call-8778761271394130701'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-17737362930517738246'], 'r') as f:
    civic_docs = json.load(f)

# Extract project names with > 50000 funding
funded_projects = set()
for record in funding_data:
    if float(record['Amount']) > 50000:
        funded_projects.add(record['Project_Name'])

extracted_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    in_design_section = False
    
    # Iterate through lines
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Detect start of section
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            continue
        
        # Detect end of section (start of next section)
        if in_design_section:
            if "Capital Improvement Projects (" in line and "Design" not in line:
                in_design_section = False
                continue
            
            # Heuristic for project names
            # Project names are usually non-empty, don't start with (cid:190) or (cid:131) (which are bullets)
            # And usually followed by Updates or Description
            if not line:
                continue
            
            if line.startswith("(cid:") or line.startswith("Page ") or line.startswith("Agenda Item"):
                continue
                
            # Check if it looks like a project name
            # It should be followed by a line starting with (cid:190) in the next few non-empty lines
            # Let's peek ahead
            is_project = False
            for k in range(i + 1, len(lines)):
                next_line = lines[k].strip()
                if not next_line:
                    continue
                if next_line.startswith("(cid:190)"):
                    is_project = True
                    break
                else:
                    # If we hit another text line before a bullet, the current line might not be a project name
                    # OR project name spans multiple lines?
                    # Based on preview, project name is one line.
                    break
            
            if is_project:
                extracted_design_projects.add(line)

# Intersection
result_projects = extracted_design_projects.intersection(funded_projects)

print("__RESULT__:")
print(json.dumps({
    "count": len(result_projects),
    "projects": list(result_projects),
    "extracted_sample": list(extracted_design_projects)[:10],
    "funded_sample": list(funded_projects)[:10]
}))"""

env_args = {'var_function-call-8778761271394130701': 'file_storage/function-call-8778761271394130701.json', 'var_function-call-8778761271394130352': 'file_storage/function-call-8778761271394130352.json', 'var_function-call-17737362930517738246': 'file_storage/function-call-17737362930517738246.json'}

exec(code, env_args)
