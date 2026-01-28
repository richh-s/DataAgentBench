code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-14903426179249248889'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-5886239330701821032'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Helper to normalize name for searching (remove suffixes)
def normalize_name(name):
    # Remove (FEMA Project), (CalOES Project), etc.
    name = re.sub(r'\s*\(.*?\)', '', name)
    return name.strip()

# Combine all texts for easier searching (or search doc by doc if needed)
# Since we need to find the context of the project name, we should search per doc.
# But a project might appear in multiple docs. We'll look for the most detailed schedule.

project_info = {}

for index, row in df_funding.iterrows():
    full_name = row['Project_Name']
    clean_name = normalize_name(full_name)
    funding_amt = int(row['Amount'])
    
    # Determine type from Name
    p_type = "capital" # default
    if re.search(r'(FEMA|CalOES|CalJPIA|Disaster)', full_name, re.IGNORECASE):
        p_type = "disaster"
    
    # Search in documents
    found_start_date = None
    found_type_in_text = None
    
    for doc in civic_docs:
        text = doc['text']
        if clean_name in text:
            # Extract context (e.g., 500 chars after name)
            # Find the start index
            idx = text.find(clean_name)
            # We want to capture the section belonging to this project.
            # Usually until the next project or double newline?
            # Let's take a chunk.
            chunk = text[idx:idx+2000]
            
            # Check for type indicators in text if not already disaster
            if p_type != "disaster":
                if "Disaster Recovery Projects" in text[:idx]: # Check previous header? Hard.
                    pass
                if re.search(r'(FEMA|CalOES|CalJPIA)', chunk, re.IGNORECASE):
                    p_type = "disaster"
                # Check for topic keywords
                if re.search(r'(FEMA|fire|emergency|disaster)', chunk, re.IGNORECASE):
                    p_type = "disaster"

            # Check for Start Date
            # Patterns: "Begin Construction: <Date>", "Start Date: <Date>", "Advertise: <Date>"
            # We prioritize Begin Construction
            
            # Regex for Begin Construction
            match = re.search(r'Begin [Cc]onstruction:?\s*([A-Za-z0-9, ]+)', chunk)
            if match:
                found_start_date = match.group(1)
            else:
                # Try "Construction Start"
                match = re.search(r'[Cc]onstruction [Ss]tart:?\s*([A-Za-z0-9, ]+)', chunk)
                if match:
                    found_start_date = match.group(1)
                else:
                    # Try "Advertise" if we consider it start? Prompt says "started". 
                    # Usually construction start is the metric.
                    # Let's check "Advertise" just in case no construction date.
                    # match = re.search(r'Advertise:?\s*([A-Za-z0-9, ]+)', chunk)
                    # if match and not found_start_date:
                    #     found_start_date = match.group(1) # maybe?
                    pass
            
            # Also check "Construction was completed <Date>" -> indicates it started before.
            # But the prompt asks for "started IN 2022".
            # If "Construction was completed November 2022", it *might* have started in 2022.
            # Let's look for "Start" strictly first.
            
            if found_start_date:
                break # Stop if we found a date
    
    project_info[full_name] = {
        "type": p_type,
        "start_date": found_start_date,
        "funding": funding_amt
    }

# Filter and Sum
total_funding = 0
disaster_projects = []

for name, info in project_info.items():
    if info['type'] == 'disaster':
        s_date = info['start_date']
        if s_date and '2022' in s_date:
            total_funding += info['funding']
            disaster_projects.append(name)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": disaster_projects, "debug_info": project_info}))"""

env_args = {'var_function-call-15213602487228843125': ['civic_docs'], 'var_function-call-15213602487228845628': ['Funding'], 'var_function-call-1978545647983937996': 'file_storage/function-call-1978545647983937996.json', 'var_function-call-1978545647983936213': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14903426179249248889': 'file_storage/function-call-14903426179249248889.json', 'var_function-call-5886239330701821032': 'file_storage/function-call-5886239330701821032.json'}

exec(code, env_args)
