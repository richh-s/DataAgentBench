code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-10729501578572278771'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

with open(locals()['var_function-call-14279954887626903002'], 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    lines = [l.strip() for l in lines if l.strip()]
    
    for i, line in enumerate(lines):
        if "Updates:" in line:
            if i > 0:
                proj_name = lines[i-1]
                # Context: take lines until next project or end
                # Heuristic: next project title doesn't have "Updates:"
                # We'll take a safe number of lines, say 15
                chunk = " ".join(lines[i:i+15])
                extracted_projects.append({
                    "Project_Name": proj_name,
                    "text_chunk": chunk
                })

matched_projects = []
for p in extracted_projects:
    name = p['Project_Name']
    chunk = p['text_chunk'].lower()
    full_str = (name + " " + chunk).lower()
    
    # Strict Park Check
    if re.search(r'\bparks?\b', full_str):
        # Check completion date
        # Capture the date string after completed
        # Look for "completed <date>" or "complete construction: <date>"
        
        # Regex to capture Month Year (e.g. November 2022, Spring 2022)
        # We allow for some characters between (colon, space)
        # Pattern: (completed|complete construction) (punctuation/space) (Month/Season) (Year)
        
        # We find all matches to be safe
        matches = re.findall(r'(?:completed|complete construction)[\s\:\,]+([a-z]+\s+\d{4})', chunk)
        
        is_2022 = False
        completion_date = None
        for m in matches:
            if "2022" in m:
                is_2022 = True
                completion_date = m
                break
        
        if is_2022:
            matched_projects.append({
                "Project_Name": name,
                "completion_date": completion_date,
                "reason": "Found park and 2022 completion"
            })

# Merge
total = 0
final_list = []

if matched_projects:
    df_match = pd.DataFrame(matched_projects)
    df_match['join_key'] = df_match['Project_Name'].apply(lambda x: x.lower().strip())
    funding_df['join_key'] = funding_df['Project_Name'].apply(lambda x: x.lower().strip())
    
    merged = pd.merge(df_match, funding_df, on='join_key', how='inner')
    merged = merged.drop_duplicates(subset=['Project_Name_y'])
    
    total = int(merged['Amount'].sum())
    final_list = merged[['Project_Name_y', 'Amount', 'completion_date']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps({"total": total, "projects": final_list}))"""

env_args = {'var_function-call-10729501578572278771': 'file_storage/function-call-10729501578572278771.json', 'var_function-call-14279954887626903002': 'file_storage/function-call-14279954887626903002.json', 'var_function-call-17936722017621136426': {'total': 152000, 'projects': ['Malibu Road Slope Repairs', 'Encinal Canyon Road Repairs', 'PCH Signal Synchronization System Improvements Project', 'Storm Drain Trash Screens Phase Two', 'Bluffs Park Shade Structure']}}

exec(code, env_args)
