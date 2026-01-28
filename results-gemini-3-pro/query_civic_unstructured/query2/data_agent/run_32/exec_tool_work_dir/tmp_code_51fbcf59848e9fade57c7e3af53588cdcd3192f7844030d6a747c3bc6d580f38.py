code = """import json
import pandas as pd

funding_key = "var_function-call-4014968237340428108"
docs_key = "var_function-call-4014968237340429633"

with open(locals()[funding_key], "r") as f:
    funding_data = json.load(f)

with open(locals()[docs_key], "r") as f:
    docs_data = json.load(f)

df = pd.DataFrame(funding_data)
df["Amount"] = pd.to_numeric(df["Amount"])
all_names = list(df["Project_Name"].unique())

matches = []

for d in docs_data:
    txt = d["text"]
    lines = txt.splitlines()
    
    current_proj = None
    chunk = []
    
    for line in lines:
        l = line.strip()
        if len(l) == 0:
            continue
            
        found = None
        l_lower = l.lower()
        
        for name in all_names:
            if l_lower == name.lower():
                found = name
                break
        
        if found:
            if current_proj:
                full_text = " ".join(chunk).lower()
                
                # Check criteria
                is_park = False
                if "park" in full_text: is_park = True
                if "park" in current_proj.lower(): is_park = True
                
                is_completed = False
                if "completed" in full_text:
                    if "2022" in full_text:
                        is_completed = True
                
                if is_park and is_completed:
                    matches.append(current_proj)

            current_proj = found
            chunk = []
        elif current_proj:
            chunk.append(l)

    if current_proj:
        full_text = " ".join(chunk).lower()
        is_park = False
        if "park" in full_text: is_park = True
        if "park" in current_proj.lower(): is_park = True
        
        is_completed = False
        if "completed" in full_text:
            if "2022" in full_text:
                is_completed = True
        
        if is_park and is_completed:
            matches.append(current_proj)

matches = list(set(matches))
total = df[df["Project_Name"].isin(matches)]["Amount"].sum()

print("__RESULT__:")
print(json.dumps({"matches": matches, "total": int(total)}))"""

env_args = {'var_function-call-1448852997668966591': ['civic_docs'], 'var_function-call-1448852997668967958': ['Funding'], 'var_function-call-4014968237340428108': 'file_storage/function-call-4014968237340428108.json', 'var_function-call-4014968237340429633': 'file_storage/function-call-4014968237340429633.json'}

exec(code, env_args)
