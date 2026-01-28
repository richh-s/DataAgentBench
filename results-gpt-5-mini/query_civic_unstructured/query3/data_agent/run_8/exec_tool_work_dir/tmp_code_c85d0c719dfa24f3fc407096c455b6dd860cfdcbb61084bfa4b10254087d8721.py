code = """import json

# Load source files from earlier query_db results
funding_path = var_call_U60WqxOGdjsbcqS6PF9PWbjF
docs_path = var_call_8vBnfmWWXT7qozNkwSfsNVHc

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# helper status inference
def infer_status_from_context(ctx):
    c = ctx.lower()
    if any(k in c for k in ['construction was completed', 'notice of completion', 'complete construction', 'completed']):
        return 'completed'
    if any(k in c for k in ['begin construction', 'begin construction:', 'begin construction', 'under construction']):
        return 'design'
    if any(k in c for k in ['complete design', 'plans are being finalized', 'final design', 'design']):
        return 'design'
    if any(k in c for k in ['not started', 'identified', 'awaiting', 'pending', 'preliminary design', 'to be discussed']):
        return 'not started'
    return None

keywords = ['fema', 'emergency', 'outdoor warning', 'sirens', 'caloes']
related = {}

for rec in funding:
    pname = rec.get('Project_Name','')
    pname_low = pname.lower()
    is_related = False
    status = None

    # check name for keywords
    for k in keywords:
        if k in pname_low:
            is_related = True
            break

    # check docs for mentions
    for d in docs:
        txt = d.get('text','')
        txt_low = txt.lower()
        if pname_low and pname_low in txt_low:
            # if doc mentions fema/emergency
            if any(k in txt_low for k in keywords):
                is_related = True
            # infer status from context
            idx = txt_low.find(pname_low)
            start = max(0, idx-300)
            end = min(len(txt_low), idx+300)
            ctx = txt_low[start:end]
            s = infer_status_from_context(ctx)
            if s:
                status = s
    if is_related:
        # ensure amount is int
        try:
            amt = int(rec.get('Amount',0))
        except:
            try:
                amt = int(float(rec.get('Amount',0)))
            except:
                amt = 0
        related[pname] = {
            'Project_Name': pname,
            'Funding_Source': rec.get('Funding_Source',''),
            'Amount': amt,
            'Status': status or 'unknown'
        }

# Also include projects that appear in docs near keywords even if funding name didn't match earlier
for d in docs:
    txt_low = d.get('text','').lower()
    if any(k in txt_low for k in ['fema', 'emergency', 'caloes']):
        # try to find capitalized project-like lines (naive): lines with title case and words
        lines = d.get('text','').split('\n')
        for line in lines:
            line_stripped = line.strip()
            if not line_stripped:
                continue
            # if line is short and contains capitalized words, consider as project candidate
            if 3 <= len(line_stripped) <= 120 and any(ch.isupper() for ch in line_stripped):
                # check if this project has funding record
                for rec in funding:
                    if rec.get('Project_Name','').lower() in line_stripped.lower():
                        pname = rec.get('Project_Name')
                        if pname not in related:
                            try:
                                amt = int(rec.get('Amount',0))
                            except:
                                amt = 0
                            related[pname] = {
                                'Project_Name': pname,
                                'Funding_Source': rec.get('Funding_Source',''),
                                'Amount': amt,
                                'Status': 'unknown'
                            }

# Build sorted list
result = list(related.values())
result.sort(key=lambda x: x['Project_Name'])

# Build plain-text table lines
lines = []
lines.append('Project Name | Funding Source | Amount | Status')
for r in result:
    name = r['Project_Name']
    src = r['Funding_Source']
    amt = r['Amount']
    status = r['Status']
    line = "{} | {} | ${:,} | {}".format(name, src, amt, status)
    lines.append(line)

answer = '\n'.join(lines)

print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_8vBnfmWWXT7qozNkwSfsNVHc': 'file_storage/call_8vBnfmWWXT7qozNkwSfsNVHc.json', 'var_call_U60WqxOGdjsbcqS6PF9PWbjF': 'file_storage/call_U60WqxOGdjsbcqS6PF9PWbjF.json', 'var_call_LjDjToKzxMRjHcG573Em5PnB': 'file_storage/call_LjDjToKzxMRjHcG573Em5PnB.json'}

exec(code, env_args)
