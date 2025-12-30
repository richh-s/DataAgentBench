code = """import json

# Load papers
with open(locals()['var_function-call-8026237664886157710'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-6945791491886797443'], 'r') as f:
    citations = json.load(f)

food_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Author Keywords
    # Heuristic: look for "Author Keywords" and take text until "ACM Classification Keywords" or "INTRODUCTION"
    # Or just search for "food" in the whole text?
    # The prompt says "For each paper, you may need to extract: ... domain". And "Common domains include: 'food'...".
    # And "Fields like domain ... may contain multiple values".
    # The sample paper showed domains in Author Keywords.
    # Let's try to find "Author Keywords"
    
    lower_text = text.lower()
    start_marker = "author keywords"
    end_markers = ["acm classification keywords", "introduction", "general terms", "abstract"] 
    # abstract usually comes before, but sometimes formatting varies. 
    # Usually "Author Keywords" is followed by "ACM Classification Keywords" or "Introduction".
    
    start_idx = lower_text.find(start_marker)
    if start_idx != -1:
        # found section
        content = lower_text[start_idx + len(start_marker):]
        # find nearest end marker
        nearest_end = len(content)
        for end_m in end_markers:
            idx = content.find(end_m)
            if idx != -1 and idx < nearest_end:
                nearest_end = idx
        
        keywords_section = content[:nearest_end]
        
        # Check for 'food' in keywords section
        if "food" in keywords_section:
            food_titles.append(title)
            
    else:
        # If no explicit "Author Keywords" section found, what should I do?
        # Maybe the paper is not in the domain, or format is different.
        # Given the "Common domains include" hint, it strongly suggests keywords.
        # However, let's check if the title contains "food" as well, just in case.
        if "food" in title.lower():
             food_titles.append(title)

# Filter citations
total_citations = 0
matched_papers_count = 0

# Create a set for faster lookup
food_titles_set = set(food_titles)

for citation in citations:
    c_title = citation.get('title')
    c_count = int(citation.get('citation_count', 0))
    
    if c_title in food_titles_set:
        total_citations += c_count

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_papers_count": len(food_titles_set), "food_titles": list(food_titles_set)}))"""

env_args = {'var_function-call-16660481108527722743': 'file_storage/function-call-16660481108527722743.json', 'var_function-call-16660481108527725918': ['Citations', 'sqlite_sequence'], 'var_function-call-8026237664886157710': 'file_storage/function-call-8026237664886157710.json', 'var_function-call-6945791491886797443': 'file_storage/function-call-6945791491886797443.json'}

exec(code, env_args)
