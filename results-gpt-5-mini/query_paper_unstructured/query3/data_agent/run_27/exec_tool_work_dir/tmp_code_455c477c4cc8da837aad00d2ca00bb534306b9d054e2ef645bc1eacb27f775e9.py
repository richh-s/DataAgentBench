code = """import json
import re
from pathlib import Path

# Load data from storage file paths
with open(var_call_2adNILeGBA9O9XRguYGkM96L, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
with open(var_call_Az0muYD0sj3rj7XCLmRhOsuu, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Helper to extract title from filename
def title_from_filename(fn):
    if not fn:
        return None
    return fn.rstrip().rsplit('.txt', 1)[0].strip()

# Helper to extract first year (between 1950 and 2026) from text
year_re = re.compile(r"\b(19|20)\d{2}\b")

def extract_year(text):
    if not text:
        return None
    m = year_re.search(text)
    if m:
        y = int(m.group(0))
        if 1950 <= y <= 2026:
            return y
    return None

# Normalize title for matching
def normalize_title(t):
    if t is None:
        return None
    t2 = t.strip()
    # remove surrounding quotes if exist
    if (t2.startswith('"') and t2.endswith('"')) or (t2.startswith("'") and t2.endswith("'")):
        t2 = t2[1:-1].strip()
    return re.sub(r"\s+", " ", t2).lower()

# Build citations dict: normalized title -> total_citations (int)
cit_map = {}
for rec in citations:
    raw_title = rec.get('title')
    if raw_title is None:
        continue
    norm = normalize_title(raw_title)
    # convert citation count to int
    try:
        cnt = int(rec.get('total_citations'))
    except Exception:
        try:
            cnt = int(rec.get('citation_count', 0))
        except Exception:
            cnt = 0
    cit_map[norm] = cnt

# Process papers: filter for 'empirical' in text and year > 2016
results = []
for doc in paper_docs:
    fn = doc.get('filename')
    text = doc.get('text', '')
    title = title_from_filename(fn)
    year = extract_year(text)
    if title is None or year is None:
        continue
    if year <= 2016:
        continue
    if 'empirical' in text.lower():
        norm = normalize_title(title)
        total_cites = cit_map.get(norm, 0)
        results.append({'title': title, 'total_citations': total_cites, 'year': year})

# Sort results by total_citations descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)
# Prepare output: only title and total_citations
out = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results_sorted]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_2adNILeGBA9O9XRguYGkM96L': 'file_storage/call_2adNILeGBA9O9XRguYGkM96L.json', 'var_call_Az0muYD0sj3rj7XCLmRhOsuu': 'file_storage/call_Az0muYD0sj3rj7XCLmRhOsuu.json'}

exec(code, env_args)
