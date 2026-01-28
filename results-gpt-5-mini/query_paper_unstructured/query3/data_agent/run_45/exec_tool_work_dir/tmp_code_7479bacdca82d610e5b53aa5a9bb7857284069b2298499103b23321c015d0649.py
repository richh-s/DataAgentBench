code = """import json, re

# Load the query results from MongoDB (papers containing 'empirical') and the citation totals
with open(var_call_wSNySQeG1VyEW3WgcW0OUT1R, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_zhJyw3ksCwxLBV4S11w8lgdY, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a lookup for citation totals by title
cit_lookup = {rec['title'].strip(): int(rec['total_citations']) for rec in citations}

results = []
for doc in papers:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    # find year: look for first 4-digit year between 2000 and 2026
    years = re.findall(r"(20[0-2][0-9])", text)
    year = None
    if years:
        year = int(years[0])
    else:
        # fallback: try any 4-digit
        m = re.search(r"(19|20)\d{2}", text)
        if m:
            year = int(m.group(0))
    # check empirical term present (should be, since query filtered) and year > 2016
    if year and year > 2016 and re.search(r"\bempirical\b", text, re.IGNORECASE):
        total_citations = cit_lookup.get(title, None)
        results.append({"title": title, "year": year, "total_citations": total_citations})

# Sort results by total_citations descending (None treated as -1)
results.sort(key=lambda x: (x['total_citations'] if x['total_citations'] is not None else -1), reverse=True)

# Prepare JSON string
output = json.dumps(results)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_WwcUfVd5mW2E2J8J56k8eQpH': ['paper_docs'], 'var_call_pANPbmmfqrWx6BE5oK3djgqE': ['Citations', 'sqlite_sequence'], 'var_call_YUTagNubZfkZ9rZa5NEj5Ap0': 'file_storage/call_YUTagNubZfkZ9rZa5NEj5Ap0.json', 'var_call_wSNySQeG1VyEW3WgcW0OUT1R': 'file_storage/call_wSNySQeG1VyEW3WgcW0OUT1R.json', 'var_call_zhJyw3ksCwxLBV4S11w8lgdY': 'file_storage/call_zhJyw3ksCwxLBV4S11w8lgdY.json'}

exec(code, env_args)
