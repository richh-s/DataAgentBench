code = """import json
import re

# Load paper docs
with open(locals()['var_function-call-11391268532651985749'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-9528525890526779817'], 'r') as f:
    citations = json.load(f)

food_papers = set()

# Regex pattern
# We use \\n for newlines in the regex string just to be safe with the tool's string handling
pattern = re.compile(r'(Author Keywords|Keywords)\s*([\s\S]*?)(?:\n\n|ACM Classification|INTRODUCTION|ABSTRACT)', re.IGNORECASE)

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    keywords_text = ""
    match = pattern.search(text)
    
    if match:
        keywords_text = match.group(2)
    else:
        # Fallback
        match2 = re.search(r'Keywords:\s*(.*)', text, re.IGNORECASE)
        if match2:
            keywords_text = match2.group(1)
            
    if "food" in keywords_text.lower():
        food_papers.add(title)

total_citations = 0
for cit in citations:
    if cit['title'] in food_papers:
        try:
            count = int(cit['citation_count'])
            total_citations += count
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_papers_count": len(food_papers),
    "total_citations": total_citations,
    "sample_food_papers": list(food_papers)[:5]
}))"""

env_args = {'var_function-call-2084014560423739449': 'file_storage/function-call-2084014560423739449.json', 'var_function-call-11352259319045470857': 'file_storage/function-call-11352259319045470857.json', 'var_function-call-9528525890526779817': 'file_storage/function-call-9528525890526779817.json', 'var_function-call-11391268532651985749': 'file_storage/function-call-11391268532651985749.json'}

exec(code, env_args)
