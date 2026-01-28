code = """import json, re

# Load the civic_docs query result and the funding query result from storage files
with open(var_call_obVV96DW1GOT64AY8SA7EULO, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_rPIjNDypSV56rdInKUQPK9gh, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts to integers
for rec in funding:
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        # If conversion fails, attempt to strip non-digits
        nums = re.findall(r"\d+", str(rec.get('Amount', '0')))
        rec['Amount'] = int(nums[0]) if nums else 0

# Build list of civic doc texts
texts = [d.get('text','') for d in civic_docs]

matched_projects = []

# For each funding record, search for occurrences in civic documents where the project
# appears with "completed" and "2022" in the nearby context, and where context
# or name indicates a park-related project.
for rec in funding:
    name = rec.get('Project_Name','')
    name_l = name.lower()
    amount = rec.get('Amount',0)
    found = False
    for t in texts:
        t_l = t.lower()
        # Try exact match search first
        idx = t_l.find(name_l)
        if idx == -1:
            # try a more permissive check: search for core tokens (first 3 words)
            tokens = re.findall(r"[a-z0-9]+", name_l)
            if len(tokens) >= 3:
                core = ' '.join(tokens[:3])
                idx = t_l.find(core)
            elif tokens:
                core = ' '.join(tokens)
                idx = t_l.find(core)
        if idx != -1:
            window = t_l[max(0, idx-200): idx+len(name_l)+200]
            if 'completed' in window and '2022' in window:
                # Determine if park-related via name or window context
                if ('park' in name_l) or ('park' in window) or ('playground' in name_l) or ('playground' in window):
                    matched_projects.append({'Project_Name': name, 'Amount': amount})
                    found = True
                    break
        # also as fallback, sometimes project name not present but document mentions a park project and completion
        # We'll skip broad heuristics to avoid false matches
    # end for texts
# end for funding

# Aggregate total funding
total = sum([p['Amount'] for p in matched_projects])

# Prepare result dict
result = {
    'total_funding': total,
    'currency': 'USD',
    'projects_count': len(matched_projects),
    'projects': matched_projects
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_obVV96DW1GOT64AY8SA7EULO': 'file_storage/call_obVV96DW1GOT64AY8SA7EULO.json', 'var_call_AcZ1Ej311kJUnAhDzaAZmJVu': ['Funding'], 'var_call_rPIjNDypSV56rdInKUQPK9gh': 'file_storage/call_rPIjNDypSV56rdInKUQPK9gh.json'}

exec(code, env_args)
