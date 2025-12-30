code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-7295023987179093116'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-10283202643711845823'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check start of Design section
        if "Capital Improvement Projects" in line and "Design" in line:
            in_design_section = True
            i += 1
            continue
            
        # Check start of other sections to exit
        if "Capital Improvement Projects" in line and "Design" not in line:
            in_design_section = False
        if "Disaster Recovery Projects" in line:
            in_design_section = False
            
        if in_design_section:
            # Simple heuristic: Project name is a line followed by "Updates:" or marker
            # Avoid empty lines
            if len(line) > 5 and "Page" not in line and "Agenda Item" not in line:
                # Look ahead
                is_candidate = False
                for k in range(1, 5):
                    if i + k < len(lines):
                        next_l = lines[i+k].strip()
                        if "Updates:" in next_l or "Project Description:" in next_l or "(cid:" in next_l:
                            is_candidate = True
                            break
                if is_candidate:
                    projects.append(line)
        
        i += 1

# Funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
funding_filtered = funding_df[funding_df['Amount'] > 50000]

# Join
extracted_df = pd.DataFrame({'Project_Name': projects})
# Drop duplicates in extraction
extracted_df = extracted_df.drop_duplicates()

merged = pd.merge(extracted_df, funding_filtered, on='Project_Name', how='inner')

print("__RESULT__:")
print(json.dumps(merged['Project_Name'].unique().tolist()))"""

env_args = {'var_function-call-7295023987179093116': 'file_storage/function-call-7295023987179093116.json', 'var_function-call-10283202643711845823': 'file_storage/function-call-10283202643711845823.json'}

exec(code, env_args)
