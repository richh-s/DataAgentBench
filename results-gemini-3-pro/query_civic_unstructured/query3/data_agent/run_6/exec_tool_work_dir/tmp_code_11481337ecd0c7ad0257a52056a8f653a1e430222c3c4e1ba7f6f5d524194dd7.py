code = """import json

# Load funding data
funding_data = []
with open(locals()['var_function-call-15202175332951554163'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
civic_docs = []
with open(locals()['var_function-call-15202175332951553736'], 'r') as f:
    civic_docs = json.load(f)

def normalize_status(section_header, update_text):
    status = "not started" # Default?
    header_lower = section_header.lower()
    text_lower = update_text.lower()
    
    if "design" in header_lower:
        status = "design"
    elif "construction" in header_lower:
        if "completed" in text_lower and "currently under construction" not in text_lower:
             status = "completed"
        elif "notice of completion" in text_lower:
             status = "completed"
        else:
             # If under construction, maybe map to 'design' or keep as 'completed' if the prompt implies simple mapping?
             # The Hint says: "Projects have three statuses: 'design', 'completed', and 'not started'".
             # If it's under construction, it's not 'not started', not 'completed', not 'design'.
             # But maybe 'design' is 'in progress'? No, design is pre-construction.
             # I will output "construction" if it doesn't match the 3, 
             # OR I will assume 'completed' only if explicitly stated.
             # Let's verify later. For now, use "construction" for clarity, or if the user forces 3, I'll have to guess.
             # But usually "Statuses" in the answer implies I should use the extracted status.
             status = "construction" 
    elif "not started" in header_lower:
        status = "not started"
        
    return status

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = ""
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            current_section = line
            i += 1
            continue
            
        # Check for project start
        # Look ahead for "Updates:" or "Project Description:"
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # We match partial string because of bullets
            if ("Updates:" in next_line or "Project Description:" in next_line or "Project Updates:" in next_line) and line:
                project_name = line
                
                # Extract block
                block_text = ""
                j = i + 1
                while j < len(lines):
                    sub_line = lines[j].strip()
                    if "Capital Improvement Projects" in sub_line or "Disaster Recovery Projects" in sub_line:
                        break
                    
                    # Check if this sub_line is a start of another project
                    if j + 1 < len(lines):
                        sub_next = lines[j+1].strip()
                        if ("Updates:" in sub_next or "Project Description:" in sub_next or "Project Updates:" in sub_next) and sub_line:
                             break
                    
                    block_text += sub_line + " "
                    j += 1
                
                # Filter by keywords
                full_text_search = (project_name + " " + block_text).lower()
                if 'emergency' in full_text_search or 'fema' in full_text_search:
                    status = normalize_status(current_section, block_text)
                    extracted_projects.append({
                        "Project_Name": project_name,
                        "Status": status
                    })
                
                i = j - 1
        i += 1

# Join
final_results = []
funding_map = {f['Project_Name']: f for f in funding_data}
funding_map_lower = {k.lower(): v for k, v in funding_map.items()}

for proj in extracted_projects:
    p_name = proj['Project_Name']
    match = funding_map.get(p_name)
    if not match:
        match = funding_map_lower.get(p_name.lower())
    
    if match:
        final_results.append({
            "Project_Name": match['Project_Name'],
            "Funding_Source": match['Funding_Source'],
            "Amount": match['Amount'],
            "Status": proj['Status']
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-8043042587493176858': ['Funding'], 'var_function-call-8043042587493178041': ['civic_docs'], 'var_function-call-15202175332951554163': 'file_storage/function-call-15202175332951554163.json', 'var_function-call-15202175332951553736': 'file_storage/function-call-15202175332951553736.json'}

exec(code, env_args)
