code = """import json
import re

funding_path = locals()['var_function-call-13109238308160603251']
docs_path = locals()['var_function-call-13109238308160604256']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Use chr(10) for newline to avoid escaping issues
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
        if not block_started:
            k = i - 1
            title_candidate = None
            while k >= 0:
                prev = lines[k].strip()
                if prev:
                    if "(cid:190)" in prev or "(cid:131)" in prev:
                        break
                    if prev.lower().startswith("agenda"): break
                    if prev.lower().startswith("page"): break
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

total_funding = 0
matched_projects = []

for p in projects_found:
    name = p['name']
    text = p['text'].lower()
    
    # Tokenize text
    # Escape \W+ as \\W+
    tokens = re.split(r'\\W+', text)
    
    park_keywords = ['park', 'playground', 'recreation', 'walkway', 'trail', 'beach']
    is_park = False
    
    # Check name
    if any(k in name.lower() for k in park_keywords):
        is_park = True
    else:
        # Check text tokens
        if "park" in tokens or "playground" in tokens:
            is_park = True
            
    # Check completion
    # Simple check: "2022" and "completed" in text
    if "2022" in tokens and "completed" in tokens:
        # Verify proximity or phrase?
        # The simple check might be enough given the doc structure.
        # But let's check for "Construction was completed" phrase.
        if "construction was completed" in text or "complete construction" in text or "completed" in text:
             # Just checking presence might trigger on "not completed".
             # But usually "completed" is used in positive sense in these reports (e.g. "Notice of completion").
             # Check if "2022" is in the text.
             # Refined check:
             if re.search(r'(completed|complete construction).*?2022', text, re.DOTALL):
                 if is_park:
                     # Match funding
                     clean_name = name.strip()
                     current_funding = 0
                     found_match = False
                     
                     for f in funding_data:
                         f_name = f['Project_Name']
                         if f_name == clean_name or f_name.startswith(clean_name + " ("):
                             current_funding += int(f['Amount'])
                             found_match = True
                     
                     if found_match:
                         matched_projects.append({"name": clean_name, "amount": current_funding})
                         total_funding += current_funding

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-4994192944937523556': ['civic_docs'], 'var_function-call-4994192944937523005': ['Funding'], 'var_function-call-4994192944937522454': 'file_storage/function-call-4994192944937522454.json', 'var_function-call-4994192944937521903': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13109238308160603251': 'file_storage/function-call-13109238308160603251.json', 'var_function-call-13109238308160604256': 'file_storage/function-call-13109238308160604256.json'}

exec(code, env_args)
