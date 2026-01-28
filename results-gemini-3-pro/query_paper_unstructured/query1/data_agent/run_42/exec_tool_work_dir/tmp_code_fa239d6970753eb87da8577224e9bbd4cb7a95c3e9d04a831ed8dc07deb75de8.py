code = """import json
import re

# Load papers (filtered by regex 'food' from DB)
with open(locals()['var_function-call-18282859333790879824'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-1190130121296070370'], 'r') as f:
    citations = json.load(f)

food_titles = set()

# Helper to check keywords
def has_food_keyword(text):
    text_lower = text.lower()
    # Find start
    # Common keyword headers
    start_match = re.search(r'(author keywords|keywords|index terms|general terms)', text_lower)
    if not start_match:
        # Fallback: maybe it's just "Keywords" at the start of a line?
        pass
        return False
    
    start_idx = start_match.end()
    
    # Heuristic: Take next 2000 chars 
    chunk = text_lower[start_idx:start_idx+2000]
    
    # Truncate at common next sections
    stop_words = ['introduction', 'acm classification', 'categories and subject descriptors', 'general terms', 'reference', 'abstract']
    min_stop_idx = len(chunk)
    for sw in stop_words:
        # We want to find these words when they are likely headers (e.g. at start of line or preceded by newlines)
        # But simple find is safer to avoid missing.
        idx = chunk.find(sw)
        if idx != -1 and idx < min_stop_idx:
            # check if it's "categories and subject descriptors" which often follows keywords
            min_stop_idx = idx
            
    keywords_section = chunk[:min_stop_idx]
    
    # Check for "food"
    return 'food' in keywords_section

for p in papers:
    filename = p.get('filename', '')
    title = filename.replace('.txt', '').strip()
    text = p.get('text', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
        
    # Check keywords
    if has_food_keyword(text):
        food_titles.add(title)

# Filter citations and sum
total_citations = 0
matched_papers = set()

for c in citations:
    c_title = c.get('title', '').strip()
    if c_title in food_titles:
        try:
            count = int(c.get('citation_count', 0))
            total_citations += count
            matched_papers.add(c_title)
        except ValueError:
            pass

print("__RESULT__:")
print(json.dumps({
    "total_citations": total_citations,
    "food_paper_count": len(food_titles),
    "matched_papers_list": list(matched_papers)
}))"""

env_args = {'var_function-call-14800347907700836141': 'file_storage/function-call-14800347907700836141.json', 'var_function-call-1190130121296070370': 'file_storage/function-call-1190130121296070370.json', 'var_function-call-1190130121296070935': 'file_storage/function-call-1190130121296070935.json', 'var_function-call-16405168858787139098': {'total_citations': 0, 'food_paper_count': 0, 'matched_citations_records': 0, 'matched_papers_in_citations': 0}, 'var_function-call-18164685780746731910': {'total_papers': 5, 'sample_titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'food_titles_sample': [], 'sample_keyword_chunk': ' \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., hci). \n\nintroduction \npersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  increasingly  prevalent.  personal \ninformatics can serve a goal-driven purpose, such as tracking \nweight loss, increasing physical activity, having a record of \nplaces  visited,  or  tracking  s'}, 'var_function-call-18282859333790879824': 'file_storage/function-call-18282859333790879824.json'}

exec(code, env_args)
