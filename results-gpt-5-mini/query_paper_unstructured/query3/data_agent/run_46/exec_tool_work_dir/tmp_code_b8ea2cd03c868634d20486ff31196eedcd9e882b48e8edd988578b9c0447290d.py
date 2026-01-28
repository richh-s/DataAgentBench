code = """import json, re
path = var_call_w8bG5ETjdgtkQPAM4apPcQPk
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

year_counts = {}
titles_after_2016 = []
for r in records:
    filename = r.get('filename','')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = r.get('text','') or ''
    year_match = re.search(r"\b(19|20)\d{2}\b", text)
    year = int(year_match.group(0)) if year_match else None
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        if year > 2016:
            titles_after_2016.append({"title": title, "year": year})

# sort year_counts
year_counts_sorted = dict(sorted(year_counts.items()))
out = {"year_counts": year_counts_sorted, "titles_after_2016_sample": titles_after_2016[:50], "titles_after_2016_count": len(titles_after_2016)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_HHOGIk0EQpTyZ8Po5Dx8DSmd': ['paper_docs'], 'var_call_MlaOdx8CNusaOxsaweOzC5mx': ['Citations', 'sqlite_sequence'], 'var_call_w8bG5ETjdgtkQPAM4apPcQPk': 'file_storage/call_w8bG5ETjdgtkQPAM4apPcQPk.json', 'var_call_zVyYkpA9Kzg8p13CUW2ciuo3': [], 'var_call_ghl7bPuKnvgZEbmH8SMI0kZj': [], 'var_call_YOIRpDaDPbcfd1d7ZyVC35d9': [], 'var_call_IAEwANlWF5I06jPweYpKoI2I': 'file_storage/call_IAEwANlWF5I06jPweYpKoI2I.json'}

exec(code, env_args)
