code = """import json, re
import pandas as pd

# Load civic docs (may be file)
cd = var_call_gsbYlFUmFtwBGaBGpXKYjgoA
if isinstance(cd, str):
    with open(cd, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = cd

# Load funded project names > 50k
fp = var_call_NvAkBh0AB6whaps5nn2niXAn
if isinstance(fp, str):
    with open(fp, 'r', encoding='utf-8') as f:
        funded = json.load(f)
else:
    funded = fp
funded_names = [r['Project_Name'] for r in funded if r.get('Project_Name')]

# Build big text corpus
texts = []
for d in civic_docs:
    t = d.get('text')
    if t:
        texts.append(t)
corpus = "\n".join(texts)

# Heuristic: consider a funded project 'design status' if it appears under a heading containing '(Design)'
# In these agenda reports, section: 'Capital Improvement Projects (Design)' then lists project names line-by-line.
# We'll mark design_names if exact line match appears after that heading within same document.

def extract_design_projects(text):
    design_set = set()
    # find blocks after 'Capital Improvement Projects (Design)' or 'Disaster Recovery Projects (Design)'
    pattern = re.compile(r"(?:Capital Improvement Projects|Disaster Recovery Projects)\s*\(Design\)(.*?)(?:\n\s*(?:Capital Improvement Projects|Disaster Recovery Projects)\s*\(|\Z)", re.IGNORECASE|re.DOTALL)
    for m in pattern.finditer(text):
        block = m.group(1)
        # project names often appear as standalone lines (not bullet lines). capture lines with letters/numbers and not too long
        for line in block.splitlines():
            ln = line.strip()
            if not ln:
                continue
            if re.search(r"^(?:\(cid|Page\s+\d+|Agenda Item|Updates|Project Schedule|Estimated Schedule|Complete Design|Advertise|Begin Construction)\b", ln, re.IGNORECASE):
                continue
            # plausible project name: contains letters and is not a sentence
            if len(ln) > 3 and len(ln) < 120 and re.search(r"[A-Za-z]", ln) and not ln.endswith(':'):
                # exclude obvious non-names
                if ln.lower() in {'discussion','recommended action'}:
                    continue
                design_set.add(ln)
    return design_set

# Extract design projects from each doc and union
all_design = set()
for d in civic_docs:
    t = d.get('text','')
    if t:
        all_design |= extract_design_projects(t)

# Now count funded project names that are exactly in all_design
funded_design = [name for name in funded_names if name in all_design]

result = {
    "count": int(len(set(funded_design)))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WdBEy05jPeQ4xShF7NNuqxZ2': [{'cnt': '276'}], 'var_call_gsbYlFUmFtwBGaBGpXKYjgoA': 'file_storage/call_gsbYlFUmFtwBGaBGpXKYjgoA.json', 'var_call_NvAkBh0AB6whaps5nn2niXAn': 'file_storage/call_NvAkBh0AB6whaps5nn2niXAn.json'}

exec(code, env_args)
