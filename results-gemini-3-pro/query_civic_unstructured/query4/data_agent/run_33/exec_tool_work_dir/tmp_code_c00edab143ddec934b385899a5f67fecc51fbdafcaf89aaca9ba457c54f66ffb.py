code = """import json
import pandas as pd

# Load Funding Data
try:
    with open(locals()['var_function-call-2782363778885918640'], 'r') as f:
        funding_data = json.load(f)
    funding_df = pd.DataFrame(funding_data)

    # Load Civic Docs
    with open(locals()['var_function-call-9895724899221676838'], 'r') as f:
        civic_docs = json.load(f)
except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))
    exit()

extracted_projects = []

def is_spring_2022(date_str):
    if not date_str:
        return False
    d = date_str.lower().strip()
    if 'spring 2022' in d or 'spring, 2022' in d:
        return True
    if '2022' in d:
        if 'march' in d or 'april' in d or 'may' in d:
            return True
        # Check numeric dates 03/22, 3/22, 04/22, 05/22 etc.
        # Simple check for /03/ or /04/ or /05/ with 22 or 2022
        # But text usually uses names.
    return False

for doc in civic_docs:
    text = doc['text']
    # Normalize
    text = text.replace('(cid:190)', '>>').replace('(cid:131)', '-')
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Look for ">> Updates:"
        if 'Updates:' in line and '>>' in line:
            # Backtrack for Project Name
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                project_name = lines[j].strip()
                
                # Forward for Start Date
                start_date = None
                k = i + 1
                while k < len(lines):
                    if 'Updates:' in lines[k] and '>>' in lines[k]:
                        break 
                    
                    content = lines[k].strip()
                    # Check for start indicators
                    if 'Begin Construction:' in content:
                        parts = content.split('Begin Construction:')
                        if len(parts) > 1:
                            start_date = parts[1].strip()
                        break
                    if 'Start Date:' in content:
                        parts = content.split('Start Date:')
                        if len(parts) > 1:
                            start_date = parts[1].strip()
                        break
                    
                    k += 1
                
                if project_name and start_date:
                    extracted_projects.append({
                        'Project_Name': project_name,
                        'Start_Date': start_date
                    })

# Filter
target_projects = []
for p in extracted_projects:
    if is_spring_2022(p['Start_Date']):
        target_projects.append(p['Project_Name'])

target_projects = list(set(target_projects))

# Join with Funding
target_projects_norm = [n.lower().strip() for n in target_projects]
funding_df['Project_Name_Norm'] = funding_df['Project_Name'].str.lower().str.strip()

# We need exact matches on name?
# The hint says "The Project_Name in the Funding SQLite table matches the project names that can be extracted".
# So exact match (after normalization) should work.

matched_funding = funding_df[funding_df['Project_Name_Norm'].isin(target_projects_norm)]

unique_projects_count = matched_funding['Project_Name_Norm'].nunique()
total_funding = matched_funding['Amount'].astype(float).sum()

result = {
    "extracted_samples": extracted_projects[:5],
    "target_projects": target_projects,
    "unique_projects_count": int(unique_projects_count),
    "total_funding": float(total_funding)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4138183868648967311': ['civic_docs'], 'var_function-call-15559280801211844213': 'file_storage/function-call-15559280801211844213.json', 'var_function-call-2782363778885918640': 'file_storage/function-call-2782363778885918640.json', 'var_function-call-9895724899221676838': 'file_storage/function-call-9895724899221676838.json'}

exec(code, env_args)
