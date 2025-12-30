code = """import json
import re

# Load data
funding_path = locals()['var_function-call-11583348027309783975']
civic_docs_path = locals()['var_function-call-7486836115047757941']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# 1. Identify Capital Projects > $50k
target_projects = set()
for record in funding_data:
    try:
        amt = float(record.get('Amount', 0))
    except:
        amt = 0
    if amt > 50000:
        name = record.get('Project_Name', '').strip()
        # Filter disaster projects based on suffixes
        # Suffixes: (FEMA Project), (CalJPIA Project), (CalOES Project)
        # Also exclude if name implies disaster explicitly if needed, but suffixes are the main indicator.
        is_disaster = False
        for suffix in ["(FEMA", "(CalJPIA", "(CalOES", "FEMA Project", "CalOES Project"]:
            if suffix in name:
                is_disaster = True
                break
        if not is_disaster and name:
            target_projects.add(name)

# 2. Sort docs by date descending
def get_date_str(filename):
    # malibucity_agenda__01262022-1835.txt
    match = re.search(r'(\d{8})', filename)
    if match:
        return match.group(1) # MMDDYYYY
    return "00000000"

def sort_key(doc):
    d = get_date_str(doc.get('filename', ''))
    if len(d) == 8:
        # YYYYMMDD
        return d[4:] + d[:4] + d[2:4] + d[0:2] # Wait, d[4:] is YYYY, d[:4] is MMDD. Correct is YYYYMMDD.
        # d = "01262022" -> Month=01, Day=26, Year=2022
        # d[4:] = "2022"
        # d[:2] = "01"
        # d[2:4] = "26"
        return d[4:] + d[:2] + d[2:4]
    return "00000000"

civic_docs.sort(key=sort_key, reverse=True)

# 3. Find status
# Map headers to status
header_map = [
    (r"Capital Improvement Projects\s*\(Design\)", "Design"),
    (r"Capital Improvement Projects\s*\(Construction\)", "Other"),
    (r"Capital Improvement Projects\s*\(Not Started\)", "Other"),
    (r"Disaster Recovery Projects", "Other") # If found under Disaster, it's not Capital Design
]

found_status = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_status = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check header
        is_header = False
        for pattern, status in header_map:
            if re.search(pattern, line_clean, re.IGNORECASE):
                current_status = status
                is_header = True
                break
        if is_header:
            continue
            
        # Check project
        if current_status is not None:
            if line_clean in target_projects:
                if line_clean not in found_status:
                    found_status[line_clean] = current_status

# 4. Count
count = sum(1 for s in found_status.values() if s == "Design")

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-11583348027309783975': 'file_storage/function-call-11583348027309783975.json', 'var_function-call-11583348027309784792': 'file_storage/function-call-11583348027309784792.json', 'var_function-call-7486836115047757941': 'file_storage/function-call-7486836115047757941.json'}

exec(code, env_args)
