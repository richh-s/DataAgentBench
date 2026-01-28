code = """import json
import pandas as pd

# Load funding data
funding_data = pd.read_json(locals()['var_function-call-8349484065091426871'])
project_names = set(funding_data['Project_Name'].str.strip().tolist())

# Load doc text
with open(locals()['var_function-call-3235961165398988678'], 'r') as f:
    docs = json.load(f)

extracted_projects = []

for doc in docs:
    text = doc['text']
    lines = text.split('\\n')
    
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        if line_clean in project_names:
            current_project = line_clean
        
        if current_project:
            lower_line = line_clean.lower()
            if "begin construction" in lower_line:
                parts = line_clean.split(':')
                if len(parts) > 1:
                    date_str = parts[-1].strip()
                    extracted_projects.append({
                        "Project_Name": current_project,
                        "st": date_str
                    })
                    current_project = None

df_extracted = pd.DataFrame(extracted_projects)
print("__RESULT__:")
print(df_extracted.to_json(orient='records'))"""

env_args = {'var_function-call-3235961165398988678': 'file_storage/function-call-3235961165398988678.json', 'var_function-call-8349484065091426871': 'file_storage/function-call-8349484065091426871.json'}

exec(code, env_args)
