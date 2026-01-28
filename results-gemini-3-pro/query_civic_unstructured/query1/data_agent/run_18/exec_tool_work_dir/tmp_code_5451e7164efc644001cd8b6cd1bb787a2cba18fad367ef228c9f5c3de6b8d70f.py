code = """import json
import re

# Load data
funding_data = json.load(open('var_function-call-5363402596982368323.json'))
docs_data = json.load(open('var_function-call-5363402596982368440.json'))

print(f"Number of docs: {len(docs_data)}")

# Process funding
funded_projects = set()
for item in funding_data:
    try:
        amount = int(item['Amount'])
        if amount > 50000:
            funded_projects.add(item['Project_Name'].strip())
    except:
        pass

print(f"Funded projects (>50k): {len(funded_projects)}")

# Process docs to find Capital Design projects
# We want to know if there are multiple docs with different dates.
doc_dates = []
for doc in docs_data:
    text = doc.get('text', '')
    # extract date
    date_match = re.search(r'Meeting date:\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})', text)
    if date_match:
        doc_dates.append(date_match.group(1))
    else:
        doc_dates.append("Unknown")

print(f"Doc dates: {doc_dates}")

# Strategy: Extract projects from 'Capital Improvement Projects (Design)' section
# Regex for the section
# We look for "Capital Improvement Projects (Design)"
# And end at the next section.
# Next sections could be "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"
# Or just double newlines followed by a Header-like line?

# Let's define a function to extract projects from a text
def extract_design_projects(text):
    projects = set()
    # Find start
    start_pattern = r"Capital Improvement Projects \(Design\)"
    match = re.search(start_pattern, text, re.IGNORECASE)
    if not match:
        return projects
    
    start_idx = match.end()
    
    # Find end - look for known next sections or end of string
    # Known headers in the text based on preview
    next_headers = [
        r"Capital Improvement Projects \(Construction\)",
        r"Capital Improvement Projects \(Not Started\)",
        r"Disaster Recovery Projects"
    ]
    
    end_idx = len(text)
    for nh in next_headers:
        m = re.search(nh, text[start_idx:], re.IGNORECASE)
        if m:
            end_idx = min(end_idx, start_idx + m.start())
            
    section_text = text[start_idx:end_idx]
    
    # Parse projects
    # Pattern: Line with Project Name, followed by (cid:190) Updates: or similar
    # In the preview:
    # Project Name
    # (cid:190) Updates:
    #
    # Sometimes there are newlines.
    
    lines = section_text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if next non-empty line starts with (cid:190) or "Updates:"
        is_project = False
        # Look ahead
        for j in range(i+1, len(lines)):
            next_line = lines[j].strip()
            if not next_line:
                continue
            
            # Check markers
            # The bullet (cid:190) might be encoded. In the preview string it appeared as (cid:190).
            # Let's check for 'Updates:' or 'Project Description:'
            if 'Updates:' in next_line or 'Project Description:' in next_line or next_line.startswith('(cid:190)'):
                is_project = True
            break
        
        if is_project:
            # Current line is likely the project name
            # exclude lines that look like headers or page numbers
            if "Agenda Item" in line or "Page" in line:
                continue
            projects.add(line)
            
    return projects

all_design_projects = set()
for doc in docs_data:
    projs = extract_design_projects(doc['text'])
    all_design_projects.update(projs)

print(f"Extracted Design Projects: {sorted(list(all_design_projects))}")

# Intersection
matching_projects = all_design_projects.intersection(funded_projects)
print(f"Matching Projects: {len(matching_projects)}")
print(f"Matching List: {sorted(list(matching_projects))}")

print("__RESULT__:")
print(len(matching_projects))"""

env_args = {'var_function-call-5363402596982368323': 'file_storage/function-call-5363402596982368323.json', 'var_function-call-5363402596982368440': 'file_storage/function-call-5363402596982368440.json'}

exec(code, env_args)
