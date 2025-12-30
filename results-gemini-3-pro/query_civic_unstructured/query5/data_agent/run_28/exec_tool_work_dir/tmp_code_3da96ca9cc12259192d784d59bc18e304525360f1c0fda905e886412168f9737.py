code = """import json
import re

# Load data
funding_path = locals()['var_function-call-12659606830151872944']
civic_path = locals()['var_function-call-12659606830151872835']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Combine all text for easier searching, or search per doc. 
# Search per doc is better to avoid context bleeding, but "extracted from civic documents" implies they might be anywhere.
# But distinct projects might appear in different docs.
# I will search in all docs.

# Helper to find project info
matched_funding = []
total_funding = 0
debug_matches = []

# Pre-process text: create a large string or list of strings
# The projects seem to be listed in "Status Reports".
# I'll iterate through each funding record and try to find it in the text.

for record in funding_data:
    p_name = record['Project_Name']
    amount = int(record['Amount'])
    
    # Check for Disaster Type based on Name Suffix first (Strong indicator)
    is_disaster_name = any(x in p_name for x in ["(FEMA", "(CalJPIA", "(CalOES"])
    
    # Search in text
    found_in_text = False
    is_disaster_text = False
    started_2022 = False
    
    # We search in each document
    for doc in civic_data:
        text = doc['text']
        if p_name in text:
            found_in_text = True
            # Extract context: from p_name match to next double newline or next project name?
            # In the sample, project names are followed by updates.
            # I'll take a chunk of 1000 chars.
            start_idx = text.find(p_name)
            # Refine start_idx: the name should ideally be a header or at start of line
            # But simple find is okay for now.
            context = text[start_idx:start_idx+1500]
            
            # Check for Disaster keywords in context if name doesn't have it
            if not is_disaster_name:
                # Look for FEMA, CalOES, Disaster Recovery, Woolsey
                # Be careful not to match "Disaster" in the main title of the doc only.
                # But context is local to the project.
                if re.search(r'\b(FEMA|CalOES|CalJPIA|Woolsey|Disaster Recovery)\b', context, re.IGNORECASE):
                    is_disaster_text = True
            
            # Check for Start Date 2022
            # 1. Name contains 2022
            if "2022" in p_name:
                started_2022 = True
            
            # 2. Context contains indicators
            # "Begin Construction: ... 2022"
            # "Advertise: ... 2022"
            # "Complete Design: ... 2022" (Design started before, but maybe considered "started" phase?)
            # "Spring 2022", "Summer 2022", "Fall 2022", "Winter 2022"
            # "Construction was completed ... 2022" -> Start might be 2021 or 2022.
            # "Updates: ... November 2022"
            
            # Let's look for specific "Begin" or "Start" patterns with 2022
            if re.search(r'(Begin|Start|Advertise|Award).*?2022', context, re.IGNORECASE):
                started_2022 = True
            
            # Also check for "Spring 2022", "Summer 2022" in the schedule section
            if re.search(r'(Spring|Summer|Fall|Winter)\s*2022', context, re.IGNORECASE):
                started_2022 = True
                
            # If found in one doc, we can break? 
            # Projects might be mentioned in multiple docs. We want to confirm status.
            # If any doc confirms it started in 2022, we take it.
            if started_2022: 
                break
    
    # Logic to include
    # Must be Disaster (Name or Text) AND Started in 2022
    is_disaster = is_disaster_name or is_disaster_text
    
    if is_disaster and started_2022:
        total_funding += amount
        debug_matches.append({
            "name": p_name,
            "amount": amount,
            "reason": "Disaster & 2022"
        })

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matches": debug_matches}))"""

env_args = {'var_function-call-2535695967286563365': 'file_storage/function-call-2535695967286563365.json', 'var_function-call-2535695967286564710': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-12659606830151872944': 'file_storage/function-call-12659606830151872944.json', 'var_function-call-12659606830151872835': 'file_storage/function-call-12659606830151872835.json'}

exec(code, env_args)
