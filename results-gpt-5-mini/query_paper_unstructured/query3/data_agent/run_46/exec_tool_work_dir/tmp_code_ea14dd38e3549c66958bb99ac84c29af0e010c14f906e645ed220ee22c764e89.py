code = """import json, re
path = var_call_w8bG5ETjdgtkQPAM4apPcQPk
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

keywords = [
    'user study','user studies','participants','interview','interviews','survey',
    'field study','field studies','controlled study','randomized','experiment',
    'case study','observational study','within-subject','between-subject','participants were',
    'we conducted','we conducted a study','we ran a study','n =','n=','participants (', 'participants,']

candidates = []
for r in records:
    filename = r.get('filename','')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = r.get('text','') or ''
    text_l = text.lower()
    year_match = re.search(r"\b(?:19|20)\d{2}\b", text)
    year = int(year_match.group(0)) if year_match else None
    if not year or year<=2016:
        continue
    found = False
    found_terms = []
    for kw in keywords:
        if kw in text_l:
            found = True
            found_terms.append(kw)
    # also look for patterns like 'we interviewed' or 'we administered a survey'
    if re.search(r"we (interviewed|surveyed|observed|recruited|ran a study|conducted interviews|conducted a survey)", text_l):
        found = True
        found_terms.append('we_*_study')
    if found:
        candidates.append({"title": title, "year": year, "matched_terms": list(set(found_terms))})

out = json.dumps(candidates)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_HHOGIk0EQpTyZ8Po5Dx8DSmd': ['paper_docs'], 'var_call_MlaOdx8CNusaOxsaweOzC5mx': ['Citations', 'sqlite_sequence'], 'var_call_w8bG5ETjdgtkQPAM4apPcQPk': 'file_storage/call_w8bG5ETjdgtkQPAM4apPcQPk.json', 'var_call_zVyYkpA9Kzg8p13CUW2ciuo3': [], 'var_call_ghl7bPuKnvgZEbmH8SMI0kZj': []}

exec(code, env_args)
