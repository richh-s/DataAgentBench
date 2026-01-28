code = """import json

with open(locals()['var_function-call-4570374009180656928'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = [item['Project_Name'] for item in funding_data if int(item['Amount']) > 50000]

with open(locals()['var_function-call-13689454801406461365'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    start_idx = text.find("Capital Improvement Projects (Design)")
    if start_idx == -1:
        continue
        
    # Find end
    end_idx = len(text)
    for marker in ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects", "Staff has also prepared"]:
        idx = text.find(marker, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
    
    section = text[start_idx:end_idx]
    
    for line in section.split('\n'):
        line = line.strip()
        if not line: continue
        
        matches = [p for p in high_funding_projects if p in line]
        if matches:
            found_projects.add(max(matches, key=len))

print("__RESULT__:")
print(json.dumps(list(found_projects)))"""

env_args = {'var_function-call-4570374009180656928': 'file_storage/function-call-4570374009180656928.json', 'var_function-call-12751430188961870496': 'file_storage/function-call-12751430188961870496.json', 'var_function-call-13689454801406461365': 'file_storage/function-call-13689454801406461365.json', 'var_function-call-6647682698323320664': ['Malibu Bluffs Park South Walkway Repairs', 'Permanent Skate Park', 'Storm Drain Master Plan', 'PCH Median Improvements Project', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Clover Heights Storm Drain', 'Civic Center Stormwater Diversion Structure']}

exec(code, env_args)
