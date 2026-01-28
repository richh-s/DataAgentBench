code = """import json
import re

# Load data
with open(locals()['var_function-call-8460811092792669481'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-8460811092792670416'], 'r') as f:
    civic_docs = json.load(f)

# Funding map
funding_map = {item['Project_Name'].strip(): int(item['Amount']) for item in funding_data}
funding_names = list(funding_map.keys())
# Sort by length desc to match longest name first
funding_names.sort(key=len, reverse=True)

matched_projects = set()

def check_date(d):
    d = d.lower()
    if '2022' not in d: return False
    if 'spring' in d: return True
    if 'march' in d or 'april' in d or 'may' in d: return True
    # 03/2022 etc
    if '03/' in d or '04/' in d or '05/' in d: return True
    if '-03' in d or '-04' in d or '-05' in d: return True
    return False

for doc in civic_docs:
    text = doc['text']
    
    # Find all start dates
    # We look for "Begin Construction: <value>"
    # Use simple regex
    matches = list(re.finditer(r"Begin Construction\s*[:]\s*([^\n]+)", text, re.IGNORECASE))
    
    for m in matches:
        date_str = m.group(1).strip()
        if check_date(date_str):
            # Find associated project
            # Search backwards from m.start() for a project name
            best_name = None
            best_idx = -1
            
            # This segment searches for the closest preceding project name
            # We limit search to say 2000 chars back to avoid false positives from far away
            search_limit = max(0, m.start() - 5000)
            search_text = text[search_limit:m.start()]
            
            for name in funding_names:
                # Find last occurrence of name in search_text
                idx = search_text.rfind(name)
                if idx != -1:
                    # Adjust idx to be absolute
                    abs_idx = search_limit + idx
                    if abs_idx > best_idx:
                        best_idx = abs_idx
                        best_name = name
            
            if best_name:
                matched_projects.add(best_name)

# Sum
count = 0
total_funding = 0
for p in matched_projects:
    count += 1
    total_funding += funding_map[p]

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(matched_projects)}))"""

env_args = {'var_function-call-15438762544756245875': 'file_storage/function-call-15438762544756245875.json', 'var_function-call-15438762544756246872': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-8460811092792669481': 'file_storage/function-call-8460811092792669481.json', 'var_function-call-8460811092792670416': 'file_storage/function-call-8460811092792670416.json'}

exec(code, env_args)
