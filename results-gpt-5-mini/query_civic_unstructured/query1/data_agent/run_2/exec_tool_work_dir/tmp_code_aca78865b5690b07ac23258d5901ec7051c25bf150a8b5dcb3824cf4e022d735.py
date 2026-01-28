code = """import json
# Load files
with open(var_call_df8qViYTCLLtXU81Hgz3TO1e, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_jpv42uLhPUQHHm66rydnByEb, 'r') as f:
    funding_records = json.load(f)

# filter funding > 50000
funding_filtered = [r for r in funding_records if int(r.get('Amount', 0)) > 50000]

# helper clean function without regex
def simple_clean(s):
    if s is None:
        return ''
    s = s.lower()
    # remove parenthetical suffix
    if '(' in s:
        s = s.split('(')[0]
    # remove common words
    for w in ['project','projects','improvements','repair','repairs','infrastructure','phase','design','construction',':']:
        s = s.replace(w, ' ')
    # keep alphanumerics and spaces
    s2 = []
    for ch in s:
        if ch.isalnum() or ch.isspace():
            s2.append(ch)
        else:
            s2.append(' ')
    s = ''.join(s2)
    s = ' '.join(s.split())
    return s

# extract design sections and candidate titles
design_titles = set()
marker = 'capital improvement projects (design)'
for doc in civic_docs:
    text = doc.get('text','')
    lower = text.lower()
    i = lower.find(marker)
    if i == -1:
        continue
    # find end
    end1 = lower.find('capital improvement projects (construction)', i+1)
    end2 = lower.find('capital improvement projects (not started)', i+1)
    ends = [e for e in [end1,end2] if e != -1]
    end = min(ends) if ends else None
    section = text[i:end] if end else text[i:]
    # split into lines
    for line in section.splitlines():
        s = line.strip()
        if not s:
            continue
        ls = s.lower()
        # filters
        if any(k in ls for k in ['updates', 'project schedule', 'page', 'agenda', 'item', 'recommended action', 'discussion']):
            continue
        if ls.startswith('capital improvement'):
            continue
        if len(s) < 5 or len(s) > 120:
            continue
        if ':' in s:
            # include sometimes but skip if looks like sentence
            if s.endswith(':') or s.count(':')>1:
                continue
        if s.startswith('('):
            continue
        # likely a title if it contains letters
        if any(c.isalpha() for c in s):
            design_titles.add(s)

# clean design titles
clean_design = {t: simple_clean(t) for t in design_titles}

# clean funding names
funding_names = [r['Project_Name'] for r in funding_filtered]
clean_funding = {n: simple_clean(n) for n in funding_names}

# match: if cleaned funding contains cleaned design or vice versa or share tokens
matched = []
for fname, fclean in clean_funding.items():
    for dtitle, dclean in clean_design.items():
        if not fclean or not dclean:
            continue
        if fclean in dclean or dclean in fclean:
            amt = int([r for r in funding_filtered if r['Project_Name']==fname][0]['Amount'])
            matched.append({'Funding_Project': fname, 'Matched_Design_Title': dtitle, 'Amount': amt})
            break
        # token overlap
        fset = set(fclean.split())
        dset = set(dclean.split())
        if fset and dset and len(fset & dset) >= 2:
            amt = int([r for r in funding_filtered if r['Project_Name']==fname][0]['Amount'])
            matched.append({'Funding_Project': fname, 'Matched_Design_Title': dtitle, 'Amount': amt})
            break

# deduplicate
unique = {m['Funding_Project']: m for m in matched}
count = len(unique)

result = {'count': count, 'matched_projects': list(unique.values()), 'design_titles': list(design_titles)[:50]}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cpU66Y0nmO07pRNq09LTN6Bj': ['civic_docs'], 'var_call_jVRqXM2AtLoY3dT6tx43Xuuv': ['Funding'], 'var_call_df8qViYTCLLtXU81Hgz3TO1e': 'file_storage/call_df8qViYTCLLtXU81Hgz3TO1e.json', 'var_call_jpv42uLhPUQHHm66rydnByEb': 'file_storage/call_jpv42uLhPUQHHm66rydnByEb.json'}

exec(code, env_args)
