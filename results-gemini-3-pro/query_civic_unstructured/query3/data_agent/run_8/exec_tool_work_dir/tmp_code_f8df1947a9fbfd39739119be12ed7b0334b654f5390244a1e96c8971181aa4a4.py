code = """import json
import pandas as pd

# Files
f_civic = locals()['var_function-call-2910026112661516748']
f_funding = locals()['var_function-call-10585127880706054254']

with open(f_civic, 'r') as f:
    civic = json.load(f)
with open(f_funding, 'r') as f:
    funding = json.load(f)

df_funding = pd.DataFrame(funding)
projects = []

for doc in civic:
    text = doc['text']
    # Use chr(10) for newline to avoid escaping issues
    lines = [x.strip() for x in text.split(chr(10)) if x.strip()]
    
    status = "unknown"
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if "Capital Improvement Projects (Design)" in line:
            status = "design"
            i += 1; continue
        if "Capital Improvement Projects (Construction)" in line:
            status = "construction"
            i += 1; continue
        if "Capital Improvement Projects (Not Started)" in line:
            status = "not started"
            i += 1; continue
            
        if "Updates:" in line or "Project Description:" in line:
            if i > 0:
                name = lines[i-1]
                if "Capital Improvement Projects" in name:
                    i += 1; continue
                
                p_text_lines = [name, line]
                j = i + 1
                while j < len(lines):
                    l2 = lines[j]
                    if "Capital Improvement Projects" in l2:
                        break
                    if "Updates:" in l2 or "Project Description:" in l2:
                        break
                    p_text_lines.append(l2)
                    j += 1
                
                if j < len(lines) and ("Updates:" in lines[j] or "Project Description:" in lines[j]):
                     if len(p_text_lines) > 1:
                         p_text_lines.pop()
                
                full_text = " ".join(p_text_lines)
                
                p_status = status
                if status == "construction" and "completed" in full_text.lower():
                    p_status = "completed"
                
                projects.append({"Project_Name": name, "Status": p_status, "Full_Text": full_text})
        i += 1

filtered = []
kws = ['emergency', 'fema']
for p in projects:
    if any(k in p['Full_Text'].lower() for k in kws):
        filtered.append(p)

df_p = pd.DataFrame(filtered)

if not df_p.empty:
    merged = pd.merge(df_funding, df_p, on='Project_Name', how='inner')
    res = merged[['Project_Name', 'Funding_Source', 'Amount', 'Status']].to_dict(orient='records')
else:
    res = []

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-9102831309616723132': ['civic_docs'], 'var_function-call-9102831309616723245': ['Funding'], 'var_function-call-12492854141756139028': 'file_storage/function-call-12492854141756139028.json', 'var_function-call-7907601960746092281': 'file_storage/function-call-7907601960746092281.json', 'var_function-call-10585127880706054254': 'file_storage/function-call-10585127880706054254.json', 'var_function-call-2910026112661516748': 'file_storage/function-call-2910026112661516748.json'}

exec(code, env_args)
