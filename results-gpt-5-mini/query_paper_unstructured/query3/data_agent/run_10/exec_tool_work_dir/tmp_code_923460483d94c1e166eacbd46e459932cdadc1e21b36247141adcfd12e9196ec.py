code = """import json, re

# Load data from previous tool results (file paths)
with open(var_call_ENApJlzPfTnkWOuQUUBkbYER, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_eJzZrc8H0Mtc51YeBib7FZ8k, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation dict mapping title -> total_citations (int)
cit_map = {}
for rec in citations:
    title = rec.get('title')
    # citation value might be string; convert
    try:
        total = int(rec.get('total_citations'))
    except Exception:
        try:
            total = int(rec.get('total_citations', 0))
        except:
            total = 0
    cit_map[title] = total

results = []

def extract_year(text):
    if not text:
        return None
    # find first 4-digit year between 1900 and 2030
    m = re.search(r"\b(19|20)\d{2}\b", text)
    if m:
        try:
            y = int(m.group(0))
            return y
        except:
            return None
    return None

for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    year = extract_year(text)
    # check for 'empirical' contribution by substring in text (case-insensitive)
    is_empirical = 'empirical' in text.lower()
    if year and year > 2016 and is_empirical:
        total_citations = cit_map.get(title, 0)
        results.append({'title': title, 'total_citations': total_citations, 'year': year})

# Sort results by total_citations desc
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Reduce output to title and total_citations only
out = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_D81gzes9XQUPeCBl3ybjvbuv': ['paper_docs'], 'var_call_ENApJlzPfTnkWOuQUUBkbYER': 'file_storage/call_ENApJlzPfTnkWOuQUUBkbYER.json', 'var_call_tayPC6SiL3sKLfNaYl8j56Vk': ['Citations', 'sqlite_sequence'], 'var_call_eJzZrc8H0Mtc51YeBib7FZ8k': 'file_storage/call_eJzZrc8H0Mtc51YeBib7FZ8k.json'}

exec(code, env_args)
