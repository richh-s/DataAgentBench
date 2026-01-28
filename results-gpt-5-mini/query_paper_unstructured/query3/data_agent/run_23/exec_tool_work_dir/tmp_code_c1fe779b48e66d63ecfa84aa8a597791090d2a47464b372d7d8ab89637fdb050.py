code = """import json, re

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

year_pattern = re.compile(r"\b(2017|2018|2019|2020|2021|2022|2023|2024|2025|2026)\b")
for doc in mongo_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # Check for 'empirical' contribution mention
    if 'empirical' not in text.lower():
        continue
    # Extract publication year from text
    m = year_pattern.search(text)
    if not m:
        continue
    year = int(m.group(0))
    if year <= 2016:
        continue
    total_citations = cit_lookup.get(title)
    # Only include if we have a citation record
    if total_citations is None:
        # skip if no citation info
        continue
    results.append({"title": title, "total_citations": total_citations, "year": year})

# Prepare a plain-text answer string
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
