code = """import json
import re

path_fund = locals()['var_function-call-10469334728230477233']
path_civic = locals()['var_function-call-2938925832300121320']

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + chr(10)

lines = full_text.split(chr(10))
projects = {}
current_name = None
current_text = []

# Simplified skip list
skip = ["Page ", "Agenda Item", "Prepared by", "Approved by", "Subject:", "RECOMMENDED ACTION", "DISCUSSION", "Public Works", "Commission Meeting"]
headers = ["Capital Improvement Projects", "Disaster Recovery Projects"]

def check_line(l):
    l = l.strip()
    if not l: return False
    # Check start chars
    if l.startswith("(") or l.startswith("•"): return False
    # Check keywords
    for s in skip:
        if s in l: return False
    for h in headers:
        if h in l: return False
    if len(l) > 80: return False
    if len(l) < 5: return False
    return True

for line in lines:
    if check_line(line):
        if current_name:
            projects[current_name] = chr(10).join(current_text)
        current_name = line.strip()
        current_text = []
    else:
        if current_name:
            current_text.append(line)

if current_name:
    projects[current_name] = chr(10).join(current_text)

# Match and sum
total = 0
matches = []

for item in funding_data:
    p_name = item['Project_Name']
    amt = item['Amount']
    
    # Check disaster
    is_disaster = False
    if "FEMA" in p_name or "CalOES" in p_name or "CalJPIA" in p_name:
        is_disaster = True
    
    # Check text for start date
    # Find matching project text
    # Clean name
    clean_name = p_name.split('(')[0].strip()
    
    txt = ""
    if p_name in projects:
        txt = projects[p_name]
    elif clean_name in projects:
        txt = projects[clean_name]
    else:
        # fuzzy
        for k in projects:
            if clean_name in k:
                txt = projects[k]
                break
    
    # Check year in text or name
    start_2022 = False
    if "2022" in p_name:
        start_2022 = True
    elif txt:
        # Check specific phrases
        # "Begin Construction: ... 2022"
        # "Advertise: ... 2022"
        # We look for "2022" near "Begin" or "Start"
        if "2022" in txt:
             # Look closer
             # Regex for "Begin Construction.*2022"
             if re.search(r"Begin [Cc]onstruction.{0,50}2022", txt):
                 start_2022 = True
             elif re.search(r"Advertise.{0,50}2022", txt):
                 # Advertise implies start of process? 
                 # Maybe. But "started in 2022" usually means execution.
                 # Let's count it if uncertain.
                 start_2022 = True
    
    if is_disaster and start_2022:
        total += float(amt)
        matches.append(p_name)

print("__RESULT__:")
print(json.dumps({"total": total, "matches": matches, "parsed_titles": list(projects.keys())[:5]}))"""

env_args = {'var_function-call-10469334728230477233': 'file_storage/function-call-10469334728230477233.json', 'var_function-call-10469334728230474172': 'file_storage/function-call-10469334728230474172.json', 'var_function-call-2938925832300121320': 'file_storage/function-call-2938925832300121320.json'}

exec(code, env_args)
