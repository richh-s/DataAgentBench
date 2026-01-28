code = """import json
import pandas as pd

funding_path = locals()['var_function-call-13193485311528156786']
civic_docs_path = locals()['var_function-call-13193485311528154511']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_project = None
    current_project_text = []
    
    # Identify project starts
    # We store the index of lines that start with the marker
    markers = []
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith('(cid:190) Updates:') or line.startswith('(cid:190) Project Description:') or line.startswith('(cid:190) Project Updates:'):
            markers.append(i)
            
    # Now extract each block
    for k in range(len(markers)):
        marker_idx = markers[k]
        # Project Name is usually the line before, skipping empty lines
        name_idx = marker_idx - 1
        while name_idx >= 0 and not lines[name_idx].strip():
            name_idx -= 1
        
        if name_idx >= 0:
            project_name = lines[name_idx].strip()
            
            # Text block is from marker_idx to next marker_idx
            if k + 1 < len(markers):
                end_idx = markers[k+1]
                # Adjust to exclude the next project's name (which is before the marker)
                # We can't easily know where the name starts, but usually it's just a line or two.
                # Let's just take until the next marker line index - 5 (buffer) or just marker_idx of next.
                # Actually, the name is distinct.
                # Let's just take the block from marker_idx to markers[k+1]
                block_lines = lines[marker_idx:markers[k+1]]
            else:
                block_lines = lines[marker_idx:]
            
            block_text = " ".join(block_lines)
            
            # Find Start Date
            start_date = None
            if "Begin Construction:" in block_text:
                parts = block_text.split("Begin Construction:")
                if len(parts) > 1:
                    # Take the immediate text after
                    candidate = parts[1].strip()
                    # It might be followed by other text or (cid:131)
                    # Let's take first 20 chars
                    start_date = candidate[:20]
            elif "Construction Start:" in block_text:
                 parts = block_text.split("Construction Start:")
                 if len(parts) > 1:
                    start_date = parts[1].strip()[:20]
            
            extracted_projects.append({
                "Project_Name": project_name,
                "Start_Date": start_date,
                "Is_Disaster": any(x in project_name for x in ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster"])
            })

print("__RESULT__:")
print(pd.DataFrame(extracted_projects).to_json(orient="records"))"""

env_args = {'var_function-call-11217381671134747036': ['Funding'], 'var_function-call-11217381671134747201': ['civic_docs'], 'var_function-call-13193485311528156786': 'file_storage/function-call-13193485311528156786.json', 'var_function-call-13193485311528154511': 'file_storage/function-call-13193485311528154511.json'}

exec(code, env_args)
