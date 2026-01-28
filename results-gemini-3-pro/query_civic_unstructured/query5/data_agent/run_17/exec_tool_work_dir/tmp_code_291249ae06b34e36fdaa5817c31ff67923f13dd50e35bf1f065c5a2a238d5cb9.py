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
    # item['Amount'] is a string in the preview, need to convert to int
    try:
        amount = int(item['Amount'])
    except:
        amount = 0
    funding_map[item['Project_Name']] = amount

project_names = list(funding_map.keys())
# Sort by length descending to match longest names first
project_names.sort(key=len, reverse=True)

project_findings = {name: {'is_disaster': False, 'start_dates': set(), 'text_snippets': []} for name in project_names}

disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Disaster", "Woolsey", "Emergency", "Fire"]

def extract_year(date_str):
    match = re.search(r'20\d{2}', date_str)
    if match:
        return match.group(0)
    return None

def is_disaster_related(text, name):
    # Check name
    for kw in disaster_keywords:
        if kw.lower() in name.lower():
            return True
    # Check text
    # This might be too broad if text is long, but we'll try
    for kw in disaster_keywords:
        if kw.lower() in text.lower():
            return True
    return False

# Iterate through documents
for doc in civic_docs:
    text = doc.get('text', '')
    # Find project occurrences
    # We want to find where a project starts. 
    # A simple way is to find all start indices of all project names, then sort them.
    
    matches = []
    for name in project_names:
        # Simple string find might match inside other words, but project names are usually distinct
        # Use regex to ensure word boundary if possible, but names have spaces.
        # Just use simple find for now, assuming names are unique enough.
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1:
                break
            matches.append((idx, name))
            start = idx + len(name)
    
    matches.sort(key=lambda x: x[0])
    
    # Now extract text for each project
    for i in range(len(matches)):
        start_idx, name = matches[i]
        end_idx = matches[i+1][0] if i+1 < len(matches) else len(text)
        
        # Limit the text length to avoid reading into next unrelated sections too much
        # (Though next match usually delimits it)
        snippet = text[start_idx:end_idx]
        
        project_findings[name]['text_snippets'].append(snippet)
        
        # Analyze snippets immediately or later? Later is fine.

# Analyze findings
valid_projects = []
debug_info = []

for name, info in project_findings.items():
    snippets = info['text_snippets']
    if not snippets:
        continue
        
    full_text = " ".join(snippets)
    
    # Check disaster
    if is_disaster_related(full_text, name):
        info['is_disaster'] = True
    
    # Extract Start Date
    # Look for "Begin Construction: [Date]"
    # "Start Date: [Date]"
    # "Advertise: [Date]" -> Start of procurement
    # "Construction start: [Date]"
    
    # Regex patterns
    # (cid:131) is a bullet point in the text
    patterns = [
        r"Begin Construction[:\s]+([A-Za-z0-9\s,]+)",
        r"Start Construction[:\s]+([A-Za-z0-9\s,]+)",
        r"Construction Start[:\s]+([A-Za-z0-9\s,]+)",
        r"Begin Design[:\s]+([A-Za-z0-9\s,]+)",
        r"Start Date[:\s]+([A-Za-z0-9\s,]+)",
        # "Advertise" implies start of process
        r"Advertise[:\s]+([A-Za-z0-9\s,]+)"
    ]
    
    start_years = set()
    for pat in patterns:
        matches = re.findall(pat, full_text, re.IGNORECASE)
        for m in matches:
            # Clean match
            date_str = m.strip()
            # Extract year
            y = extract_year(date_str)
            if y:
                start_years.add(y)
    
    info['start_years'] = start_years
    
    if info['is_disaster'] and '2022' in start_years:
        valid_projects.append(name)
        debug_info.append({"name": name, "years": list(start_years), "amount": funding_map[name]})

total_funding = sum(funding_map[name] for name in valid_projects)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "valid_projects": valid_projects, "debug_info": debug_info}))"""

env_args = {'var_function-call-16231141509996642335': 'file_storage/function-call-16231141509996642335.json', 'var_function-call-16231141509996645280': 'file_storage/function-call-16231141509996645280.json', 'var_function-call-1791089883245818751': 'file_storage/function-call-1791089883245818751.json'}

exec(code, env_args)
