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

# Year extraction patterns
venue_words = "(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)"
pattern_venue_year4 = re.compile(r"(?i)" + venue_words + r"[^\n]{0,200}?(19\d{2}|20\d{2})")
pattern_venue_year2 = re.compile(r"(?i)" + venue_words + r"[^\n]{0,200}?[\'\u2019](\d{2})")
pattern_month_year = re.compile(r"(?i)(January|February|March|April|May|June|July|August|September|October|November|December)\s+(19\d{2}|20\d{2})")
pattern_copyright = re.compile(r"(?i)(copyright|\u00a9|\(c\))\s*(19\d{2}|20\d{2})")
pattern_any_year = re.compile(r"\b(19\d{2}|20\d{2})\b")

YEAR_MIN = 1990
YEAR_MAX = 2030


def extract_year(text):
    head = text[:5000]
    # Try copyright
    m = pattern_copyright.search(head)
    if m:
        y = int(m.group(2))
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    # Try venue with 4-digit year
    m = pattern_venue_year4.search(head)
    if m:
        y = int(m.group(2))
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    # Try venue with 2-digit year like CHI '17
    m = pattern_venue_year2.search(head)
    if m:
        yy = int(m.group(2))
        y = 2000 + yy if yy <= 30 else 1900 + yy
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    # Try month followed by year
    m = pattern_month_year.search(head)
    if m:
        y = int(m.group(2))
        if YEAR_MIN <= y <= YEAR_MAX:
            return y
    # Fallback: take the largest year in the head between 2000 and 2030
    years = [int(s) for s in pattern_any_year.findall(head)]
    years = [y for y in years if YEAR_MIN <= y <= YEAR_MAX]
    if years:
        # Heuristic: use max to avoid picking old reference years
        y = max(years)
        return y
    return None


def has_empirical(text, filename):
    tl = text.lower()
    fl = filename.lower()
    if 'empirical' in tl or 'empirical' in fl:
        return True
    # Contributions line
    m = re.search(r"(?is)contribution[s]?\s*(?:\:|\-|is)\s*([^\n]+)", text)
    if m and ('empirical' in m.group(1).lower()):
        return True
    # Common phrasing
    if re.search(r"\bempirical study|empirical evaluation|empirical findings|empirical evidence\b", tl):
        return True
    return False

# Collect candidates
candidates = []
for doc in paper_docs:
    filename = doc.get('filename') or ''
    text = doc.get('text') or ''
    if not filename or not text:
        continue
    title = filename.strip()
    if title.lower().endswith('.txt'):
        title = title[:-4]
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    if not has_empirical(text, filename):
        continue
    total_citations = citation_map.get(title)
    if total_citations is None:
        alt = title.strip().strip('"')
        total_citations = citation_map.get(alt)
    if total_citations is None:
        # case-insensitive exact match
        for k, v in citation_map.items():
            if isinstance(k, str) and k.lower() == title.lower():
                total_citations = v
                break
    if total_citations is None:
        continue
    candidates.append({'title': title, 'total_citations': total_citations})

# Sort by citations desc then title
candidates.sort(key=lambda x: (-x['total_citations'], x['title']))

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': [], 'var_call_lk7wSCfnHF8Qhr71426NHQZw': []}

exec(code, env_args)
