code = """import json

# Load results from previous tool calls stored as file paths
with open(var_call_SkuKwOV7UCqCiQHfhxdzaEJF, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_BIur1IuepFu2vyVGXYkkFLim, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build map from title (filename without .txt) to paper text
paper_map = {}
for doc in papers:
    filename = doc.get('filename', '')
    title = filename
n
for doc in papers:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title_key = filename[:-4]
    else:
        title_key = filename
    paper_map[title_key] = doc.get('text', '')

# Filter citations for 2018 already applied in SQL query; citations list contains dicts with title and citation_count
acm_counts = []
missing_titles = []
for rec in citations:
    title = rec.get('title')
    # Some citation_count may be strings
    try:
        count = int(rec.get('citation_count', 0))
    except:
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    # Match title to paper_map
    if title in paper_map:
        text = paper_map[title] or ''
        if 'acm' in text.lower():
            acm_counts.append(count)
    else:
        missing_titles.append(title)

# Compute average
if len(acm_counts) > 0:
    average = sum(acm_counts) / len(acm_counts)
else:
    average = None

result = {
    'average_citation_count': (average if average is None else round(average, 4)),
    'paper_count': len(acm_counts)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SkuKwOV7UCqCiQHfhxdzaEJF': 'file_storage/call_SkuKwOV7UCqCiQHfhxdzaEJF.json', 'var_call_BIur1IuepFu2vyVGXYkkFLim': 'file_storage/call_BIur1IuepFu2vyVGXYkkFLim.json'}

exec(code, env_args)
