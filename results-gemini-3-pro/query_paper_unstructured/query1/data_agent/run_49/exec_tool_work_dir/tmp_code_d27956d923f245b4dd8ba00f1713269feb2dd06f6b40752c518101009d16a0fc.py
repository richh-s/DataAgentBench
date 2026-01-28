code = """import json

key_papers = 'var_function-call-8289692166466302904'
key_citations = 'var_function-call-5010856936099612049'

with open(locals()[key_papers], 'r') as f:
    papers = json.load(f)

with open(locals()[key_citations], 'r') as f:
    citations = json.load(f)

food_titles = set()

# Debug lists
debug_titles_found = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    is_food = False
    
    # 1. Check title
    if 'food' in title.lower():
        is_food = True
        
    # 2. Check Keywords if not already found
    if not is_food:
        lower_text = text.lower()
        # Try finding keywords section
        # Priority: Author Keywords -> Keywords
        start_idx = lower_text.find("author keywords")
        if start_idx == -1:
            start_idx = lower_text.find("keywords")
        
        if start_idx != -1:
            # Extract window
            # Usually keywords are at the beginning, but sometimes at end? 
            # In CHI format, they are on first page.
            # Let's take 1000 chars after the match
            window = lower_text[start_idx:start_idx+1000]
            
            # Find end of section
            # Common markers for next section
            next_sections = ["acm classification", "introduction", "general terms", "category", "abstract"]
            end_idx = 1000
            for marker in next_sections:
                idx = window.find(marker)
                # Ensure the marker is after the keyword label itself (which is at index 0 of window basically)
                # But "keywords" is at 0.
                if idx != -1 and idx > 10 and idx < end_idx:
                    end_idx = idx
            
            keywords_text = window[:end_idx]
            if 'food' in keywords_text:
                is_food = True

    if is_food:
        food_titles.add(title)
        debug_titles_found.append(title)

# Filter citations
total_count = 0
matched_citations_count = 0

for c in citations:
    # SQLite might return title with or without extension? 
    # Usually the prompt says "The paper title in the Citations SQLite table matches the filename (without .txt extension)"
    if c['title'] in food_titles:
        try:
            total_count += int(c['citation_count'])
            matched_citations_count += 1
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_count))"""

env_args = {'var_function-call-6408765231398554984': ['paper_docs'], 'var_function-call-6408765231398555607': ['Citations', 'sqlite_sequence'], 'var_function-call-15918017667196444195': 'file_storage/function-call-15918017667196444195.json', 'var_function-call-15918017667196440718': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-211035955538813966': 'file_storage/function-call-211035955538813966.json', 'var_function-call-5010856936099612049': 'file_storage/function-call-5010856936099612049.json', 'var_function-call-9151466501287581759': 0, 'var_function-call-4949709722104029505': 'debug_done', 'var_function-call-2608386440494267822': {'total_papers': 5, 'total_citations': 1405, 'food_titles_in_citations': ['Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture'], 'food_filenames': [], 'first_paper_keywords_idx': 1487, 'first_paper_snippet': 'Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation ', 'papers_with_food_in_keywords': 0}, 'var_function-call-8289692166466302904': 'file_storage/function-call-8289692166466302904.json'}

exec(code, env_args)
