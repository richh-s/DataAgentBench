code = """import json
import pandas as pd

funding_path = locals()['var_function-call-13193485311528156786']
civic_docs_path = locals()['var_function-call-13193485311528154511']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Re-run extraction for debugging
extracted_debug = []
for doc in civic_docs:
    lines = doc['text'].split(chr(10))
    markers = []
    for i, line in enumerate(lines):
        line = line.strip()
        if ("Updates:" in line or "Project Description:" in line) and "(cid:" in line:
            markers.append(i)
            
    for k in range(len(markers)):
        marker_idx = markers[k]
        name_idx = marker_idx - 1
        while name_idx >= 0 and not lines[name_idx].strip():
            name_idx -= 1
        if name_idx >= 0:
            project_name = lines[name_idx].strip()
            if k + 1 < len(markers):
                end_idx = markers[k+1]
            else:
                end_idx = len(lines)
            block_lines = lines[marker_idx:end_idx]
            block_text = " ".join(block_lines)
            start_date = None
            keywords = ["Begin Construction:", "Construction Start:", "Begin construction:"]
            for kw in keywords:
                if kw in block_text:
                    parts = block_text.split(kw)
                    if len(parts) > 1:
                        remainder = parts[1].strip()
                        if "  " in remainder:
                            candidate = remainder.split("  ")[0]
                        else:
                            candidate = remainder[:30]
                        start_date = candidate.strip()
                        break
            
            if start_date and "2022" in start_date:
                extracted_debug.append({"Project": project_name, "Date": start_date})

# Filter for the ones we matched
matched_names = ["Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)", 
                 "Clover Heights Storm Drain (FEMA Project)", 
                 "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)", 
                 "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)", 
                 "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)", 
                 "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)", 
                 "Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)", 
                 "Westward Beach Road Shoulder Repairs (CalOES Project)"]

print("__RESULT__:")
print(json.dumps([x for x in extracted_debug if x['Project'] in matched_names]))"""

env_args = {'var_function-call-11217381671134747036': ['Funding'], 'var_function-call-11217381671134747201': ['civic_docs'], 'var_function-call-13193485311528156786': 'file_storage/function-call-13193485311528156786.json', 'var_function-call-13193485311528154511': 'file_storage/function-call-13193485311528154511.json', 'var_function-call-16349189720385277872': 'file_storage/function-call-16349189720385277872.json', 'var_function-call-8983212948348442456': {'total_funding': 495000.0, 'matched_projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)'], 'debug_targets': ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'damaged by the Woolsey Fire.']}}

exec(code, env_args)
