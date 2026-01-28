code = """import json, re
path = var_call_w8bG5ETjdgtkQPAM4apPcQPk
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

matches = []
for r in records:
    filename = r.get('filename','')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = r.get('text','')
    year_match = re.search(r"\b(?:19|20)\d{2}\b", text)
    year = int(year_match.group(0)) if year_match else None
    emp_count = len(re.findall(r"\bempirical\b", text, re.IGNORECASE))
    # also look for 'empiric' or 'empirically'
    emp_count += len(re.findall(r"\bempiric(?:al|ally)?\b", text, re.IGNORECASE))
    if emp_count>0:
        matches.append({"title": title, "year": year, "empirical_mentions": emp_count})

out = json.dumps(matches)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_HHOGIk0EQpTyZ8Po5Dx8DSmd': ['paper_docs'], 'var_call_MlaOdx8CNusaOxsaweOzC5mx': ['Citations', 'sqlite_sequence'], 'var_call_w8bG5ETjdgtkQPAM4apPcQPk': 'file_storage/call_w8bG5ETjdgtkQPAM4apPcQPk.json', 'var_call_zVyYkpA9Kzg8p13CUW2ciuo3': []}

exec(code, env_args)
