code = """import json
import re
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
    match = re.search("[0-9]{8}", filename)
    if match:
        return datetime.strptime(match.group(0), "%m%d%Y")
    return datetime.min

civic_docs.sort(key=lambda x: get_date(x["filename"]))

project_status = {name: None for name in target_projects}

def normalize(s):
    # Regex [ \t\n\r]+
    ws = chr(32) + chr(9) + chr(10) + chr(13)
    pattern = "[" + ws + "]+"
    return re.sub(pattern, " ", s).strip().lower()

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

BS = chr(92) # Backslash
LP = chr(40) # Left Paren
RP = chr(41) # Right Paren
# Regex: Capital ... \(Design\)
def escape_parens(s):
    return s.replace("(", BS + LP).replace(")", BS + RP)

SECTIONS = [
    (escape_parens("Capital Improvement Projects (Design)"), "design"),
    (escape_parens("Capital Improvement Projects (Construction)"), "construction"),
    (escape_parens("Capital Improvement Projects (Not Started)"), "not started"),
    ("Disaster Recovery Projects", "IGNORE")
]

for doc in civic_docs:
    text = doc["text"]
    text = text.replace(chr(13) + chr(10), NL)
    
    starts = []
    for header_regex, label in SECTIONS:
        matches = list(re.finditer(header_regex, text, re.IGNORECASE))
        for m in matches:
            starts.append((m.start(), label))
            
    starts.append((len(text), "END"))
    starts.sort()
    
    for k in range(len(starts) - 1):
        start_idx, label = starts[k]
        end_idx = starts[k+1][0]
        
        if label == "END": continue
        
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
