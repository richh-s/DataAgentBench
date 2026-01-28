code = """import json

k_fund = locals()['var_function-call-16838995843230881233']
k_docs = locals()['var_function-call-13293051466899965091']

with open(k_fund, 'r') as f:
    funding_data = json.load(f)

high_funding = set()
for item in funding_data:
    if float(item['Amount']) > 50000:
        high_funding.add(item['Project_Name'])

with open(k_docs, 'r') as f:
    civic_docs = json.load(f)

target = "Capital Improvement Projects (Design)"
others = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

found_projects = set()

def normalize(s):
    return " ".join(s.split())

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    start = text.find(target)
    while start != -1:
        s_start = start + len(target)
        s_end = len(text)
        
        for h in others:
            idx = text.find(h, s_start)
            if idx != -1 and idx < s_end:
                s_end = idx
        
        chunk = text[s_start:s_end]
        
        for line in chunk.splitlines():
            n_line = normalize(line)
            if not n_line:
                continue
            
            # Find all matches in this line
            matches = []
            for proj in high_funding:
                if proj in n_line:
                    matches.append(proj)
            
            if matches:
                # Pick the longest match
                longest = max(matches, key=len)
                found_projects.add(longest)
        
        start = text.find(target, s_start)

print("__RESULT__:")
print(json.dumps(list(found_projects)))"""

env_args = {'var_function-call-16838995843230881233': 'file_storage/function-call-16838995843230881233.json', 'var_function-call-16838995843230880788': 'file_storage/function-call-16838995843230880788.json', 'var_function-call-13293051466899965091': 'file_storage/function-call-13293051466899965091.json', 'var_function-call-16442694046434714773': 12, 'var_function-call-11146164805513452029': ['Malibu Bluffs Park South Walkway Repairs', 'PCH Median Improvements Project', 'Westward Beach Road Drainage Improvements Project', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Latigo Canyon Road Retaining Wall Repair Project', 'Clover Heights Storm Drain', 'Civic Center Stormwater Diversion Structure', 'Storm Drain Master Plan', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway', 'Malibu Canyon Road Traffic Study'], 'var_function-call-5515255172171098873': ['Westward Beach Road Drainage Improvements Project', 'PCH at Trancas Canyon Road Right Turn Lane', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Civic Center Stormwater Diversion Structure', 'PCH Median Improvements Project', 'Permanent Skate Park'], 'var_function-call-12951025348195897546': ['Clover Heights Storm Drain']}

exec(code, env_args)
