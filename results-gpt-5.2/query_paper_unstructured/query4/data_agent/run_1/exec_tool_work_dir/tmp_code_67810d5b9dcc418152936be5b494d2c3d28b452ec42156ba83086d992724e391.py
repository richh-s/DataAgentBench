code = """import json, re
import pandas as pd

# load mongo docs (subset) that likely include year info
path = var_call_uVaBQiXCLJw7TGNKKOOfZnPM
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# heuristic: physical activity domain if text contains phrase
pa_docs = []
for d in docs:
    txt = d.get('text','') or ''
    if re.search(r'physical activity', txt, flags=re.IGNORECASE):
        pa_docs.append(d)

# determine publication year by searching for venue lines like "CHI 2016" etc.
venue_year_patterns = [
    r'\bCHI\s+2016\b', r'\bUbiComp\s+2016\b', r'\bCSCW\s+2016\b', r'\bDIS\s+2016\b',
    r'\bPervasiveHealth\s+2016\b', r'\bIUI\s+2016\b', r'\bWWW\s+2016\b', r'\bTEI\s+2016\b',
    r'\bOzCHI\s+2016\b', r'\bAH\s+2016\b'
]
compiled = [re.compile(p, re.IGNORECASE) for p in venue_year_patterns]

def is_pub_2016(text):
    for cp in compiled:
        if cp.search(text):
            return True
    # fallback: look for copyright year 2016 with ACM/IEEE; may be noisy
    if re.search(r'\bCopyright\b.*\b2016\b', text, flags=re.IGNORECASE|re.DOTALL):
        return True
    if re.search(r'\b©\s*2016\b', text, flags=re.IGNORECASE):
        return True
    return False

pub2016_titles = []
for d in pa_docs:
    if is_pub_2016(d.get('text','') or ''):
        title = re.sub(r'\.txt$','', d.get('filename',''))
        pub2016_titles.append(title)

pub2016_titles = sorted(set(pub2016_titles))

print('__RESULT__:')
print(json.dumps({'titles': pub2016_titles, 'n_titles': len(pub2016_titles)}))"""

env_args = {'var_call_COmGVncUODl5zdBzJJcc7YJx': 'file_storage/call_COmGVncUODl5zdBzJJcc7YJx.json', 'var_call_uVaBQiXCLJw7TGNKKOOfZnPM': 'file_storage/call_uVaBQiXCLJw7TGNKKOOfZnPM.json'}

exec(code, env_args)
