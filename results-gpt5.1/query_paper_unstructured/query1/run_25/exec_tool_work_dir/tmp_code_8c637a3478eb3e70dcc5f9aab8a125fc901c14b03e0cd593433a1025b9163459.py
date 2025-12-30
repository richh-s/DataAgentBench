code = """import json

food_papers = [doc['filename'].replace('.txt', '') for doc in var_call_zQyw08MaBJEbEUtioLE2e5ml]

with open(var_call_T801GVXtgdwgqVgviu9hrM43, 'r') as f:
    citations = json.load(f)

food_titles = set(food_papers)

total_citations_food = 0
for row in citations:
    if row['title'] in food_titles:
        total_citations_food += int(row['total_citations'])

result = json.dumps(total_citations_food)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_zQyw08MaBJEbEUtioLE2e5ml': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_call_T801GVXtgdwgqVgviu9hrM43': 'file_storage/call_T801GVXtgdwgqVgviu9hrM43.json'}

exec(code, env_args)
