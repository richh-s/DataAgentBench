code = """import json, re

# Load the MongoDB query result from file path
path = var_call_30lJdgJVaQJdZAMe6h3V85Ch
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

venues = ["chi","ubicomp","cscw","dis","pervasivehealth","www","iui","ozchi","tei","ah"]

def is_2016(text):
    if not text:
        return False
    header = text[:2000]
    lower = header.lower()
    # Look for common header indicators of year 2016
    if re.search(r"copyright\s*2016", lower):
        return True
    if re.search(r"\b2016\b", header):
        return True
    if re.search(r"[\'’]\s*16", header):
        return True
    # Venue + year pattern within header region
    if re.search(r"(" + "|".join(venues) + r")([^\n]{0,80})(2016|[\'’]\s*16)", lower):
        return True
    return False

result_titles = []
for doc in docs:
    fn = doc.get('filename') or ''
    text = doc.get('text') or ''
    # Ensure domain match (already filtered, but double-check)
    if 'physical activity' not in text.lower():
        continue
    if is_2016(text):
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        if title and title not in result_titles:
            result_titles.append(title)

out = json.dumps(result_titles)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_30lJdgJVaQJdZAMe6h3V85Ch': 'file_storage/call_30lJdgJVaQJdZAMe6h3V85Ch.json'}

exec(code, env_args)
