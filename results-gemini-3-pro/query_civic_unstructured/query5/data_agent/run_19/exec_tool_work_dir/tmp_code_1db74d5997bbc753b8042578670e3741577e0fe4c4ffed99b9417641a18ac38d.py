code = """import sqlite3
import pandas as pd
import json

con = sqlite3.connect("funding_database.db")
funding_data = pd.read_sql_query("SELECT * FROM Funding", con)
funding_data["Amount"] = pd.to_numeric(funding_data["Amount"])

with open(locals()["var_function-call-1716930988388569207"], "r") as f:
    civic_docs = json.load(f)

def is_disaster_project(name):
    keywords = ["FEMA", "CalOES", "CalJPIA"]
    return any(k in name for k in keywords)

disaster_funding = funding_data[funding_data["Project_Name"].apply(is_disaster_project)].copy()

def get_base_name(name):
    return name.split("(")[0].strip()

disaster_funding["Base_Name"] = disaster_funding["Project_Name"].apply(get_base_name)

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
            lc = line_clean.lower()
            if ("begin" in lc and "construction" in lc) or \
               ("start" in lc and "construction" in lc) or \
               ("construction" in lc and "completed" in lc) or \
               ("advertise" in lc):
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

env_args = {'var_function-call-3449562557564616894': 'file_storage/function-call-3449562557564616894.json', 'var_function-call-3449562557564617795': 'file_storage/function-call-3449562557564617795.json', 'var_function-call-1716930988388569207': 'file_storage/function-call-1716930988388569207.json'}

exec(code, env_args)
