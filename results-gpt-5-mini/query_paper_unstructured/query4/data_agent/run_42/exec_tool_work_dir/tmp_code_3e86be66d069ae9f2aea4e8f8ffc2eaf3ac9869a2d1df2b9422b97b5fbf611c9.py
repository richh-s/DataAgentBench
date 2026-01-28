code = """import json

# Load MongoDB query result (paper documents)
with open(var_call_usSEjUtT2IWF6PvzKjAUuDtw, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Load Citations table result
with open(var_call_7gKBgYMSZNpz0J1drwuCFJsn, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Sum citations per title
cit_sum = {}
for r in citations:
    title = r.get('title')
    try:
        count = int(float(r.get('citation_count', 0)))
    except:
        count = 0
    cit_sum[title] = cit_sum.get(title, 0) + count

results = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # We assume the Mongo query already filtered for text containing 'physical activity' and '2016'
    total_citations = cit_sum.get(title, 0)
    results.append({"title": title, "total_citation_count": total_citations})

# Sort by title for consistency
results = sorted(results, key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_cql4grllXOR9TdyPMEBiUmP9': ['paper_docs'], 'var_call_usSEjUtT2IWF6PvzKjAUuDtw': 'file_storage/call_usSEjUtT2IWF6PvzKjAUuDtw.json', 'var_call_7gKBgYMSZNpz0J1drwuCFJsn': 'file_storage/call_7gKBgYMSZNpz0J1drwuCFJsn.json'}

exec(code, env_args)
