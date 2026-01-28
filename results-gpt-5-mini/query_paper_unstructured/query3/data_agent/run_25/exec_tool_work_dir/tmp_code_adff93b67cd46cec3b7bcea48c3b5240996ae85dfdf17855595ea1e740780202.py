code = """import json, re

# Load data from storage-provided file paths
paper_docs_path = var_call_0gh5eqpvouo4RIMJIJ0yWH3g
citations_path = var_call_B4DyUEw1gKcTxREJELQ2KG6q

with open(paper_docs_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation lookup: title -> total citations (int)
cit_lookup = {}
for rec in citations:
    title = rec.get('title')
    # Some citation counts may be strings; convert safely
    try:
        count = int(rec.get('total_citations', 0))
    except:
        try:
            count = int(float(rec.get('total_citations', 0)))
        except:
            count = 0
    cit_lookup[title] = count

results = []

def extract_year(text):
    # Search the first 1000 chars first for a 4-digit year
    search_area = text[:1000]
    m = re.search(r"\b(19|20)\d{2}\b", search_area)
    if m:
        return int(m.group(0))
    # fallback to full text
    m = re.search(r"\b(19|20)\d{2}\b", text)
    if m:
        return int(m.group(0))
    return None

for doc in papers:
    filename = doc.get('filename','')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = doc.get('text','') or ''
    year = extract_year(text)
    if year is None:
        continue
    # contribution: check if 'empirical' appears in text
    contribution_empirical = 'empirical' in text.lower()
    if contribution_empirical and year > 2016:
        total_citations = cit_lookup.get(title, 0)
        results.append({'title': title, 'total_citations': total_citations})

# Sort results by title for consistency
results = sorted(results, key=lambda x: x['title'])

# Print according to required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_pWVaciMY2EeKAy7f9w75MmiV': ['paper_docs'], 'var_call_0gh5eqpvouo4RIMJIJ0yWH3g': 'file_storage/call_0gh5eqpvouo4RIMJIJ0yWH3g.json', 'var_call_yfZLdyYjut6a9wwVthh86ZuS': ['Citations', 'sqlite_sequence'], 'var_call_B4DyUEw1gKcTxREJELQ2KG6q': 'file_storage/call_B4DyUEw1gKcTxREJELQ2KG6q.json'}

exec(code, env_args)
