code = """import json

with open(locals()['var_function-call-990771525359343970'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-990771525359343617'], 'r') as f:
    funding_data = json.load(f)

project_funding = {}
for item in funding_data:
    project_funding[item['Project_Name']] = int(item['Amount'])

project_names = list(project_funding.keys())
project_names.sort(key=len, reverse=True)

qualifying_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Simple segmentation by project name
    # We will iterate through the text and identify which project is being discussed
    # Since text is linear, we can find all occurrences of all project names
    
    hits = []
    for pname in project_names:
        idx = text.find(pname)
        while idx != -1:
            hits.append((idx, pname))
            idx = text.find(pname, idx + 1)
            
    hits.sort()
    
    # Iterate through hits to define segments
    for i in range(len(hits)):
        idx, pname = hits[i]
        
        # Determine end of this segment (start of next hit)
        if i + 1 < len(hits):
            end_idx = hits[i+1][0]
        else:
            end_idx = len(text)
            
        segment = text[idx:end_idx]
        segment_lower = segment.lower()
        
        # Check if park related
        if "park" not in pname.lower() and "park" not in segment_lower:
            continue
            
        # Check completion in 2022
        # Look for "construction ... completed ... 2022" patterns
        # or "complete construction ... 2022"
        
        lines = segment.split('\n')
        for line in lines:
            l = line.lower()
            if "2022" in l:
                if "construction" in l and ("completed" in l or "complete" in l):
                    # Check if it says "design" or "begin" to avoid false positives?
                    # "Begin Construction: Fall 2022" -> NO
                    # "Complete Design: Fall 2022" -> NO
                    # "Complete Construction: Fall 2022" -> YES
                    
                    if "begin construction" in l:
                        continue
                    if "complete design" in l:
                        continue
                    if "design" in l and "complete" in l: # ambiguous
                        pass 
                    
                    # Strong signal: "complete construction" or "construction was completed"
                    if "complete construction" in l or "construction was completed" in l:
                        qualifying_projects.add(pname)
                        
total_amount = 0
for p in qualifying_projects:
    total_amount += project_funding[p]

result = {"qualifying_projects": list(qualifying_projects), "total_funding": total_amount}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-990771525359343970': 'file_storage/function-call-990771525359343970.json', 'var_function-call-990771525359343617': 'file_storage/function-call-990771525359343617.json'}

exec(code, env_args)
