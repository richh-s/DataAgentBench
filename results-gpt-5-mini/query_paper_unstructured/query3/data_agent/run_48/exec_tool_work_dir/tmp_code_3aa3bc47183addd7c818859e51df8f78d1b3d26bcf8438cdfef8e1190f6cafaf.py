code = """import json, re

# Load the Mongo query results and the citations aggregation results
# Variables provided by storage:
# var_call_Qf1v8D8C8MZhdY7Fo0WcVzNG and var_call_78aa2ahx5zPbIXCBXtPwVEY8

# Read files if variables are file paths

def load_storage(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_docs = load_storage(var_call_Qf1v8D8C8MZhdY7Fo0WcVzNG)
citations = load_storage(var_call_78aa2ahx5zPbIXCBXtPwVEY8)

# Build citation map: title -> total_citations (int)
cit_map = {}
for rec in citations:
    title = rec.get('title', '').strip()
    # Some titles may be quoted; strip surrounding quotes and whitespace
    if len(title) >= 2 and ((title[0] == '"' and title[-1] == '"') or (title[0] == "'" and title[-1] == "'")):
        title = title[1:-1].strip()
    try:
        total = int(rec.get('total_citations') if rec.get('total_citations') is not None else 0)
    except:
        try:
            total = int(str(rec.get('total_citations')).replace(',', ''))
        except:
            total = 0
    cit_map[title] = total

# Process paper docs: extract title (filename without .txt), year (first 4-digit >=2000), and check for 'empirical'
results = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = doc.get('text', '') or ''
    # find first 4-digit year between 2000 and 2026
    years = re.findall(r'(?<!\d)(20\d{2})(?!\d)', text)
    year = None
    for y in years:
        yi = int(y)
        if 2000 <= yi <= 2026:
            year = yi
            break
    # check empirical substring in text or filename
    is_empirical = bool(re.search(r'(?i)\bempirical\b', text)) or bool(re.search(r'(?i)\bempirical\b', title))
    if is_empirical and year is not None and year > 2016:
        total_citations = cit_map.get(title, 0)
        results.append({"title": title, "total_citations": total_citations, "year": year})

# Sort results by total_citations desc
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Prepare output: only title and total_citations
out = [{"title": r['title'], "total_citations": r['total_citations']} for r in results]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_DmUILQGsTF5x3AezQGGFA3rA': ['paper_docs'], 'var_call_Qf1v8D8C8MZhdY7Fo0WcVzNG': 'file_storage/call_Qf1v8D8C8MZhdY7Fo0WcVzNG.json', 'var_call_78aa2ahx5zPbIXCBXtPwVEY8': 'file_storage/call_78aa2ahx5zPbIXCBXtPwVEY8.json'}

exec(code, env_args)
