code = """import json

# Load funding data
funding_path = locals()['var_function-call-1599065279211733274']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
docs_path = locals()['var_function-call-1599065279211735013']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Filter funding
funded_projects_gt_50k = set()
for item in funding_data:
    try:
        val_str = str(item['Amount']).replace(',', '').replace('$', '')
        if val_str:
            amt = float(val_str)
            if amt > 50000:
                funded_projects_gt_50k.add(item['Project_Name'].strip())
    except:
        pass

capital_design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    
    start_marker = "Capital Improvement Projects (Design)"
    start_idx = text.find(start_marker)
    if start_idx == -1:
        continue
    
    # Start after the marker
    start_idx += len(start_marker)
    subtext = text[start_idx:]
    
    # Find end
    end_markers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects",
        "Agenda Item"
    ]
    
    end_idx = len(subtext)
    for m in end_markers:
        idx = subtext.find(m)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = subtext[:end_idx]
    
    lines = [l.strip() for l in section_text.split('\n') if l.strip()]
    
    for i in range(len(lines)):
        line = lines[i]
        # Skip junk
        if line.startswith("Page ") or len(line) < 3:
            continue
        if "Updates" in line or "Project Schedule" in line:
            continue
            
        # Check next line for signs of being a description start
        if i + 1 < len(lines):
            next_line = lines[i+1]
            # If next line has "Updates:" or "(cid:190)" or "Project Description:", current line is likely title
            # Checking substring is safer than regex
            is_header = False
            if "Updates:" in next_line: is_header = True
            if "(cid:190)" in next_line: is_header = True
            if "Project Description:" in next_line: is_header = True
            
            if is_header:
                capital_design_projects.add(line)

result_projects = capital_design_projects.intersection(funded_projects_gt_50k)

print("__RESULT__:")
print(json.dumps({
    "count": len(result_projects),
    "projects": list(result_projects),
    "debug_extracted": list(capital_design_projects),
    "debug_funded_sample": list(funded_projects_gt_50k)[:5]
}))"""

env_args = {'var_function-call-1599065279211733274': 'file_storage/function-call-1599065279211733274.json', 'var_function-call-1599065279211735013': 'file_storage/function-call-1599065279211735013.json'}

exec(code, env_args)
