code = """import json, re

# Load the large results from the stored file paths
with open(var_call_VwM8mU5sM7MmoDrEaMaPTIDF, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_szHqXJAEi5xjoAPcU8IdvnIq, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Parse design projects from civic_docs texts
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    header = 'Capital Improvement Projects (Design)'
    if header in text:
        start = text.find(header) + len(header)
        # find next section header after start
        # possible next headers
        candidates = ['Capital Improvement Projects (Construction)',
                      'Capital Improvement Projects (Not Started)',
                      'Capital Improvement Projects (Design)']
        end = None
        for c in candidates:
            idx = text.find(c, start)
            if idx != -1:
                if end is None or idx < end:
                    end = idx
        if end is None:
            # fallback: try to find 'Capital Improvement Projects' next occurrence
            idx = text.find('Capital Improvement Projects', start)
            if idx != -1:
                end = idx
        if end is None:
            end = len(text)
        segment = text[start:end]
        # split into lines and pick probable project name lines
        lines = [ln.strip() for ln in segment.splitlines()]
        for i, ln in enumerate(lines):
            if not ln:
                continue
            # skip lines that are clearly part of updates or labels
            low = ln.lower()
            if low.startswith('(cid') or 'updates' in low or 'project schedule' in low or low.startswith('page'):
                continue
            if ':' in ln and len(ln.split(':',1)[0].split())>0:
                # likely a label like "Updates:" or "Project Schedule:" or "Subject:"; skip
                # but many project names contain ':'? unlikely
                # ensure line is not short label
                # we'll skip lines where colon is followed by non-empty content in same line
                parts = ln.split(':')
                if len(parts[0].split()) <= 3:
                    continue
            # heuristic: project names are not long paragraphs
            if len(ln) > 200:
                continue
            # also skip lines that look like sentences (contain multiple periods)
            if ln.endswith('.') and len(ln.split())>5:
                continue
            # Add the line as project name
            design_projects.add(ln)

# Normalize whitespace in project names
design_projects = set(p.strip() for p in design_projects if p.strip())

# Build funding sums per project
funding_sums = {}
for rec in funding_records:
    name = rec.get('Project_Name')
    amt = rec.get('Amount')
    # clean amount
    try:
        if isinstance(amt, str):
            clean = amt.replace(',', '').strip()
            val = int(clean)
        else:
            val = int(amt)
    except:
        try:
            val = int(float(amt))
        except:
            val = 0
    funding_sums[name] = funding_sums.get(name, 0) + val

# Find design capital projects with funding > 50000
matched = []
for p in sorted(design_projects):
    total = funding_sums.get(p, 0)
    if total > 50000:
        matched.append({'Project_Name': p, 'Total_Funding': total})

result = {'count': len(matched), 'projects': matched}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NQuAGWCrCFepMbFk65zP0gQA': ['civic_docs'], 'var_call_dNNS6EpWeELr9r5y9awC9kjt': ['Funding'], 'var_call_szHqXJAEi5xjoAPcU8IdvnIq': 'file_storage/call_szHqXJAEi5xjoAPcU8IdvnIq.json', 'var_call_VwM8mU5sM7MmoDrEaMaPTIDF': 'file_storage/call_VwM8mU5sM7MmoDrEaMaPTIDF.json'}

exec(code, env_args)
