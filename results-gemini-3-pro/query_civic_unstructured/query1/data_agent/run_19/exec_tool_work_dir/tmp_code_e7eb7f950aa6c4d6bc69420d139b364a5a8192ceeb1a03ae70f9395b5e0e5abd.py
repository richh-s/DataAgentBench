code = """import json

with open(locals()['var_function-call-10318342191074584213'], 'r') as f:
    funding_data = json.load(f)

high_funding_db = {}
for item in funding_data:
    try:
        if float(item['Amount']) > 50000:
            high_funding_db[item['Project_Name']] = float(item['Amount'])
    except:
        pass

with open(locals()['var_function-call-9654609134184919281'], 'r') as f:
    civic_docs = json.load(f)

extracted_lines = []
for doc in civic_docs:
    text = doc['text']
    start_idx = text.find("Capital Improvement Projects (Design)")
    if start_idx == -1: continue
    
    end_markers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]
    end_idx = len(text)
    for marker in end_markers:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section = text[start_idx:end_idx]
    
    lines = section.split('\n')
    for line in lines:
        line = line.strip()
        if not line: continue
        if "Page" in line and "of" in line: continue
        if "Agenda Item" in line: continue
        if "Updates:" in line or "Project Schedule:" in line: continue
        if "Capital Improvement Projects" in line: continue
        if "Date prepared" in line: continue
        if "Recommendation" in line: continue
        extracted_lines.append(line)

matched_db_projects = set()

for line in extracted_lines:
    candidates = []
    for db_name in high_funding_db.keys():
        if db_name in line or line in db_name:
            candidates.append(db_name)
    
    if candidates:
        candidates.sort(key=len, reverse=True)
        best_match = candidates[0]
        matched_db_projects.add(best_match)

print("__RESULT__:")
print(json.dumps({"count": len(matched_db_projects), "matches": list(matched_db_projects)}))"""

env_args = {'var_function-call-10318342191074584213': 'file_storage/function-call-10318342191074584213.json', 'var_function-call-9654609134184919281': 'file_storage/function-call-9654609134184919281.json', 'var_function-call-4559528786802393198': {'count': 12, 'matches': ['Outdoor Warning Signs', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Bluffs Park South Walkway', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Storm Drain Master Plan', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Canyon Road Traffic Study', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane']}}

exec(code, env_args)
