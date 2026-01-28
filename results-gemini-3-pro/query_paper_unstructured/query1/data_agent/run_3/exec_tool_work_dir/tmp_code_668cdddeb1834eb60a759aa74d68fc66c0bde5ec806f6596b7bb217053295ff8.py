code = """import json
import re

with open(locals()['var_function-call-8384665205253997752'], 'r') as f:
    paper_docs = json.load(f)

print("__RESULT__:")
debug_info = {}
debug_info['titles'] = [d['filename'] for d in paper_docs[:10]]

# Check keywords extraction for the first paper
text0 = paper_docs[0]['text']
match = re.search(r'(Author Keywords|Keywords)([\s\S]{1,500}?)(INTRODUCTION|ACM Classification|ABSTRACT)', text0, re.IGNORECASE)
debug_info['keywords_extraction_sample'] = match.group(0) if match else "No match"

# Find papers with 'food' in text
food_in_text = []
for doc in paper_docs:
    if 'food' in doc['text'].lower():
        food_in_text.append(doc['filename'])

debug_info['papers_with_food_in_text'] = food_in_text[:20] # Limit to 20
debug_info['count_food_in_text'] = len(food_in_text)

print(json.dumps(debug_info))"""

env_args = {'var_function-call-5922621878014711528': ['paper_docs'], 'var_function-call-11455490410163430330': 'file_storage/function-call-11455490410163430330.json', 'var_function-call-8384665205253997752': 'file_storage/function-call-8384665205253997752.json', 'var_function-call-10278166770112498048': 'file_storage/function-call-10278166770112498048.json', 'var_function-call-2640047506381148300': {'food_titles': [], 'total_citations': 0, 'count_of_citation_records': 0}}

exec(code, env_args)
