code = """import json

# Load papers
with open(locals()['var_function-call-5992210223060542077'], 'r') as f:
    papers_data = json.load(f)
    # Check if papers_data is a list of dicts or a dict with results
    if isinstance(papers_data, dict) and 'results' in papers_data:
        papers = papers_data['results']
    elif isinstance(papers_data, list):
        papers = papers_data
    else:
        papers = [] # Should not happen based on preview

# Load citations
with open(locals()['var_function-call-13564221464732274520'], 'r') as f:
    citations = json.load(f)

food_papers_titles = set()

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    is_food = False
    
    # Check Title
    if 'food' in title.lower():
        is_food = True
    
    # Check Author Keywords
    if not is_food:
        lower_text = text.lower()
        # Look for Author Keywords block
        start_idx = lower_text.find('author keywords')
        if start_idx != -1:
            # Try to find the end of the keywords section
            # Common next sections
            next_sections = ['acm classification keywords', 'introduction', 'general terms', 'categories and subject descriptors']
            end_idx = -1
            
            # Find the earliest occurrence of a next section
            possible_ends = []
            for ns in next_sections:
                idx = lower_text.find(ns, start_idx)
                if idx != -1:
                    possible_ends.append(idx)
            
            if possible_ends:
                end_idx = min(possible_ends)
            else:
                # Fallback: look for double newline or just take some chars
                end_idx = start_idx + 1000
            
            keywords_text = lower_text[start_idx:end_idx]
            if 'food' in keywords_text:
                is_food = True
    
    if is_food:
        food_papers_titles.add(title)

# Calculate total citations
total_citations = 0
matched_papers_count = 0
for cit in citations:
    if cit['title'] in food_papers_titles:
        try:
            total_citations += int(cit['citation_count'])
            # matched_papers_count += 1 (citations are per year, so this counts records, not papers)
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_papers_count": len(food_papers_titles),
    "total_citations": total_citations,
    "food_paper_titles": list(food_papers_titles)
}))"""

env_args = {'var_function-call-18115772371800026671': 'file_storage/function-call-18115772371800026671.json', 'var_function-call-5992210223060542077': 'file_storage/function-call-5992210223060542077.json', 'var_function-call-13564221464732274520': 'file_storage/function-call-13564221464732274520.json'}

exec(code, env_args)
