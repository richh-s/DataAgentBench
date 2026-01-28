code = """import json, pandas as pd

food_files = [d['filename'] for d in var_call_bQ6l1sH1yWk78nbY0kx2aBu6]
food_titles = [f[:-4] if f.lower().endswith('.txt') else f for f in food_files]

with open(var_call_vzl9SO6sN7oF3RPCTtD0CQPd, 'r') as f:
    citations = json.load(f)

df = pd.DataFrame(citations)
food_citations = df[df['title'].isin(food_titles)]

total = int(food_citations['total_citations'].astype(int).sum())

res = json.dumps({"total_food_domain_citations": total})
print("__RESULT__:")
print(res)"""

env_args = {'var_call_bQ6l1sH1yWk78nbY0kx2aBu6': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_call_vzl9SO6sN7oF3RPCTtD0CQPd': 'file_storage/call_vzl9SO6sN7oF3RPCTtD0CQPd.json'}

exec(code, env_args)
