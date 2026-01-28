code = """import json
import re

# Load funding data
funding_data = []
with open(locals()['var_function-call-15202175332951554163'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
civic_docs = []
with open(locals()['var_function-call-15202175332951553736'], 'r') as f:
    civic_docs = json.load(f)

# Helper to normalize status
def normalize_status(section_header, update_text):
    status = "Unknown"
    header_lower = section_header.lower()
    if "design" in header_lower:
        status = "design"
    elif "not started" in header_lower:
        status = "not started"
    elif "construction" in header_lower:
        if "completed" in update_text.lower() and "currently under construction" not in update_text.lower():
             status = "completed"
        elif "notice of completion" in update_text.lower():
             status = "completed"
        else:
             # If strictly following 3 statuses: 'design', 'completed', 'not started'
             # 'Under construction' implies it's started but not completed. 
             # Maybe it's not one of the requested statuses?
             # However, usually construction comes after design. 
             # Given the hints, maybe I should just report what I find or map 'under construction' to something.
             # Hint: "Projects have three statuses: 'design' ..., 'completed' ..., and 'not started' ..."
             # This suggests these are the only statuses of interest or the only ones defined.
             # I will label it "construction" for now and see.
             status = "construction"
    return status

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = ""
    current_project = None
    buffer_lines = []
    
    # Regex to find project blocks markers
    # The preview shows markers like (cid:190) which is unicode char \u00be (¾) or similar.
    # I'll look for the specific pattern or just lines that act as headers.
    
    # Iterate lines to find structure
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            current_section = line
            # Reset current project when section changes? 
            # Usually yes, but let's just proceed.
            i += 1
            continue
            
        # Check for project start
        # A project usually starts with a Name line, followed immediately by Update/Desc block
        # The block lines often start with a special bullet or "Updates:", "Project Description:", etc.
        # Let's look ahead to identify if this line is a project name.
        
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Check for markers in next line
            # Common markers in preview: (cid:190) Updates:, (cid:190) Project Description:
            if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                # Found a project name at 'line'
                project_name = line
                if not project_name: # Handle empty line case
                    # Sometimes name might be on previous line?
                    # Let's assume names are non-empty.
                    i += 1
                    continue

                # Clean project name
                project_name = project_name.strip()
                
                # Extract the full block until next project or section
                # We consume lines until we hit a line that looks like a new project name or section
                # A new project name is followed by a marker line.
                # A section header contains "Projects" usually.
                
                block_text = ""
                j = i + 1
                while j < len(lines):
                    sub_line = lines[j].strip()
                    if "Capital Improvement Projects" in sub_line or "Disaster Recovery Projects" in sub_line:
                        break
                    
                    # Check if sub_line is a new project name
                    # Look ahead from j
                    if j + 1 < len(lines):
                        sub_next = lines[j+1].strip()
                        if ("(cid:190)" in sub_next or "Updates:" in sub_next or "Project Description:" in sub_next) and sub_line:
                            # Found start of next project
                            break
                    
                    block_text += sub_line + " "
                    j += 1
                
                # Determine status
                status = normalize_status(current_section, block_text)
                
                # Check keywords
                # Keywords: 'emergency', 'FEMA'
                # Check in Project Name and block_text
                full_text_search = (project_name + " " + block_text).lower()
                
                is_relevant = False
                if 'emergency' in full_text_search or 'fema' in full_text_search:
                    is_relevant = True
                
                if is_relevant:
                    extracted_projects.append({
                        "Project_Name": project_name,
                        "Status": status,
                        "Raw_Status_Info": block_text[:100], # Debug
                        "Source_Doc": doc['filename']
                    })
                
                # Update main loop index
                i = j - 1 # process this line next iteration (it will increment to j)
        
        i += 1

# Join with Funding
# Funding has Project_Name. Join on exact match or fuzzy?
# Prompt says: "The Project_Name in the Funding SQLite table matches the project names that can be extracted"
# So assume exact match or close enough.

final_results = []
funding_map = {f['Project_Name']: f for f in funding_data}

# Also try to clean up extracted names if they have extra spaces or artifacts
# And check for names in funding that match extracted
for proj in extracted_projects:
    p_name = proj['Project_Name']
    
    # Try direct match
    match = funding_map.get(p_name)
    
    # If not found, try strip, or check if one is substring
    if not match:
        # Check case insensitive
        for k, v in funding_map.items():
            if k.lower() == p_name.lower():
                match = v
                break
    
    if match:
        final_results.append({
            "Project_Name": match['Project_Name'],
            "Funding_Source": match['Funding_Source'],
            "Amount": match['Amount'],
            "Status": proj['Status']
        })
    else:
        # If extracted project is not in funding, maybe we skip or include with None?
        # "What are the project names, funding sources, amounts, and statuses..."
        # Usually implies intersection.
        pass

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-8043042587493176858': ['Funding'], 'var_function-call-8043042587493178041': ['civic_docs'], 'var_function-call-15202175332951554163': 'file_storage/function-call-15202175332951554163.json', 'var_function-call-15202175332951553736': 'file_storage/function-call-15202175332951553736.json'}

exec(code, env_args)
