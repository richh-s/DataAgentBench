code = """import json
import re

with open(locals()['var_function-call-13030964589425590204'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-16179877025922844511'], 'r') as f:
    civic_docs = json.load(f)

funding_map = {item['Project_Name']: item['Amount'] for item in funding_data}
project_names = list(funding_map.keys())
project_names.sort(key=len, reverse=True)

processed_projects = set()
total_funding = 0
matched_details = []

for doc in civic_docs:
    text = doc['text']
    occurrences = []
    for name in project_names:
        escaped_name = re.escape(name)
        for m in re.finditer(escaped_name, text, re.IGNORECASE):
            occurrences.append((m.start(), name))
    occurrences.sort(key=lambda x: x[0])
    
    clean_occurrences = []
    if occurrences:
        curr_start, curr_name = occurrences[0]
        curr_end = curr_start + len(curr_name)
        clean_occurrences.append((curr_start, curr_name))
        for i in range(1, len(occurrences)):
            start, name = occurrences[i]
            end = start + len(name)
            if start >= curr_end:
                clean_occurrences.append((start, name))
                curr_start, curr_name = start, name
                curr_end = end
                
    for i in range(len(clean_occurrences)):
        start_idx, name = clean_occurrences[i]
        end_idx = clean_occurrences[i+1][0] if i < len(clean_occurrences) - 1 else len(text)
        chunk = text[start_idx:end_idx]
        
        is_park = "park" in name.lower() or "park" in chunk.lower()
        if not is_park:
            continue
            
        completed_2022 = False
        lines = chunk.splitlines()
        for line in lines:
            l = line.lower()
            if "design" in l:
                continue
            if ("complete" in l or "completion" in l) and "2022" in l:
                completed_2022 = True
                break
        
        if completed_2022 and name not in processed_projects:
            processed_projects.add(name)
            amount = funding_map.get(name, 0)
            total_funding += amount
            matched_details.append({"name": name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total": total_funding, "projects": matched_details}))"""

env_args = {'var_function-call-13030964589425589265': 'file_storage/function-call-13030964589425589265.json', 'var_function-call-13030964589425590204': 'file_storage/function-call-13030964589425590204.json', 'var_function-call-16179877025922844511': 'file_storage/function-call-16179877025922844511.json'}

exec(code, env_args)
