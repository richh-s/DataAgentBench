code = """import json
import re

# Load funding data
with open('var_function-call-8816954503851875086') as f:
    funding_data = json.load(f)

# Load civic docs
with open('var_function-call-11062513582446324049') as f:
    civic_docs = json.load(f)

# Combine all text
full_text = chr(10).join([doc['text'] for doc in civic_docs])

# Prepare funding dict
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower()
    if "spring 2022" in date_str:
        return True
    if "2022" in date_str:
        if any(m in date_str for m in ["march", "april", "may"]):
            return True
    return False

def get_start_date(project_name, text):
    escaped_name = re.escape(project_name)
    matches = [m.start() for m in re.finditer(escaped_name, text, re.IGNORECASE)]
    start_dates = []
    
    # Regex patterns with double backslashes for python string inside json
    # We want \s and \d to reach python code
    
    date_patterns = [
        r"Begin [Cc]onstruction:?\s*([A-Za-z0-9, ]+)",
        r"Start [Dd]ate:?\s*([A-Za-z0-9, ]+)",
        r"Construction [Ss]tart:?\s*([A-Za-z0-9, ]+)",
        r"Construction to begin:?\s*([A-Za-z0-9, ]+)"
    ]
    
    for start_idx in matches:
        chunk = text[start_idx:start_idx+1000]
        for pat in date_patterns:
            m = re.search(pat, chunk)
            if m:
                raw_date = m.group(1).split(chr(10))[0].strip()
                start_dates.append(raw_date)
    return start_dates

projects_started_spring_2022 = []

for project_name, amount in funding_map.items():
    dates = get_start_date(project_name, full_text)
    
    # Check if any of the extracted dates is Spring 2022
    is_started = False
    valid_dates = []
    for d in dates:
        if is_spring_2022(d):
            is_started = True
            valid_dates.append(d)
            
    if is_started:
        projects_started_spring_2022.append({
            "Project_Name": project_name,
            "Amount": amount,
            "Dates_Found": valid_dates
        })

count = len(projects_started_spring_2022)
total_funding = sum(p['Amount'] for p in projects_started_spring_2022)

print("__RESULT__:")
print(json.dumps({
    "count": count,
    "total_funding": total_funding,
    "projects": projects_started_spring_2022
}))"""

env_args = {'var_function-call-13891692615433348012': 'file_storage/function-call-13891692615433348012.json', 'var_function-call-8816954503851875086': 'file_storage/function-call-8816954503851875086.json', 'var_function-call-11062513582446324049': 'file_storage/function-call-11062513582446324049.json'}

exec(code, env_args)
