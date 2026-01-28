code = """import json

mongo_path = var_call_ymVAAUnYUlW5BmI2odMZ75wC
citations_path = var_call_sMdGCvUlKzwNoJJjCix29a0p

with open(mongo_path, 'r', encoding='utf-8') as f:
    mongo_docs = json.load(f)
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

lookup = {}
for rec in citations:
    lookup[rec['title']] = int(rec['total_citations'])

results = []
years = [str(y) for y in range(2017, 2027)]
for doc in mongo_docs:
    filename = doc.get('filename', '')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = doc.get('text', '') or ''
    if 'empirical' not in text.lower():
        continue
    found_year = None
    for y in years:
        if y in text:
            found_year = int(y)
            break
    if not found_year:
        continue
    if found_year <= 2016:
        continue
    if title in lookup:
        results.append({'title': title, 'total_citations': lookup[title], 'year': found_year})

results = sorted(results, key=lambda x: x['title'])

if results:
    answer_text = "\n".join([r['title'] + ': ' + str(r['total_citations']) for r in results])
else:
    answer_text = "No papers found matching the criteria."

output = {'results': results, 'answer_text': answer_text}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_U1Ff80T1kKXuRvdhRUjUwawe': ['paper_docs'], 'var_call_8Hby2Sk3LnewtJQJZ7U1h8GG': ['Citations', 'sqlite_sequence'], 'var_call_ymVAAUnYUlW5BmI2odMZ75wC': 'file_storage/call_ymVAAUnYUlW5BmI2odMZ75wC.json', 'var_call_sMdGCvUlKzwNoJJjCix29a0p': 'file_storage/call_sMdGCvUlKzwNoJJjCix29a0p.json', 'var_call_vb4EwbOIJIafyvfDhCj7lric': {'citations_count': 259}}

exec(code, env_args)
