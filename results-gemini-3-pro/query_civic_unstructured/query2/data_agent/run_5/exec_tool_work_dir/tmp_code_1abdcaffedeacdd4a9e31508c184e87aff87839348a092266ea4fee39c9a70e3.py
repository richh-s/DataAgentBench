code = """import json
import pandas as pd

with open(locals()["var_function-call-11358458194836773499"], "r") as f:
    civic_docs = json.load(f)

with open(locals()["var_function-call-2972859759702192456"], "r") as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df["Amount"] = pd.to_numeric(funding_df["Amount"])
project_names = funding_df["Project_Name"].unique().tolist()

matched_projects = []

for doc in civic_docs:
    text = doc["text"]
    found_projects = []
    for pname in project_names:
        idx = text.find(pname)
        if idx != -1:
            found_projects.append({"name": pname, "start": idx})
    
    found_projects.sort(key=lambda x: x["start"])
    
    for i in range(len(found_projects)):
        p = found_projects[i]
        start = p["start"]
        if i < len(found_projects) - 1:
            end = found_projects[i+1]["start"]
        else:
            end = len(text)
        
        segment = text[start:end]
        segment_lower = segment.lower()
        
        is_park = False
        if "park" in p["name"].lower():
            is_park = True
        elif "park" in segment_lower:
            is_park = True
            
        is_completed_2022 = False
        lines = segment.splitlines()
        for line in lines:
            l = line.lower()
            if "2022" in l:
                if "construction" in l:
                     if "complete" in l or "completed" in l:
                         if "begin" not in l and "start" not in l:
                             is_completed_2022 = True
        
        if is_park and is_completed_2022:
            matched_projects.append(p["name"])

unique_projects = list(set(matched_projects))
total_funding = float(funding_df[funding_df["Project_Name"].isin(unique_projects)]["Amount"].sum())

print("__RESULT__:")
print(json.dumps({
    "matched_projects": unique_projects,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-11358458194836773499': 'file_storage/function-call-11358458194836773499.json', 'var_function-call-2972859759702192456': 'file_storage/function-call-2972859759702192456.json'}

exec(code, env_args)
