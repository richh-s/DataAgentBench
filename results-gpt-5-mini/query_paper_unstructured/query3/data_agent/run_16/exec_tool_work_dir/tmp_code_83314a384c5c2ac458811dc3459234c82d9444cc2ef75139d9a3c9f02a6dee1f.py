code = """import json, re
path = var_call_HWIzGp9Q8Mszq8gzqBmGqkfc
with open(path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# basic stats
total = len(papers)
filenames = [p.get('filename','') for p in papers][:20]

# find years by regex for 4-digit 2000-2029
def extract_years(text):
    return re.findall(r"\b(20[0-2][0-9])\b", text)

found = []
for p in papers:
    filename = p.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = p.get('text','') or ''
    years = extract_years(text)
    has_emp = 'empirical' in text.lower()
    if has_emp and years:
        # take first year
        y = int(years[0])
        if y > 2016:
            found.append({'title': title, 'year': y})

# prepare result
res = {'total_docs_with_empirical': total, 'sample_filenames': filenames, 'matched_after_2016_count': len(found), 'matched_after_2016_sample': found[:50]}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_nRINhIm1ITwxpdsbY9l1GZUf': ['paper_docs'], 'var_call_yCC4E8r7SIzhVgHbHKsaG3oC': ['Citations', 'sqlite_sequence'], 'var_call_HWIzGp9Q8Mszq8gzqBmGqkfc': 'file_storage/call_HWIzGp9Q8Mszq8gzqBmGqkfc.json', 'var_call_3P9GPZkBqpzCNZw1V6MtxuHw': []}

exec(code, env_args)
