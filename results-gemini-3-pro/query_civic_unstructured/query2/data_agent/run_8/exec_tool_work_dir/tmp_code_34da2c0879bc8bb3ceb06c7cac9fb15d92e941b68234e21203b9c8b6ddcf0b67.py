code = """import json
import re

funding_path = locals()['var_function-call-13109238308160603251']
docs_path = locals()['var_function-call-13109238308160604256']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

newline = chr(10)
full_text = newline.join([d['text'] for d in civic_docs])
lines = full_text.split(newline)

projects_found = []
current_name = None
current_text = ""
block_started = False

for i, line in enumerate(lines):
    line = line.strip()
    if not line: continue
    
    if "(cid:190)" in line:
        # Check for new project
        k = i - 1
        title_candidate = None
        while k >= 0:
            prev = lines[k].strip()
            if prev:
                if "(cid:190)" in prev or "(cid:131)" in prev:
                    break
                if prev.lower().startswith("agenda"): break
                if prev.lower().startswith("page"): break
                if "capital improvement" in prev.lower(): break # Exclude headers
                title_candidate = prev
                break
            k -= 1
        
        if title_candidate:
            if current_name:
                projects_found.append({"name": current_name, "text": current_text})
            current_name = title_candidate
            current_text = line
            block_started = True
        else:
            if current_name:
                current_text += newline + line
    else:
        if "(cid:131)" in line:
            if current_name:
                current_text += newline + line
        else:
            if current_name:
                current_text += newline + line

if current_name:
    projects_found.append({"name": current_name, "text": current_text})

debug_list = []
park_keywords = ['park', 'playground', 'recreation', 'walkway', 'trail', 'beach']

total_funding = 0

for p in projects_found:
    name = p['name']
    text = p['text'].lower()
    tokens = re.split(r'\\W+', text)
    
    is_park = False
    if any(k in name.lower() for k in park_keywords):
        is_park = True
    elif "park" in tokens or "playground" in tokens:
        is_park = True
        
    is_completed_2022 = False
    if "2022" in text and re.search(r'(completed|complete construction).*?2022', text, re.DOTALL):
        is_completed_2022 = True
    
    funding_val = 0
    clean_name = name.strip()
    match_name = ""
    for f in funding_data:
         f_name = f['Project_Name']
         if f_name == clean_name or f_name.startswith(clean_name + " ("):
             funding_val += int(f['Amount'])
             match_name = f_name
    
    if is_park and is_completed_2022:
        total_funding += funding_val
        
    debug_list.append({
        "name": name,
        "is_park": is_park,
        "is_completed_2022": is_completed_2022,
        "funding": funding_val
    })

print("__RESULT__:")
print(json.dumps({"debug": debug_list, "total": total_funding}))"""

env_args = {'var_function-call-4994192944937523556': ['civic_docs'], 'var_function-call-4994192944937523005': ['Funding'], 'var_function-call-4994192944937522454': 'file_storage/function-call-4994192944937522454.json', 'var_function-call-4994192944937521903': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13109238308160603251': 'file_storage/function-call-13109238308160603251.json', 'var_function-call-13109238308160604256': 'file_storage/function-call-13109238308160604256.json', 'var_function-call-16246474712525603340': {'total_funding': 38000, 'projects': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000}]}}

exec(code, env_args)
