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
        # If tc is not directly convertible, attempt float then int
        try:
            citation_map[title] = int(float(tc))
        except Exception:
            citation_map[title] = None

# Helper to extract year from text
YEAR_MIN = 1990
YEAR_MAX = 2030

def extract_year(text):
    # Try Copyright year first
    m = re.search(r"(?i)copyright\s+(\d{4})", text)
    if m:
        y = int(m.group(1))
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    # Search in the first 2500 characters for a 4-digit year
    head = text[:2500]
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", head)
    for ystr in years:
        y = int(ystr)
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    # Fallback: search entire text for a year near venue patterns
    m2 = re.search(r"(?i)(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[^\n]{0,200}?(19\d{2}|20\d{2})", text)
    if m2:
        y = int(m2.group(2))
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    return None

# Helper to check empirical contribution

def has_empirical_contribution(text):
    txt_lower = text.lower()
    # Search for explicit contribution lines
    # Capture after 'contribution' or 'contributions' followed by ':' or '-' or 'is'
    m = re.search(r"(?is)(contribution[s]?\s*(?:\:|\-|is)\s*)(.+?)\n", text)
    if m:
        contrib_line = m.group(2).strip().lower()
        # Split by common delimiters
        parts = re.split(r"[,;|/]\s*", contrib_line)
        parts = [p.strip() for p in parts if p.strip()]
        # Also split by 'and'
        expanded = []
        for p in parts:
            expanded.extend([s.strip() for s in re.split(r"\band\b", p)])
        parts = [p for p in expanded if p]
        # Normalize
        parts_norm = [re.sub(r"[^a-z ]", "", p) for p in parts]
        parts_norm = [p.strip() for p in parts_norm if p.strip()]
        if any('empirical' == p or 'empirical' in p.split() for p in parts_norm):
            return True
    # Fallback: search anywhere for the word empirical as standalone
    if re.search(r"\bempirical\b", txt_lower):
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
    if year is None:
        continue
    if year <= 2016:
        continue
    if not has_empirical_contribution(text):
        continue
    total_citations = citation_map.get(title)
    if total_citations is None:
        # If no direct match, try relaxed matching: strip extra quotes and spaces
        alt = title.strip().strip('"')
        total_citations = citation_map.get(alt)
    if total_citations is None:
        # Skip if citations unavailable
        continue
    results.append({'title': title, 'total_citations': total_citations, 'year': year})

# Sort by total citations descending, then title
results.sort(key=lambda x: (-x['total_citations'], x['title']))

# Prepare final output without year as not requested
final_out = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

print("__RESULT__:")
print(json.dumps(final_out))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json'}

exec(code, env_args)
