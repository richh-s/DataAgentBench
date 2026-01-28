code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-13609634735217417921'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-13507259868243532000'], 'r') as f:
    civic_docs = json.load(f)

# Create base names
def get_base_name(name):
    # Remove (Suffix) at the end
    return re.sub(r'\s*\(.*?\)$', '', name)

funding_df['base_name'] = funding_df['Project_Name'].apply(get_base_name)

# Map base_name to list of project names
base_to_names = funding_df.groupby('base_name')['Project_Name'].apply(list).to_dict()

# Search keys: unique base names
search_names = list(base_to_names.keys())
search_names.sort(key=len, reverse=True)

found_base_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    occurrences = []
    for proj in search_names:
        start = 0
        while True:
            idx = text.find(proj, start)
            if idx == -1:
                break
            occurrences.append((idx, proj))
            start = idx + len(proj)
            
    occurrences.sort(key=lambda x: x[0])
    
    for i in range(len(occurrences)):
        pos, proj_name = occurrences[i]
        
        if i < len(occurrences) - 1:
            end_pos = occurrences[i+1][0]
        else:
            end_pos = len(text)
            
        segment = text[pos:end_pos]
        
        match = re.search(r"(?:Begin|Start) [Cc]onstruction:?\s*([A-Za-z0-9, \-]+)", segment)
        
        if match:
            date_str = match.group(1).strip()
            d = date_str.lower()
            if "2022" in d:
                if "spring" in d:
                    found_base_names.add(proj_name)
                elif "march" in d or "april" in d or "may" in d:
                    found_base_names.add(proj_name)

# Calculate results
# Filter funding for all variants of found base names
all_found_project_names = []
for bn in found_base_names:
    all_found_project_names.extend(base_to_names[bn])

result_df = funding_df[funding_df['Project_Name'].isin(all_found_project_names)]

total_funding = int(pd.to_numeric(result_df['Amount']).sum())
count = len(found_base_names)

print("__RESULT__:")
print(json.dumps({
    "count": count, 
    "total_funding": total_funding, 
    "base_projects": list(found_base_names),
    "all_funding_records": list(result_df['Project_Name'].unique())
}))"""

env_args = {'var_function-call-17342646837596843535': 'file_storage/function-call-17342646837596843535.json', 'var_function-call-13609634735217417921': 'file_storage/function-call-13609634735217417921.json', 'var_function-call-13507259868243532000': 'file_storage/function-call-13507259868243532000.json', 'var_function-call-3851609115190188045': {'count': 9, 'total_funding': 459000, 'projects': ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Marie Canyon Green Streets', 'Bluffs Park Shade Structure', 'Trancas Canyon Park Slope Stabilization Project', 'Latigo Canyon Road Culvert Repairs', 'Civic Center Water Treatment Facility Phase 2', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Encinal Canyon Road Drainage Improvements', 'Trancas Canyon Park Planting and Irrigation Repairs']}}

exec(code, env_args)
