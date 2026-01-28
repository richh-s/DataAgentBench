code = """import json, re
# load tool results from storage file paths
with open(var_call_df8qViYTCLLtXU81Hgz3TO1e, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_jpv42uLhPUQHHm66rydnByEb, 'r') as f:
    funding_records = json.load(f)

# Filter funding records Amount > 50000
funding_filtered = [r for r in funding_records if int(r.get('Amount', 0)) > 50000]

# helper normalize
import string
remove_chars = string.punctuation

def clean(s):
    if s is None: return ''
    s = s.lower()
    # remove parenthetical suffixes like (fema...)
    s = re.sub(r"\([^)]*\)", "", s)
    s = ''.join(ch if ch.isalnum() or ch.isspace() else ' ' for ch in s)
    s = re.sub(r'\s+', ' ', s).strip()
    # remove common words
    for w in ['project','projects','improvements','repair','repairs','repairing','infrastructure','phase','project','design','construction','project:']:
        s = re.sub(r'\b'+re.escape(w)+r'\b','', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# extract design sections from civic docs
design_texts = []
for doc in civic_docs:
    text = doc.get('text','')
    lower = text.lower()
    start_marker = 'capital improvement projects (design)'
    si = lower.find(start_marker)
    if si == -1:
        # also try 'capital improvement projects (design)\n' variants
        continue
    # find end marker
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'capital improvement projects (construction)', 'capital improvement projects (not started)']
    ei = -1
    for m in end_markers:
        idx = lower.find(m, si+1)
        if idx != -1:
            ei = idx
            break
    if ei == -1:
        # fallback: look for '\n\ncapital improvement projects' subsequent
        m = re.search(r'capital improvement projects \(', lower[si+1:])
        if m:
            ei = si+1+m.start()
    section = text[si:ei] if ei!=-1 else text[si:]
    design_texts.append(section)

# From design_texts, extract candidate project titles by splitting on double newlines and taking plausible lines
design_titles = set()
for sec in design_texts:
    parts = re.split(r'\n\s*\n', sec)
    for p in parts:
        # take first line as title candidate
        lines = [L.strip() for L in p.splitlines() if L.strip()]
        if not lines: continue
        first = lines[0]
        # exclude headings and short non-title lines
        if len(first) < 5 or len(first) > 200: continue
        if any(k in first.lower() for k in ['updates','project schedule','agenda','page','item','recommended action','discussion']):
            continue
        # exclude lines that are like 'Capital Improvement Projects (Design)'
        if 'capital improvement' in first.lower(): continue
        design_titles.add(first)

# Normalize design titles
clean_design_titles = {title: clean(title) for title in design_titles}

# Normalize funding names
funding_filtered_names = [r['Project_Name'] for r in funding_filtered]
clean_funding = {name: clean(name) for name in funding_filtered_names}

# Matching via token Jaccard or substring
def tokens(s):
    return set(s.split()) if s else set()

matched = []
for fname, fclean in clean_funding.items():
    f_tokens = tokens(fclean)
    matched_flag = False
    for dtitle, dclean in clean_design_titles.items():
        d_tokens = tokens(dclean)
        if not fclean or not dclean:
            continue
        # substring match
        if fclean in dclean or dclean in fclean:
            matched_flag = True
            match_title = dtitle
            break
        # jaccard
        inter = f_tokens & d_tokens
        union = f_tokens | d_tokens
        jacc = (len(inter)/len(union)) if union else 0
        if jacc >= 0.5 or (len(inter) >= max(2, min(len(f_tokens), len(d_tokens))//2)):
            matched_flag = True
            match_title = dtitle
            break
    if matched_flag:
        matched.append({'Funding_Project': fname, 'Matched_Design_Title': match_title, 'Amount': int([r for r in funding_filtered if r['Project_Name']==fname][0]['Amount'])})

# deduplicate by funding project name
unique_matched = {m['Funding_Project']: m for m in matched}
count = len(unique_matched)

result = {'count': count, 'matched_projects': list(unique_matched.values())}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cpU66Y0nmO07pRNq09LTN6Bj': ['civic_docs'], 'var_call_jVRqXM2AtLoY3dT6tx43Xuuv': ['Funding'], 'var_call_df8qViYTCLLtXU81Hgz3TO1e': 'file_storage/call_df8qViYTCLLtXU81Hgz3TO1e.json', 'var_call_jpv42uLhPUQHHm66rydnByEb': 'file_storage/call_jpv42uLhPUQHHm66rydnByEb.json'}

exec(code, env_args)
