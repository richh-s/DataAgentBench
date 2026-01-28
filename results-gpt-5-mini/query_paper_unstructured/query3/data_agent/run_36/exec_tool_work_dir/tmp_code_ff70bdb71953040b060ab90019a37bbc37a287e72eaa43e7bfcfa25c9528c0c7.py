code = """import json, re
# Load data from storage file paths
path_papers = var_call_3eKiVvtGerjhPLpQu1j0iLjA
path_citations = var_call_EyoMZl1uyfN4f9f0goZKAlMI
with open(path_papers, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(path_citations, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# Build citations map
cit_map = {}
for r in citations:
    title = r.get('title')
    tc = r.get('total_citations')
    try:
        val = int(tc)
    except:
        try:
            val = int(str(tc).strip())
        except:
            val = 0
    cit_map[title] = val

# Helper to find year
year_re = re.compile(r'(19|20)\d{2}')

def find_year_in_text(text):
    if not text:
        return None
    # try first 500 chars first
    prefix = text[:500]
    m = year_re.search(prefix)
    if m:
        y = int(m.group())
        if 1990 <= y <= 2026:
            return y
    # fallback to full text
    m = year_re.search(text)
    if m:
        y = int(m.group())
        if 1990 <= y <= 2026:
            return y
    return None

results = []
for doc in papers:
    filename = doc.get('filename','')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = doc.get('text','') or ''
    text_lower = text.lower()
    # contribution contains 'empirical'?
    if 'empirical' not in text_lower:
        continue
    year = find_year_in_text(text)
    if year is None:
        continue
    if year > 2016:
        total = cit_map.get(title, 0)
        results.append({'title': title, 'total_citations': total, 'year': year})

# Sort results by total_citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_O5uPwSG9V2J6IaiV1sbs1mk0': ['paper_docs'], 'var_call_3eKiVvtGerjhPLpQu1j0iLjA': 'file_storage/call_3eKiVvtGerjhPLpQu1j0iLjA.json', 'var_call_iTtj361KuZ7bsefcPFPgtwj4': ['Citations', 'sqlite_sequence'], 'var_call_EyoMZl1uyfN4f9f0goZKAlMI': 'file_storage/call_EyoMZl1uyfN4f9f0goZKAlMI.json'}

exec(code, env_args)
