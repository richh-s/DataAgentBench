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
    lines = doc['text'].split(chr(10)) # Split by newline
    
    markers = []
    for i, line in enumerate(lines):
        line = line.strip()
        # Check for the specific update marker using substring
        if "Updates:" in line and "(cid:" in line:
            markers.append(i)
        elif "Project Description:" in line and "(cid:" in line:
            markers.append(i)
            
    for k in range(len(markers)):
        marker_idx = markers[k]
        name_idx = marker_idx - 1
        while name_idx >= 0 and not lines[name_idx].strip():
            name_idx -= 1
        
        if name_idx >= 0:
            project_name = lines[name_idx].strip()
            
            # Determine end of block
            if k + 1 < len(markers):
                end_idx = markers[k+1]
                # Try to avoid including the next project name
                # Look backwards from next marker to find the blank line separating projects
                tmp_idx = end_idx - 1
                while tmp_idx > marker_idx and lines[tmp_idx].strip():
                    tmp_idx -= 1
                if tmp_idx > marker_idx:
                    end_idx = tmp_idx
            else:
                end_idx = len(lines)
            
            block_lines = lines[marker_idx:end_idx]
            block_text = " ".join(block_lines)
            
            start_date = None
            # Check keywords for start
            keywords = ["Begin Construction:", "Construction Start:", "Begin construction:", "Construction start:"]
            for kw in keywords:
                if kw in block_text:
                    parts = block_text.split(kw)
                    if len(parts) > 1:
                        # Grab chunk after
                        val = parts[1].strip()
                        # Clean it up. It usually ends with a newline or another bullet point
                        # In the "join"ed text, newlines are spaces.
                        # Look for "(cid:" to stop
                        if "(cid:" in val:
                            val = val.split("(cid:")[0]
                        start_date = val.strip()
                        break
            
            # Check if disaster
            # Hints: "Capital" vs "Disaster".
            # Look for FEMA, CalOES, CalJPIA in name.
            is_disaster = False
            disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Disaster", "Woolsey"]
            for dkw in disaster_keywords:
                if dkw in project_name:
                    is_disaster = True
                    break
            
            extracted_projects.append({
                "Project_Name": project_name,
                "Start_Date": start_date,
                "Is_Disaster": is_disaster
            })

print("__RESULT__:")
print(pd.DataFrame(extracted_projects).to_json(orient="records"))"""

env_args = {'var_function-call-11217381671134747036': ['Funding'], 'var_function-call-11217381671134747201': ['civic_docs'], 'var_function-call-13193485311528156786': 'file_storage/function-call-13193485311528156786.json', 'var_function-call-13193485311528154511': 'file_storage/function-call-13193485311528154511.json'}

exec(code, env_args)
