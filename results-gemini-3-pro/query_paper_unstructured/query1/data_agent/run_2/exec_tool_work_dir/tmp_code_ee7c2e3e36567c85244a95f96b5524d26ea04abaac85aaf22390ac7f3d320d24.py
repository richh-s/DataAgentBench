code = """import json

with open(locals()['var_function-call-16861145491754002893'], 'r') as f:
    papers = json.load(f)

check_titles = [
    "A Stage-based Model of Personal Informatics Systems",
    "Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use"
]

results = {}
for p in papers:
    title = p.get('filename', '').replace('.txt', '')
    if title in check_titles:
        text = p.get('text', '').lower()
        # extract keywords
        kw_start = text.find('keywords')
        kw_section = text[kw_start:kw_start+300] if kw_start != -1 else "Not Found"
        results[title] = kw_section

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5516583949260656826': 'file_storage/function-call-5516583949260656826.json', 'var_function-call-6649186005887820433': 'file_storage/function-call-6649186005887820433.json', 'var_function-call-16861145491754002893': 'file_storage/function-call-16861145491754002893.json', 'var_function-call-4378801704425368314': 'file_storage/function-call-4378801704425368314.json', 'var_function-call-8391609740285932729': {'food_papers_count': 1, 'food_papers_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling'], 'total_citations': 270}, 'var_function-call-2521471083806893142': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use']}

exec(code, env_args)
