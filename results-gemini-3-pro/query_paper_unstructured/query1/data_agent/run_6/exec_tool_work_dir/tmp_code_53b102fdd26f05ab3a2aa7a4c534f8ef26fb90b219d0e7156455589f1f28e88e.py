code = """import json

with open(locals()['var_function-call-8026237664886157710'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
# Print titles
titles = [p['filename'] for p in papers]
print(json.dumps({"titles": titles[:20]}))

# Check for "food" in text of first 5 papers
for i, p in enumerate(papers[:5]):
    text = p['text'].lower()
    if "food" in text:
        print(f"Paper {i} contains 'food'. Snippet around it:")
        idx = text.find("food")
        print(text[idx-50:idx+50])

# Check Author Keywords extraction for first 5
for i, p in enumerate(papers[:5]):
    text = p['text'].lower()
    start = text.find("author keywords")
    if start != -1:
        print(f"Paper {i} has Author Keywords. First 100 chars after:")
        print(text[start:start+100])
    else:
        print(f"Paper {i} has NO Author Keywords found.")"""

env_args = {'var_function-call-16660481108527722743': 'file_storage/function-call-16660481108527722743.json', 'var_function-call-16660481108527725918': ['Citations', 'sqlite_sequence'], 'var_function-call-8026237664886157710': 'file_storage/function-call-8026237664886157710.json', 'var_function-call-6945791491886797443': 'file_storage/function-call-6945791491886797443.json', 'var_function-call-12216116696517767484': {'total_citations': 0, 'food_papers_count': 0, 'food_titles': []}}

exec(code, env_args)
