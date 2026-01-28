code = """import json
import re

# Load funding data
funding_path = locals()['var_function-call-1599065279211733274']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
docs_path = locals()['var_function-call-1599065279211735013']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Filter funding for Amount > 50000
# Ensure Amount is treated as int/float
funded_projects_gt_50k = set()
for item in funding_data:
    try:
        amt = float(str(item['Amount']).replace(',', '').replace('$', ''))
        if amt > 50000:
            funded_projects_gt_50k.add(item['Project_Name'].strip())
    except:
        pass

# Extract capital design projects
capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Locate the "Capital Improvement Projects (Design)" section
    # Regex to find the section header
    # It might be spread across lines or have slightly different spacing, but exact string is likely "Capital Improvement Projects (Design)"
    
    # We want to capture text between "Capital Improvement Projects (Design)" and the next section header.
    # Potential next headers: "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects..."
    
    # Let's find the start
    start_match = re.search(r'Capital Improvement Projects \(Design\)', text, re.IGNORECASE)
    if not start_match:
        continue
    
    start_index = start_match.end()
    
    # Find the end of this section
    # We look for the next section header.
    # Patterns to look for as next header:
    # "Capital Improvement Projects (Construction)"
    # "Capital Improvement Projects (Not Started)"
    # "Disaster Recovery Projects"
    # "Public Works Commission" (start of next item?)
    # "Agenda Item" (footer?)
    
    # Let's slice the text from start_index
    subtext = text[start_index:]
    
    # Find the nearest next section header
    next_section_pattern = r'(Capital Improvement Projects \((Construction|Not Started)\)|Disaster Recovery Projects|Agenda Item)'
    end_match = re.search(next_section_pattern, subtext, re.IGNORECASE)
    
    if end_match:
        section_text = subtext[:end_match.start()]
    else:
        section_text = subtext # Go to end if no other section found
        
    # Now parse project names from section_text
    # Structure seems to be:
    # Project Name
    # (cid:190) Updates:
    
    # or just:
    # Project Name
    # Updates:
    
    lines = section_text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if the NEXT line starts with an update marker
        # Look ahead
        is_project_name = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Common update markers in the text preview: "(cid:190) Updates:", "(cid:131)", "Updates:"
            if '(cid:190)' in next_line or 'Updates:' in next_line or 'Project Description:' in next_line:
                is_project_name = True
            # Also sometimes there might be empty lines between name and update
            # But the preview shows them adjacent or close.
            # Let's try searching for the marker in the next few lines?
            # Actually, let's stick to the immediate next non-empty line check if possible.
        
        # Refined strategy: Iterate lines. If a line is followed (ignoring empty lines) by a line containing "Updates:" or "(cid:190)", it's a project name.
        
    # Re-loop with lookahead ignoring empty lines
    clean_lines = [l.strip() for l in lines if l.strip()]
    for i, line in enumerate(clean_lines):
        # Skip lines that are page numbers or artifacts
        if line.startswith('Page ') or line.startswith('Agenda Item'):
            continue
        if line == "(cid:190)": continue
            
        # Check if next line is an update block
        if i + 1 < len(clean_lines):
            next_l = clean_lines[i+1]
            if 'Updates:' in next_l or '(cid:190)' in next_l or 'Project Description:' in next_l or 'Project Schedule:' in next_l:
                # Potential project name
                # Also exclude lines that are clearly not names
                if not line.startswith('(cid:') and 'Updates:' not in line:
                    capital_design_projects.add(line)

# Intersection
result_projects = capital_design_projects.intersection(funded_projects_gt_50k)

print("__RESULT__:")
print(json.dumps({
    "count": len(result_projects),
    "projects": list(result_projects),
    "debug_extracted": list(capital_design_projects),
    "debug_funded": list(funded_projects_gt_50k)[:10] # Sample
}))"""

env_args = {'var_function-call-1599065279211733274': 'file_storage/function-call-1599065279211733274.json', 'var_function-call-1599065279211735013': 'file_storage/function-call-1599065279211735013.json'}

exec(code, env_args)
