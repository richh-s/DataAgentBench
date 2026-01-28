code = """import json
import re
# Load Mongo query result from file path variable
path = var_call_VUXvOspLetLt5Con2KvfAtOt
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles_2016 = []
for d in docs:
    filename = d.get('filename', '')
    if not filename:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text', '')
    # Search for year occurrences in the first 800 chars then full text
    search_area = text[:800] if text else ''
    years = re.findall(r"\b(19|20)\d{2}\b", search_area)
    # re.findall with group gives only '19' or '20', so use findall without group
    years = re.findall(r"\b(?:19|20)\d{2}\b", search_area)
    year = None
    if years:
        year = int(years[0])
    else:
        # fallback: search whole text
        years_all = re.findall(r"\b(?:19|20)\d{2}\b", text)
        if years_all:
            year = int(years_all[0])
    if year == 2016:
        titles_2016.append(title)

# Deduplicate
titles_2016 = sorted(list(dict.fromkeys(titles_2016)))
import json as _json
print("__RESULT__:")
print(_json.dumps(titles_2016))"""

env_args = {'var_call_IGldEbXgZoelD1zKxMwMtdEX': ['paper_docs'], 'var_call_XACNxD8OT8SN9vqerPeW7TT0': ['Citations', 'sqlite_sequence'], 'var_call_VUXvOspLetLt5Con2KvfAtOt': 'file_storage/call_VUXvOspLetLt5Con2KvfAtOt.json'}

exec(code, env_args)
