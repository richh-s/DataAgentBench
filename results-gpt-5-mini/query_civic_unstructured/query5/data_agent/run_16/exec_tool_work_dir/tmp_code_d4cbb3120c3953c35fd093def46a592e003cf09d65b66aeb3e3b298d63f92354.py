code = """import json

# Load data files provided by previous tool calls
with open(var_call_zOxJAXyiUvuRoRPWatEiq5lx, 'r') as f:
    funding = json.load(f)
with open(var_call_0GxLFGimWWtyZ5EaoIHD7wLd, 'r') as f:
    civic_docs = json.load(f)

# Combine civic docs text into one lowercase string
parts = []
for d in civic_docs:
    t = d.get('text', '')
    if t:
        parts.append(t.lower())
full_text = "\n".join(parts)

# Helper to extract integer amount safely
def to_int_amount(x):
    s = str(x)
    digits = ''.join(ch for ch in s if ch.isdigit())
    return int(digits) if digits else 0

# Disaster keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency', 'federal assistance']

selected = []
for r in funding:
    amt = to_int_amount(r.get('Amount', 0))
    name = r.get('Project_Name', '')
    name_norm = name.lower()
    # check name indicates disaster
    name_disaster = any(kw in name_norm for kw in disaster_keywords)
    # check if name contains 2022
    name_2022 = '2022' in name_norm
    # search occurrences in civic docs
    found = False
    found_2022 = False
    found_disaster_near = False
    if name_norm:
        start = 0
        while True:
            idx = full_text.find(name_norm, start)
            if idx == -1:
                break
            found = True
            # define window
            wstart = max(0, idx-300)
            wend = min(len(full_text), idx+300)
            snippet = full_text[wstart:wend]
            if '2022' in snippet:
                found_2022 = True
            if any(kw in snippet for kw in disaster_keywords):
                found_disaster_near = True
            start = idx + 1
    # determine started in 2022
    started_2022 = name_2022 or found_2022
    is_disaster = name_disaster or found_disaster_near
    if is_disaster and started_2022:
        selected.append({'Project_Name': name, 'Amount': amt})

total = sum(p['Amount'] for p in selected)

out = {
    'total_funding': total,
    'count_projects': len(selected),
    'projects': selected
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_zOxJAXyiUvuRoRPWatEiq5lx': 'file_storage/call_zOxJAXyiUvuRoRPWatEiq5lx.json', 'var_call_0GxLFGimWWtyZ5EaoIHD7wLd': 'file_storage/call_0GxLFGimWWtyZ5EaoIHD7wLd.json', 'var_call_fWleDfLyPaPnAG17iseqd9Gk': {'test': True}}

exec(code, env_args)
