code = """import json
import pandas as pd

# Load Funding data
funding_path = locals()['var_function-call-5679613479952350120']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Map Project Name to Amount
project_map = {}
for item in funding_data:
    amt = item.get('Amount', 0)
    if isinstance(amt, str):
        try:
            amt = int(amt)
        except:
            amt = 0
    project_map[item['Project_Name']] = amt

# Load Docs
docs_path = locals()['var_function-call-5679613479952350149']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

found_projects = set()
target_season_terms = ["spring", "march", "april", "may"]

for doc in docs_data:
    text = doc.get('text', "")
    if not text:
        continue
    
    for proj_name in project_map:
        if proj_name in found_projects:
            continue
            
        if proj_name in text:
            idx = text.find(proj_name)
            while idx != -1:
                chunk = text[idx:idx+2000]
                chunk_lower = chunk.lower()
                
                # Check for Begin Construction
                # We need to match the line carefully
                lines = chunk.splitlines()
                for line in lines:
                    l_lower = line.lower()
                    if "begin construction" in l_lower or "start" in l_lower:
                        # Check if this line is relevant to the schedule
                        # Simple heuristic: contains 2022 and season
                        if "2022" in l_lower:
                            if any(t in l_lower for t in target_season_terms):
                                # Ensure it is a start event
                                if "begin construction" in l_lower:
                                    found_projects.add(proj_name)
                                elif "start" in l_lower and "construction" in l_lower:
                                     found_projects.add(proj_name)
                                elif "advertise" in l_lower:
                                    # Advertise is not start
                                    pass
                
                idx = text.find(proj_name, idx+1)

total_funding = sum(project_map[p] for p in found_projects)
count = len(found_projects)

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(found_projects)}))"""

env_args = {'var_function-call-10787328583776950224': ['civic_docs'], 'var_function-call-10787328583776949317': ['Funding'], 'var_function-call-8503351920656414567': 'file_storage/function-call-8503351920656414567.json', 'var_function-call-5679613479952350149': 'file_storage/function-call-5679613479952350149.json', 'var_function-call-5679613479952350120': 'file_storage/function-call-5679613479952350120.json'}

exec(code, env_args)
