code = """import json
import re

# Load data
funding_path = locals()['var_function-call-61089627249181938']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

docs_path = locals()['var_function-call-61089627249180915']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_map = {item['Project_Name']: item['Amount'] for item in funding_data}
project_names = list(funding_map.keys())
project_names.sort(key=len, reverse=True)

relevant_projects = set()

for doc in civic_docs:
    text = doc['text']
    # Find all occurrences
    occurrences = []
    for name in project_names:
        pattern = re.compile(re.escape(name), re.IGNORECASE)
        for match in pattern.finditer(text):
            occurrences.append((match.start(), name))
    
    occurrences.sort(key=lambda x: x[0])
    
    for i in range(len(occurrences)):
        start_idx, name = occurrences[i]
        end_idx = occurrences[i+1][0] if i + 1 < len(occurrences) else len(text)
        segment = text[start_idx:end_idx].lower()
        
        # 1. Park check
        is_park = "park" in name.lower() or "park" in segment
        
        # 2. Completion check
        is_completed_2022 = False
        
        lines = segment.split('\n')
        for line in lines:
            if "2022" in line:
                if "design" in line and "complete" in line:
                    continue 
                
                if "construction" in line and ("complete" in line or "completed" in line):
                    is_completed_2022 = True
                    break
                
                if "completed" in line and "design" not in line:
                    is_completed_2022 = True
                    break
                    
                if "notice of completion" in line:
                    is_completed_2022 = True
                    break

        if is_park and is_completed_2022:
            relevant_projects.add(name)

total = 0
for name in relevant_projects:
    total += int(funding_map[name])

print("__RESULT__:")
print(json.dumps({"total": total, "projects": list(relevant_projects)}))"""

env_args = {'var_function-call-11325768186704868544': ['Funding'], 'var_function-call-11325768186704870109': ['civic_docs'], 'var_function-call-61089627249181938': 'file_storage/function-call-61089627249181938.json', 'var_function-call-61089627249180915': 'file_storage/function-call-61089627249180915.json'}

exec(code, env_args)
