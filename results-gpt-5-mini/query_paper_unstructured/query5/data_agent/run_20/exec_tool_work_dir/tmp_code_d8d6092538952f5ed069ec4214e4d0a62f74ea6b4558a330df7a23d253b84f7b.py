code = """import json, re

# Load the large results from the query_db calls (file paths provided in storage variables)
with open(var_call_YnY1GuWjNZOZiSZ1JA5HPh33, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_Cz9owk3ICuJDWyvdsRLdiod7, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Build a map from title to citation_count for citation_year=2020
cit_map = {}
for rec in citations:
    title = rec.get('title')
    # citation_count may be string, convert to int safely
    try:
        count = int(rec.get('citation_count', 0))
    except:
        # If empty or non-numeric, skip or set 0
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    cit_map[title] = count

# Function to detect CHI venue in text
def is_chi(text):
    if not text:
        return False
    # Look for patterns that indicate CHI conference: 'CHI', "CHI '15", 'Proceedings of the CHI', 'ACM CHI', etc.
    patterns = [r"\bCHI\b",
                r"CHI\s*'\d{2}",
                r"Proceedings.*CHI",
                r"ACM\s+CHI",
                r"CHI:\s",
                r"CHI\s*201\d",
               ]
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False

# For each paper doc, check if venue is CHI and if title is cited in 2020
matched = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    # title in citations table matches filename without .txt
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = doc.get('text', '')
    if is_chi(text):
        if title in cit_map:
            matched.append({'title': title, 'citation_count': cit_map[title]})

# Also ensure there are no CHI papers in citations that weren't in paper_docs (unlikely per hint)
# But we will also scan citation titles and try to match to paper_docs by title
paper_titles_set = set([ (d.get('filename')[:-4] if d.get('filename','').lower().endswith('.txt') else d.get('filename')) for d in paper_docs ])
for title, count in cit_map.items():
    if title in paper_titles_set:
        # find the document and check CHI if not already included
        if title not in [m['title'] for m in matched]:
            # find doc
            docs = [d for d in paper_docs if ((d.get('filename','')[:-4] if d.get('filename','').lower().endswith('.txt') else d.get('filename'))==title)]
            if docs:
                if is_chi(docs[0].get('text','')):
                    matched.append({'title': title, 'citation_count': count})

# Compute total citations
total = sum([m['citation_count'] for m in matched])

# Sort matched list by citation_count desc
matched_sorted = sorted(matched, key=lambda x: x['citation_count'], reverse=True)

# Prepare JSON-serializable result
result = {
    'total_citations_2020_for_CHI_papers': total,
    'num_chi_papers_cited_in_2020': len(matched_sorted),
    'papers': matched_sorted
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YnY1GuWjNZOZiSZ1JA5HPh33': 'file_storage/call_YnY1GuWjNZOZiSZ1JA5HPh33.json', 'var_call_A0mEyPqlauwzxdNPp2mIJEzR': ['paper_docs'], 'var_call_Cz9owk3ICuJDWyvdsRLdiod7': 'file_storage/call_Cz9owk3ICuJDWyvdsRLdiod7.json'}

exec(code, env_args)
