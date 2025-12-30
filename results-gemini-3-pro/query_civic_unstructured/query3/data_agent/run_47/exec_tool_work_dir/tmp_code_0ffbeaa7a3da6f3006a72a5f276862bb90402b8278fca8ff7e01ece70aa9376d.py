code = """import json
import sqlite3
import pandas as pd
import re

# Load previous results
# We use the keys provided in previous turns
civic_key = 'var_function-call-620945809164347431'
funding_key = 'var_function-call-620945809164347688'

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

with open(locals()[funding_key], 'r') as f:
    funding_records = json.load(f)

df_funding = pd.DataFrame(funding_records)
df_funding['Project_Name'] = df_funding['Project_Name'].str.strip()

projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_type = None
    current_status = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect Headers
        if "Capital Improvement Projects" in line:
            current_type = "capital"
            if "(Design)" in line:
                current_status = "design"
            elif "(Construction)" in line:
                current_status = "construction"
            elif "(Not Started)" in line:
                current_status = "not started"
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster"
            if "(Design)" in line:
                current_status = "design"
            elif "(Construction)" in line:
                current_status = "construction"
            elif "(Not Started)" in line:
                current_status = "not started"

        # Check for Project Start
        is_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Check for markers like Updates, Project Description
            if "Updates:" in next_line or "Project Description:" in next_line:
                # Ensure line is a title candidate
                if line and "Projects" not in line and "Page" not in line and "Item" not in line:
                    is_project = True
        
        if is_project:
            p_name = line
            p_status = current_status
            
            # Extract block
            block_lines = []
            j = i + 1
            while j < len(lines):
                subline = lines[j].strip()
                if "Capital Improvement Projects" in subline or "Disaster Recovery Projects" in subline:
                    break
                
                # Check if new project starts
                if j + 1 < len(lines):
                    next_sub = lines[j+1].strip()
                    if ("Updates:" in next_sub or "Project Description:" in next_sub) and subline and "Projects" not in subline and "Page" not in subline:
                        break
                
                block_lines.append(subline)
                j += 1
            
            block_text = " ".join(block_lines)
            
            # Topics
            keywords = ["park", "road", "FEMA", "fire", "emergency", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail"]
            found_topics = [k for k in keywords if k.lower() in block_text.lower() or k.lower() in p_name.lower()]
            p_topic = ", ".join(sorted(list(set(found_topics))))
            
            # Refine Status
            if p_status == "construction":
                if "construction was completed" in block_text.lower() or "notice of completion" in block_text.lower():
                    p_status = "completed"
            
            projects.append({
                "Project_Name": p_name,
                "topic": p_topic,
                "status": p_status
            })
            
            i = j - 1
        
        i += 1

df_projects = pd.DataFrame(projects)

# Merge
merged = pd.merge(df_funding, df_projects, on='Project_Name', how='inner')

# Filter
def is_related(row):
    text_check = (str(row['topic']) + " " + str(row['Project_Name'])).lower()
    if 'emergency' in text_check or 'fema' in text_check:
        return True
    return False

filtered = merged[merged.apply(is_related, axis=1)]

# Select columns
# Query asks for: project names, funding sources, amounts, and statuses
final_df = filtered[['Project_Name', 'Funding_Source', 'Amount', 'status']]

print("__RESULT__:")
print(final_df.to_json(orient='records'))"""

env_args = {'var_function-call-12743158555268498599': 'file_storage/function-call-12743158555268498599.json', 'var_function-call-12743158555268500242': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-620945809164347431': 'file_storage/function-call-620945809164347431.json', 'var_function-call-620945809164347688': 'file_storage/function-call-620945809164347688.json'}

exec(code, env_args)
