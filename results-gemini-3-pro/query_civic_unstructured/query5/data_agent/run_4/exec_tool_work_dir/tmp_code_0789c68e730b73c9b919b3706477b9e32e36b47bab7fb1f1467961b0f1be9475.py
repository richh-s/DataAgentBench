code = """import json
import re

# Load data
with open(locals()['var_function-call-7842478251555825910'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-7842478251555825611'], 'r') as f:
    funding_data = json.load(f)

# Extract unique project names from Funding
funding_names = set(item['Project_Name'] for item in funding_data)

# Helper to find project sections
# We will search for lines in the text that exactly match a project name in funding_data
# But since funding_data has suffixes, we should look for the "base" names.
# Or maybe the text has the full names. 
# Let's inspect the text content to see how project names appear.

full_text = "\n".join([d['text'] for d in civic_docs])

# Let's print a sample of extracted project names from the text to verify matching strategy
# We'll look for lines that are in funding_names
found_projects = []
lines = full_text.split('\n')
current_project = None
project_texts = {}

# Sort funding names by length desc to match longest first if needed, 
# but here we are matching line by line.
# Clean lines
lines = [l.strip() for l in lines if l.strip()]

matched_names_in_text = []

for line in lines:
    # Check if line is a project name
    # We strip special chars like (cid:190) from the line for check?
    # The preview showed clean names on lines.
    clean_line = line.strip()
    if clean_line in funding_names:
        current_project = clean_line
        if current_project not in project_texts:
            project_texts[current_project] = ""
        matched_names_in_text.append(clean_line)
    elif current_project:
        project_texts[current_project] += "\n" + clean_line

# Now analyze each found project
disaster_projects_2022 = []

print(f"Found {len(project_texts)} projects in text.")
print("Sample matched names:", matched_names_in_text[:10])

total_funding = 0
debug_info = []

for pname, text in project_texts.items():
    # 1. Check start date
    # Look for "Begin Construction: <Date>"
    # Regex: Begin Construction:?\s*(.*)
    # Also "Start Date" or similar? 
    # Based on preview: "(cid:131) Begin Construction: Fall 2023"
    
    start_matches = re.findall(r"Begin Construction[:\s]+([A-Za-z0-9\s]+)", text, re.IGNORECASE)
    # Also try to match "Advertise" if Begin Construction is missing? 
    # Prompt says "st: Start time/date". 
    # If multiple matches, take the first? Or check all?
    
    started_2022 = False
    start_date_found = None
    for date_str in start_matches:
        if "2022" in date_str:
            started_2022 = True
            start_date_found = date_str
            break
            
    # If no "Begin Construction" with 2022, maybe check "Construction was completed"?
    # "Construction was completed November 2022" -> Likely started in 2022 or 2021.
    # But strictly "Started in 2022".
    # I will stick to "Begin Construction" containing 2022.
    # Also check if text mentions "Start: ... 2022"
    if not started_2022:
        start_matches_2 = re.findall(r"Start(?:ed|s|ing)?[:\s]+([A-Za-z0-9\s]+)", text, re.IGNORECASE)
        for date_str in start_matches_2:
            if "2022" in date_str:
                started_2022 = True
                start_date_found = date_str
                break
                
    # 2. Check disaster related
    # Keywords: FEMA, CalOES, Disaster, Recovery, Fire, Emergency
    # Also check headers in text? (Hard to do with dict, but we can check text content)
    # Also check project name for suffixes (FEMA, CalOES)
    
    is_disaster = False
    
    # Check Name
    if any(x in pname for x in ["FEMA", "CalOES", "CalJPIA", "Disaster", "Recovery"]):
        is_disaster = True
        
    # Check Text
    if not is_disaster:
        # Check topic keywords in text
        # (cid:190) Project Description: ...
        if re.search(r"(FEMA|CalOES|CalJPIA|Woolsey|Disaster|Recovery|Emergency)", text, re.IGNORECASE):
            is_disaster = True
            
    if started_2022 and is_disaster:
        disaster_projects_2022.append(pname)
        debug_info.append({"name": pname, "date": start_date_found, "reason": "Matched"})

# Calculate funding
# Strategy: For each project in disaster_projects_2022, sum funding.
# AND sum funding for related "suffix" projects in funding_database if they exist.
# Example: If "Project A" is found, sum "Project A", "Project A (FEMA)", etc.

processed_funding_ids = set()
final_funding_amount = 0
matched_funding_records = []

for target_pname in disaster_projects_2022:
    # Find all funding records that match target_pname or target_pname + " ("
    for record in funding_data:
        r_pname = record['Project_Name']
        r_amt = record['Amount']
        r_id = record['Funding_ID']
        
        match = False
        if r_pname == target_pname:
            match = True
        elif r_pname.startswith(target_pname + " ("):
            match = True
            
        if match:
            if r_id not in processed_funding_ids:
                final_funding_amount += int(r_amt)
                processed_funding_ids.add(r_id)
                matched_funding_records.append(r_pname)

print("__RESULT__:")
print(json.dumps({
    "disaster_projects_started_2022": debug_info,
    "matched_funding_records": matched_funding_records,
    "total_funding": final_funding_amount
}))"""

env_args = {'var_function-call-7842478251555825910': 'file_storage/function-call-7842478251555825910.json', 'var_function-call-7842478251555825611': 'file_storage/function-call-7842478251555825611.json'}

exec(code, env_args)
