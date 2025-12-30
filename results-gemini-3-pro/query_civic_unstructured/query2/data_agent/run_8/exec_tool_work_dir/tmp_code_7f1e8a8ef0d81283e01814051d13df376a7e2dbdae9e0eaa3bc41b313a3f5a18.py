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
        k = i - 1
        title_candidate = None
        while k >= 0:
            prev = lines[k].strip()
            if prev:
                if "(cid:190)" in prev or "(cid:131)" in prev:
                    break
                if prev.lower().startswith("agenda"): break
                if prev.lower().startswith("page"): break
                if "capital improvement" in prev.lower(): break
                if len(prev.split()) > 15: break # Skip long lines (junk)
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

# Filtering
park_keywords = ['park', 'playground', 'recreation', 'walkway', 'trail', 'skate', 'bench', 'arbor']
negative_keywords = ['road', 'street', 'highway', 'avenue', 'drive', 'drainage', 'storm drain', 'resurfacing', 'water quality', 'sewer', 'traffic', 'signal']

total_funding = 0
final_projects = []

for p in projects_found:
    name = p['name'].strip()
    text = p['text'].lower()
    name_lower = name.lower()
    
    # Park Check
    is_park = False
    has_pos = any(k in name_lower for k in park_keywords)
    has_neg = any(k in name_lower for k in negative_keywords)
    
    if has_pos and not has_neg:
        is_park = True
    
    # Edge case: "Park" in name but also "Road"? e.g. "Malibu Park Road".
    # Logic above excludes it.
    
    # Completion Check
    is_completed_2022 = False
    if "2022" in text and re.search(r'(completed|complete construction|construction complete).*?2022', text, re.DOTALL):
        is_completed_2022 = True
        
    if is_park and is_completed_2022:
        # Sum funding
        project_funding = 0
        match_found = False
        for f in funding_data:
            f_name = f['Project_Name']
            # Match: exact or startswith(name + " (")
            if f_name == name or f_name.startswith(name + " ("):
                project_funding += int(f['Amount'])
                match_found = True
        
        if match_found:
            # Check if already added?
            # projects_found might have duplicates if multiple reports mention it.
            # But the extracted blocks are unique by position.
            # If the same project appears in multiple blocks (multiple documents), we might double count!
            # We should track matched names.
            if name not in [fp['name'] for fp in final_projects]:
                 final_projects.append({"name": name, "amount": project_funding})
                 total_funding += project_funding

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": final_projects}))"""

env_args = {'var_function-call-4994192944937523556': ['civic_docs'], 'var_function-call-4994192944937523005': ['Funding'], 'var_function-call-4994192944937522454': 'file_storage/function-call-4994192944937522454.json', 'var_function-call-4994192944937521903': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13109238308160603251': 'file_storage/function-call-13109238308160603251.json', 'var_function-call-13109238308160604256': 'file_storage/function-call-13109238308160604256.json', 'var_function-call-16246474712525603340': {'total_funding': 38000, 'projects': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000}]}, 'var_function-call-9336587759981175788': 'file_storage/function-call-9336587759981175788.json'}

exec(code, env_args)
