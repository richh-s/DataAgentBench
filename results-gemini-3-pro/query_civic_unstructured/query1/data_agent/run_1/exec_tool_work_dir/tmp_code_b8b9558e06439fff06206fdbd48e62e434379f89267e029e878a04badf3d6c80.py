code = """import json

with open(locals()['var_function-call-4958646437851811265'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = []
for record in funding_data:
    try:
        if int(record['Amount']) > 50000:
            high_funding_projects.append(record['Project_Name'].strip())
    except ValueError:
        continue

with open(locals()['var_function-call-11007850212329188700'], 'r') as f:
    civic_docs = json.load(f)

def clean_token(t):
    if t.endswith('s') and len(t) > 1:
        return t[:-1]
    return t

def get_tokens(text):
    # Remove parens and other chars
    clean = text.lower().replace('&', '').replace(',', '').replace('.', '').replace('(', '').replace(')', '')
    raw = clean.split()
    return set(clean_token(t) for t in raw)

doc_project_names = set()

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
        # Any header starting with Capital or Disaster ends the section
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
            
        # Heuristics for project name
        if not line[0].isupper():
            continue
        if line.endswith('.'):
            continue
            
        # Check next line
        j = i + 1
        found_marker = False
        while j < len(section_lines):
            next_l = section_lines[j].strip()
            if next_l:
                if next_l.startswith('(cid:190) Updates') or next_l.startswith('(cid:190) Project Description'):
                     found_marker = True
                break
            j += 1
            
        if found_marker:
            doc_project_names.add(line)

final_matches = set()
for d_name in doc_project_names:
    d_tokens = get_tokens(d_name)
    best_match = None
    
    if d_name in high_funding_projects:
        final_matches.add(d_name)
        continue
        
    for f_name in high_funding_projects:
        f_tokens = get_tokens(f_name)
        common = d_tokens.intersection(f_tokens)
        if not f_tokens: continue
        score = len(common) / len(f_tokens)
        score2 = len(common) / len(d_tokens)
        
        if score >= 0.8 or score2 >= 0.8:
            final_matches.add(d_name)
            break

print("__RESULT__:")
print(json.dumps({"count": len(final_matches), "matched": list(final_matches)}))"""

env_args = {'var_function-call-4958646437851811265': 'file_storage/function-call-4958646437851811265.json', 'var_function-call-11007850212329188700': 'file_storage/function-call-11007850212329188700.json', 'var_function-call-17427938851555691024': {'count': 10, 'matched': ['Malibu Canyon Road Traffic Study', 'PCH at Trancas Canyon Road Right Turn Lane', 'Civic Center Stormwater Diversion Structure', 'Outdoor Warning Signs', 'Permanent Skate Park', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Storm Drain Master Plan', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway Repairs'], 'extracted_sample': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'or phasing out the project', 'Westward Beach Road Repair Project']}, 'var_function-call-7722921194275743764': {'count': 10, 'matched': ['Civic Center Stormwater Diversion Structure', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'Permanent Skate Park', 'Storm Drain Master Plan', 'Westward Beach Road Drainage Improvements Project', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'PCH Median Improvements Project', 'PCH at Trancas Canyon Road Right Turn Lane'], 'extracted_sample': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH Median Improvements Project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'Clover Heights Storm Drainage Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground', 'Malibu Canyon Road Traffic Study', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Bluffs Park Shade Structure', 'shade structures at Malibu Bluffs Park.', 'Permanent Skate Park', 'amenities such as trash cans, benches, tables, and restrooms.', 'PCH at Trancas Canyon Road Right Turn Lane', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Civic Center Stormwater Diversion Structure', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Malibu Park Drainage Improvements', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Civic Center Stormwater Diversion Structure', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Malibu Park Drainage Improvements', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Bluffs Park Shade Structure', 'shade structures at Malibu Bluffs Park.', 'Permanent Skate Park', 'amenities such as trash cans, benches, tables, and restrooms.', 'PCH at Trancas Canyon Road Right Turn Lane', 'turn lane at the intersection of PCH and Trancas Canyon Road.']}, 'var_function-call-14388753569429659092': {'count': 13, 'matched': ['Westward Beach Road Repair Project', 'Malibu Bluffs Park South Walkway Repairs', 'Permanent Skate Park', 'Storm Drain Master Plan', 'PCH at Trancas Canyon Road Right Turn Lane', 'Westward Beach Road Drainage Improvements Project', 'Trancas Canyon Park Playground', 'Civic Center Stormwater Diversion Structure', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'Westward Beach Road Improvements Project', 'PCH Median Improvements Project', 'Outdoor Warning Signs']}, 'var_function-call-14709806059033962677': {'count': 17, 'matched': ['PCH Median Improvements Project', 'Westward Beach Road Improvements Project', 'Trancas Canyon Park Playground', 'Outdoor Warning Signs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Permanent Skate Park', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'PCH Signal Synchronization System Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Clover Heights Storm Drainage Improvements', 'Storm Drain Master Plan', 'Malibu Bluffs Park South Walkway Repairs', 'Civic Center Stormwater Diversion Structure', 'Westward Beach Road Drainage Improvements Project', 'Westward Beach Road Repair Project', 'Malibu Canyon Road Traffic Study', 'Trancas Canyon Park Upper and Lower Slopes Repair']}, 'var_function-call-9298957449057996268': ['27: Capital Improvement Projects and Disaster Recovery Projects Status', '31: upcoming Capital Improvement Projects and Disaster Recovery Projects.', '36: Capital Improvement Projects (Design)', '276: Capital Improvement Projects (Construction)', '351: Capital Improvement Projects (Not Started)', '27: Capital Improvement Projects and Disaster Recovery Projects Status', '31: upcoming Capital Improvements Projects and Disaster Recovery Projects.', '36: Capital Improvement Projects (Design)', '218: Capital Improvement Projects (Construction)', '234: Capital Improvement Projects (Not Started)', '272: Capital Improvement Projects (Completed)', '25: Capital Improvement Projects and Disaster Recovery Projects Status', '29: upcoming Capital Improvements Projects and Disaster Recovery Projects.', '34: Capital Improvement Projects (Design)', '171: Capital Improvement Projects (Construction)', '212: Capital Improvement Projects (Completed)', '239: Capital Improvement Projects (Not Started)', '23: Capital Improvement Projects and Disaster Recovery Projects Status', '27: upcoming Capital Improvements Projects and Disaster Recovery Projects.', '32: Capital Improvement Projects (Design)', '178: Capital Improvement Projects (Construction)', '230: Capital Improvement Projects (Not Started)', '27: Capital Improvement Projects and Disaster Recovery Projects Status', '31: upcoming Capital Improvements Projects and Disaster Recovery Projects.', '36: Capital Improvement Projects (Design)', '243: Capital Improvement Projects (Construction)', '247: Capital Improvement Projects (Not Started)', '299: Capital Improvement Projects (Completed)']}

exec(code, env_args)
