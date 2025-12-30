code = """import json
import re

# Load data
with open(locals()['var_function-call-16231141509996645280'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-1791089883245818751'], 'r') as f:
    civic_docs = json.load(f)

# Build project map
funding_map = {}
for item in funding_data:
    try:
        amount = int(item['Amount'])
    except:
        amount = 0
    funding_map[item['Project_Name']] = amount

project_names = list(funding_map.keys())
# Sort by length descending for priority
project_names.sort(key=len, reverse=True)

disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Disaster", "Woolsey", "Emergency", "Fire"]

def extract_year(date_str):
    match = re.search(r'20\d{2}', date_str)
    if match:
        return match.group(0)
    return None

def is_disaster_related(text, name):
    for kw in disaster_keywords:
        if kw.lower() in name.lower():
            return True
    for kw in disaster_keywords:
        if kw.lower() in text.lower():
            return True
    return False

project_findings = {name: {'is_disaster': False, 'start_years': set(), 'text_snippets': []} for name in project_names}

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all matches
    matches = []
    for name in project_names:
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1:
                break
            matches.append({'start': idx, 'end': idx + len(name), 'name': name})
            start = idx + len(name)
    
    # Sort by start asc, then length desc (implicit by order of finding if we cared, but explicit sort is safer)
    # Actually, we want to prioritize longer matches at same position.
    matches.sort(key=lambda x: (x['start'], -len(x['name'])))
    
    # Filter overlaps
    kept_matches = []
    last_end = -1
    for m in matches:
        if m['start'] >= last_end:
            kept_matches.append(m)
            last_end = m['end']
    
    # Extract text
    for i in range(len(kept_matches)):
        m = kept_matches[i]
        name = m['name']
        start_snippet = m['end']
        end_snippet = kept_matches[i+1]['start'] if i+1 < len(kept_matches) else len(text)
        
        snippet = text[start_snippet:end_snippet]
        project_findings[name]['text_snippets'].append(snippet)

# Analyze
valid_projects = []
debug_info = []

patterns = [
    r"Begin Construction[:\s]+([A-Za-z0-9\s,]+)",
    r"Start Construction[:\s]+([A-Za-z0-9\s,]+)",
    r"Construction Start[:\s]+([A-Za-z0-9\s,]+)",
    r"Begin Design[:\s]+([A-Za-z0-9\s,]+)",
    r"Start Date[:\s]+([A-Za-z0-9\s,]+)",
    r"Advertise[:\s]+([A-Za-z0-9\s,]+)",
    r"Award Contract[:\s]+([A-Za-z0-9\s,]+)",
    r"Notice to Proceed[:\s]+([A-Za-z0-9\s,]+)",
    r"Construction[:\s]+.*Begin[:\s]+([A-Za-z0-9\s,]+)", # e.g. "Construction Phase: Begin Spring 2022"
    r"Project Schedule[:\s]+.*Begin[:\s]+([A-Za-z0-9\s,]+)"
]

for name, info in project_findings.items():
    snippets = info['text_snippets']
    if not snippets:
        continue
    full_text = " ".join(snippets)
    
    if is_disaster_related(full_text, name):
        info['is_disaster'] = True
    
    # Extract years
    for pat in patterns:
        found = re.findall(pat, full_text, re.IGNORECASE)
        for date_str in found:
            y = extract_year(date_str)
            if y:
                info['start_years'].add(y)
    
    # Special check: if no explicit start date found, but "Completed" is in 2022?
    # No, stick to explicit start.
    
    if info['is_disaster'] and '2022' in info['start_years']:
        valid_projects.append(name)
        debug_info.append({"name": name, "years": list(info['start_years']), "amount": funding_map[name]})

total_funding = sum(funding_map[name] for name in valid_projects)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "valid_projects": valid_projects, "debug_info": debug_info}))"""

env_args = {'var_function-call-16231141509996642335': 'file_storage/function-call-16231141509996642335.json', 'var_function-call-16231141509996645280': 'file_storage/function-call-16231141509996645280.json', 'var_function-call-1791089883245818751': 'file_storage/function-call-1791089883245818751.json', 'var_function-call-4984436726342417826': {'total_funding': 517000, 'valid_projects': ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Slope Stabilization Project', 'Encinal Canyon Road Drainage Improvements', 'Latigo Canyon Road Culvert Repairs', 'Clover Heights Storm Drain', 'Malibu Road Slope Repairs'], 'debug_info': [{'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'years': ['2021', '2022'], 'amount': 19000}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'years': ['2021', '2022'], 'amount': 87000}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'years': ['2022'], 'amount': 77000}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'years': ['2022'], 'amount': 78000}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'years': ['2022'], 'amount': 68000}, {'name': 'Encinal Canyon Road Drainage Improvements', 'years': ['2022'], 'amount': 34000}, {'name': 'Latigo Canyon Road Culvert Repairs', 'years': ['2022'], 'amount': 57000}, {'name': 'Clover Heights Storm Drain', 'years': ['2023', '2022'], 'amount': 53000}, {'name': 'Malibu Road Slope Repairs', 'years': ['2021', '2022'], 'amount': 44000}]}}

exec(code, env_args)
