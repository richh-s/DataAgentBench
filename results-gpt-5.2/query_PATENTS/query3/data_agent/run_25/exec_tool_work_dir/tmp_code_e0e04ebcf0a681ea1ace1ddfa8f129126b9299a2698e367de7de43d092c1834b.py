code = """import json, re
import pandas as pd

# Load large result set
path = var_call_Q3MjtjvabKQfHafD8ojtn4yk
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

def parse_patents_info_assignee(pi: str):
    # Try common patterns
    m = re.search(r"owned by ([^.,]+)", pi)
    if m:
        return m.group(1).strip()
    m = re.search(r"is assigned to ([^.,]+)", pi)
    if m:
        return m.group(1).strip()
    m = re.search(r"holds the [A-Z]{2} patent filing .*? is (?:owned by|assigned to) ([^.,]+)", pi)
    if m:
        return m.group(1).strip()
    m = re.search(r"^([^,]+) holds the", pi)
    if m:
        return m.group(1).strip()
    return None

# Build UC set of publication numbers
uc_pubs = set()
for r in recs:
    pi = r.get('Patents_info') or ''
    if 'UNIV CALIFORNIA' in pi:
        m = re.search(r"pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", pi)
        if m:
            uc_pubs.add(m.group(1))
        else:
            m = re.search(r"publication number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)", pi)
            if m:
                uc_pubs.add(m.group(1))

# Find citing publications: any publication whose citation list contains a UC pub
citing_rows = []
for r in recs:
    cit = r.get('citation')
    if not cit or cit == '[]':
        continue
    try:
        cit_list = json.loads(cit)
    except Exception:
        continue
    cited_pubs = {c.get('publication_number') for c in cit_list if isinstance(c, dict)}
    if cited_pubs & uc_pubs:
        assignee = parse_patents_info_assignee(r.get('Patents_info',''))
        if assignee and 'UNIV CALIFORNIA' not in assignee:
            # primary CPC subclasses = codes with first==true; take subclass (group) e.g. F25B21/00 -> F25B21/00? but subclass in CPC is 4-char class + 1-digit subclass letter. However asked primary CPC subclasses; interpret as first CPC codes, then map to subclass symbol (first 4+letter?)
            try:
                cpc_list = json.loads(r.get('cpc') or '[]')
            except Exception:
                cpc_list = []
            primary_codes = [c.get('code') for c in cpc_list if isinstance(c, dict) and c.get('first') is True and c.get('code')]
            primary_codes = list(dict.fromkeys(primary_codes))
            citing_rows.append({'assignee': assignee, 'primary_codes': primary_codes})

# Unique assignee->codes
assignee_to_codes = {}
for row in citing_rows:
    a = row['assignee']
    assignee_to_codes.setdefault(a, set()).update(row['primary_codes'])

# Convert codes to CPC subclass symbols (take part before '/') and trim to subclass level: first 4 chars + 1 letter (e.g., F25B)
# If code like Y02A50/30 => subclass Y02A; F25B21/00 => subclass F25B

def to_subclass(code):
    if not code:
        return None
    main = code.split('/')[0]
    # remove spaces
    main = main.strip()
    # subclass is first 4 plus subclass letter if present as 4th? Actually pattern: section letter +2 digits + subclass letter => 4 chars
    return main[:4]

assignee_to_subclasses = {a: sorted({to_subclass(c) for c in codes if to_subclass(c)}) for a, codes in assignee_to_codes.items()}

# Output subclasses list for querying titles
subclasses = sorted({sc for lst in assignee_to_subclasses.values() for sc in lst})

out = {'assignee_to_subclasses': {a: v for a,v in assignee_to_subclasses.items()}, 'subclasses': subclasses}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_twNJqIxYfLGMb2nepTSusHVV': ['publicationinfo'], 'var_call_A59NZXE0giSlSxSefltXS83H': ['cpc_definition'], 'var_call_XUPCNyIMvQa2wmQCB6AVzYBH': [], 'var_call_RW6XY5YgUpjjwVTOcUDCkcVx': [], 'var_call_Q3MjtjvabKQfHafD8ojtn4yk': 'file_storage/call_Q3MjtjvabKQfHafD8ojtn4yk.json'}

exec(code, env_args)
