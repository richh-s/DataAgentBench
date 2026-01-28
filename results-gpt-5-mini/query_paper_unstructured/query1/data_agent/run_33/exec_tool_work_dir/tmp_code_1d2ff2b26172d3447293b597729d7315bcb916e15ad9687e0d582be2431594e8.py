code = """import json
# Load data from storage-provided JSON file paths
with open(var_call_8kxeQ4GNae4EwLVlqS2LqUyr, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_s1xrnzzyCIYBqKyJ3XLrpQvW, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build mapping from title to total citations
cit_map = {}
for r in citations:
    title = r.get('title')
    val = r.get('total_citations') if 'total_citations' in r else r.get('citation_count')
    try:
        v = int(val)
    except:
        try:
            v = int(str(val))
        except:
            v = 0
    cit_map[title] = v

# Identify papers in the 'food' domain by substring matching in text
food_titles = []
for d in docs:
    fname = d.get('filename','')
    title = fname[:-4] if fname.lower().endswith('.txt') else fname
    text = d.get('text','') or ''
    if 'food' in text.lower():
        food_titles.append(title)

# Sum citations for those titles
total = 0
per_title = []
for t in food_titles:
    c = cit_map.get(t, 0)
    total += c
    per_title.append({'title': t, 'citations': c})

result = {'domain': 'food', 'total_citations': total, 'papers_counted': len(food_titles), 'papers': per_title}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_A54FFH09GAdN8fswA9hTbsxn': ['paper_docs'], 'var_call_8kxeQ4GNae4EwLVlqS2LqUyr': 'file_storage/call_8kxeQ4GNae4EwLVlqS2LqUyr.json', 'var_call_D1kzlXsWNBn4uFncwoNJYuR2': ['Citations', 'sqlite_sequence'], 'var_call_s1xrnzzyCIYBqKyJ3XLrpQvW': 'file_storage/call_s1xrnzzyCIYBqKyJ3XLrpQvW.json'}

exec(code, env_args)
