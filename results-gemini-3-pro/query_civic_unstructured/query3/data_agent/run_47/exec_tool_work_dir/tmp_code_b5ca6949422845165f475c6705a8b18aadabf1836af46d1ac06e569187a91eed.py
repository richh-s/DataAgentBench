code = """import json
import sqlite3
import pandas as pd

# Load previous results
civic_docs = json.load(open(locals()['var_function-call-620945809164347431']))
funding_records = json.load(open(locals()['var_function-call-620945809164347688']))

# Create DataFrame for funding
df_funding = pd.DataFrame(funding_records)

# Helper to normalize strings if needed (strip whitespace)
df_funding['Project_Name'] = df_funding['Project_Name'].str.strip()

# Parsing logic for civic_docs
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_type = None
    current_status = None
    
    # Iterate through lines
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for Headers
        if "Capital Improvement Projects" in line:
            current_type = "capital"
            if "(Design)" in line:
                current_status = "design"
            elif "(Construction)" in line:
                current_status = "construction"
            elif "(Not Started)" in line:
                current_status = "not started"
            elif "(Completed)" in line:
                 current_status = "completed"
            else:
                # Keep previous status or default? 
                # Sometimes headers are split?
                pass
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster"
            if "(Design)" in line:
                current_status = "design"
            elif "(Construction)" in line:
                current_status = "construction"
            elif "(Not Started)" in line:
                current_status = "not started"
        
        # Identify Project Name
        # Look for a line that acts as a project title.
        # It is usually followed by a line starting with (cid:190) which maps to a bullet point or marker.
        # In the text preview: "2022 Morning View..." \n "(cid:190) Updates:"
        # So we check if i+1 starts with "(cid:190)" or similar.
        # Also ensure line is not empty and not a header.
        
        is_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith("(cid:190)") or next_line.startswith("Updates:") or next_line.startswith("Project Description:"):
                # Potential project
                # Exclude if line looks like a header or empty
                if line and "Projects" not in line and "Page" not in line and "Item" not in line:
                    is_project = True
        
        if is_project:
            p_name = line
            # Extract details from the block
            # Block ends at next project or header (which we detect in main loop) or end of file
            # But we can look ahead here
            
            p_topic_keywords = []
            p_st = None
            p_et = None
            p_status = current_status
            
            # Scan block
            j = i + 1
            block_text = ""
            while j < len(lines):
                subline = lines[j].strip()
                # Stop if we hit a new project or header
                # How to detect new project? The same logic: line followed by marker.
                # But headers are easier.
                if "Capital Improvement Projects" in subline or "Disaster Recovery Projects" in subline:
                    break
                
                # Check if this subline is a new project name?
                # If subline is followed by marker, it's a new project.
                # So verify j+1
                if j + 1 < len(lines):
                    next_sub = lines[j+1].strip()
                    if (next_sub.startswith("(cid:190)") or next_sub.startswith("Updates:")) and subline and "Projects" not in subline:
                        # Found start of next project
                        break
                
                block_text += " " + subline
                j += 1
            
            # Extract info from block_text
            # Topics
            keywords = ["park", "road", "FEMA", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]
            found_topics = [k for k in keywords if k.lower() in block_text.lower()]
            # Also check Project Name for topics
            found_topics += [k for k in keywords if k.lower() in p_name.lower()]
            
            p_topic = ", ".join(sorted(list(set(found_topics))))
            
            # Status override
            if p_status == "construction":
                if "construction was completed" in block_text.lower() or "notice of completion" in block_text.lower():
                    p_status = "completed"
            
            # Dates
            # Extract "Begin Construction: <Date>"
            # Regex might be better, but let's do simple parsing
            import re
            
            # st
            st_match = re.search(r"Begin Construction[:\s]+([A-Za-z0-9\s,]+)", block_text, re.IGNORECASE)
            if st_match:
                p_st = st_match.group(1).strip()
            else:
                # Try "Advertise" as fallback for st? No, explicit ST preferred.
                # Maybe "Complete Design" implies end of design, start of construction?
                pass
                
            # et
            et_match = re.search(r"Complete Construction[:\s]+([A-Za-z0-9\s,]+)", block_text, re.IGNORECASE)
            if et_match:
                p_et = et_match.group(1).strip()
            
            projects.append({
                "Project_Name": p_name,
                "topic": p_topic,
                "type": current_type,
                "status": p_status,
                "st": p_st,
                "et": p_et
            })
            
            i = j - 1 # Update outer loop index (j is the start of next project or header)
        
        i += 1

df_projects = pd.DataFrame(projects)

# Join with Funding
# Merge on Project_Name
merged = pd.merge(df_funding, df_projects, on='Project_Name', how='inner')

# Filter for 'emergency' or 'FEMA'
# Check topic and Project_Name
def is_related(row):
    text_to_check = (str(row['topic']) + " " + str(row['Project_Name'])).lower()
    if 'emergency' in text_to_check or 'fema' in text_to_check:
        return True
    return False

filtered = merged[merged.apply(is_related, axis=1)]

# Select required columns
result_df = filtered[['Project_Name', 'Funding_Source', 'Amount', 'status']]

# Deduplicate if needed (multiple funding sources for same project might result in multiple rows - query asks for list of names, sources, amounts, statuses)
# So keeping all rows is correct.

print("__RESULT__:")
print(result_df.to_json(orient='records'))"""

env_args = {'var_function-call-12743158555268498599': 'file_storage/function-call-12743158555268498599.json', 'var_function-call-12743158555268500242': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-620945809164347431': 'file_storage/function-call-620945809164347431.json', 'var_function-call-620945809164347688': 'file_storage/function-call-620945809164347688.json'}

exec(code, env_args)
