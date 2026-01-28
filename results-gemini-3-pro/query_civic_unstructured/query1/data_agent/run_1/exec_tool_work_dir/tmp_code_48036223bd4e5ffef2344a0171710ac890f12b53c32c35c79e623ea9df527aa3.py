code = """import json

# Load funding data
with open(locals()['var_function-call-4958646437851811265'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
for record in funding_data:
    try:
        if int(record['Amount']) > 50000:
            high_funding_projects.add(record['Project_Name'].strip())
    except ValueError:
        continue

# Load civic docs
with open(locals()['var_function-call-11007850212329188700'], 'r') as f:
    civic_docs = json.load(f)

matched_projects = set()
all_extracted_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split(chr(10))
    
    start_index = -1
    for i, line in enumerate(lines):
        if "Capital Improvement Projects (Design)" in line:
            start_index = i
            break
            
    if start_index == -1:
        continue
        
    end_index = len(lines)
    for i in range(start_index + 1, len(lines)):
        line = lines[i].strip()
        if "Capital Improvement Projects" in line and "(Design)" not in line:
            end_index = i
            break
        if "Disaster Recovery Projects" in line:
            end_index = i
            break
            
    section_lines = lines[start_index+1:end_index]
    
    for i in range(len(section_lines)):
        line = section_lines[i].strip()
        if not line:
            continue
            
        is_project = False
        j = i + 1
        while j < len(section_lines):
            next_l = section_lines[j].strip()
            if next_l:
                # Check for Updates or Project Description
                if next_l.startswith('(cid:190) Updates') or next_l.startswith('(cid:190) Project Description'):
                    is_project = True
                break
            j += 1
            
        if is_project:
            proj_name = line
            all_extracted_names.append(proj_name)
            # Fuzzy match or exact match?
            # Funding names might not match exactly if there are typos in doc
            # But earlier results showed exact matches working well
            if proj_name in high_funding_projects:
                matched_projects.add(proj_name)
            else:
                # Try simple cleaning or checking substring
                pass

print("__RESULT__:")
print(json.dumps({"count": len(matched_projects), "matched": list(matched_projects), "extracted_sample": all_extracted_names}))"""

env_args = {'var_function-call-4958646437851811265': 'file_storage/function-call-4958646437851811265.json', 'var_function-call-11007850212329188700': 'file_storage/function-call-11007850212329188700.json', 'var_function-call-17427938851555691024': {'count': 10, 'matched': ['Malibu Canyon Road Traffic Study', 'PCH at Trancas Canyon Road Right Turn Lane', 'Civic Center Stormwater Diversion Structure', 'Outdoor Warning Signs', 'Permanent Skate Park', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Storm Drain Master Plan', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway Repairs'], 'extracted_sample': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'or phasing out the project', 'Westward Beach Road Repair Project']}}

exec(code, env_args)
