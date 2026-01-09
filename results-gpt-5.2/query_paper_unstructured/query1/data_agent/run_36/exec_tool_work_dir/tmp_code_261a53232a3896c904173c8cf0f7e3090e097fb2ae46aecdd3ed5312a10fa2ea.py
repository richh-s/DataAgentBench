code = """import json, pandas as pd

# Load citations totals per title
cit_path = var_call_KSGg1yOJfvvpsCcT0RKkNIdN
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# ensure numeric
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'])

# Identify food-domain papers via title keywords (food/diet/nutrition/eating/meal)
food_terms = [
    'food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 'myfitnesspal', 'grocery', 'restaurant'
]
pat = '(' + '|'.join([pd.regex.escape(t) if hasattr(pd, 'regex') else t for t in food_terms]) + ')'
# pandas doesn't have regex.escape; use re
import re
pat = re.compile(r'(' + '|'.join([re.escape(t) for t in food_terms]) + r')', re.IGNORECASE)

mask = df_cit['title'].fillna('').apply(lambda x: bool(pat.search(x)))
food_total = int(df_cit.loc[mask, 'total_citations'].sum())

print('__RESULT__:')
print(json.dumps({'food_total_citations': food_total, 'food_paper_count': int(mask.sum())}))"""

env_args = {'var_call_6cfaraVSMv1Eg5ww0sN3lvGV': 'file_storage/call_6cfaraVSMv1Eg5ww0sN3lvGV.json', 'var_call_LSGZSd1F403PmG5TuCynH715': 'file_storage/call_LSGZSd1F403PmG5TuCynH715.json', 'var_call_Uh8FAlhtVAEmlq2FelxACCWo': [], 'var_call_KSGg1yOJfvvpsCcT0RKkNIdN': 'file_storage/call_KSGg1yOJfvvpsCcT0RKkNIdN.json'}

exec(code, env_args)
