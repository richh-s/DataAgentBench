code = """import json

try:
    with open(locals()['var_function-call-2491706478099471168'], 'r') as f:
        civic_docs = json.load(f)
except:
    civic_docs = []

try:
    with open(locals()['var_function-call-148111800493069151'], 'r') as f:
        funding_data = json.load(f)
except:
    funding_data = []

projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = [l.strip() for l in text.splitlines()]
    
    current_status = "Unknown"
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if "Capital Improvement Projects (Design)" in line:
            current_status = "Design"
        elif "Capital Improvement Projects (Construction)" in line:
            current_status = "Construction"
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status = "Not Started"
        
        is_project = False
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if "Updates:" in next_line:
                is_project = True
        
        if is_project and line:
            p_name = line
            p_text = ""
            j = i + 1
            while j < len(lines):
                l2 = lines[j]
                if "Capital Improvement Projects (" in l2:
                    break
                if j + 1 < len(lines):
                    l3 = lines[j+1]
                    if "Updates:" in l3 and l2 != "":
                        break
                p_text += l2 + " "
                j += 1
            
            p_status = current_status
            if "Construction was completed" in p_text:
                p_status = "Completed"
            elif "construction was completed" in p_text.lower():
                p_status = "Completed"
            
            projects.append({
                "name": p_name,
                "status": p_status,
                "text": p_text
            })
            i = j
        else:
            i += 1

final_results = []
keywords = ['emergency', 'fema', 'disaster', 'fire', 'warning']

for p in projects:
    p_name_clean = p['name'].strip()
    p_text_lower = p['text'].lower()
    p_name_lower = p_name_clean.lower()
    
    is_related = False
    if any(k in p_name_lower for k in keywords):
        is_related = True
    if any(k in p_text_lower for k in keywords):
        is_related = True
        
    matches = []
    for f in funding_data:
        f_name = f['Project_Name']
        f_name_lower = f_name.lower()
        
        match = False
        if p_name_lower == f_name_lower:
            match = True
        elif p_name_lower in f_name_lower and len(p_name_lower) > 10:
            match = True
        elif f_name_lower in p_name_lower and len(f_name_lower) > 10:
            match = True
            
        if match:
            if any(k in f_name_lower for k in keywords):
                is_related = True
            matches.append(f)
    
    if is_related and matches:
        for m in matches:
            status_out = p['status']
            # Normalize statuses to hint if possible
            if status_out == "Construction":
                 pass # keep as construction or map to something else if needed
            if status_out.lower() == "design":
                status_out = "design"
            if status_out.lower() == "completed":
                status_out = "completed"
            if status_out.lower() == "not started":
                status_out = "not started"

            final_results.append({
                "Project_Name": m['Project_Name'],
                "Funding_Source": m['Funding_Source'],
                "Amount": m['Amount'],
                "Status": status_out
            })

unique_results = []
seen = set()
for r in final_results:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'], r['Status'])
    if key not in seen:
        seen.add(key)
        unique_results.append(r)

print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_function-call-247840188859049492': ['civic_docs'], 'var_function-call-247840188859048797': ['Funding'], 'var_function-call-5543153819745217051': 'file_storage/function-call-5543153819745217051.json', 'var_function-call-5543153819745218422': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-2491706478099471168': 'file_storage/function-call-2491706478099471168.json', 'var_function-call-148111800493069151': 'file_storage/function-call-148111800493069151.json'}

exec(code, env_args)
