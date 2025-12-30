code = """import json
import re

# Load data
with open(locals()['var_function-call-13069126616893175602'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-2392722741691488193'], 'r') as f:
    civic_docs = json.load(f)

# Extract unique project names
project_names = set()
for record in funding_data:
    project_names.add(record['Project_Name'])

sorted_p_names = sorted(list(project_names), key=len, reverse=True)

target_months = ['march', 'april', 'may']
target_season = 'spring'
target_year = '2022'

matches_info = []

for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    
    found_projects = []
    for p_name in sorted_p_names:
        escaped_name = re.escape(p_name)
        for match in re.finditer(escaped_name, text, re.IGNORECASE):
            found_projects.append((match.start(), p_name))
            
    found_projects.sort(key=lambda x: x[0])
    
    for i in range(len(found_projects)):
        start_idx, p_name = found_projects[i]
        if i < len(found_projects) - 1:
            end_idx = found_projects[i+1][0]
        else:
            end_idx = len(text)
        
        segment = text[start_idx:min(end_idx, start_idx + 2000)]
        
        date_patterns = [
            r"(Begin [Cc]onstruction:?\s*)([A-Za-z0-9\s,]+)",
            r"(Construction [Ss]tart:?\s*)([A-Za-z0-9\s,]+)",
            r"([Ss]tart [Dd]ate:?\s*)([A-Za-z0-9\s,]+)",
            r"(Construction to begin:?\s*)([A-Za-z0-9\s,]+)"
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, segment)
            if match:
                prefix = match.group(1)
                date_str = match.group(2).lower()
                
                if target_year in date_str:
                    if target_season in date_str or any(m in date_str for m in target_months):
                        matches_info.append({
                            "project": p_name,
                            "filename": filename,
                            "date_found": date_str,
                            "context": segment[:200].replace('\n', ' ')
                        })

print("__RESULT__:")
print(json.dumps(matches_info))"""

env_args = {'var_function-call-11013100090032240627': ['Funding'], 'var_function-call-11013100090032239808': ['civic_docs'], 'var_function-call-13069126616893175602': 'file_storage/function-call-13069126616893175602.json', 'var_function-call-13069126616893177209': 'file_storage/function-call-13069126616893177209.json', 'var_function-call-2392722741691488193': 'file_storage/function-call-2392722741691488193.json', 'var_function-call-14951084394473417957': {'count': 9, 'total_funding': 459000, 'projects': ['Bluffs Park Shade Structure', 'Marie Canyon Green Streets', 'Trancas Canyon Park Slope Stabilization Project', 'Latigo Canyon Road Culvert Repairs', 'Civic Center Water Treatment Facility Phase 2', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Encinal Canyon Road Drainage Improvements', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Latigo Canyon Road Roadway/Retaining Wall Improvements']}}

exec(code, env_args)
