code = """import json, re

# Load MongoDB paper documents
with open(var_call_WPw67wgXaskTYVaZBay2hrci, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Load aggregated citation totals
with open(var_call_1ntqvKIgCKBFjh2PBN0ocFX8, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build mapping from title to total citations (int)
citation_map = {}
for rec in citations:
    title = rec.get('title')
    tc = rec.get('total_citations')
    try:
        citation_map[title] = int(tc)
    except Exception:
        try:
            citation_map[title] = int(float(tc))
        except Exception:
            citation_map[title] = None

YEAR_MIN = 1990
YEAR_MAX = 2030

venue_pattern = re.compile(r"(?i)(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[^\n]{0,200}?(19\d{2}|20\d{2})")
copyright_pattern = re.compile(r"(?i)(?:copyright|\u00a9|\(c\))\s*(19\d{2}|20\d{2})")
header_year2_pattern = re.compile(r"(?i)(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[^\n]{0,200}?['\u2019](\d{2})")


def extract_year(text):
    head = text[:4000]
    # Try Copyright first
    m = copyright_pattern.search(head)
    if m:
        y = int(m.group(1))
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    # Try venue with explicit 4-digit year
    m = venue_pattern.search(head)
    if m:
        y = int(m.group(2))
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    # Try venue with two-digit year like '18 or ’18
    m = header_year2_pattern.search(head)
    if m:
        yy = int(m.group(2))
        y = 2000 + yy if yy <= 30 else 1900 + yy
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    # Fallback: any 4-digit year near top that is >= 2000
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", head)
    for ystr in years:
        y = int(ystr)
        if YEAR_MIN <= y <= YEAR_MAX and y >= 2000:
            return y
    return None


def has_empirical_contribution(text, filename):
    tl = text.lower()
    fl = filename.lower()
    if 'empirical' in tl or 'empirical' in fl:
        return True
    # Also check for a contributions list mentioning empirical
    m = re.search(r"(?is)contribution[s]?\s*(?:\:|\-|is)\s*([^\n]+)", text)
    if m:
        contrib_line = m.group(1).lower()
        if 'empirical' in contrib_line:
            return True
    return False

results = []
for doc in paper_docs:
    filename = doc.get('filename')
    text = doc.get('text') or ''
    if not filename or not text:
        continue
    # Title from filename without .txt
    title = filename.strip()
    if title.lower().endswith('.txt'):
        title = title[:-4]
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    if not has_empirical_contribution(text, filename):
        continue
    total_citations = citation_map.get(title)
    if total_citations is None:
        alt = title.strip().strip('"')
        total_citations = citation_map.get(alt)
    if total_citations is None:
        continue
    results.append({'title': title, 'total_citations': total_citations})

results.sort(key=lambda x: (-x['total_citations'], x['title']))

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': []}

exec(code, env_args)
