code = """import json
import re

# Load funding data
# Using the variable from previous call. The user provided key var_function-call-4872762091954436572 for funding
# But wait, I need to read the variable content.
# The tool output says "The result is too large, so it is stored in a file. The file path is stored under key: var_function-call-4872762091954436572"
# So I need to read the file.
funding_file = locals()['var_function-call-4872762091954436572']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Filter funding for > 50,000
high_funding_projects = set()
for item in funding_data:
    try:
        amount = float(item['Amount'])
        if amount > 50000:
            high_funding_projects.add(item['Project_Name'].strip())
    except:
        pass

# Load civic docs
docs_file = locals()['var_function-call-4872762091954434845']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

# Section headers to look for
target_header = "Capital Improvement Projects (Design)"
# Potential next headers
next_headers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects",
    "Disaster Recovery Projects (Design)",
    "Disaster Recovery Projects (Construction)",
    "Disaster Recovery Projects (Not Started)"
]

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the target section
    start_idx = text.find(target_header)
    if start_idx == -1:
        continue
    
    # Move start_idx to after the header
    start_idx += len(target_header)
    
    # Find end of section
    end_idx = len(text)
    for nh in next_headers:
        idx = text.find(nh, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx:end_idx]
    
    # Parse section text to find project names
    lines = [line.strip() for line in section_text.split('\n')]
    
    # Iterate through lines
    # Pattern: Project Name (line) -> Bullet line (Updates/Desc/Schedule)
    for i in range(len(lines) - 1):
        line = lines[i]
        next_line = lines[i+1]
        
        # Candidate project name line should not be empty and not look like a bullet
        if not line:
            continue
        
        # Check if next line looks like a bullet line starting a block
        # Bullet chars often appear as non-alphanumeric.
        # Check for specific keywords in next line
        if re.search(r'^\W+\s*(Updates|Project Description|Project Schedule|Estimated Schedule)', next_line) or \
           next_line.startswith('(cid:190)') or \
           re.match(r'^[\u2022\u25E6\u2023\u2043\u2219]\s', next_line):
            
            # Further validation of the project name line
            # Should not be a page number or header junk
            if "Page" in line and "of" in line:
                continue
            if "Agenda Item" in line:
                continue
            
            capital_design_projects.add(line)

# Intersection
result_projects = capital_design_projects.intersection(high_funding_projects)

print("__RESULT__:")
print(json.dumps({
    "count": len(result_projects),
    "projects": list(result_projects),
    "debug_capital_design": list(capital_design_projects)
}))"""

env_args = {'var_function-call-4872762091954436572': 'file_storage/function-call-4872762091954436572.json', 'var_function-call-4872762091954434845': 'file_storage/function-call-4872762091954434845.json'}

exec(code, env_args)
