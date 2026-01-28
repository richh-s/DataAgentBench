code = """import json

# Load DB results
with open(locals()['var_function-call-15734796110705634843']) as f:
    funding_data = json.load(f)

# Create a set of high-funding project names (Amount > 50000)
# The query already filtered > 50000, but being safe
funded_projects = set()
for row in funding_data:
    if float(row['Amount']) > 50000:
        funded_projects.add(row['Project_Name'].strip())

# Load Docs
with open(locals()['var_function-call-3653011467868570124']) as f:
    docs = json.load(f)

extracted_design_projects = set()

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    in_design_section = False
    buffer_line = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check section headers
        # Use simple string matching
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            buffer_line = None # Reset buffer
            continue
        
        # End conditions
        if "Capital Improvement Projects (Construction)" in line or \
           "Capital Improvement Projects (Not Started)" in line or \
           "Disaster Recovery Projects" in line:
            in_design_section = False
            buffer_line = None
            continue
            
        if in_design_section:
            # Check for bullet indicating details
            # Preview shows (cid:190)
            if line.startswith("(cid:190)") or line.startswith("Updates:") or line.startswith("Project Description:"):
                # The previous buffered line is likely the project name
                if buffer_line:
                    # Filter out noise like Page numbers or header repetitions
                    if "Page" not in buffer_line and "Agenda" not in buffer_line and "Subject:" not in buffer_line:
                        extracted_design_projects.add(buffer_line)
                buffer_line = None
            else:
                # Update buffer line. 
                # If we have consecutive text lines, we might only keep the last one.
                # To handle multi-line names, we could append?
                # But based on preview, names are single lines separated by blank lines from headers/bullets.
                # However, if there are multiple lines of text, it's safer to just take the line immediately preceding the bullet.
                buffer_line = line

# Matching
matches = []
unmatched = []
for proj in extracted_design_projects:
    if proj in funded_projects:
        matches.append(proj)
    else:
        unmatched.append(proj)

# Debug prints
print("Found Design Projects:", extracted_design_projects)
print("Matches:", matches)
print("Unmatched:", unmatched)

print("__RESULT__:")
print(json.dumps(len(matches)))"""

env_args = {'var_function-call-15734796110705634843': 'file_storage/function-call-15734796110705634843.json', 'var_function-call-15734796110705631480': 'file_storage/function-call-15734796110705631480.json', 'var_function-call-3653011467868570124': 'file_storage/function-call-3653011467868570124.json'}

exec(code, env_args)
