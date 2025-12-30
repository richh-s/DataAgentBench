code = """import json
import pandas as pd

# Load data
funding_path = locals()['var_function-call-7838865705427955035']
civic_path = locals()['var_function-call-5237099237942450066']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Process Funding
# Amount is string in JSON, convert to int/float
funding_projects = []
for row in funding_data:
    try:
        amt = float(row['Amount'])
        if amt > 50000:
            funding_projects.append(row['Project_Name'])
    except ValueError:
        continue

# Normalize funding names (strip whitespace)
funding_projects = set([n.strip() for n in funding_projects])

# Process Civic Docs
extracted_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    buffer_line = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            continue
        if "Capital Improvement Projects (Construction)" in line or \
           "Capital Improvement Projects (Not Started)" in line or \
           "Disaster Recovery Projects" in line:
            in_design_section = False
            continue
            
        if in_design_section:
            # Check for bullet point that indicates start of details
            # The preview showed "(cid:190)" or similar.
            # We'll check for "Updates:" or "Project Description:" or specific bullets if possible.
            # Also checking the unicode char if "cid:190" is not literal text.
            # But the preview showed "(cid:190)". Let's check if line starts with specific markers.
            # Also the lines containing "Updates:" seem to follow the name.
            
            is_detail_start = False
            if line.startswith("(cid:190)") or "Updates:" in line or "Project Description:" in line:
                # If the current line is a detail starter, the previous buffered line was likely the project name
                # But we need to ensure the detail starter is valid (e.g. starts with bullet or is 'Updates:')
                # In sample: "(cid:190) Updates:"
                # So if line contains "Updates:"
                 is_detail_start = True
            
            if is_detail_start:
                if buffer_line:
                    # buffer_line is the project name
                    extracted_projects.append(buffer_line)
                    buffer_line = None # Reset
            else:
                # This line might be a project name or part of the details
                # If we are already inside a project block (updates, etc), we should probably ignore until next name?
                # But how do we know we are in a block?
                # Project names don't start with (cid:131) (another bullet).
                if line.startswith("(cid:131)") or line.startswith("Page ") or "Agenda Item" in line:
                    continue
                
                # Assume this line is a potential project name, store it in buffer
                # If the next relevant line triggers 'is_detail_start', then this was the name.
                # If we encounter another potential name without triggering detail start, the previous one was probably noise or we missed something.
                # But looking at the text, names are single lines.
                buffer_line = line

# Clean extracted projects
extracted_projects_clean = set([p.strip() for p in extracted_projects])

# Find matches
# We extracted from "Design" section only.
intersection = extracted_projects_clean.intersection(funding_projects)

print("__RESULT__:")
print(json.dumps({
    "extracted_count": len(extracted_projects_clean),
    "funding_filtered_count": len(funding_projects),
    "intersection_count": len(intersection),
    "intersection_projects": list(intersection),
    "extracted_preview": list(extracted_projects_clean)[:10]
}))"""

env_args = {'var_function-call-13459136201759015403': ['Funding'], 'var_function-call-13459136201759017542': ['civic_docs'], 'var_function-call-7838865705427955035': 'file_storage/function-call-7838865705427955035.json', 'var_function-call-7838865705427954030': 'file_storage/function-call-7838865705427954030.json', 'var_function-call-5237099237942450066': 'file_storage/function-call-5237099237942450066.json'}

exec(code, env_args)
