code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function_call_10631543890590275884'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function_call_10631543890590275137'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

projects = []

def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower().strip()
    # Explicit "Spring 2022"
    if 'spring 2022' in date_str or 'spring, 2022' in date_str:
        return True
    # Month checking for 2022
    if '2022' in date_str:
        if 'march' in date_str or 'april' in date_str or 'may' in date_str:
            return True
        # Numeric checks
        # 03/2022, 04/2022, 05/2022
        if re.search(r'(03|3|04|4|05|5)[/-]2022', date_str) or re.search(r'2022[/-](03|3|04|4|05|5)', date_str):
             return True
    return False

cid_bullet = "(cid:190)" # Use variable to avoid repeated literals

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    extracted_projects = {}
    current_proj_name = None
    current_proj_lines = []
    
    # Improved heuristics for project name detection
    # A project name is a line that:
    # 1. Does NOT start with "(cid:"
    # 2. Is NOT a known header (Page, Agenda, etc.)
    # 3. IS followed shortly by a line starting with "(cid:190)" (Updates, Description, Schedule)
    
    ignore_keywords = ["Page ", "Agenda Item", "Public Works", "Commission", "Date prepared", "Meeting date", "Subject:", "RECOMMENDED ACTION:", "DISCUSSION:", "Capital Improvement Projects"]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if line is a potential name
        is_potential_name = True
        if line.startswith('('): is_potential_name = False
        for kw in ignore_keywords:
            if kw in line:
                is_potential_name = False
                break
        
        if is_potential_name:
            # Check lookahead for a bullet
            found_bullet = False
            for k in range(1, 5): # Look ahead 4 lines
                if i + k < len(lines):
                    next_line = lines[i+k]
                    if next_line.startswith('(cid:190)'):
                        found_bullet = True
                        break
                    # If we hit another non-bullet non-header line, maybe our assumption is wrong
                    if not next_line.startswith('(') and len(next_line) > 5:
                         # Check if this next line is actually the header (e.g. multi-line title?)
                         # For now, simplistic approach
                         pass
            
            if found_bullet:
                # Found a new project
                if current_proj_name:
                    extracted_projects[current_proj_name] = "\n".join(current_proj_lines)
                
                current_proj_name = line
                current_proj_lines = []
                i += 1
                continue
        
        if current_proj_name:
            current_proj_lines.append(line)
        
        i += 1

    if current_proj_name:
        extracted_projects[current_proj_name] = "\n".join(current_proj_lines)
        
    # Analyze extracted projects
    for proj_name, content in extracted_projects.items():
        content_lower = content.lower()
        
        # Extract Dates
        # Logic: Find "Spring 2022" context
        
        # Check specific fields first
        start_date = None
        
        # Regex for fields
        # (cid:131) Begin Construction: ...
        # (cid:131) Advertise: ...
        
        # We look for "Begin Construction: <val>"
        # or "Advertise: <val>" if begin construction is missing?
        # The prompt says "started in Spring 2022".
        
        # Let's extract all dates associated with keys
        schedule_map = {}
        # Simple extraction of Key: Value lines
        # Lines often look like: "(cid:131) Key: Value"
        
        for subline in content.split('\n'):
            if ':' in subline:
                parts = subline.split(':', 1)
                key = parts[0].replace('(cid:131)', '').replace('(cid:190)', '').strip().lower()
                val = parts[1].strip()
                schedule_map[key] = val
        
        # Determine start
        candidate_date = None
        
        if 'begin construction' in schedule_map:
            candidate_date = schedule_map['begin construction']
        elif 'advertise' in schedule_map:
             # If advertise is in Spring 2022, and begin construction is later (e.g. Summer), 
             # does the project count as "started" in Spring?
             # Usually "Started" = "Begin Construction" or project start.
             # But if "Advertise" is the first step shown...
             # Let's stick to "Begin Construction" as the primary "start". 
             # Unless the question implies "Project started" in a general sense.
             # Let's check if 'begin construction' is missing.
             pass
        
        # Let's also check for just "Start: ..."
        
        # Search for "Spring 2022" in the whole content to be safe.
        # If "Spring 2022" is found, check if it relates to a start event.
        
        if is_spring_2022(candidate_date):
            projects.append({'Project_Name': proj_name, 'Start_Date': candidate_date, 'Source': 'Begin Construction'})
        else:
            # Fallback: check if "Advertise" is Spring 2022 AND "Begin Construction" is NOT mentioned or is later?
            # Or maybe "Project Schedule" has a date.
            
            # Let's check extracting any date that is Spring 2022 and see what the key is.
            found_spring = False
            for k, v in schedule_map.items():
                if is_spring_2022(v):
                    # Found a Spring 2022 date. Check key.
                    if 'complete' not in k and 'finish' not in k and 'end' not in k:
                        # Likely a start event (Advertise, Begin, Start, etc.)
                        # Exception: "Complete Design: Spring 2022". This is an end of a phase.
                        # Does "Complete Design" mean project started? No, it started earlier.
                        # But "Advertise: Spring 2022" means construction procurement started.
                        # "Begin Construction: Spring 2022" is ideal.
                        
                        # Let's look at the sample text:
                        # "Latigo Canyon Road Retaining Wall Repair Project"
                        # "Advertise: Spring 2022"
                        # "Begin Construction: Summer 2022"
                        # Did this start in Spring 2022? Yes, the advertising started.
                        
                        # "Trancas Canyon Park Upper and Lower Slopes Repair"
                        # "Advertise: Spring 2022"
                        # "Begin Construction: Summer 2022"
                        
                        # "Permanent Skate Park"
                        # "Complete Design: Spring 2022" -> Not a start.
                        
                        # "PCH at Trancas Canyon..."
                        # "expecting comments in the Spring 2023" -> Not a start.
                        
                        # So, valid starts: "Advertise", "Begin Construction".
                        if 'advertise' in k or 'begin construction' in k or 'start' in k:
                             projects.append({'Project_Name': proj_name, 'Start_Date': v, 'Source': k})
                             found_spring = True
                             break
            
            if not found_spring:
                 # What if "Spring 2022" is in the text but not in a key-value pair?
                 pass

# Deduplicate projects if multiple entries (e.g. from multiple docs or double match)
# We use Project_Name as key
df_projects = pd.DataFrame(projects)
if not df_projects.empty:
    df_projects = df_projects.drop_duplicates(subset=['Project_Name'])

# Join
def normalize(name):
    if not name: return ""
    return name.lower().strip()

df_funding['join_key'] = df_funding['Project_Name'].apply(normalize)

if not df_projects.empty:
    df_projects['join_key'] = df_projects['Project_Name'].apply(normalize)
    merged = pd.merge(df_projects, df_funding, on='join_key', how='inner')
else:
    merged = pd.DataFrame(columns=['Amount'])

print("__RESULT__:")
print(json.dumps({
    "projects_found": projects,
    "merged_count": len(merged),
    "total_funding": merged['Amount'].sum() if not merged.empty else 0,
    "project_names": merged['Project_Name_x'].tolist() if not merged.empty else [],
    "unmerged": df_projects[~df_projects['join_key'].isin(df_funding['join_key'])]['Project_Name'].tolist() if not df_projects.empty else []
}))"""

env_args = {'var_function-call-16904404130023659614': 'file_storage/function-call-16904404130023659614.json', 'var_function-call-16904404130023657657': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-10631543890590275137': 'file_storage/function-call-10631543890590275137.json', 'var_function-call-10631543890590275884': 'file_storage/function-call-10631543890590275884.json'}

exec(code, env_args)
