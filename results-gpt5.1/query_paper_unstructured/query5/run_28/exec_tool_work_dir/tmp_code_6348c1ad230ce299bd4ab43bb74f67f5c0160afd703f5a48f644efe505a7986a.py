code = """import json, re

# Load full citation results
with open(var_call_AZ7s5VGX7lc0BaM8unM0JQDy, 'r') as f:
    citations = json.load(f)

# Load full paper docs results
with open(var_call_6c5Seg2O7m0oIMdkZwT0Y2XY, 'r') as f:
    papers = json.load(f)

# Build a mapping from title (filename without .txt) to venue by heuristically parsing text
# We'll look for typical CHI markers in the first 2000 characters.

def infer_venue(text):
    header = text[:2000].upper()
    if 'CHI ' in header or "CONFERENCE ON HUMAN FACTORS IN COMPUTING SYSTEMS" in header:
        return 'CHI'
    return None

venue_by_title = {}
for doc in papers:
    filename = doc.get('filename') or ''
    if not filename.lower().endswith('.txt'):
        continue
    title = filename[:-4]
    venue = infer_venue(doc.get('text',''))
    if venue:
        venue_by_title[title] = venue

# Sum citation counts for 2020 citations where venue is CHI

total_citations_chi_2020 = 0
for row in citations:
    title = row.get('title')
    if not title:
        continue
    if venue_by_title.get(title) == 'CHI':
        try:
            c = int(row.get('citation_count', 0))
        except Exception:
            c = 0
        total_citations_chi_2020 += c

result = json.dumps(total_citations_chi_2020)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_AZ7s5VGX7lc0BaM8unM0JQDy': 'file_storage/call_AZ7s5VGX7lc0BaM8unM0JQDy.json', 'var_call_6c5Seg2O7m0oIMdkZwT0Y2XY': 'file_storage/call_6c5Seg2O7m0oIMdkZwT0Y2XY.json'}

exec(code, env_args)
