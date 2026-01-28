code = """import json

# Load the query results from provided storage file paths
with open(var_call_bL3GaMT9aRuk5IYztuJtmf6B, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_x7aqU6vz0ZsKaLH4mtwjbPXb, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build funding lookup list
funding_list = []
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        amt_int = int(amt)
    except Exception:
        try:
            amt_int = int(float(amt))
        except Exception:
            amt_int = 0
    funding_list.append({'name': name, 'amount': amt_int})

# Helper to check valid candidate project name line
def is_valid_candidate(line):
    if not line:
        return False
    s = line.strip()
    if len(s) < 3 or len(s) > 120:
        return False
    if s.endswith(':'):
        return False
    low = s.lower()
    # exclude common headings
    for bad in ['project schedule', 'updates', 'project description', 'agenda', 'page', 'complete design', 'capital improvement projects', 'disaster projects', 'project schedule', 'estimated schedule']:
        if bad in low:
            return False
    if low.isupper() and len(s.split()) < 4:
        return False
    return True

extracted = {}
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        # look for lines indicating start in spring 2022 within a small window
        if ('begin construction' in low or 'begin design' in low or 'begin construction:' in low or 'begin design:' in low or 'begin construction' in low) and 'spring' in low:
            # ensure 2022 appears in nearby context (within +/-3 lines)
            window = '\n'.join(lines[max(0, i-3): min(len(lines), i+4)]).lower()
            if '2022' not in window:
                continue
            # find project name by searching backwards
            proj = None
            for j in range(i-1, max(-1, i-13), -1):
                cand = lines[j].strip()
                if is_valid_candidate(cand):
                    proj = cand
                    break
            if not proj:
                for j in range(i-1, max(-1, i-21), -1):
                    cand = lines[j].strip()
                    if cand and len(cand.split()) <= 8:
                        proj = cand
                        break
            if proj:
                norm = ' '.join(proj.split())
                extracted[norm] = extracted.get(norm, 0) + 1

# Convert extracted keys to sorted list
extracted_projects = sorted(extracted.keys())

# Match funding
project_funding = []
for proj in extracted_projects:
    total = 0
    matched_entries = []
    proj_low = proj.lower()
    # exact match
    for fr in funding_list:
        if fr['name'] and fr['name'].strip().lower() == proj_low:
            total += fr['amount']
            matched_entries.append(fr['name'])
    # substring match if no exact
    if total == 0:
        for fr in funding_list:
            if fr['name'] and (proj_low in fr['name'].lower() or fr['name'].lower() in proj_low):
                total += fr['amount']
                matched_entries.append(fr['name'])
    project_funding.append({'name': proj, 'funding': total, 'matched_funding_entries': matched_entries})

total_projects = len(project_funding)
total_funding = sum(p['funding'] for p in project_funding)

result = {
    'project_count': total_projects,
    'total_funding': total_funding,
    'projects': project_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_MujWVKL2rzsnCnBkRhI5jdNc': ['civic_docs'], 'var_call_CkJufZ8OKzfyEKZaSzfjxgyj': ['Funding'], 'var_call_bL3GaMT9aRuk5IYztuJtmf6B': 'file_storage/call_bL3GaMT9aRuk5IYztuJtmf6B.json', 'var_call_x7aqU6vz0ZsKaLH4mtwjbPXb': 'file_storage/call_x7aqU6vz0ZsKaLH4mtwjbPXb.json'}

exec(code, env_args)
