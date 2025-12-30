code = """import json

# Load papers
with open(locals()['var_function-call-7936328187832548215'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-6945791491886797443'], 'r') as f:
    citations = json.load(f)

food_titles = []
debug_keywords = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    start_idx = text.find("author keywords")
    if start_idx != -1:
        sub = text[start_idx+15:]
        end_idx = len(sub)
        # Check markers
        for marker in ["acm classification", "introduction", "general terms", "abstract"]:
            idx = sub.find(marker)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        
        keywords = sub[:end_idx]
        
        if "food" in keywords:
            food_titles.append(title)
            if len(debug_keywords) < 5:
                debug_keywords.append((title, keywords))

# Sum citations
total_citations = 0
food_titles_set = set(food_titles)

for citation in citations:
    if citation['title'] in food_titles_set:
        total_citations += int(citation['citation_count'])

print("__RESULT__:")
print(json.dumps({
    "total_citations": total_citations,
    "food_papers_count": len(food_titles),
    "sample_food_titles": food_titles[:5]
}))"""

env_args = {'var_function-call-16660481108527722743': 'file_storage/function-call-16660481108527722743.json', 'var_function-call-16660481108527725918': ['Citations', 'sqlite_sequence'], 'var_function-call-8026237664886157710': 'file_storage/function-call-8026237664886157710.json', 'var_function-call-6945791491886797443': 'file_storage/function-call-6945791491886797443.json', 'var_function-call-12216116696517767484': {'total_citations': 0, 'food_papers_count': 0, 'food_titles': []}, 'var_function-call-11714859170304537355': [], 'var_function-call-14747132790696887913': [['A Lived Informatics Model of Personal Informatics.txt', 13], ['A Stage-based Model of Personal Informatics Systems.txt', 13], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 1]], 'var_function-call-4996250190729561735': 5, 'var_function-call-7936328187832548215': 'file_storage/function-call-7936328187832548215.json'}

exec(code, env_args)
