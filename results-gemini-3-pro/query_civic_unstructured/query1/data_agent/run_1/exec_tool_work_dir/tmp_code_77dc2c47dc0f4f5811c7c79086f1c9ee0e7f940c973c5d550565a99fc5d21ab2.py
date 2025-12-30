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

matched_projects = set()
# Keep track of which funding project matched to avoid double counting?
# No, we want count of projects in "Design" status.
# If multiple funding records match one design project, is it one project?
# The question: "How many capital projects..."
# Usually distinct project names in the document.

def get_tokens(text):
    return set(text.lower().replace('&', '').replace(',', '').split())

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
            
        j = i + 1
        while j < len(section_lines):
            next_l = section_lines[j].strip()
            if next_l:
                if next_l.startswith('(cid:190) Updates') or next_l.startswith('(cid:190) Project Description'):
                     doc_project_names.add(line)
                break
            j += 1

# Match logic
final_matches = set()
for d_name in doc_project_names:
    d_tokens = get_tokens(d_name)
    best_match = None
    best_score = 0
    
    # Check exact match first
    if d_name in high_funding_projects:
        final_matches.add(d_name)
        continue
        
    # Check fuzzy
    for f_name in high_funding_projects:
        f_tokens = get_tokens(f_name)
        common = d_tokens.intersection(f_tokens)
        if not f_tokens: continue
        score = len(common) / len(f_tokens) # Coverage of funding name
        
        # Also check coverage of doc name
        score2 = len(common) / len(d_tokens)
        
        if score > 0.75 or score2 > 0.75:
            # Additional check: specific keywords should match if present?
            # e.g. "Drain" vs "Drainage"
            final_matches.add(d_name)
            break

print("__RESULT__:")
print(json.dumps({"count": len(final_matches), "matched": list(final_matches)}))"""

env_args = {'var_function-call-4958646437851811265': 'file_storage/function-call-4958646437851811265.json', 'var_function-call-11007850212329188700': 'file_storage/function-call-11007850212329188700.json', 'var_function-call-17427938851555691024': {'count': 10, 'matched': ['Malibu Canyon Road Traffic Study', 'PCH at Trancas Canyon Road Right Turn Lane', 'Civic Center Stormwater Diversion Structure', 'Outdoor Warning Signs', 'Permanent Skate Park', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Storm Drain Master Plan', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway Repairs'], 'extracted_sample': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'or phasing out the project', 'Westward Beach Road Repair Project']}, 'var_function-call-7722921194275743764': {'count': 10, 'matched': ['Civic Center Stormwater Diversion Structure', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'Permanent Skate Park', 'Storm Drain Master Plan', 'Westward Beach Road Drainage Improvements Project', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'PCH Median Improvements Project', 'PCH at Trancas Canyon Road Right Turn Lane'], 'extracted_sample': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH Median Improvements Project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'Clover Heights Storm Drainage Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground', 'Malibu Canyon Road Traffic Study', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Bluffs Park Shade Structure', 'shade structures at Malibu Bluffs Park.', 'Permanent Skate Park', 'amenities such as trash cans, benches, tables, and restrooms.', 'PCH at Trancas Canyon Road Right Turn Lane', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Civic Center Stormwater Diversion Structure', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Malibu Park Drainage Improvements', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Civic Center Stormwater Diversion Structure', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Malibu Park Drainage Improvements', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Westward Beach Road Improvements Project', 'Civic Center Water Treatment Facility Phase 2', 'Bluffs Park Shade Structure', 'shade structures at Malibu Bluffs Park.', 'Permanent Skate Park', 'amenities such as trash cans, benches, tables, and restrooms.', 'PCH at Trancas Canyon Road Right Turn Lane', 'turn lane at the intersection of PCH and Trancas Canyon Road.']}}

exec(code, env_args)
