code = """import json
import re

# Load
with open(locals()['var_function-call-11529138748773800259'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-6363168235283738913'], 'r') as f:
    funding_data = json.load(f)

funding_lookup = {}
for item in funding_data:
    funding_lookup[item['Project_Name'].strip()] = float(item['Amount'])

matched_projects = []

for doc in civic_docs:
    text = doc['text']
    parts = text.split('(cid:190)')
    
    current_project = None
    # Parse first part
    p0 = parts[0].strip()
    if p0:
        lines = [l.strip() for l in p0.split('\n') if l.strip()]
        # Skip headers
        # simplified check
        valid_lines = []
        for l in lines:
            if "Capital" in l or "Agenda" in l or "Page" in l or "Subject" in l:
                continue
            valid_lines.append(l)
        if valid_lines:
            current_project = valid_lines[-1]

    projects_found = {}
    
    for i in range(1, len(parts)):
        chunk = parts[i]
        if current_project:
            if current_project not in projects_found:
                projects_found[current_project] = ""
            projects_found[current_project] += " " + chunk
            
        # Find next
        lines = [l.strip() for l in chunk.strip().split('\n') if l.strip()]
        candidate = None
        for line in reversed(lines):
            # Check delimiters
            if "Updates:" in line or "Schedule:" in line or "Construction:" in line:
                break
            if "Agenda" in line or "Page" in line:
                continue
            if len(line) < 100 and not line.endswith('.'):
                candidate = line
                break
        if candidate:
            current_project = candidate

    # Check
    for name, content in projects_found.items():
        if 'park' in name.lower():
            # Check completion 2022
            # Look for 'completed ... 2022'
            # Simplify regex
            if re.search(r"completed[\w\s,]+2022", content, re.IGNORECASE):
                # Ensure it's not 'Design completed'
                # Check context?
                # Usually: "Construction was completed..."
                if "construction" in content.lower():
                    matched_projects.append(name)
            elif re.search(r"Complete Construction:[\w\s]+2022", content, re.IGNORECASE):
                matched_projects.append(name)

matched_projects = list(set(matched_projects))

total = 0.0
matches = []

for p in matched_projects:
    # Exact
    if p in funding_lookup:
        total += funding_lookup[p]
        matches.append(p)
    else:
        # Fuzzy: check if p is substring of keys
        for k, v in funding_lookup.items():
            if p in k:
                # Avoid matching "Park" to "Parker"
                # Check if k starts with p?
                if k.startswith(p):
                   total += v
                   matches.append(k)

print("__RESULT__:")
print(json.dumps({"matches": matches, "total_funding": total}))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json'}

exec(code, env_args)
