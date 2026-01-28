code = """import json, re, os

# load docs that likely include 2016 (already filtered by regex) and citations

def load(path_or_list):
    if isinstance(path_or_list, str) and os.path.exists(path_or_list):
        with open(path_or_list,'r',encoding='utf-8') as f:
            return json.load(f)
    return path_or_list

paper_docs = load(var_call_8aDRM5cI4RsJ2JVHuYRA6qBN)
cites = load(var_call_027K08n9PiGCRWzcVGBYGyka)

# Determine physical activity domain using title keywords and text keywords

def pa_domain(title, text):
    t = (title + ' ' + (text[:6000] if text else '')).lower()
    return ('physical activity' in t) or ('activity tracker' in t) or ('fitness tracker' in t) or ('activity tracking' in t)

# Determine publication year from explicit "ACM Reference Format" line: "<year>. <Title>."

def extract_pub_year(text, title):
    if not text:
        return None
    m = re.search(r'ACM Reference Format:\s*.*?\b(19\d{2}|20\d{2})\b\s*\.\s*'+re.escape(title)+r'\b', text, flags=re.IGNORECASE|re.DOTALL)
    if m:
        return int(m.group(1))
    # try generic: first occurrence of year in ACM reference format block
    m2 = re.search(r'ACM Reference Format:.*?\b(19\d{2}|20\d{2})\b', text, flags=re.IGNORECASE|re.DOTALL)
    if m2:
        return int(m2.group(1))
    # try proceedings publication date line
    m3 = re.search(r'Publication date:\s*[^\n]*\b(19\d{2}|20\d{2})\b', text, flags=re.IGNORECASE)
    if m3:
        return int(m3.group(1))
    # try venue year patterns
    m4 = re.search(r'\b(CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|WWW|TEI|OzCHI|PervasiveHealth)\s*(19\d{2}|20\d{2})\b', text)
    if m4:
        return int(m4.group(2))
    return None

papers = []
for d in paper_docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn)
    text = d.get('text','')
    if not pa_domain(title, text):
        continue
    year = extract_pub_year(text, title)
    if year == 2016:
        papers.append(title)

papers = sorted(set(papers))

# total citations across all years
from collections import defaultdict

tot = defaultdict(int)
for r in cites:
    tot[r['title']] += int(r['citation_count'])

out = [{'title': t, 'total_citation_count': tot.get(t,0)} for t in papers]
out = sorted(out, key=lambda x: (-x['total_citation_count'], x['title']))

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_CWXupshSWmsTyUlUGwo0qtk0': 'file_storage/call_CWXupshSWmsTyUlUGwo0qtk0.json', 'var_call_027K08n9PiGCRWzcVGBYGyka': 'file_storage/call_027K08n9PiGCRWzcVGBYGyka.json', 'var_call_8aDRM5cI4RsJ2JVHuYRA6qBN': 'file_storage/call_8aDRM5cI4RsJ2JVHuYRA6qBN.json', 'var_call_ywhIFAt6OZc0Ogmyjd1AmoVF': [], 'var_call_Vy73AKJIEXWsDIzHFebLu6yo': 'file_storage/call_Vy73AKJIEXWsDIzHFebLu6yo.json'}

exec(code, env_args)
