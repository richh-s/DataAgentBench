code = """import json
# Load the stored query results from file paths provided by previous tool calls
with open(var_call_iTvlrKgSxNXNzS3d9qwOt8gI, 'r') as f:
    papers = json.load(f)
with open(var_call_R4QbvyDwpnmFKb3asBGRnXKJ, 'r') as f:
    citations = json.load(f)

# Extract titles from paper filenames (remove .txt extension)
titles = set()
for p in papers:
    fn = p.get('filename', '')
    if fn.lower().endswith('.txt'):
        titles.add(fn[:-4])
    else:
        titles.add(fn)

# Sum citation counts for titles that match the 'food' papers
total = 0
matched_titles = []
for c in citations:
    t = c.get('title')
    cnt = c.get('citation_count', 0)
    try:
        cnt_int = int(cnt)
    except:
        try:
            cnt_int = int(float(cnt))
        except:
            cnt_int = 0
    if t in titles:
        total += cnt_int
        matched_titles.append(t)

# Prepare result
result = {"domain": "food", "total_citation_count": total, "matched_paper_count": len(matched_titles)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ydqh7OL7i2wJ2JyShm0kzIDx': 'file_storage/call_ydqh7OL7i2wJ2JyShm0kzIDx.json', 'var_call_R4QbvyDwpnmFKb3asBGRnXKJ': 'file_storage/call_R4QbvyDwpnmFKb3asBGRnXKJ.json', 'var_call_iTvlrKgSxNXNzS3d9qwOt8gI': 'file_storage/call_iTvlrKgSxNXNzS3d9qwOt8gI.json'}

exec(code, env_args)
