code = """import json

with open('var_function-call-8728366382386706787', 'r') as f:
    civic_docs = json.load(f)

with open('var_function-call-8728366382386704966', 'r') as f:
    funding_data = json.load(f)

funding_map = {row['Project_Name'].strip(): row['Amount'] for row in funding_data}

projects_found = {}

def check_date(d):
    d = d.lower()
    if '2022' in d:
        if 'spring' in d: return True
        if 'march' in d or 'april' in d or 'may' in d: return True
        # Check for 03/2022, 04/2022, 05/2022
        # Simple check for numeric patterns
        import re
        if re.search(r'(03|04|05)[/-]2022', d): return True
        if re.search(r'2022[/-](03|04|05)', d): return True
    return False

# Parse text
for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_proj = None
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line: continue
        
        # Check if project name
        # Look ahead for (cid:190)
        is_proj = False
        for j in range(i+1, min(i+5, len(lines))):
            if '(cid:190)' in lines[j]:
                # If there's a line with (cid:190) shortly after, and the current line is not a header?
                # Headers: "Capital Improvement Projects..."
                if "Capital Improvement" in line or "Agenda Item" in line:
                    break
                is_proj = True
                break
            if lines[j].strip(): # Stop at first non-empty line to be strict? 
                # The sample showed "Project Name" \n \n "(cid:190)..."
                # So we can skip empty lines.
                if '(cid:190)' in lines[j]:
                    is_proj = True
                break
        
        if is_proj:
            current_proj = line
            if current_proj not in projects_found:
                projects_found[current_proj] = []
        
        if current_proj:
            # Check for start date
            low = line.lower()
            if 'begin construction' in low or 'construction start' in low:
                # Extract the value
                parts = line.split(':')
                if len(parts) > 1:
                    val = parts[1].strip()
                    projects_found[current_proj].append(val)

# Filter
spring_projs = []
for p, dates in projects_found.items():
    for d in dates:
        if check_date(d):
            spring_projs.append(p)
            break

# Calc funding
total = 0
matched = []
unmatched = []

for p in spring_projs:
    # Exact match
    if p in funding_map:
        total += funding_map[p]
        matched.append(p)
    else:
        # Fuzzy match?
        # Maybe the project name in text has extra spaces or something?
        # Try normalizing
        found = False
        for fp in funding_map:
            if fp.lower() == p.lower():
                total += funding_map[fp]
                matched.append(p)
                found = True
                break
        if not found:
            unmatched.append(p)

print("__RESULT__:")
print(json.dumps({
    "count": len(spring_projs),
    "total_funding": total,
    "projects": spring_projs,
    "unmatched": unmatched,
    "debug_dates": projects_found
}))"""

env_args = {'var_function-call-8728366382386706787': 'file_storage/function-call-8728366382386706787.json', 'var_function-call-8728366382386704966': 'file_storage/function-call-8728366382386704966.json'}

exec(code, env_args)
