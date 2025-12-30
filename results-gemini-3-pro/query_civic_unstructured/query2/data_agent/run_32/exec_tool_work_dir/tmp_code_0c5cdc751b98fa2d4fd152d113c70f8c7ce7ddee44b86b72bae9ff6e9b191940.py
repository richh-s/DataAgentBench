code = """import json
import pandas as pd
import re

# Load Funding Data
with open(locals()['var_function-call-4014968237340428108'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
project_names = set(funding_df['Project_Name'].unique())

# Load Civic Docs
with open(locals()['var_function-call-4014968237340429633'], 'r') as f:
    civic_docs = json.load(f)

identified_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_project_buffer = []
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check if line matches a project name
        # We check for exact match or contained match to handle headers
        found_name = None
        for name in project_names:
            # Check if the line is exactly the project name or "Project Name:"
            if line_clean.lower() == name.lower() or line_clean.lower() == name.lower() + ":":
                found_name = name
                break
        
        if found_name:
            if current_project:
                identified_projects.append({
                    'Project_Name': current_project,
                    'text': " ".join(current_project_buffer)
                })
            current_project = found_name
            current_project_buffer = []
        elif current_project:
            current_project_buffer.append(line_clean)
            
    if current_project:
        identified_projects.append({
            'Project_Name': current_project,
            'text': " ".join(current_project_buffer)
        })

# Filter
park_projects_2022 = []
for proj in identified_projects:
    name = proj['Project_Name']
    text = proj['text'].lower()
    
    # Check Topic
    is_park = 'park' in name.lower() or 'park' in text
    
    # Check Status and Date
    # looking for "completed" and "2022"
    # Example: "Construction was completed November 2022"
    if is_park:
        if 'completed' in text and '2022' in text:
            # check proximity or just presence? 
            # The prompt says "completed in 2022". 
            # If the text says "Completed: November 2022", that works.
            # If it says "Updates: ... completed ... 2022", that works.
            # We must avoid "Not completed in 2022" but that's unlikely in these reports.
            # A potential false positive is "Completed design in 2022" for a "completed" status query?
            # The prompt asks for "projects that were completed in 2022". Usually implies construction completion.
            # The text often distinguishes "Complete Design" and "Complete Construction".
            # Example text: "Complete Construction: April 2023", "Construction was completed November 2022"
            
            # Let's be more specific: "construction" and "completed" and "2022"?
            # Or just "completed" and "2022" as per hint?
            # Hint says: "Projects have three statuses: 'design', 'completed', 'not started'"
            # If the text says "Construction was completed", the status is completed.
            # If it says "Complete Design: Summer 2023", the status is design (future) or design completed (past).
            # But the project status itself is "completed" only if construction is done.
            
            # Let's look for "construction was completed" or "completed construction" or just "completed" associated with 2022
            # AND verify it is not "design".
            
            if "construction was completed" in text or "complete construction: 2022" in text or ("completed" in text and "2022" in text and "design" not in text):
                 park_projects_2022.append(name)
            elif "completed" in text and "2022" in text:
                # Fallback, but exclude if it explicitly says "Complete Design: ... 2022" and nothing about construction completion.
                if "complete design" in text and "begin construction" in text:
                     # This is likely a schedule. Check dates.
                     pass 
                else:
                     park_projects_2022.append(name)

park_projects_2022 = list(set(park_projects_2022))

total_funding = 0
matched_records = []
for name in park_projects_2022:
    record = funding_df[funding_df['Project_Name'] == name]
    if not record.empty:
        amount = record['Amount'].sum()
        total_funding += amount
        matched_records.append({"name": name, "amount": int(amount)})

print("__RESULT__:")
print(json.dumps({"projects": matched_records, "total": int(total_funding)}))"""

env_args = {'var_function-call-1448852997668966591': ['civic_docs'], 'var_function-call-1448852997668967958': ['Funding'], 'var_function-call-4014968237340428108': 'file_storage/function-call-4014968237340428108.json', 'var_function-call-4014968237340429633': 'file_storage/function-call-4014968237340429633.json'}

exec(code, env_args)
