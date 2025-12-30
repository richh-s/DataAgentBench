code = """import json
import re
import pandas as pd

funding_path = locals()['var_function-call-13193485311528156786']
civic_docs_path = locals()['var_function-call-13193485311528154511']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    # Regex to find project blocks
    # Looking for a line (Project Name) followed by a line starting with (cid:190) Updates or Project Description
    # We use distinct patterns
    pattern = re.compile(r"([^\n]+)\n+\s*\(cid:190\) (?:Updates|Project Description|Project Updates):", re.MULTILINE)
    
    matches = list(pattern.finditer(text))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_index = match.start()
        
        # Determine end index (next match or end of string)
        if i + 1 < len(matches):
            end_index = matches[i+1].start()
        else:
            end_index = len(text)
            
        block_text = text[start_index:end_index]
        
        # Extract dates
        # Pattern for Begin Construction
        # Based on preview: "(cid:131) Begin Construction: Fall 2023"
        start_date = None
        date_match = re.search(r"Begin Construction[:\s]+([^\n\r]+)", block_text, re.IGNORECASE)
        if date_match:
            start_date = date_match.group(1).strip()
        
        # Add to list
        extracted_projects.append({
            "Project_Name": project_name,
            "Start_Date": start_date,
            "Raw_Text": block_text[:200] # Preview for debugging
        })

df = pd.DataFrame(extracted_projects)
print("__RESULT__:")
print(df.to_json(orient="records"))"""

env_args = {'var_function-call-11217381671134747036': ['Funding'], 'var_function-call-11217381671134747201': ['civic_docs'], 'var_function-call-13193485311528156786': 'file_storage/function-call-13193485311528156786.json', 'var_function-call-13193485311528154511': 'file_storage/function-call-13193485311528154511.json'}

exec(code, env_args)
