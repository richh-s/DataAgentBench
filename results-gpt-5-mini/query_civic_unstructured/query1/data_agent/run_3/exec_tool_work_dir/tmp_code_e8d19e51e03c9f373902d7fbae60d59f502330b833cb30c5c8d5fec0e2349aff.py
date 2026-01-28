code = """import json
import os

# Load tool results from storage variables
# var_call_F6Rv2iK59dpvmVHWzeQUSQxs and var_call_sVhPCP5IgNUjQ8N9sM9776oS are file paths to JSON files
funding_path = var_call_F6Rv2iK59dpvmVHWzeQUSQxs
civic_path = var_call_sVhPCP5IgNUjQ8N9sM9776oS

with open(funding_path, 'r') as f:
    funding = json.load(f)

with open(civic_path, 'r') as f:
    civic = json.load(f)

# Extract text from civic documents and find projects listed under 'Capital Improvement Projects (Design)'
design_projects = set()
for doc in civic:
    text = doc.get('text','')
    # normalize spacing
    if 'Capital Improvement Projects (Design)' in text:
        start = text.index('Capital Improvement Projects (Design)')
        # find end marker - next major section could be 'Capital Improvement Projects (Construction)' or '(Construction)' or 'Capital Improvement Projects (Not Started)'
        end_markers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']
        end = None
        for m in end_markers:
            if m in text[start:]:
                end = start + text[start:].index(m)
                break
        if end is None:
            # fallback: take next occurrence of 'Capital Improvement Projects' without '(Design)'
            try:
                idx = text.index('Capital Improvement Projects', start+1)
                end = idx
            except ValueError:
                end = len(text)
        segment = text[start:end]
        # split into lines and pick candidate project title lines
        lines = [ln.strip() for ln in segment.splitlines()]
        for i,ln in enumerate(lines):
            if not ln:
                continue
            # skip the header line
            if i==0 and 'Capital Improvement Projects' in ln:
                continue
            # stop if we hit a subheading like 'Updates:' or 'DISCUSSION' etc
            if ln.lower().startswith('discussion') or ln.lower().startswith('subject'):
                continue
            # heuristics: project names are lines that are not starting with '(' and not containing ':' and not all caps words like 'RECOMMENDED ACTION'
            if ln.startswith('('):
                continue
            if ':' in ln:
                continue
            if ln.isupper():
                continue
            # ignore lines that are like 'Updates' or 'Project Schedule'
            if 'Updates' in ln or 'Project Schedule' in ln or 'Project Description' in ln or 'Estimated Schedule' in ln:
                continue
            # ignore lines that look like page markers
            if ln.lower().startswith('page'):
                continue
            # ignore very short lines
            if len(ln) < 5:
                continue
            # also ignore lines that are obviously sentences (contain periods)
            if '.' in ln and not ln.strip().endswith('Project'):
                # but some project names include periods? unlikely
                pass
            # Now accept this as a project name
            # Sometimes lines include leading bullets like '•' or similar; strip
            clean = ln.strip('•\u2022 ').strip()
            # Exclude lines that are words like 'Updates' or 'RECOMMENDED ACTION'
            if any(x in clean for x in ['Updates','Project Schedule','RECOMMENDED ACTION','DISCUSSION','Agenda Item']):
                continue
            # Avoid lines that are sentences containing verbs
            if any(verb in clean for verb in ['is','are','will','working','Plans','Staff','City']):
                # but some names may include 'Park' etc, safe to include if capitalized words
                pass
            # Heuristic: if line contains words like 'Project', 'Improvements', 'Repairs', 'Study', 'Park', 'Walkway', 'Median', 'Drain', 'Skate', 'HVAC'
            keywords = ['Project','Improvements','Repairs','Study','Park','Walkway','Median','Drain','Skate','HVAC','Road','Roadway','Culvert','Retaining','Storm','Trail','Facility','Parking','Playground','Sidewalk','Bridge','Curb','Paver','Irrigation','Biofilter']
            if not any(k in clean for k in keywords):
                # maybe not a project name
                continue
            design_projects.add(clean)

# Also try a simpler approach: find lines between header and first '(cid:' occurrence; many project names are followed by '(cid:190) Updates:' so take lines that precede that
for doc in civic:
    text = doc.get('text','')
    if 'Capital Improvement Projects (Design)' in text:
        seg = text.split('Capital Improvement Projects (Design)',1)[1]
        # find where '(cid:' appears frequently; limit to before 'Capital Improvement Projects (Construction)'
        end_tokens = ['Capital Improvement Projects (Construction)','Capital Improvement Projects (Not Started)']
        for t in end_tokens:
            if t in seg:
                seg = seg.split(t,1)[0]
        parts = seg.split('(cid:')
        # first part may be preface; subsequent parts start with number and then project text; so examine small windows
        # we'll extract lines that are standalone titles by scanning for lines that are title-like
        lines = [ln.strip() for ln in seg.splitlines()]
        for idx,ln in enumerate(lines):
            if not ln:
                continue
            if ln.startswith('(cid:'):
                # previous non-empty line might be project title
                prev = None
                for j in range(idx-1,-1,-1):
                    if lines[j]:
                        prev = lines[j]
                        break
                if prev:
                    clean = prev.strip('•\u2022 ').strip()
                    if any(k in clean for k in keywords):
                        design_projects.add(clean)

# Now load funding data and filter amounts > 50000
funding_over = {}
for rec in funding:
    name = rec.get('Project_Name')
    amt = rec.get('Amount')
    try:
        amt_val = int(str(amt))
    except:
        # try remove non-digits
        import re
        s = re.sub(r"[^0-9]", "", str(amt))
        amt_val = int(s) if s else 0
    if amt_val > 50000:
        funding_over[name] = amt_val

# Join by exact match of project names
matched = []
for pname in sorted(design_projects):
    if pname in funding_over:
        matched.append({'Project_Name': pname, 'Amount': funding_over[pname]})

# Also attempt fuzzy matching: remove suffixes like '(FEMA Project)' etc and compare
import re
fund_keys = list(funding_over.keys())
for pname in sorted(design_projects):
    if any(p['Project_Name']==pname for p in matched):
        continue
    # try fuzzy: compare lowercase alphanumeric
    def normalize(s):
        return re.sub(r'[^a-z0-9]','', s.lower())
    np = normalize(pname)
    for fk in fund_keys:
        if np == normalize(fk) or np in normalize(fk) or normalize(fk) in np:
            matched.append({'Project_Name': pname, 'Amount': funding_over[fk]})
            break

# Unique matched by project name
unique = {m['Project_Name']: m for m in matched}
result = {'count': len(unique), 'projects': list(unique.values())}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_F6Rv2iK59dpvmVHWzeQUSQxs': 'file_storage/call_F6Rv2iK59dpvmVHWzeQUSQxs.json', 'var_call_GcbP1Q650C0FHLYegHbT6UXW': ['civic_docs'], 'var_call_sVhPCP5IgNUjQ8N9sM9776oS': 'file_storage/call_sVhPCP5IgNUjQ8N9sM9776oS.json'}

exec(code, env_args)
