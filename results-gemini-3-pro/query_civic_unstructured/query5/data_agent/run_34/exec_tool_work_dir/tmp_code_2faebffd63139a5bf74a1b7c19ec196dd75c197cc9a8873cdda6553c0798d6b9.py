code = """import json
import pandas as pd
import re

# Load funding data
with open(locals()['var_function-call-6570500424665690713'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic docs
with open(locals()['var_function-call-6570500424665692862'], 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = "Unknown"
    
    # We will buffer lines to find project names
    # A project name is usually a line that is followed (after optional empty lines) by "(cid:190)" lines
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers
        if "Capital Improvement Projects" in line:
            current_section = "Capital"
            i += 1
            continue
        if "Disaster Recovery Projects" in line:
            current_section = "Disaster"
            i += 1
            continue
            
        # Check for potential project name
        # Heuristic: non-empty, no special start chars, followed by Updates
        # Skip purely numeric or page numbers
        if not line or line.startswith("Page") or line.startswith("Agenda") or line.startswith("(cid"):
            i += 1
            continue
            
        # Look ahead for project details
        is_project = False
        details_found = False
        start_year = None
        project_type = current_section
        
        # Check next few lines for keywords indicating this line was a project name
        for j in range(i + 1, min(i + 10, len(lines))):
            next_line = lines[j].strip()
            if not next_line:
                continue
            if "Updates:" in next_line or "Project Description:" in next_line or next_line.startswith("(cid:190)"):
                is_project = True
            
            # If we hit another project start or header, stop
            # But hard to detect "another project start" without validating it.
            # simpler: if we found "Updates", it's a project.
            
            if is_project:
                # Scrape details until next project
                # We need "Begin Construction"
                # Scan lines from j onwards until we hit something that looks like a new project or header?
                # Actually, let's just grab the block.
                break
        
        if is_project:
            p_name = line
            # Determine type from name if section is not clear or to override
            if any(x in p_name for x in ["FEMA", "CalOES", "CalJPIA"]):
                project_type = "Disaster"
            
            # Extract start date
            # Scan forward until next project or end
            # We'll assume the next project starts when we see a line that looks like a project name (hard) 
            # or we can just scan until we see a line with "Updates:" again (which belongs to next project)
            # or just scan a fixed number of lines or until a blank line sequence.
            # Better: Scan until next "Updates:" or Header.
            
            p_text = ""
            for k in range(i + 1, len(lines)):
                l = lines[k].strip()
                if "Capital Improvement Projects" in l or "Disaster Recovery Projects" in l:
                    break
                # Check if this line is the start of a NEW project
                # It would be a name followed by Updates. 
                # This is tricky. Let's look for the Updates line.
                # If we see "Updates:" and it's not the one we just found for this project...
                # Actually, the structure is Name -> Updates.
                # So if we see a line X, and X+1 has "Updates:", then X is a new project.
                
                # Let's peek ahead for k
                if k+1 < len(lines):
                    next_l = lines[k+1].strip()
                    if ("Updates:" in next_l or "Project Description:" in next_l) and l:
                        # Found start of new project at line k
                        break
                
                p_text += " " + l
            
            # Check for Begin Construction in p_text
            # Look for "Begin Construction: <Date>"
            match = re.search(r"Begin [Cc]onstruction:?\s*([A-Za-z0-9\s]+)", p_text)
            st_date = ""
            if match:
                st_date = match.group(1)
            
            projects.append({
                "Project_Name": p_name,
                "Type": project_type,
                "Start_Date": st_date,
                "Raw_Text": p_text[:200]
            })
            
            # Move i to k (start of next project)
            i = k
        else:
            i += 1

# Filter for Disaster and 2022
disaster_projects_2022 = []
for p in projects:
    # Check type
    is_disaster = p['Type'] == "Disaster"
    # Check start date 2022
    started_2022 = "2022" in p['Start_Date']
    
    if is_disaster and started_2022:
        disaster_projects_2022.append(p['Project_Name'])

# Join with funding
# Need to fuzzy match or exact match? Prompt says "Project_Name... matches...".
# I'll try exact match first.
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
filtered_funding = funding_df[funding_df['Project_Name'].isin(disaster_projects_2022)]

total_amount = filtered_funding['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "disaster_projects_2022": disaster_projects_2022,
    "total_amount": total_amount,
    "debug_projects": projects[:5], # print first 5 to check parsing
    "debug_disaster_all": [p for p in projects if p['Type'] == "Disaster"]
}))"""

env_args = {'var_function-call-2007247411734305584': ['Funding'], 'var_function-call-2007247411734305063': ['civic_docs'], 'var_function-call-6570500424665690713': 'file_storage/function-call-6570500424665690713.json', 'var_function-call-6570500424665692862': 'file_storage/function-call-6570500424665692862.json'}

exec(code, env_args)
