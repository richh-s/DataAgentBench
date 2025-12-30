code = """import pandas as pd
import json
import re

# Load Funding
with open(locals()["var_function-call-3449562557564616894"], "r") as f:
    funding_data = pd.DataFrame(json.load(f))
funding_data["Amount"] = pd.to_numeric(funding_data["Amount"])

# Load Civic Docs
with open(locals()["var_function-call-1716930988388569207"], "r") as f:
    civic_docs = json.load(f)

# Disaster Helper
def is_disaster_project(name):
    keywords = ["FEMA", "CalOES", "CalJPIA"]
    return any(k in name for k in keywords)

disaster_funding = funding_data[funding_data["Project_Name"].apply(is_disaster_project)].copy()
disaster_funding["Base_Name"] = disaster_funding["Project_Name"].apply(lambda x: x.split("(")[0].strip())

# Strict Parsing
project_start_years = {}

known_projects = set(funding_data["Project_Name"].unique())
known_base_names = set(disaster_funding["Base_Name"].unique())
all_names = known_projects.union(known_base_names)
normalized_names = {n.lower().strip(): n for n in all_names}

for doc in civic_docs:
    text = doc["text"]
    lines = text.split(chr(10))
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        norm_line = line_clean.lower()
        if norm_line in normalized_names:
            current_project = normalized_names[norm_line]
            continue
            
        if current_project and "2022" in line_clean:
            # Strict Regex
            # pattern: begin/start construction ... 2022
            # or construction ... completed ... 2022
            
            # Using simple string checks to avoid regex escaping hell in tool call
            lc = line_clean.lower()
            
            # Check for specific phrases
            # "begin construction" AND "2022"
            # "start construction" AND "2022"
            # "construction" AND "completed" AND "2022"
            
            matched = False
            if "2022" in lc:
                if "begin construction" in lc or "start construction" in lc:
                    matched = True
                elif "construction" in lc and "completed" in lc:
                    matched = True
            
            if matched:
                project_start_years[current_project] = 2022

total_funding = 0
funded_projects = []

for index, row in disaster_funding.iterrows():
    p_name = row["Project_Name"]
    b_name = row["Base_Name"]
    amount = row["Amount"]
    
    started = False
    if p_name in project_start_years and project_start_years[p_name] == 2022:
        started = True
    elif b_name in project_start_years and project_start_years[b_name] == 2022:
        started = True
        
    if started:
        total_funding += amount
        funded_projects.append({"name": p_name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "funded_projects": funded_projects, "debug_starts": list(project_start_years.keys())}))"""

env_args = {'var_function-call-3449562557564616894': 'file_storage/function-call-3449562557564616894.json', 'var_function-call-3449562557564617795': 'file_storage/function-call-3449562557564617795.json', 'var_function-call-1716930988388569207': 'file_storage/function-call-1716930988388569207.json', 'var_function-call-8005303632771619844': {'total_funding': 568000, 'funded_projects': [{'name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'amount': 81000}, {'name': 'Clover Heights Storm Drain (FEMA Project)', 'amount': 21000}, {'name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'amount': 94000}, {'name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'amount': 36000}, {'name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'amount': 44000}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000}, {'name': 'Malibu Road Slope Repairs (CalOES Project)', 'amount': 37000}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'amount': 44000}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'amount': 43000}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'amount': 77000}], 'debug_starts': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)']}}

exec(code, env_args)
