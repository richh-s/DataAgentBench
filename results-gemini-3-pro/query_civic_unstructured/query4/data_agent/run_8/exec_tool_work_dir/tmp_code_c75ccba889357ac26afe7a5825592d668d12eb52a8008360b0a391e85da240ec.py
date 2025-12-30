code = """import json
import re

with open(locals()['var_function-call-18089333164037500904'], 'r') as f:
    docs = json.load(f)
    
with open(locals()['var_function-call-7145739676015495870'], 'r') as f:
    funding_data = json.load(f)

known_projects = set(item['Project_Name'] for item in funding_data)
sorted_projects = sorted(list(known_projects), key=len, reverse=True)

matching_projects = set()
debug_matches = []

for doc in docs:
    text = doc['text']
    
    # Identify project blocks (same logic)
    project_indices = []
    for proj in sorted_projects:
        start = 0
        while True:
            idx = text.find(proj, start)
            if idx == -1:
                break
            project_indices.append((idx, proj))
            start = idx + len(proj)
            
    project_indices.sort()
    
    final_indices = []
    if project_indices:
        curr = project_indices[0]
        final_indices.append(curr)
        for next_proj in project_indices[1:]:
            prev_start, prev_name = final_indices[-1]
            prev_end = prev_start + len(prev_name)
            next_start, next_name = next_proj
            if next_start < prev_end:
                if len(next_name) > len(prev_name):
                     final_indices.pop()
                     final_indices.append(next_proj)
            else:
                final_indices.append(next_proj)
                
    for i in range(len(final_indices)):
        start_idx, proj_name = final_indices[i]
        if i + 1 < len(final_indices):
            end_idx = final_indices[i+1][0]
        else:
            end_idx = len(text)
            
        block = text[start_idx:end_idx]
        lines = block.splitlines()
        
        for line in lines:
            # Check context
            if "Begin Construction" in line or "Start Date" in line or "beginning in" in line or "Advertis" in line:
                lower_line = line.lower()
                # Check year 2022
                if "2022" in lower_line:
                    # Check month/season with boundaries
                    # \b(spring|march|april|may)\b
                    if re.search(r'\b(spring|march|april|may)\b', lower_line):
                        matching_projects.add(proj_name)
                        debug_matches.append((proj_name, line))
                        break # Found for this project

print("__RESULT__:")
print(json.dumps({"matches": list(matching_projects), "debug": debug_matches}))"""

env_args = {'var_function-call-6715434972998628537': 'file_storage/function-call-6715434972998628537.json', 'var_function-call-18089333164037500904': 'file_storage/function-call-18089333164037500904.json', 'var_function-call-5763327326687142161': ['PCH Signal Synchronization System Improvements Project', 'sending this project out to bid during the Spring of 2022.', 'scheduled for the April 11, 2022 Council meeting.', 'beginning in Spring 2022.', 'agreement will be sent to City Council in March.', '(cid:131) Next public community meeting is scheduled for March 25th.', 'timber with non-combustible materials.', 'that was damaged by the Woolsey Fire.', 'beginning in April 2022.', '(cid:131) The project consultant has started the design of this project.', 'is finalizing the bid documents.', 'assessment district will be created.', 'Fire.', 'advertised for construction bids shortly after this date.'], 'var_function-call-7145739676015495870': 'file_storage/function-call-7145739676015495870.json', 'var_function-call-3674796017122603571': ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'PCH Signal Synchronization System Improvements Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Civic Center Water Treatment Facility Phase 2', 'Bluffs Park Shade Structure']}

exec(code, env_args)
