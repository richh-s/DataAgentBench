code = """import json
import re

# Load data
with open(locals()['var_function-call-7626705312140276657'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-7626705312140279754'], 'r') as f:
    civic_docs = json.load(f)

total_funding = 0
found_projects = []

for row in funding_data:
    name = row['Project_Name']
    amount = int(row['Amount'])
    
    # Check if Disaster Project
    is_disaster = False
    if "FEMA" in name or "CalOES" in name or "CalJPIA" in name or "Disaster" in name:
        is_disaster = True
    
    if not is_disaster:
        continue
        
    # Check Start Date in Docs
    started_2022 = False
    for doc in civic_docs:
        text = doc['text']
        if name in text:
            # Find the index of the name
            idx = text.find(name)
            while idx != -1:
                # Look at the text following the name (approx 1000 chars)
                context = text[idx:idx+1000]
                
                # Check for Start in 2022
                # matches "Begin Construction... 2022" or "Advertise... 2022"
                # Use simple regex
                if re.search("Begin Construction.*?2022", context, re.IGNORECASE):
                    started_2022 = True
                elif re.search("Advertise.*?2022", context, re.IGNORECASE):
                    started_2022 = True
                elif re.search("Start.*?2022", context, re.IGNORECASE):
                    started_2022 = True
                
                if started_2022:
                    break
                
                # Find next occurrence
                idx = text.find(name, idx+1)
        if started_2022:
            break
            
    if started_2022:
        total_funding += amount
        found_projects.append(name)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_projects}))"""

env_args = {'var_function-call-7626705312140276657': 'file_storage/function-call-7626705312140276657.json', 'var_function-call-7626705312140279754': 'file_storage/function-call-7626705312140279754.json'}

exec(code, env_args)
