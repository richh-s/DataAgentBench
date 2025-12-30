code = """import json
import re

# Load data
citations = json.load(open('citations_database_Citations.json')) # Using the variable key would be better but I don't know the exact filename mapping for the previous large output unless I use the variable provided.
# Actually I should use the variable names provided in previous steps or just open the files if I knew the path. 
# The system said: "The file path is stored under key: var_function-call-..."
# I need to look up the keys from previous turns.
# Turn 2 (citations): var_function-call-99245770254800995
# Turn 3 (paper_docs): var_function-call-5874155478376628757

citations_path = locals()['var_function-call-99245770254800995']
papers_path = locals()['var_function-call-5874155478376628757']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers = []
debug_info = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Try to find Author Keywords
    # Pattern: Author Keywords (capture until next section)
    # Next section usually starts with all caps or specific headers
    
    match = re.search(r"Author Keywords\s*[:\n]\s*(.*?)(?:\n\n|\n[A-Z ]{5,}|\nACM Classification Keywords)", text, re.DOTALL | re.IGNORECASE)
    
    keywords = ""
    if match:
        keywords = match.group(1).replace('\n', ' ')
        
    # Check if 'food' is in keywords
    # Be careful with "food" as a substring of "non-food"
    # Split by ; or ,
    kw_list = [k.strip().lower() for k in re.split(r'[;,]', keywords)]
    
    is_food = False
    for k in kw_list:
        if 'food' in k: # Substring match as per hint
            is_food = True
            break
            
    if is_food:
        food_papers.append(title)
        
    # debug_info.append({"title": title, "keywords": keywords, "is_food": is_food})

# Now sum citations
total_citations = 0
for cit in citations:
    if cit['title'] in food_papers:
        # Check if citation_count is int or str
        count = cit['citation_count']
        if isinstance(count, str):
            if count.strip() == '': count = 0
            else: count = int(count)
        total_citations += count

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_paper_count": len(food_papers), "food_papers": food_papers}))"""

env_args = {'var_function-call-853909438841445340': 'file_storage/function-call-853909438841445340.json', 'var_function-call-1978902813264061650': 'file_storage/function-call-1978902813264061650.json', 'var_function-call-99245770254800995': 'file_storage/function-call-99245770254800995.json', 'var_function-call-5874155478376628757': 'file_storage/function-call-5874155478376628757.json'}

exec(code, env_args)
