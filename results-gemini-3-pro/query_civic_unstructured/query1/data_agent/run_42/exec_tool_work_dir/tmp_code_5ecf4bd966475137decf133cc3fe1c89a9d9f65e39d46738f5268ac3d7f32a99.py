code = """import json

# Load funding data
with open(locals()['var_function-call-8778761271394130701'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-17737362930517738246'], 'r') as f:
    civic_docs = json.load(f)

# Extract project names with > 50000 funding
funded_projects = set()
for record in funding_data:
    try:
        if float(record['Amount']) > 50000:
            funded_projects.add(record['Project_Name'])
    except:
        pass

extracted_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Start of Design section
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            continue
            
        # End of section logic
        if in_design_section:
            # If we hit another main header
            if "Capital Improvement Projects (" in line and "Design" not in line:
                in_design_section = False
                continue
            
            # Skip empty lines
            if not line:
                continue
            
            # Skip page numbers, agenda markers, etc.
            if line.startswith("Page ") or line.startswith("Agenda Item") or line.lower().startswith("prepared by") or line.lower().startswith("approved by"):
                continue
            
            # Skip lines starting with (cid:
            if line.startswith("(cid:"):
                continue
                
            # If a line is followed by a (cid: line (likely bullet points), it's probably a project title
            # Look ahead for the next non-empty line
            is_project = False
            for k in range(i + 1, len(lines)):
                next_l = lines[k].strip()
                if not next_l:
                    continue
                if next_l.startswith("(cid:"):
                    is_project = True
                    break
                else:
                    # Found another text line before bullets. 
                    # This implies current line might not be project title, or title is multi-line.
                    # Given the preview, titles seem single line.
                    break
            
            if is_project:
                extracted_design_projects.add(line)

# Intersection
result_projects = extracted_design_projects.intersection(funded_projects)

print("__RESULT__:")
print(json.dumps({
    "count": len(result_projects),
    "projects": list(result_projects),
    "debug_extracted": list(extracted_design_projects),
    "debug_funded": list(funded_projects)[:5]
}))"""

env_args = {'var_function-call-8778761271394130701': 'file_storage/function-call-8778761271394130701.json', 'var_function-call-8778761271394130352': 'file_storage/function-call-8778761271394130352.json', 'var_function-call-17737362930517738246': 'file_storage/function-call-17737362930517738246.json'}

exec(code, env_args)
