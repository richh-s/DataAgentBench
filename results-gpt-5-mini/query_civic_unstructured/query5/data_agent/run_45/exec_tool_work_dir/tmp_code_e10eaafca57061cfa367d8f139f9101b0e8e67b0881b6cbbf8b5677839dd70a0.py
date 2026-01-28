code = """import json, re

# Load previous tool results (they may be file paths or in-memory lists)
funding_data = var_call_BZc6s5TsUUW8XsKVJyVqw2h6
civic_docs = var_call_TQ1LaBnxQrv4Og9TkjtQVt4F

def load_if_path(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

funding = load_if_path(funding_data)
docs = load_if_path(civic_docs)

# Disaster-related keywords to detect in funding project names
disaster_kw = ['fema', 'caloes', 'caljpia', 'disaster', 'emergency', 'fire', 'fema/', 'fema)']

candidates = [r for r in funding if any(kw in r['Project_Name'].lower() for kw in disaster_kw)]

started_projects = []

for r in candidates:
    name = r['Project_Name']
    try:
        amount = int(r['Amount'])
    except:
        # skip non-numeric amounts
        continue
    found_start = False
    lname = name.lower()
    for doc in docs:
        text = doc.get('text', '')
        low = text.lower()
        # find occurrences of the project name or its base (strip parentheses content)
        patterns = [re.escape(name.lower())]
        # also try base name without parentheses suffixes
        base_name = re.sub(r"\s*\([^)]*\)", "", name).strip().lower()
        if base_name and base_name != name.lower():
            patterns.append(re.escape(base_name))
        # search for any pattern
        for pat in patterns:
            for m in re.finditer(pat, low):
                span_start = max(0, m.start()-400)
                span_end = min(len(low), m.end()+400)
                snippet = low[span_start:span_end]
                if '2022' in snippet:
                    # Look for indicators that imply start in 2022
                    indicators = ['begin construction', 'begin:', 'advertise:', 'advertise', 'begin construction:', 'begin', 'start', 'started', 'start construction', 'construction was completed', 'construction was completed, november 2022', 'construction was completed, november 2022']
                    if any(ind in snippet for ind in indicators):
                        # Ensure that if the indicator is 'construction was completed' we still accept since project was active in 2022
                        found_start = True
                        break
            if found_start:
                break
        if found_start:
            break
    if found_start:
        started_projects.append({'Project_Name': name, 'Amount': amount})

total = sum(p['Amount'] for p in started_projects)

result = {'total': total, 'projects': started_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8dxjntUjIkLSoFYAAkgEchkf': ['civic_docs'], 'var_call_pHTQZq5ul1MEfN3ptLYxb2Ig': ['Funding'], 'var_call_BZc6s5TsUUW8XsKVJyVqw2h6': 'file_storage/call_BZc6s5TsUUW8XsKVJyVqw2h6.json', 'var_call_TQ1LaBnxQrv4Og9TkjtQVt4F': 'file_storage/call_TQ1LaBnxQrv4Og9TkjtQVt4F.json'}

exec(code, env_args)
