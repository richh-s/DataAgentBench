code = """import json, re
# Load the citations (SQLite query result)
with open(var_call_yEYd1i8bfORfLdhaGVD6Uj4J, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# Load the paper docs result from the Mongo CHI regex query
with open(var_call_ySRn3Te9En7KwCOVb0vAQjtw, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Build mapping from filename to text
file_text = {doc.get('filename',''): doc.get('text','') for doc in paper_docs}

# Define function to detect CHI venue from text
def is_chi(text):
    if not text:
        return False
    # common CHI indicators
    patterns = [r"\bCHI\b", r"Proceedings of the SIGCHI", r"SIGCHI", r"ACM CHI", r"CHI '", r"CHI\\d{2}", r"CHI Conference"]
    for p in patterns:
        if re.search(p, text, flags=re.IGNORECASE):
            return True
    return False

# Sum citation counts for papers whose filename matches and detected as CHI
total = 0
matched_titles = []
for rec in citations:
    title = rec.get('title','')
    filename = title + '.txt'
    count_raw = rec.get('citation_count', 0)
    try:
        count = int(count_raw)
    except:
        try:
            count = int(float(count_raw))
        except:
            count = 0
    text = file_text.get(filename)
    if text and is_chi(text):
        total += count
        matched_titles.append({'title': title, 'citation_count': count})

# Prepare output: total and number of matched papers
output = {'total_citation_count': total, 'matched_paper_count': len(matched_titles), 'matched_papers': matched_titles}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_yEYd1i8bfORfLdhaGVD6Uj4J': 'file_storage/call_yEYd1i8bfORfLdhaGVD6Uj4J.json', 'var_call_PdjtBb60nhijxlRjarbHaeIl': 'file_storage/call_PdjtBb60nhijxlRjarbHaeIl.json', 'var_call_ySRn3Te9En7KwCOVb0vAQjtw': 'file_storage/call_ySRn3Te9En7KwCOVb0vAQjtw.json'}

exec(code, env_args)
