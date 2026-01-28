code = """import json
import re

# Load paper docs
with open(locals()['var_function-call-11391268532651985749'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-9528525890526779817'], 'r') as f:
    citations = json.load(f)

food_papers = set()

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Try to find keywords
    # Pattern to capture text after "Author Keywords" or "Keywords" until double newline or next section
    # Note: The text layout might vary. 
    # Let's look for "Author Keywords" or "Keywords" and take the next few lines.
    
    match = re.search(r'(Author Keywords|Keywords)\s*([\s\S]*?)(?:\n\n|ACM Classification|INTRODUCTION|ABSTRACT)', text, re.IGNORECASE)
    
    keywords_text = ""
    if match:
        keywords_text = match.group(2)
    else:
        # Fallback: Maybe it's just labelled "Keywords:"
        match2 = re.search(r'Keywords:\s*(.*)', text, re.IGNORECASE)
        if match2:
            keywords_text = match2.group(1)
    
    # Check for "food"
    if "food" in keywords_text.lower():
        food_papers.add(title)

# Filter citations
total_citations = 0
matched_citation_records = 0

for cit in citations:
    if cit['title'] in food_papers:
        # citation_count is string in the preview, convert to int
        try:
            count = int(cit['citation_count'])
            total_citations += count
            matched_citation_records += 1
        except ValueError:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_papers_count": len(food_papers),
    "matched_citation_records": matched_citation_records,
    "total_citations": total_citations,
    "sample_food_papers": list(food_papers)[:5]
}))"""

env_args = {'var_function-call-2084014560423739449': 'file_storage/function-call-2084014560423739449.json', 'var_function-call-11352259319045470857': 'file_storage/function-call-11352259319045470857.json', 'var_function-call-9528525890526779817': 'file_storage/function-call-9528525890526779817.json', 'var_function-call-11391268532651985749': 'file_storage/function-call-11391268532651985749.json'}

exec(code, env_args)
