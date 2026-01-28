code = """import json, re

# Load the MongoDB query result stored in the provided file path variable
path = var_call_w8bG5ETjdgtkQPAM4apPcQPk
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

result = []
for r in records:
    filename = r.get('filename','')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = r.get('text','')
    # find first 4-digit year between 1900 and 2026
    year_match = re.search(r"\b(?:19|20)\d{2}\b", text)
    year = int(year_match.group(0)) if year_match else None
    # detect contribution = empirical by substring matching
    is_empirical = bool(re.search(r"\bempirical\b", text, re.IGNORECASE))
    if year and year > 2016 and is_empirical:
        result.append({"title": title, "year": year})

# produce JSON string
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_HHOGIk0EQpTyZ8Po5Dx8DSmd': ['paper_docs'], 'var_call_MlaOdx8CNusaOxsaweOzC5mx': ['Citations', 'sqlite_sequence'], 'var_call_w8bG5ETjdgtkQPAM4apPcQPk': 'file_storage/call_w8bG5ETjdgtkQPAM4apPcQPk.json'}

exec(code, env_args)
