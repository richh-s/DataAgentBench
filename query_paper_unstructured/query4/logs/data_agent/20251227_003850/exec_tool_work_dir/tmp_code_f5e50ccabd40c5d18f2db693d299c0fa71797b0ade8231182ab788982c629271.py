code = """import json, re

path = var_call_30lJdgJVaQJdZAMe6h3V85Ch
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

venues = ['chi','ubicomp','cscw','dis','pervasivehealth','www','iui','ozchi','tei','ah']

# Compile regexes for 2016
patterns = [
    re.compile(r"copyright\s*2016", re.IGNORECASE),
    re.compile(r"\b2016\b", re.IGNORECASE),
]
venue_patterns = [re.compile(r"\b"+v+r"\b[^\n]{0,120}(2016|'16)", re.IGNORECASE) for v in venues]


def is_2016(text):
    if not text:
        return False
    header = text[:4000]
    for rx in patterns:
        if rx.search(header):
            return True
    for rx in venue_patterns:
        if rx.search(header):
            return True
    # also search body for explicit venue-year mentions
    for rx in venue_patterns:
        if rx.search(text):
            return True
    return False

titles2016 = []
for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
    if 'physical activity' not in text.lower():
        continue
    if is_2016(text):
        fn = doc.get('filename', '')
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        if title and title not in titles2016:
            titles2016.append(title)

out = json.dumps(titles2016)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_30lJdgJVaQJdZAMe6h3V85Ch': 'file_storage/call_30lJdgJVaQJdZAMe6h3V85Ch.json', 'var_call_kxNffj8ucVhN9ULkiBzUJqBa': []}

exec(code, env_args)
