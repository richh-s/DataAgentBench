code = """import json
import re

# Load data
funding_path = locals()['var_function-call-12490776442151259677']
docs_path = locals()['var_function-call-2297309478391290844']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Combine text from all docs
full_text = ""
for d in civic_docs:
    full_text += d.get('text', '') + "\n\n"

# Map simple name to funding records
funding_map = {}
for rec in funding_data:
    name = rec['Project_Name']
    # Remove suffixes for matching
    simple = re.sub(r'\s*\(.*?\)$', '', name).strip()
    if simple not in funding_map:
        funding_map[simple] = []
    funding_map[simple].append(rec)

search_names = sorted(funding_map.keys(), key=len, reverse=True)

total_funding = 0
matched_ids = set()
debug_log = []

# Keywords for disaster
disaster_keywords = ["FEMA", "CalOES", "Disaster", "Woolsey Fire", "Recovery", "CalJPIA"]

# Patterns for starting in 2022
# We look for "Begin Construction" or similar phases in 2022.
# Also "Advertised: ... 2022" (start of procurement)
start_patterns = [
    r"Begin Construction:.*2022",
    r"Construction Start:.*2022",
    r"started.*2022",
    r"began.*2022",
    r"Award.*2022",
    r"Advertise:.*2022"
]

for name in search_names:
    # Find name in text
    # Use simple string find to be faster/safer than regex for names with special chars
    # Iterate through all occurrences
    start_idx = 0
    while True:
        idx = full_text.find(name, start_idx)
        if idx == -1:
            break
            
        # Extract context window
        window = full_text[idx:idx+1500]
        
        # Check if it's a project header or just a mention?
        # Usually headers are followed by Updates or Description
        if "Updates:" in window or "Project Description:" in window or "Project Schedule:" in window:
            
            # Check Start Date 2022
            started_2022 = False
            for pat in start_patterns:
                if re.search(pat, window, re.IGNORECASE):
                    started_2022 = True
                    break
            
            if started_2022:
                # Check Disaster
                # 1. From text context
                is_disaster_text = False
                for k in disaster_keywords:
                    if k.lower() in window.lower():
                        is_disaster_text = True
                        break
                
                # 2. From funding records
                records = funding_map[name]
                for rec in records:
                    fid = rec['Funding_ID']
                    if fid in matched_ids:
                        continue
                        
                    rec_name = rec['Project_Name']
                    is_disaster_rec = any(k in rec_name for k in ["FEMA", "CalOES", "Disaster", "CalJPIA"])
                    
                    if is_disaster_rec or is_disaster_text:
                        total_funding += int(rec['Amount'])
                        matched_ids.add(fid)
                        debug_log.append(f"Matched {rec_name}: Started 2022 (Context), Disaster (Rec/Text). Amount: {rec['Amount']}")
                        
        start_idx = idx + 1

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matches": debug_log}))"""

env_args = {'var_function-call-12490776442151259677': 'file_storage/function-call-12490776442151259677.json', 'var_function-call-12490776442151257162': 'file_storage/function-call-12490776442151257162.json', 'var_function-call-2297309478391290844': 'file_storage/function-call-2297309478391290844.json'}

exec(code, env_args)
