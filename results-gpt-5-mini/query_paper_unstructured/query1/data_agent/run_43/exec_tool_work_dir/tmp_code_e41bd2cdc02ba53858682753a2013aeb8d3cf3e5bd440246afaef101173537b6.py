code = """import json
# Load the large results from previous tool calls (paths provided in storage variables)
with open(var_call_Qvaha8lwjzOuyrrYbROQAoF3, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_ExIihXEuBxaFXbC5JiCFBnLe, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Extract titles from paper documents by removing the .txt extension from filenames
food_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    food_titles.add(title)

# Sum citations for titles that are in the food domain (i.e., appear in food_titles)
total = 0
matched_titles = []
for rec in citations:
    title = rec.get('title')
    # Convert citation count to int safely
    tc = rec.get('total_citations', 0)
    try:
        c = int(tc)
    except Exception:
        try:
            c = int(float(tc))
        except Exception:
            c = 0
    if title in food_titles:
        total += c
        matched_titles.append(title)

result = {"total_citations_food": total, "matched_paper_count": len(matched_titles), "matched_titles": matched_titles}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2RYDRdyGxpyz9Bg2VXbqLIXR': ['paper_docs'], 'var_call_Qvaha8lwjzOuyrrYbROQAoF3': 'file_storage/call_Qvaha8lwjzOuyrrYbROQAoF3.json', 'var_call_ExIihXEuBxaFXbC5JiCFBnLe': 'file_storage/call_ExIihXEuBxaFXbC5JiCFBnLe.json'}

exec(code, env_args)
