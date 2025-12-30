code = """import json
import re

# Load paper docs
with open(locals()['var_function-call-8384665205253997752'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-10278166770112498048'], 'r') as f:
    citations = json.load(f)

# Identify food papers
food_titles = set()

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
        
    # Check keywords in text
    match = re.search(r'(Author Keywords|Keywords)([\s\S]{1,500}?)(INTRODUCTION|ACM Classification|ABSTRACT)', text, re.IGNORECASE)
    if match:
        keywords_block = match.group(2)
        if 'food' in keywords_block.lower():
            food_titles.add(title)
            continue

# Filter citations
total_citations = 0
citation_count = 0

for cit in citations:
    if cit['title'] in food_titles:
        try:
            total_citations += int(cit['citation_count'])
            citation_count += 1
        except ValueError:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_titles": list(food_titles),
    "total_citations": total_citations,
    "count_of_citation_records": citation_count
}))"""

env_args = {'var_function-call-5922621878014711528': ['paper_docs'], 'var_function-call-11455490410163430330': 'file_storage/function-call-11455490410163430330.json', 'var_function-call-8384665205253997752': 'file_storage/function-call-8384665205253997752.json', 'var_function-call-10278166770112498048': 'file_storage/function-call-10278166770112498048.json'}

exec(code, env_args)
