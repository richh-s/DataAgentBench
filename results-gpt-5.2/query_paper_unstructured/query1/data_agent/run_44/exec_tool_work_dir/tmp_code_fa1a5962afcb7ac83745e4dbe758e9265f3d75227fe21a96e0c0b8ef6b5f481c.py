code = """import json, re
import pandas as pd

def load_maybe_path(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

paper_files = load_maybe_path(var_call_VcUl9kgV1nzVyd0Nebe8JfOe)
citations = load_maybe_path(var_call_6eW1h8JGMl4uhDmyJ4hsPapY)

# Identify 'food' domain papers by filename containing food-related markers.
# Since domain isn't explicitly stored in Mongo docs beyond text, use filename heuristics.
food_markers = [
    r"\bfood\b", r"\beating\b", r"\bdiet\b", r"\bnutrition\b", r"\bmeal\b", r"\bjournaling\b.*\bchoices\b", r"\bMyFitnessPal\b"
]
pattern = re.compile("|".join(food_markers), re.IGNORECASE)

food_titles = set()
for rec in paper_files:
    fn = rec.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if pattern.search(title):
        food_titles.add(title)

# Sum citations for those titles
food_cit_sum = 0
for r in citations:
    title = r.get('title')
    if title in food_titles:
        try:
            food_cit_sum += int(r.get('citation_count',0))
        except Exception:
            pass

out = {"total_citation_count_food_domain": food_cit_sum, "matched_food_papers": len(food_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VcUl9kgV1nzVyd0Nebe8JfOe': 'file_storage/call_VcUl9kgV1nzVyd0Nebe8JfOe.json', 'var_call_6eW1h8JGMl4uhDmyJ4hsPapY': 'file_storage/call_6eW1h8JGMl4uhDmyJ4hsPapY.json'}

exec(code, env_args)
