code = """import json, re, pandas as pd

# Load big funding projects (sum > 50000)
path = var_call_KNlruGsOPGg24CQ6PPSpDtEy
with open(path, 'r') as f:
    big_funding = json.load(f)

big_names = {r['Project_Name'] for r in big_funding}

# Load civic docs
docs_path = var_call_ZlZbbukElUCUh5IbgJgVel7p
with open(docs_path, 'r') as f:
    docs = json.load(f)

# Heuristic extraction: look for sections titled "Capital Improvement Projects (Design)"
# then collect subsequent project-name lines until next section heading.

section_start_re = re.compile(r'^\s*Capital Improvement Projects\s*\(Design\)\s*$', re.IGNORECASE)
section_end_re = re.compile(r'^\s*Capital Improvement Projects\s*\((Construction|Not Started)\)\s*$', re.IGNORECASE)
other_end_re = re.compile(r'^\s*Disaster Recovery Projects\b', re.IGNORECASE)

# project line candidates: non-empty, not bullets/updates/schedule/page headers
skip_re = re.compile(r'^(\(cid:|Updates?:|Project (Schedule|Description|Updates?):|Estimated Schedule:|RECOMMENDED ACTION:|DISCUSSION:|Page\s+\d+\s+of\s+\d+|Agenda Item|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|\s*$)', re.IGNORECASE)


def extract_design_projects(text):
    lines = [ln.strip() for ln in text.splitlines()]
    in_section = False
    projs = []
    for ln in lines:
        if not in_section:
            if section_start_re.match(ln):
                in_section = True
            continue
        else:
            if section_end_re.match(ln) or other_end_re.match(ln):
                break
            if skip_re.match(ln):
                continue
            # drop lines that are mostly punctuation or too short
            if len(ln) < 4:
                continue
            # exclude obvious schedule entries
            if re.match(r'^(Complete Design|Advertise|Begin Construction|Final Design)\s*:', ln, re.IGNORECASE):
                continue
            # exclude bullet characters
            ln2 = re.sub(r'^[\u2022\-\*]+\s*', '', ln).strip()
            if not ln2:
                continue
            # Heuristic: project names are Title Case-ish and not ending with ':'
            if ln2.endswith(':'):
                continue
            projs.append(ln2)
    return projs

all_design = set()
for d in docs:
    txt = d.get('text','') or ''
    for p in extract_design_projects(txt):
        all_design.add(p)

# Capital projects with design status AND funding > 50000: intersect with big funding names
intersection = sorted(all_design.intersection(big_names))

result = {
    "count": len(intersection),
    "projects": intersection[:50],
    "projects_list_truncated": len(intersection) > 50
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_RnRpTD8D12Ycfy59oDacOE4E': [{'cnt': '276'}], 'var_call_ZlZbbukElUCUh5IbgJgVel7p': 'file_storage/call_ZlZbbukElUCUh5IbgJgVel7p.json', 'var_call_KNlruGsOPGg24CQ6PPSpDtEy': 'file_storage/call_KNlruGsOPGg24CQ6PPSpDtEy.json'}

exec(code, env_args)
