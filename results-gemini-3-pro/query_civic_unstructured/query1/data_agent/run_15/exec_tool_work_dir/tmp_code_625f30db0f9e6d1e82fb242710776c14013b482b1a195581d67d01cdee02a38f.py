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
funded_projects_gt_50k = set()
for item in funding_data:
    try:
        val_str = str(item['Amount']).replace(',', '').replace('$', '')
        if val_str:
            amt = float(val_str)
            if amt > 50000:
                funded_projects_gt_50k.add(item['Project_Name'].strip())
    except Exception as e:
        pass

# Extract capital design projects
capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Locate the "Capital Improvement Projects (Design)" section
    start_match = re.search(r'Capital Improvement Projects \(Design\)', text, re.IGNORECASE)
    if not start_match:
        continue
    
    start_index = start_match.end()
    subtext = text[start_index:]
    
    # Find the end of this section
    # Next headers could be Construction, Not Started, or Disaster Recovery
    next_headers = [
        r'Capital Improvement Projects \(Construction\)',
        r'Capital Improvement Projects \(Not Started\)',
        r'Disaster Recovery Projects',
        r'Agenda Item'
    ]
    pattern = '|'.join(next_headers)
    
    end_match = re.search(pattern, subtext, re.IGNORECASE)
    if end_match:
        section_text = subtext[:end_match.start()]
    else:
        section_text = subtext

    lines = [l.strip() for l in section_text.split('\n') if l.strip()]
    
    for i, line in enumerate(lines):
        # Skip garbage
        if line.startswith('Page ') or len(line) < 3:
            continue
            
        # Check lookahead for "Updates" indicator
        if i + 1 < len(lines):
            next_line = lines[i+1]
            # Check for markers
            if 'Updates:' in next_line or '(cid:190)' in next_line or 'Project Description:' in next_line:
                 # exclude if line itself is a marker
                 if 'Updates:' not in line and '(cid:190)' not in line:
                     capital_design_projects.add(line)

# Intersection
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
