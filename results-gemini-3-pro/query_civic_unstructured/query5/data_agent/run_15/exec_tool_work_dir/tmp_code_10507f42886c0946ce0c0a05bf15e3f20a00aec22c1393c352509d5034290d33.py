code = """import pandas as pd
import json
import re

# Load data again
with open(locals()['var_function-call-14903426179249248889'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-5886239330701821032'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Normalize name
def normalize_name(name):
    name = re.sub(r'\s*\(.*?\)', '', name)
    return name.strip()

# Check uniqueness
is_unique = df_funding['Project_Name'].is_unique
print(f"Project names unique: {is_unique}")

# Process
valid_projects = []
total_funding = 0

# We need to cache text lookup to avoid re-scanning for duplicates if any, 
# but mostly we need to sum correctly.

# Build a lookup for project status/type from text first
# to handle the logic cleanly.
# Map: normalized_name -> {type, start_date}
project_metadata = {}

# We'll iterate unique normalized names from Funding to minimize text searching
unique_names = df_funding['Project_Name'].apply(normalize_name).unique()

for name in unique_names:
    # Default
    p_type = "capital" 
    start_date = None
    
    # Search in text
    # We scan all docs? Or just find one match?
    # Better to find *best* match.
    
    found = False
    for doc in civic_docs:
        text = doc['text']
        if name in text:
            idx = text.find(name)
            chunk = text[idx:idx+2000]
            
            # Type detection
            # Check for explicitly disaster headers or keywords
            local_type = "capital"
            if re.search(r'(FEMA|CalOES|CalJPIA)', chunk, re.IGNORECASE) or \
               re.search(r'(FEMA|fire|emergency|disaster)', chunk, re.IGNORECASE):
                local_type = "disaster"
            
            # Start date detection
            local_date = None
            match = re.search(r'Begin [Cc]onstruction:?\s*([A-Za-z0-9, ]+)', chunk)
            if match:
                local_date = match.group(1)
            else:
                match = re.search(r'[Cc]onstruction [Ss]tart:?\s*([A-Za-z0-9, ]+)', chunk)
                if match:
                    local_date = match.group(1)
            
            if local_date:
                start_date = local_date
                p_type = local_type
                # If we found a date, we assume this is the correct entry and stop searching docs
                # unless we want to be more exhaustive. 
                # Usually one detailed agenda report is enough.
                found = True
                break
    
    project_metadata[name] = {"type": p_type, "start_date": start_date}

# Now iterate Funding table and sum up
total_funding = 0
final_projects = []

for index, row in df_funding.iterrows():
    full_name = row['Project_Name']
    norm_name = normalize_name(full_name)
    amount = row['Amount']
    
    # Determine Type:
    # 1. From Suffix in Full Name
    row_type = "capital"
    if re.search(r'(FEMA|CalOES|CalJPIA|Disaster)', full_name, re.IGNORECASE):
        row_type = "disaster"
    else:
        # 2. From Text Metadata
        if project_metadata.get(norm_name, {}).get("type") == "disaster":
            row_type = "disaster"
    
    # Determine Date:
    # Must come from text (metadata)
    s_date = project_metadata.get(norm_name, {}).get("start_date")
    
    # Check criteria
    if row_type == "disaster" and s_date and '2022' in s_date:
        total_funding += amount
        final_projects.append(full_name)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "count": len(final_projects)}))"""

env_args = {'var_function-call-15213602487228843125': ['civic_docs'], 'var_function-call-15213602487228845628': ['Funding'], 'var_function-call-1978545647983937996': 'file_storage/function-call-1978545647983937996.json', 'var_function-call-1978545647983936213': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14903426179249248889': 'file_storage/function-call-14903426179249248889.json', 'var_function-call-5886239330701821032': 'file_storage/function-call-5886239330701821032.json', 'var_function-call-13197773909862593452': 'file_storage/function-call-13197773909862593452.json'}

exec(code, env_args)
