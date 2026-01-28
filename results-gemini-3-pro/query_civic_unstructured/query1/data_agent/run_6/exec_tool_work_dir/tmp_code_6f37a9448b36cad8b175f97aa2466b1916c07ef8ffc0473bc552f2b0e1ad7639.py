code = """import json
import re

# Load funding data
with open(locals()['var_function-call-10013282059874824067'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
with open(locals()['var_function-call-10013282059874822964'], 'r') as f:
    civic_data = json.load(f)

# Get the text from the document (assuming the one in the list is the correct one, it's the 2023 one)
# We need to find the document with filename 'malibucity_agenda_03222023-2060.txt' or just use the first one if it's the only one.
# The previous query returned a list.
target_doc = None
for doc in civic_data:
    if "03222023" in doc['filename']:
        target_doc = doc
        break
if not target_doc:
    # Fallback to first if explicit match fails (e.g. if the list was just one item)
    target_doc = civic_data[0]

text = target_doc['text']

# Parsing Logic
# 1. Extract block for Capital Improvement Projects (Design)
start_marker = "Capital Improvement Projects (Design)"
end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

start_idx = text.find(start_marker)
if start_idx == -1:
    print(json.dumps({"error": "Section not found"}))
else:
    # Find the nearest end marker
    end_idx = len(text)
    for marker in end_markers:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
    
    section_text = text[start_idx + len(start_marker):end_idx]
    
    # Extract project names
    # Heuristic: Line is a project name if the next non-empty line starts with "(cid:190)" or contains "Updates:" or "Project Description:"
    lines = [line.strip() for line in section_text.split('\n') if line.strip()]
    
    design_projects = []
    for i in range(len(lines) - 1):
        line = lines[i]
        next_line = lines[i+1]
        
        # Check if next_line looks like a bullet/metadata line
        if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
            # Also ensure current line is not a metadata line itself
            if not any(x in line for x in ["(cid:190)", "Updates:", "Project Schedule:", "Page ", "Agenda Item"]):
                design_projects.append(line)

    # Normalize extracted names
    design_projects = [p.strip() for p in design_projects]
    
    # Filter funding > 50,000
    # Funding Amount is string in JSON, cast to float/int
    funding_projects = {item['Project_Name'] for item in funding_data if float(item['Amount']) > 50000}
    
    # Find intersection
    # We might need exact match. Let's try exact match first.
    matches = []
    for dp in design_projects:
        if dp in funding_projects:
            matches.append(dp)
        else:
            # Optional: fuzzy match or check for suffixes?
            # The hint says names match.
            pass
            
    result = {
        "design_projects_found": design_projects,
        "matches": matches,
        "count": len(matches)
    }
    
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-10013282059874824067': 'file_storage/function-call-10013282059874824067.json', 'var_function-call-10013282059874822964': 'file_storage/function-call-10013282059874822964.json', 'var_function-call-14944349868689513364': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}]}

exec(code, env_args)
