code = """import json

# Load funding data
with open(locals()['var_function-call-4958646437851811265'], 'r') as f:
    funding_data = json.load(f)

# Filter funding data for > 50000
# Also creating a set for fast lookup
# Normalize names by stripping whitespace
high_funding_projects = set()
for record in funding_data:
    try:
        if int(record['Amount']) > 50000:
            high_funding_projects.add(record['Project_Name'].strip())
    except ValueError:
        continue

# Load civic docs
with open(locals()['var_function-call-11007850212329188700'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()

# Helper to find project names in text
def extract_design_projects(text):
    projects = []
    # Normalize text
    lines = text.split('\n')
    
    # Identify section
    # We are looking for "Capital Improvement Projects (Design)"
    # And it ends at the next major header.
    # Major headers seem to start with "Capital Improvement Projects" or "Disaster Recovery Projects"
    
    start_index = -1
    for i, line in enumerate(lines):
        if "Capital Improvement Projects (Design)" in line:
            start_index = i
            break
            
    if start_index == -1:
        return []
        
    # Find end index
    end_index = len(lines)
    for i in range(start_index + 1, len(lines)):
        line = lines[i].strip()
        if "Capital Improvement Projects" in line and "(Design)" not in line: # Next section
            end_index = i
            break
        if "Disaster Recovery Projects" in line:
            end_index = i
            break
            
    section_lines = lines[start_index+1:end_index]
    
    # Extract project names
    # Strategy: Look for lines followed by a line starting with (cid:190)
    # The (cid:190) line usually contains "Updates:" or "Project Description:"
    
    for i in range(len(section_lines) - 1):
        current_line = section_lines[i].strip()
        next_line = section_lines[i+1].strip()
        
        # Skip empty lines to find the actual next content line
        next_content_idx = i + 1
        while next_content_idx < len(section_lines) and not section_lines[next_content_idx].strip():
            next_content_idx += 1
            
        if next_content_idx < len(section_lines):
            next_line_content = section_lines[next_content_idx].strip()
            # Check if next line is a bullet point indicator
            if next_line_content.startswith('(cid:190)'):
                if current_line: # Project name shouldn't be empty
                    projects.append(current_line)
                    
    return projects

all_extracted_names = []
matched_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    extracted = extract_design_projects(text)
    all_extracted_names.extend(extracted)
    
    for proj in extracted:
        # Check for match
        if proj in high_funding_projects:
            matched_projects.append(proj)

print("__RESULT__:")
print(json.dumps({"count": len(set(matched_projects)), "matched": list(set(matched_projects)), "extracted_sample": all_extracted_names[:5]}))"""

env_args = {'var_function-call-4958646437851811265': 'file_storage/function-call-4958646437851811265.json', 'var_function-call-11007850212329188700': 'file_storage/function-call-11007850212329188700.json'}

exec(code, env_args)
