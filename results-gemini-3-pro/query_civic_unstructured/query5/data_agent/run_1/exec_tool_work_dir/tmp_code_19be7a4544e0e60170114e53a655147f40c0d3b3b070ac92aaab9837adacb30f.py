code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-4188935786568154927'], 'r') as f:
    docs = json.load(f)

with open(locals()['var_function-call-4188935786568153704'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
all_project_names = set(funding_df['Project_Name'].unique())

project_metadata = {} 
# {name: {'is_disaster': False, 'start_dates': set()}}

disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Emergency"]

for doc in docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if line matches a project name exactly
        if line in all_project_names:
            current_project = line
            if current_project not in project_metadata:
                project_metadata[current_project] = {'is_disaster': False, 'start_dates': set()}
            
            # Check name for disaster cues
            if any(k in current_project for k in ["FEMA", "CalOES", "CalJPIA", "Disaster"]):
                project_metadata[current_project]['is_disaster'] = True
            continue
            
        if current_project:
            # Check for disaster keywords in text
            if any(k in line for k in disaster_keywords):
                project_metadata[current_project]['is_disaster'] = True
            
            # Check for start date
            lower_line = line.lower()
            if "begin construction" in lower_line:
                if "2022" in line:
                    project_metadata[current_project]['start_dates'].add("2022")
            elif "start" in lower_line and "date" in lower_line:
                if "2022" in line:
                    project_metadata[current_project]['start_dates'].add("2022")

# Calculate total funding
total_funding = 0
found_projects = []

for pname, info in project_metadata.items():
    is_disaster = info['is_disaster']
    started_2022 = "2022" in info['start_dates']
    
    if is_disaster and started_2022:
        amount = funding_df[funding_df['Project_Name'] == pname]['Amount'].sum()
        total_funding += amount
        found_projects.append(pname)

# Convert to native types
total_funding = int(total_funding)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_projects}))"""

env_args = {'var_function-call-4188935786568154927': 'file_storage/function-call-4188935786568154927.json', 'var_function-call-4188935786568153704': 'file_storage/function-call-4188935786568153704.json'}

exec(code, env_args)
