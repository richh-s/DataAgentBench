code = """import json

# Access file paths
file_civic = locals()['var_function-call-15771920902434159033']
file_funding = locals()['var_function-call-13220906500236783647']

with open(file_civic, 'r') as f:
    civic_docs = json.load(f)
    
with open(file_funding, 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: item for item in funding_data}

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_status = "unknown"
    current_project = None
    content_buffer = []
    
    tagged_lines = []
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        if "Capital Improvement Projects" in line_stripped or "Disaster Recovery Projects" in line_stripped:
             tagged_lines.append(('header', line_stripped))
             continue
            
        # Relaxed marker check
        if "Updates:" in line_stripped or "Project Description:" in line_stripped or "(cid:190)" in line_stripped:
            tagged_lines.append(('marker', line_stripped))
            continue
            
        tagged_lines.append(('content', line_stripped))

    for tag, text in tagged_lines:
        if tag == 'header':
            if current_project:
                current_project['desc_lines'].extend(content_buffer)
                projects.append(current_project)
                current_project = None
                content_buffer = []

            if "(" in text and ")" in text:
                current_status = text.split("(")[1].split(")")[0].lower()
            else:
                current_status = "unknown"
                
        elif tag == 'marker':
            if content_buffer:
                title = content_buffer.pop() 
                if current_project:
                    current_project['desc_lines'].extend(content_buffer)
                    projects.append(current_project)
                
                current_project = {
                    "name": title,
                    "desc_lines": [text],
                    "status": current_status
                }
                content_buffer = []
            else:
                if current_project:
                    current_project['desc_lines'].append(text)
                    
        elif tag == 'content':
            if text.startswith("Page") or text.startswith("Agenda Item"):
                continue
            content_buffer.append(text)

    if current_project:
        current_project['desc_lines'].extend(content_buffer)
        projects.append(current_project)

final_results = []
seen = set()

for p in projects:
    name = p['name'] # use internal key 'name'
    desc = " ".join(p['desc_lines'])
    status = p['status']
    
    if "construction was completed" in desc.lower():
        status = "completed"
    
    text_blob = (name + " " + desc).lower()
    
    if "emergency" in text_blob or "fema" in text_blob:
        
        # Dedupe by Name + Status? Or just Name?
        # If we have same name with diff status, keep both?
        # Let's keep unique names for simplicity, but if status differs, maybe it's interesting.
        # But if I dedupe by name, I might lose the 'current' status if I process an old doc first.
        # I'll just skip exact name duplicates.
        if name in seen:
            continue
        seen.add(name)
        
        funding = funding_map.get(name)
        if not funding:
             candidates = [v for k,v in funding_map.items() if k.startswith(name)]
             if candidates:
                 funding = candidates[0]
        
        f_source = funding['Funding_Source'] if funding else "N/A"
        f_amount = funding['Amount'] if funding else "N/A"
        
        final_results.append({
            "Project_Name": name,
            "Funding_Source": f_source,
            "Amount": f_amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-4008715317058091339': 'file_storage/function-call-4008715317058091339.json', 'var_function-call-4008715317058091730': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-15771920902434159033': 'file_storage/function-call-15771920902434159033.json', 'var_function-call-13220906500236783647': 'file_storage/function-call-13220906500236783647.json', 'var_function-call-15319677722088380488': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'Status': 'completed'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000', 'Status': 'completed'}], 'var_function-call-1921292848469715955': [{'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'completed'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'completed'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'completed'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'completed'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'completed'}]}

exec(code, env_args)
