code = """import json

# Load previous results
with open(locals()['var_function-call-16127451980327638428'], 'r') as f:
    citations_data = json.load(f)
with open(locals()['var_function-call-8746704567039347738'], 'r') as f:
    papers_data = json.load(f)

# Build citation map
citation_map = {}
for row in citations_data:
    t = row['title'].strip()
    try:
        c = int(row['citation_count'])
    except:
        c = 0
    citation_map[t] = citation_map.get(t, 0) + c

# Check citations for food titles
food_titles_from_citations = [t for t in citation_map.keys() if 'food' in t.lower()]

# Check papers
food_papers_from_text = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    if not filename: continue
    title = filename.replace('.txt', '').strip()
    
    # Criteria 1: Title
    if 'food' in title.lower():
        food_papers_from_text.append(title)
        continue

    # Criteria 2: Keywords (Simplified)
    lower_text = text.lower()
    # Find keywords section
    # Let's just look for the line starting with "Keywords" or "Author Keywords"
    # and check if "food" is in that line or next few lines
    # Instead of complex parsing, let's just check if "food" is near "keywords"
    # e.g. within 500 chars after "keywords"
    
    found_in_keywords = False
    for kw in ["author keywords", "keywords", "index terms"]:
        idx = lower_text.find(kw)
        if idx != -1:
            snippet = lower_text[idx:idx+600] # Capture the header and following text
            if "food" in snippet:
                found_in_keywords = True
                break
    
    if found_in_keywords:
        food_papers_from_text.append(title)
        continue

    # Criteria 3: Abstract
    # Find "ABSTRACT" and check next 1500 chars
    idx = lower_text.find("abstract")
    if idx != -1:
        snippet = lower_text[idx:idx+1500]
        if "food" in snippet:
            # We need to be careful. "food" might be just a word.
            # But combined with the fact that these papers were pre-filtered for "food",
            # if it's in the abstract, it's likely relevant.
            food_papers_from_text.append(title)
            continue

# Union of titles
all_food_titles = set(food_titles_from_citations + food_papers_from_text)

# Filter to only those in the 'papers_data' (confirmed existing papers) OR 'citations_map' (if we trust title)
# Actually, we should only count papers that we are sure about.
# The user asks for "papers in the 'food' domain".
# If I have a title "Food Logging...", it's definitely food domain.
# If I have a paper "Tracking..." and Abstract mentions "food", it's likely.
# I'll stick to the set of titles identified.

total_citations = 0
final_list = []
for t in all_food_titles:
    # Only count if we have citation data
    if t in citation_map:
        total_citations += citation_map[t]
        final_list.append(t)

print("__RESULT__:")
print(json.dumps({
    "total_citations": total_citations, 
    "count_food_papers": len(final_list), 
    "titles": final_list
}))"""

env_args = {'var_function-call-15196932222380505955': ['paper_docs'], 'var_function-call-15196932222380506622': ['Citations', 'sqlite_sequence'], 'var_function-call-6668322733122569881': 'file_storage/function-call-6668322733122569881.json', 'var_function-call-14852506911843357885': 'file_storage/function-call-14852506911843357885.json', 'var_function-call-8746704567039347738': 'file_storage/function-call-8746704567039347738.json', 'var_function-call-8559390036236620901': [{'count(*)': '1405'}], 'var_function-call-16127451980327638428': 'file_storage/function-call-16127451980327638428.json', 'var_function-call-5888591959133731476': {'total_citations': 270, 'count_food_papers': 1, 'matched_citations': 1, 'sample_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling']}}

exec(code, env_args)
