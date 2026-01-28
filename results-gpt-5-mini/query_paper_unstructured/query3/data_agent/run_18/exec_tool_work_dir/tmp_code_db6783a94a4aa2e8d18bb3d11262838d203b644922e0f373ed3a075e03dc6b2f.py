code = """import json, re

# Load the large query results from storage-provided file paths
with open(var_call_qvD0vgwiI2YVjbCb7dpSOJjn, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_kkQRnGT0AqxnWSKMgGBH11WD, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a mapping from title to total citations (convert to int)
cit_map = {}
for rec in citations:
    title = rec.get('title')
    # some titles may be quoted in the citations DB; normalize by stripping surrounding quotes and whitespace
    if isinstance(title, str):
        title_key = title.strip().strip('\"').strip("'")
    else:
        title_key = title
    try:
        total = int(rec.get('total_citations', 0))
    except:
        # if stored as string with commas
        tc = rec.get('total_citations', 0)
        if isinstance(tc, str):
            total = int(tc.replace(',', ''))
        else:
            total = 0
    cit_map[title_key] = total

# Year extraction helper
def extract_year(text):
    if not text:
        return None
    # Search for 4-digit years first
    m = re.search(r"\b(19|20)\d{2}\b", text)
    if m:
        year = int(m.group(0))
        return year
    # fallback: search for patterns like '15 or ’15
    m2 = re.search(r"[\'’`]\s?(\d{2})\b", text)
    if m2:
        yy = int(m2.group(1))
        if yy <= 26:
            return 2000 + yy
        else:
            return 1900 + yy
    # as another fallback, find any 2-digit year-like token preceded/followed by space and likely in range
    m3 = re.search(r"\b(\d{2})\b", text)
    if m3:
        yy = int(m3.group(1))
        if 70 <= yy <= 99:
            return 1900 + yy
        if 0 <= yy <= 26:
            return 2000 + yy
    return None

results = []
for doc in docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    year = extract_year(text)
    # contribution match: substring 'empirical' (case-insensitive)
    if text and re.search(r"\bempirical\b", text, re.IGNORECASE):
        if year and year > 2016:
            total_citations = cit_map.get(title, 0)
            results.append({"title": title, "total_citations": total_citations, "year": year})

# Sort results by total_citations descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Prepare output - only title and total citation count as requested
out = [{"title": r['title'], "total_citations": r['total_citations']} for r in results_sorted]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_TacN4CnrhUKQePmqdRb0TwXz': ['paper_docs'], 'var_call_5At4LH0pS4wiq9d2H69yxPkA': ['Citations', 'sqlite_sequence'], 'var_call_qvD0vgwiI2YVjbCb7dpSOJjn': 'file_storage/call_qvD0vgwiI2YVjbCb7dpSOJjn.json', 'var_call_kkQRnGT0AqxnWSKMgGBH11WD': 'file_storage/call_kkQRnGT0AqxnWSKMgGBH11WD.json'}

exec(code, env_args)
