code = """import json

# Load funding data
with open(locals()['var_function-call-4570374009180656928'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = []
for item in funding_data:
    try:
        if int(item['Amount']) > 50000:
            high_funding_projects.append(item['Project_Name'])
    except ValueError:
        continue

# Load civic docs
with open(locals()['var_function-call-13689454801406461365'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    start_header = "Capital Improvement Projects (Design)"
    
    end_headers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects",
        "Staff has also prepared"
    ]
    
    start_idx = text.find(start_header)
    if start_idx == -1:
        continue
        
    end_idx = len(text)
    for end_h in end_headers:
        idx = text.find(end_h, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    design_section = text[start_idx:end_idx]
    
    # Split section into lines
    lines = design_section.split('\n')
    
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue
            
        # Find all matches for this line
        matches = []
        for proj_name in high_funding_projects:
            # We check if project name is in the line.
            # Case sensitivity: The data seems to have consistent casing, but ignoring case might be safer?
            # The prompt examples show matching case. I'll stick to case-sensitive first.
            if proj_name in clean_line:
                matches.append(proj_name)
        
        if matches:
            # Pick the longest match
            best_match = max(matches, key=len)
            found_projects.add(best_match)

print("__RESULT__:")
print(json.dumps(list(found_projects)))"""

env_args = {'var_function-call-4570374009180656928': 'file_storage/function-call-4570374009180656928.json', 'var_function-call-12751430188961870496': 'file_storage/function-call-12751430188961870496.json', 'var_function-call-13689454801406461365': 'file_storage/function-call-13689454801406461365.json', 'var_function-call-6647682698323320664': ['Malibu Bluffs Park South Walkway Repairs', 'Permanent Skate Park', 'Storm Drain Master Plan', 'PCH Median Improvements Project', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Clover Heights Storm Drain', 'Civic Center Stormwater Diversion Structure']}

exec(code, env_args)
