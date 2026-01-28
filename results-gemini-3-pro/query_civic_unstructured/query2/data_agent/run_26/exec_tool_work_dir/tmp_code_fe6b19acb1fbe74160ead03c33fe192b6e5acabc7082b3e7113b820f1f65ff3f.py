code = """import json
import pandas as pd

# Load data
civic_docs_path = locals()['var_function-call-14510963906005286500']
funding_path = locals()['var_function-call-14510963906005285081']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Known projects from DB
known_projects = set(funding_df['Project_Name'].str.strip())

identified_projects = []

for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_proj = None
    buffer = []

    for line in lines:
        s_line = line.strip()
        # Heuristic: if line matches a known project name exactly
        if s_line in known_projects:
            # Process previous
            if current_proj:
                full_text = " ".join(buffer).lower()
                # Check criteria
                # 1. Park related
                is_park = "park" in current_proj.lower() or "park" in full_text
                # 2. Completed in 2022
                # Look for 'completed' and '2022' close to each other or in the update section
                is_completed_2022 = False
                if "completed" in full_text and "2022" in full_text:
                    # Refine: check for "was completed" or "construction was completed"
                    if "was completed" in full_text:
                        is_completed_2022 = True
                    # Check for "completed, november 2022" pattern
                    elif "completed," in full_text: 
                        is_completed_2022 = True
                
                if is_park and is_completed_2022:
                    identified_projects.append(current_proj)
            
            current_proj = s_line
            buffer = []
        else:
            if current_proj:
                buffer.append(s_line)
    
    # Last one
    if current_proj:
        full_text = " ".join(buffer).lower()
        is_park = "park" in current_proj.lower() or "park" in full_text
        is_completed_2022 = False
        if "completed" in full_text and "2022" in full_text:
             if "was completed" in full_text or "completed," in full_text:
                 is_completed_2022 = True
        
        if is_park and is_completed_2022:
            identified_projects.append(current_proj)

# Unique projects
unique_projects = list(set(identified_projects))

# Sum funding
total_amount = funding_df[funding_df['Project_Name'].isin(unique_projects)]['Amount'].sum()

print("__RESULT__:")
print(json.dumps({"projects": unique_projects, "total": float(total_amount)}))"""

env_args = {'var_function-call-7656597533557058168': 'file_storage/function-call-7656597533557058168.json', 'var_function-call-7656597533557058431': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14510963906005286500': 'file_storage/function-call-14510963906005286500.json', 'var_function-call-14510963906005285081': 'file_storage/function-call-14510963906005285081.json'}

exec(code, env_args)
