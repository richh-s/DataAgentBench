code = """import json

# Load previous tool results from storage files
mongo_path = var_call_ymVAAUnYUlW5BmI2odMZ75wC
citations_path = var_call_sMdGCvUlKzwNoJJjCix29a0p

with open(mongo_path, 'r', encoding='utf-8') as f:
    mongo_docs = json.load(f)
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a lookup for citation totals by title
cit_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

results = []

years = [str(y) for y in range(2017, 2027)]
for doc in mongo_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # Check for 'empirical' contribution mention
    if 'empirical' not in text.lower():
        continue
    # Find any publication year after 2016
    found_year = None
    for y in years:
        if y in text:
            found_year = int(y)
            break
    if not found_year:
        continue
    if found_year <= 2016:
        continue
    total_citations = cit_lookup.get(title)
    if total_citations is None:
        continue
    results.append({"title": title, "total_citations": total_citations, "year": found_year})

# Prepare output
if results:
    lines = [f"{r['title']}: {r['total_citations']}" for r in results]
    answer_text = "\n".join(lines)
else:
    answer_text = "No papers found matching the criteria."

output = {"results": results, "answer_text": answer_text}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_U1Ff80T1kKXuRvdhRUjUwawe': ['paper_docs'], 'var_call_8Hby2Sk3LnewtJQJZ7U1h8GG': ['Citations', 'sqlite_sequence'], 'var_call_ymVAAUnYUlW5BmI2odMZ75wC': 'file_storage/call_ymVAAUnYUlW5BmI2odMZ75wC.json', 'var_call_sMdGCvUlKzwNoJJjCix29a0p': 'file_storage/call_sMdGCvUlKzwNoJJjCix29a0p.json'}

exec(code, env_args)
