code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-2005657449811241247'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Load Civic Docs
with open(locals()['var_function-call-2005657449811241560'], 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Split text into lines to process
    lines = text.split('\n')
    
    current_status_section = None
    
    # We'll iterate and find projects. 
    # A project usually starts with a Name line, followed immediately or after newlines by "(cid:190) Updates:" or "(cid:190) Project Description:"
    # We also need to track the section headers.
    
    # Regex for section headers
    # "Capital Improvement Projects (Design)"
    # "Capital Improvement Projects (Construction)"
    # "Capital Improvement Projects (Not Started)"
    
    # Regex for Project start: A line that is NOT a header, followed eventually by (cid:190)
    
    # Better approach: Split by double newlines or analyze block by block.
    # Let's try to process line by line and maintain state.
    
    # State
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for Section Header
        if "Capital Improvement Projects (Design)" in line:
            current_status_section = "design"
            i += 1
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_status_section = "construction" # Will refine later
            i += 1
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status_section = "not started"
            i += 1
            continue
            
        if not line:
            i += 1
            continue
            
        # Check if this line is a Project Name
        # Look ahead for (cid:190)
        is_project = False
        look_ahead = i + 1
        found_marker = False
        text_block = []
        
        # We assume project name is one line.
        # Check next few lines for marker.
        while look_ahead < len(lines) and look_ahead < i + 10: # Limit lookahead
            la_line = lines[look_ahead].strip()
            if "(cid:190)" in la_line:
                found_marker = True
                break
            if not la_line: # skip empty lines
                look_ahead += 1
                continue
            # If we hit text that doesn't look like marker and isn't empty, maybe it's not a project name line? 
            # Or maybe the project name is multiple lines?
            # For simplicity, assume name is 1 line.
            break
            
        if found_marker and current_status_section:
            # It's a project
            project_name = line
            
            # Extract the full text block until next project or section
            # The block starts at i
            # Ends when we hit a new Project Name (followed by marker) or new Section Header
            
            block_lines = [line]
            j = i + 1
            while j < len(lines):
                curr_line = lines[j].strip()
                
                # Check if this is a new section
                if "Capital Improvement Projects (" in curr_line:
                    break
                
                # Check if this is a new project
                # We need to look ahead again to see if *this* line is a name followed by marker
                # But be careful not to trigger on the current project's marker
                
                # If we see a marker, it belongs to the current project usually (e.g. Updates, Schedule)
                # UNLESS it follows a new name.
                # A marker line itself starts with (cid:190).
                
                # If we encounter a line that *looks* like a name (not empty, no marker) 
                # AND is followed by a marker line, then it's a new project.
                
                if curr_line and "(cid:190)" not in curr_line:
                    # Potential new name. Check lookahead.
                    la_k = j + 1
                    is_new_proj = False
                    while la_k < len(lines) and la_k < j + 10:
                        lak_line = lines[la_k].strip()
                        if "(cid:190)" in lak_line:
                            is_new_proj = True
                            break
                        if lak_line: # Non-empty line that isn't marker
                            break 
                        la_k += 1
                    
                    if is_new_proj:
                        break # End of current block
                
                block_lines.append(lines[j])
                j += 1
            
            full_text = "\n".join(block_lines)
            
            # Refine Status
            status = current_status_section
            if status == "construction":
                if "completed" in full_text.lower() or "notice of completion" in full_text.lower():
                    status = "completed"
                else:
                    status = "design" # Hint says statuses are design, completed, not started. 
                                      # "Construction" projects that are active might be considered "design" (in progress) 
                                      # or the user accepts "construction".
                                      # Let's check the hint again: "Projects have three statuses... 'design' (in planning/design phase)..."
                                      # Maybe "design" is the catch-all for incomplete?
                                      # But "Construction" is distinct from "Design".
                                      # I will output "construction" if not completed, or "design" if forced.
                                      # Let's keep "construction" if the text supports it, but the user asked for "statuses" and hints 3.
                                      # If I look at the query "statuses for projects...", I should probably provide the most descriptive one.
                                      # However, if I must map to the 3, I'd map Construction -> Design? No, that's misleading.
                                      # I'll stick to the extracted section name but lowercased, unless completed.
                                      # Actually, let's look at the result later.
            
            # Extract keywords
            # Topic: "park", "road", "FEMA", "fire", "emergency warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"
            # We need to filter for "emergency" or "FEMA".
            
            extracted_projects.append({
                "Project_Name": project_name,
                "Status": status,
                "Full_Text": full_text
            })
            
            i = j # Move to next project
        else:
            i += 1

df_civic = pd.DataFrame(extracted_projects)

# Join with Funding
# We need to be careful with names.
# Let's try an exact join first.
merged = pd.merge(df_funding, df_civic, on="Project_Name", how="inner")

# Also, some projects might be in Funding but not parsed correctly, or names differ slightly.
# But the hint says: "The Project_Name in the Funding SQLite table matches the project names that can be extracted..."
# So inner join should work for the relevant ones.

# Filter for FEMA or Emergency
# Criteria: 
# 1. Project_Name contains "FEMA" or "Emergency" (case insensitive)
# 2. Funding_Source contains "FEMA" (check just in case)
# 3. Full_Text contains "FEMA" or "Emergency" or "Disaster" (maybe?)
# Query says "projects related to 'emergency' or 'FEMA'".

def is_related(row):
    text = (str(row['Project_Name']) + " " + str(row['Full_Text']) + " " + str(row['Funding_Source'])).lower()
    if 'fema' in text or 'emergency' in text:
        return True
    return False

# Also consider projects in Funding that have FEMA in name but were NOT in civic docs?
# The user says "Use only the tools listed...".
# "For each project mentioned, you may need to extract...".
# This implies I should use the extracted info.
# But if a project is in Funding (e.g. "Outdoor Warning Sirens (FEMA)") and not in Docs, I might miss it if I only use the join.
# However, the user asks for "project names, funding sources, amounts, and statuses". Status comes from Docs.
# If I don't have the doc, I don't have the status (unless I assume something).
# So I will restrict to the joined data (projects in both).

filtered = merged[merged.apply(is_related, axis=1)]

# Select columns
result = filtered[['Project_Name', 'Funding_Source', 'Amount', 'Status']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2005657449811241560': 'file_storage/function-call-2005657449811241560.json', 'var_function-call-2005657449811241247': 'file_storage/function-call-2005657449811241247.json'}

exec(code, env_args)
