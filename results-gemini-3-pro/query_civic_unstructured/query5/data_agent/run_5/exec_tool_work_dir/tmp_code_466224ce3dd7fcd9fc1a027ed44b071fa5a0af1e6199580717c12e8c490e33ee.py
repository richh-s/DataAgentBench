code = """import json
import pandas as pd
import re

funding_key = 'var_function-call-5948002065454245776'
civic_key = 'var_function-call-16801435053076295994'

file_path_funding = locals()[funding_key]
file_path_civic = locals()[civic_key]

df_funding = pd.read_json(file_path_funding)

with open(file_path_civic, 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + chr(10)

disaster_suffixes = [
    '(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)', 
    '(FEMA/CalOES Project)', '(FEMA)', '(CalOES)'
]

def get_base_name(name):
    base = name
    for suffix in disaster_suffixes:
        base = base.replace(suffix, '').strip()
    return base

def has_disaster_suffix(name):
    for suffix in disaster_suffixes:
        if suffix.lower() in name.lower():
            return True
    return False

# 1. Identify Base Names that are Disaster Related (have at least one suffix record)
all_base_names = set([get_base_name(n) for n in df_funding['Project_Name'].unique()])
disaster_base_names = set()
for name in df_funding['Project_Name'].unique():
    if has_disaster_suffix(name):
        disaster_base_names.add(get_base_name(name))

# 2. Extract Start Dates for ALL base names (we need to check dates for disaster projects)
project_info = {} 

for base_name in disaster_base_names:
    try:
        pattern = re.escape(base_name)
        matches = [m.start() for m in re.finditer(pattern, full_text, re.IGNORECASE)]
        
        for match_idx in matches:
            context = full_text[match_idx:match_idx+2000]
            date_match = re.search(r'Begin Construction:\s*(.*)', context, re.IGNORECASE)
            if date_match:
                date_str = date_match.group(1).strip()
                project_info[base_name] = date_str
                break 
    except Exception:
        continue

# 3. Sum Funding
total_funding = 0
included_projects = set()

for index, row in df_funding.iterrows():
    name = row['Project_Name']
    base_name = get_base_name(name)
    amount = row['Amount']
    
    # Check if this project (base name) is a disaster project
    if base_name in disaster_base_names:
        # Check start date
        start_date = project_info.get(base_name)
        if start_date and "2022" in start_date:
            total_funding += amount
            included_projects.add(base_name)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": list(included_projects)}))"""

env_args = {'var_function-call-8962819121667412249': ['Funding'], 'var_function-call-8962819121667415660': ['civic_docs'], 'var_function-call-5948002065454245776': 'file_storage/function-call-5948002065454245776.json', 'var_function-call-8815674849536334134': 'file_storage/function-call-8815674849536334134.json', 'var_function-call-16801435053076295994': 'file_storage/function-call-16801435053076295994.json', 'var_function-call-17107842843305490693': {'total_funding': 993000, 'projects': [{'name': 'Birdview Avenue Improvements (CalOES Project)', 'base': 'Birdview Avenue Improvements', 'date': 'April 2022', 'amount': 85000}, {'name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'base': 'Birdview Avenue Improvements', 'date': 'April 2022', 'amount': 14000}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'base': 'Broad Beach Road Water Quality Infrastructure Repairs', 'date': 'Spring 2022', 'amount': 81000}, {'name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'base': 'Corral Canyon Culvert Repairs', 'date': 'April 2022', 'amount': 43000}, {'name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'base': 'Corral Canyon Culvert Repairs', 'date': 'April 2022', 'amount': 15000}, {'name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'base': 'Corral Canyon Road Bridge Repairs', 'date': 'Summer 2022', 'amount': 25000}, {'name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'base': 'Corral Canyon Road Bridge Repairs', 'date': 'Summer 2022', 'amount': 58000}, {'name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'base': 'Encinal Canyon Road Drainage Improvements', 'date': 'Fall 2022', 'amount': 18000}, {'name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'base': 'Encinal Canyon Road Drainage Improvements', 'date': 'Fall 2022', 'amount': 94000}, {'name': 'Guardrail Replacement Citywide (FEMA Project)', 'base': 'Guardrail Replacement Citywide', 'date': 'Summer 2022', 'amount': 22000}, {'name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'base': 'Guardrail Replacement Citywide', 'date': 'Summer 2022', 'amount': 45000}, {'name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'base': 'Latigo Canyon Road Culvert Repairs', 'date': 'April 2022', 'amount': 36000}, {'name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'base': 'Latigo Canyon Road Culvert Repairs', 'date': 'April 2022', 'amount': 44000}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'base': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'date': 'April 2022', 'amount': 91000}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'base': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'date': 'April 2022', 'amount': 78000}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'base': 'Trancas Canyon Park Planting and Irrigation Repairs', 'date': 'Spring 2022', 'amount': 92000}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'base': 'Trancas Canyon Park Slope Stabilization Project', 'date': 'Spring 2022', 'amount': 43000}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'base': 'Trancas Canyon Park Slope Stabilization Project', 'date': 'Spring 2022', 'amount': 32000}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'base': 'Westward Beach Road Shoulder Repairs', 'date': 'Fall 2022', 'amount': 77000}]}}

exec(code, env_args)
