code = """import json, re
# Load the Mongo query result stored in var_call_1zlPrJkK16QR0ZY8tjwovvQi (file path)
path = var_call_1zlPrJkK16QR0ZY8tjwovvQi
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for doc in docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    text_low = text.lower()
    # detect domain: contains 'physical activity'
    domain_match = 'physical activity' in text_low
    # find first 4-digit year between 1900 and 2099
    year_match = None
    m = re.search(r'(?<!\d)(20\d{2})(?!\d)', text)
    if m:
        year_match = int(m.group(1))
    # Heuristic: also check first 500 chars for year
    if year_match is None:
        m2 = re.search(r'(?<!\d)(20\d{2})(?!\d)', text[:500])
        if m2:
            year_match = int(m2.group(1))
    if domain_match and year_match==2016:
        results.append(title)

# Deduplicate
results = sorted(list(dict.fromkeys(results)))
import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_tUuf1vZppweMwDXs27d2trYT': ['paper_docs'], 'var_call_hf00OHhRqU4woHAYYQM7h9BC': ['Citations', 'sqlite_sequence'], 'var_call_1zlPrJkK16QR0ZY8tjwovvQi': 'file_storage/call_1zlPrJkK16QR0ZY8tjwovvQi.json'}

exec(code, env_args)
