code = """import json

# Load files
with open(var_call_ifKTd9m49wjLskHsH8IDbSh4, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_ZK1aX28h8MGo0W1v6MBLI9wZ, 'r') as f:
    funding_rows = json.load(f)

# simple normalization
import string
translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

def normalize(s):
    if s is None:
        return ''
    s2 = s.lower().translate(translator)
    s2 = ' '.join(s2.split())
    return s2

# find project candidate lines near occurrences of 'spring' and '2022'
proj_set = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    L = len(lines)
    for i, line in enumerate(lines):
        low = line.lower()
        if 'spring' in low and '2022' in low:
            # take previous non-empty non-meta line within up to 12 lines above
            name = None
            for j in range(i-1, max(i-13, -1), -1):
                candidate = lines[j].strip()
                if not candidate:
                    continue
                cl = candidate.lower()
                if cl.startswith('(cid:') or 'updates' in cl or 'project schedule' in cl or 'agenda' in cl or cl.startswith('page'):
                    continue
                # Heuristic: line with letters and not very long
                if any(c.isalpha() for c in candidate) and len(candidate) < 200:
                    name = candidate
                    break
            if name:
                proj_set.add(name)
        # also handle cases where 'begin construction' appears nearby and year and spring in window
        if 'begin construction' in low:
            window = ' '.join(lines[max(0,i-3):min(L,i+4)]).lower()
            if 'spring' in window and '2022' in window:
                # find previous project title
                name = None
                for j in range(i-1, max(i-13, -1), -1):
                    candidate = lines[j].strip()
                    if not candidate:
                        continue
                    cl = candidate.lower()
                    if cl.startswith('(cid:') or 'updates' in cl or 'project schedule' in cl or 'agenda' in cl or cl.startswith('page'):
                        continue
                    if any(c.isalpha() for c in candidate) and len(candidate) < 200:
                        name = candidate
                        break
                if name:
                    proj_set.add(name)

# Also search for patterns like 'st: 2022-spring' or 'st: 2022 Spring' in text and take nearby project name
for doc in civic_docs:
    text = doc.get('text','')
    lowtext = text.lower()
    if '2022' in lowtext and 'spring' in lowtext:
        # split into sentences by newlines and look for lines that contain 2022 and spring
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if '2022' in line and 'spring' in line.lower():
                # previous non-empty line
                for j in range(i-1, max(i-13, -1), -1):
                    candidate = lines[j].strip()
                    if not candidate:
                        continue
                    cl = candidate.lower()
                    if cl.startswith('(cid:') or 'updates' in cl or 'project schedule' in cl or 'agenda' in cl or cl.startswith('page'):
                        continue
                    if any(c.isalpha() for c in candidate) and len(candidate) < 200:
                        proj_set.add(candidate)
                        break

# Prepare funding normalization
for r in funding_rows:
    r['norm'] = normalize(r.get('Project_Name',''))

# Match projects
project_funding = {}
for proj in proj_set:
    normp = normalize(proj)
    total = 0
    matched = False
    for r in funding_rows:
        fn = r['norm']
        if normp == fn or normp in fn or fn in normp:
            try:
                amt = int(str(r.get('Amount','0')))
            except:
                # extract digits
                s = ''.join(ch for ch in str(r.get('Amount','0')) if ch.isdigit() or ch=='-')
                try:
                    amt = int(s) if s not in ('','-') else 0
                except:
                    amt = 0
            total += amt
            matched = True
    if matched:
        project_funding[proj] = total

count_projects = len(project_funding)
total_funding = sum(project_funding.values())

out = {"count": count_projects, "total_funding": total_funding, "projects": project_funding}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ifKTd9m49wjLskHsH8IDbSh4': 'file_storage/call_ifKTd9m49wjLskHsH8IDbSh4.json', 'var_call_ZK1aX28h8MGo0W1v6MBLI9wZ': 'file_storage/call_ZK1aX28h8MGo0W1v6MBLI9wZ.json'}

exec(code, env_args)
