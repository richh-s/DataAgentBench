code = """import json

# Load funding data
with open(locals()['var_function-call-16838995843230881233'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = {item['Project_Name'] for item in funding_data if float(item['Amount']) > 50000}

# Load civic docs
with open(locals()['var_function-call-13293051466899965091'], 'r') as f:
    civic_docs = json.load(f)

target_header = "Capital Improvement Projects (Design)"
other_headers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

found_projects = set()

def normalize(s):
    return " ".join(s.split())

for doc in civic_docs:
    text = doc.get('text', '')
    
    start_idx = text.find(target_header)
    while start_idx != -1:
        section_start = start_idx + len(target_header)
        section_end = len(text)
        
        for header in other_headers:
            idx = text.find(header, section_start)
            if idx != -1 and idx < section_end:
                section_end = idx
        
        section_text = text[section_start:section_end]
        
        # Split into lines and match
        lines = section_text.split('\n')
        for line in lines:
            norm_line = normalize(line)
            if norm_line in high_funding_projects:
                found_projects.add(norm_line)
            
            # Also check if the line *starts* with the project name followed by non-alphanumeric (like colon)?
            # But the hint says names match.
        
        start_idx = text.find(target_header, section_start)

print("__RESULT__:")
print(json.dumps(list(found_projects)))"""

env_args = {'var_function-call-16838995843230881233': 'file_storage/function-call-16838995843230881233.json', 'var_function-call-16838995843230880788': 'file_storage/function-call-16838995843230880788.json', 'var_function-call-13293051466899965091': 'file_storage/function-call-13293051466899965091.json', 'var_function-call-16442694046434714773': 12, 'var_function-call-11146164805513452029': ['Malibu Bluffs Park South Walkway Repairs', 'PCH Median Improvements Project', 'Westward Beach Road Drainage Improvements Project', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Latigo Canyon Road Retaining Wall Repair Project', 'Clover Heights Storm Drain', 'Civic Center Stormwater Diversion Structure', 'Storm Drain Master Plan', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway', 'Malibu Canyon Road Traffic Study']}

exec(code, env_args)
