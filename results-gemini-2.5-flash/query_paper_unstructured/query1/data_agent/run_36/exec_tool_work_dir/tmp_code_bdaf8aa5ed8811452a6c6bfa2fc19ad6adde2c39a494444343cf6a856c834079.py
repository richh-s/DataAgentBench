code = """import json
import pandas as pd

with open(locals()['var_function-call-15880041372856478765'], 'r') as f:
    papers_data = json.load(f)

food_papers = []
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text'].lower()
    if 'domain: "food"' in text or 'domains: "food"' in text or 'food domain' in text or 'food intake' in text or 'food consumption' in text or 'eating habits' in text or 'food journal' in text:
        food_papers.append({'title': title})

food_papers_df = pd.DataFrame(food_papers)
print('__RESULT__:')
print(food_papers_df.to_json(orient='records'))"""

env_args = {'var_function-call-770696393874806011': ['paper_docs'], 'var_function-call-15880041372856478765': 'file_storage/function-call-15880041372856478765.json'}

exec(code, env_args)
