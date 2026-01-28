code = """import json
from datetime import datetime

NL = chr(10)

funding_data = json.load(open(locals()["var_function-call-6229700754411909413"]))
civic_docs = json.load(open(locals()["var_function-call-10406381100276321723"]))

target_projects = {}
for rec in funding_data:
    try:
        amt = float(rec["Amount"])
    except:
        amt = 0
    if amt > 50000:
        target_projects[rec["Project_Name"]] = amt

def get_date(filename):
    # malibucity_agenda_03222023-2060.txt
    try:
        parts = filename.split("_")
        if len(parts) >= 3:
            date_part = parts[2].split("-")[0]
            if len(date_part) == 8:
                return datetime.strptime(date_part, "%m%d%Y")
    except:
        pass
    return datetime.min

civic_docs.sort(key=lambda x: get_date(x["filename"]))

project_status = {name: None for name in target_projects}

def normalize(s):
    # Manual replace
    for char in [chr(9), chr(10), chr(13)]:
        s = s.replace(char, " ")
    while "  " in s:
        s = s.replace("  ", " ")
    return s.strip().lower()

norm_targets = {name: normalize(name) for name in target_projects}

def find_matches(section_text, status_label):
    if status_label == "IGNORE": return
    lines = section_text.split(NL)
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        is_header = False
        for j in range(i+1, len(lines)):
            next_line = lines[j].strip()
            if not next_line: continue
            if next_line.startswith("(") or next_line.startswith("Updates") or next_line.startswith("Project"):
                is_header = True
            break
        
        if is_header:
            cleaned_line = normalize(line)
            best_match = None
            max_len = 0
            
            for real_name, norm_name in norm_targets.items():
                if norm_name in cleaned_line:
                    if len(norm_name) > max_len:
                        max_len = len(norm_name)
                        best_match = real_name
                elif cleaned_line in norm_name:
                     if len(cleaned_line) > max_len:
                        max_len = len(cleaned_line)
                        best_match = real_name
            
            if best_match:
                project_status[best_match] = status_label

SECTIONS = [
    ("Capital Improvement Projects (Design)", "design"),
    ("Capital Improvement Projects (Construction)", "construction"),
    ("Capital Improvement Projects (Not Started)", "not started"),
    ("Disaster Recovery Projects", "IGNORE")
]

for doc in civic_docs:
    text = doc["text"]
    text = text.replace(chr(13) + chr(10), NL)
    lower_text = text.lower()
    
    starts = []
    for header, label in SECTIONS:
        search_start = 0
        h_lower = header.lower()
        while True:
            idx = lower_text.find(h_lower, search_start)
            if idx == -1:
                break
            starts.append((idx, label))
            search_start = idx + len(h_lower)
            
    starts.append((len(text), "END"))
    starts.sort()
    
    for k in range(len(starts) - 1):
        start_idx, label = starts[k]
        end_idx = starts[k+1][0]
        
        if label == "END": continue
        
        # Original text slice
        section_content = text[start_idx:end_idx]
        find_matches(section_content, label)

count = 0
for name, status in project_status.items():
    if status == "design":
        count += 1

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-6229700754411909413': 'file_storage/function-call-6229700754411909413.json', 'var_function-call-6229700754411910276': 'file_storage/function-call-6229700754411910276.json', 'var_function-call-10406381100276321723': 'file_storage/function-call-10406381100276321723.json'}

exec(code, env_args)
