code = """import json

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
    
    # Simple substring search for keywords section
    lower_text = text.lower()
    start_idx = lower_text.find("author keywords")
    if start_idx == -1:
        start_idx = lower_text.find("keywords")
    
    if start_idx != -1:
        # Extract next 500 chars
        snippet = lower_text[start_idx:start_idx+500]
        # Check if "food" is in this snippet
        # We should be careful not to match "food" in the next section's body text if the keywords are short
        # But usually keywords are followed by "ACM Classification" or "Introduction"
        # Let's truncate at "introduction" or "abstract" if they appear
        end_idx = snippet.find("introduction")
        if end_idx != -1:
            snippet = snippet[:end_idx]
        
        # Also check for "acm classification"
        end_idx2 = snippet.find("acm classification")
        if end_idx2 != -1:
            snippet = snippet[:end_idx2]
            
        if "food" in snippet:
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
