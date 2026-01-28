code = """import json

# Load data files
with open(var_call_WPw67wgXaskTYVaZBay2hrci, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_1ntqvKIgCKBFjh2PBN0ocFX8, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation map
citation_map = {}
for rec in citations:
    t = rec.get('title')
    tc = rec.get('total_citations')
    try:
        citation_map[t] = int(tc)
    except Exception:
        try:
            citation_map[t] = int(float(tc))
        except Exception:
            citation_map[t] = None

VENUES = ['CHI', 'CSCW', 'Ubicomp', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
YEAR_MIN = 2000
YEAR_MAX = 2030

# Helper functions

def extract_year_from_head(text):
    head = text[:6000]
    lines = head.split('\n')[:80]
    # First pass: lines with venue
    for line in lines:
        low = line.lower()
        if any(v.lower() in low for v in VENUES):
            # Try 4-digit year
            y = None
            num = ''
            for ch in line:
                if ch.isdigit():
                    num += ch
                    if len(num) >= 4:
                        try:
                            val = int(num[-4:])
                            if YEAR_MIN <= val <= YEAR_MAX:
                                y = val
                                break
                        except Exception:
                            pass
                else:
                    num = ''
            if y is not None:
                return y
            # Try two-digit year after apostrophe
            apos_positions = []
            for i, ch in enumerate(line):
                if ch == "'" or ch == '’':
                    apos_positions.append(i)
            for pos in apos_positions:
                if pos + 3 <= len(line):
                    sub = line[pos+1:pos+3]
                    if sub.isdigit():
                        yy = int(sub)
                        y = 2000 + yy if yy <= 30 else 1900 + yy
                        if YEAR_MIN <= y <= YEAR_MAX:
                            return y
    # Second pass: copyright
    for line in lines:
        low = line.lower()
        if 'copyright' in low or '©' in line or '(c)' in low:
            # find 4-digit year in line
            num = ''
            for ch in line:
                if ch.isdigit():
                    num += ch
                    if len(num) >= 4:
                        try:
                            val = int(num[-4:])
                            if YEAR_MIN <= val <= YEAR_MAX:
                                return val
                        except Exception:
                            pass
                else:
                    num = ''
    # Fallback: first 4-digit year in head
    num = ''
    for ch in head:
        if ch.isdigit():
            num += ch
            if len(num) >= 4:
                try:
                    val = int(num[-4:])
                    if YEAR_MIN <= val <= YEAR_MAX:
                        return val
                except Exception:
                    pass
        else:
            num = ''
    return None


def has_empirical(text, filename):
    tl = text.lower()
    fl = filename.lower()
    if 'empirical' in tl or 'empirical' in fl:
        return True
    # Check explicit contributions line
    head = text[:8000]
    lines = head.split('\n')[:150]
    for line in lines:
        low = line.lower()
        if 'contribution' in low:
            if 'empirical' in low:
                return True
    return False

results = []
for doc in docs:
    fn = doc.get('filename') or ''
    text = doc.get('text') or ''
    if not fn or not text:
        continue
    title = fn.strip()
    if title.lower().endswith('.txt'):
        title = title[:-4]
    year = extract_year_from_head(text)
    if year is None or year <= 2016:
        continue
    if not has_empirical(text, fn):
        continue
    tc = citation_map.get(title)
    if tc is None:
        alt = title.strip().strip('"')
        tc = citation_map.get(alt)
    if tc is None:
        # case-insensitive exact match
        for k, v in citation_map.items():
            if isinstance(k, str) and k.lower() == title.lower():
                tc = v
                break
    if tc is None:
        continue
    results.append({'title': title, 'total_citations': tc})

results.sort(key=lambda x: (-x['total_citations'], x['title']))

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_WPw67wgXaskTYVaZBay2hrci': 'file_storage/call_WPw67wgXaskTYVaZBay2hrci.json', 'var_call_1ntqvKIgCKBFjh2PBN0ocFX8': 'file_storage/call_1ntqvKIgCKBFjh2PBN0ocFX8.json', 'var_call_mYMhTkK3uSl7cJInG6UsluoL': [], 'var_call_lk7wSCfnHF8Qhr71426NHQZw': [], 'var_call_B6tTsBXqGYIrbqBYA3iowVR1': [], 'var_call_rHchAtTQ45xNOeRMELsaL42l': []}

exec(code, env_args)
