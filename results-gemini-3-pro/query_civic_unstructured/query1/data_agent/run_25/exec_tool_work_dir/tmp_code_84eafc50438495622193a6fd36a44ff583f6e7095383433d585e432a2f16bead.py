code = """import json
import pandas as pd

f_path = locals()['var_function-call-7295023987179093116']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

d_path = locals()['var_function-call-10283202643711845823']
with open(d_path, 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # using double backslash for newline escape
    lines = text.split('\n')
    
    in_design = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if "Capital Improvement Projects" in line and "Design" in line:
            in_design = True
            i += 1
            continue
            
        if "Capital Improvement Projects" in line and "Design" not in line:
            in_design = False
        if "Disaster Recovery Projects" in line:
            in_design = False
            
        if in_design:
            if len(line) > 5 and "Page " not in line and "Agenda Item" not in line:
                is_cand = False
                for k in range(1, 5):
                    if i + k < len(lines):
                        nxt = lines[i+k].strip()
                        if "Updates:" in nxt or "Project Description:" in nxt or "(cid:" in nxt:
                            is_cand = True
                            break
                if is_cand:
                    projects.append(line)
        i += 1

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
funding_filtered = funding_df[funding_df['Amount'] > 50000]

extracted_df = pd.DataFrame({'Project_Name': projects})
extracted_df = extracted_df.drop_duplicates()

merged = pd.merge(extracted_df, funding_filtered, on='Project_Name', how='inner')

print("__RESULT__:")
print(json.dumps(merged['Project_Name'].unique().tolist()))"""

env_args = {'var_function-call-7295023987179093116': 'file_storage/function-call-7295023987179093116.json', 'var_function-call-10283202643711845823': 'file_storage/function-call-10283202643711845823.json'}

exec(code, env_args)
