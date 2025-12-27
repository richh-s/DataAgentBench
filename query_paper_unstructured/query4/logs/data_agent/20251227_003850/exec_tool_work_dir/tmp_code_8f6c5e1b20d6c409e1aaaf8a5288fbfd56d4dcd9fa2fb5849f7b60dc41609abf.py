code = """import json, re

path = var_call_30lJdgJVaQJdZAMe6h3V85Ch
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

patterns = [
    r"copyright\s*2016",
    r"\bchi\b[^\n]{0,120}(2016|\b'16\b|’16)",
    r"\bubicomp\b[^\n]{0,120}(2016|\b'16\b|’16)",
    r"\bcscw\b[^\n]{0,120}(2016|\b'16\b|’16)",
    r"\bdis\b[^\n]{0,120}(2016|\b'16\b|’16)",
    r"\bpervasivehealth\b[^\n]{0,120}(2016|\b'16\b|’16)",
    r"\bwww\b[^\n]{0,120}2016",
    r"\biui\b[^\n]{0,120}(2016|\b'16\b|’16)",
    r"\bozchi\b[^\n]{0,120}2016",
    r"\btei\b[^\n]{0,120}2016",
    r"\bah\b[^\n]{0,120}2016",
    r"proceedings of (the )?2016",
    r"\b2016\b.{0,40}\bacm\b",
    r"\bacm\b.{0,40}\b2016\b"
]
compiled = [re.compile(p, flags=re.IGNORECASE) for p in patterns]

def is_2016(text):
    header = text[:10000]
    for rx in compiled:
        if rx.search(header):
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
