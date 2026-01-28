code = """import json
import re
import pandas as pd

civic_docs_path = locals()['var_function-call-774567713491960706']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_function-call-774567713491960115']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

def parse_civic_doc(text):
    text = text.replace("\r", "")
    
    sections_map = {
        "Capital Improvement Projects (Design)": "Design",
        "Capital Improvement Projects (Construction)": "Construction",
        "Capital Improvement Projects (Not Started)": "Not Started",
        "Capital Improvement Projects (Completed)": "Completed",
        "Disaster Recovery Projects": "Disaster"
    }
    
    found_sections = []
    for header, status in sections_map.items():
        pattern = re.escape(header)
        for match in re.finditer(pattern, text, re.IGNORECASE):
            found_sections.append({'status': status, 'start': match.start(), 'header': match.group()})
    
    found_sections.sort(key=lambda x: x['start'])
    
    parsed_projects = []
    
    for i in range(len(found_sections)):
        section = found_sections[i]
        start_idx = section['start'] + len(section['header'])
        end_idx = found_sections[i+1]['start'] if i+1 < len(found_sections) else len(text)
        
        section_text = text[start_idx:end_idx]
        
        # Regex: Newline, Title Group, Newline, (cid:190)
        project_matches = list(re.finditer(r"\n([^\n]+)\n+\(cid:190\)", section_text))
        
        for j in range(len(project_matches)):
            p_start = project_matches[j].start(1)
            p_end = project_matches[j+1].start(0) if j+1 < len(project_matches) else len(section_text)
            
            p_title = project_matches[j].group(1).strip()
            p_content = section_text[project_matches[j].end():p_end]
            
            parsed_projects.append({
                'Project_Name': p_title,
                'Status': section['status'],
                'Content': p_content
            })
            
    return parsed_projects

all_projects = []
for doc in civic_docs:
    all_projects.extend(parse_civic_doc(doc['text']))

df_projects = pd.DataFrame(all_projects)
df_funding = pd.DataFrame(funding_data)

# Filter projects related to 'emergency' or 'FEMA'
keywords = ['emergency', 'fema']

def is_relevant(row):
    text_content = (row['Project_Name'] + " " + row['Content']).lower()
    return any(k in text_content for k in keywords)

if not df_projects.empty:
    relevant_projects = df_projects[df_projects.apply(is_relevant, axis=1)].copy()
else:
    relevant_projects = pd.DataFrame()

# Join with Funding
# Since names might not match exactly, we can try to merge on Project_Name
# But we should also check if Funding Project_Name contains the extracted name or vice versa.

# Let's verify matches.
# We will create a merged list.

merged_results = []

# Iterate over relevant projects and find funding
# Also iterate over Funding and find if they are relevant (check if Funding Name has keywords)

# Set of processed (Project_Name, Funding_ID)
processed_funding_ids = set()

# Strategy:
# 1. From extracted projects (filtered): find matching funding.
# 2. From funding (filtered): find matching extracted project info.

# 1. Extracted Relevant Projects
for idx, proj in relevant_projects.iterrows():
    p_name = proj['Project_Name']
    # Find in Funding
    # exact match
    matches = df_funding[df_funding['Project_Name'] == p_name]
    
    # If no exact match, try contains
    if matches.empty:
        # Try if funding name starts with p_name
        matches = df_funding[df_funding['Project_Name'].str.contains(re.escape(p_name), case=False, na=False)]
    
    if not matches.empty:
        for _, fund in matches.iterrows():
            merged_results.append({
                "Project_Name": fund['Project_Name'], # Use funding name as official
                "Funding_Source": fund['Funding_Source'],
                "Amount": fund['Amount'],
                "Status": proj['Status']
            })
            processed_funding_ids.add(fund['Funding_ID'])
    else:
        # Project relevant but no funding info found?
        # The prompt asks for "project names, funding sources, amounts, and statuses".
        # If no funding, maybe amount is N/A? But Database 2 is Funding Database.
        # Maybe we should only report those with funding?
        # "Join the funding data with the extracted project information based on Project_Name"
        # I will include it with None if no funding found, but the prompt implies getting these fields.
        pass

# 2. Relevant Funding Records (that were not processed yet)
# Filter funding by keywords
relevant_funding = df_funding[df_funding['Project_Name'].str.contains('emergency|fema', case=False, regex=True)]

for idx, fund in relevant_funding.iterrows():
    if fund['Funding_ID'] not in processed_funding_ids:
        # Find status from extracted projects
        f_name = fund['Project_Name']
        # Try to find in df_projects
        # Maybe f_name contains p_name?
        # e.g. "Name (FEMA)" contains "Name"
        
        # We look for a project in df_projects where f_name contains project['Project_Name']
        # This might be slow if large, but df_projects is small (from 1 doc).
        
        # Simple check:
        # status = "Unknown"
        match_proj = df_projects[df_projects['Project_Name'].apply(lambda x: x in f_name)]
        
        status = "Unknown"
        if not match_proj.empty:
            # Pick the longest match?
            # or the one that matches best.
            # Assume the first one.
            status = match_proj.iloc[0]['Status']
        
        merged_results.append({
            "Project_Name": f_name,
            "Funding_Source": fund['Funding_Source'],
            "Amount": fund['Amount'],
            "Status": status
        })
        processed_funding_ids.add(fund['Funding_ID'])

# Convert to DF for display
df_result = pd.DataFrame(merged_results)
# Remove duplicates if any
df_result = df_result.drop_duplicates()

print("__RESULT__:")
print(df_result.to_json(orient='records'))"""

env_args = {'var_function-call-774567713491960115': 'file_storage/function-call-774567713491960115.json', 'var_function-call-774567713491960706': 'file_storage/function-call-774567713491960706.json'}

exec(code, env_args)
