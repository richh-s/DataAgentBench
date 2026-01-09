code = """import json
import pandas as pd

with open(var_call_nKcqwc5ja4sXUlqRqUJJ6uzV, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

with open(var_call_GZmXkPR1bvCkVUon7p1X0fCh, 'r', encoding='utf-8') as f:
    docs = json.load(f)

food_titles = sorted({(d.get('filename','')[:-4] if d.get('filename','').lower().endswith('.txt') else d.get('filename','')) for d in docs})

df_food = pd.DataFrame({'title': food_titles})
merged = df_food.merge(df_cit, on='title', how='left')
merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)

result = {
    'total_citation_count_for_food_domain_papers': int(merged['total_citations'].sum()),
    'num_food_papers_via_food_keyword_in_text': int(len(food_titles)),
    'num_food_papers_with_citation_records': int((merged['total_citations'] > 0).sum())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_nKcqwc5ja4sXUlqRqUJJ6uzV': 'file_storage/call_nKcqwc5ja4sXUlqRqUJJ6uzV.json', 'var_call_5d4tQE2oAez2ePpXlIQytLc6': [], 'var_call_GZmXkPR1bvCkVUon7p1X0fCh': 'file_storage/call_GZmXkPR1bvCkVUon7p1X0fCh.json'}

exec(code, env_args)
