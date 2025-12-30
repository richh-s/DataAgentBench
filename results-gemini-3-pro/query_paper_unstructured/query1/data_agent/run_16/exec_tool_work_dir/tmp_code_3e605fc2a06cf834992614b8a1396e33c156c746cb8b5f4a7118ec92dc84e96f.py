code = """import json

# Load previous results
with open(locals()['var_function-call-16127451980327638428'], 'r') as f:
    citations_data = json.load(f)
with open(locals()['var_function-call-8746704567039347738'], 'r') as f:
    papers_data = json.load(f)

# Build citation map: title -> total_count
citation_map = {}
for row in citations_data:
    t = row['title'].strip()
    try:
        c = int(row['citation_count'])
    except:
        c = 0
    citation_map[t] = citation_map.get(t, 0) + c

food_papers = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    if not filename: continue
    title = filename.replace('.txt', '').strip()
    
    is_food = False
    
    # Check 1: Title
    if 'food' in title.lower():
        is_food = True
    
    # Check 2: Keywords
    if not is_food:
        lower_text = text.lower()
        keywords_headers = ["author keywords", "index terms", "keywords", "general terms"]
        
        for header in keywords_headers:
            idx = lower_text.find(header)
            if idx != -1:
                snippet = lower_text[idx+len(header):idx+500]
                # Avoid using explicit newline character in the list to prevent syntax errors in tool
                for marker in ["introduction", "acm classification", "1."]:
                    m_idx = snippet.find(marker)
                    if m_idx != -1:
                        snippet = snippet[:m_idx]
                
                if "food" in snippet:
                    is_food = True
                break
    
    if is_food:
        food_papers.append(title)

# Calculate total citations
total_citations = 0
found_count = 0
matched_titles = []

for t in food_papers:
    if t in citation_map:
        total_citations += citation_map[t]
        found_count += 1
        matched_titles.append(t)

print("__RESULT__:")
print(json.dumps({
    "total_citations": total_citations, 
    "count_food_papers": len(food_papers), 
    "matched_citations": found_count, 
    "sample_titles": matched_titles[:5]
}))"""

env_args = {'var_function-call-15196932222380505955': ['paper_docs'], 'var_function-call-15196932222380506622': ['Citations', 'sqlite_sequence'], 'var_function-call-6668322733122569881': 'file_storage/function-call-6668322733122569881.json', 'var_function-call-14852506911843357885': 'file_storage/function-call-14852506911843357885.json', 'var_function-call-8746704567039347738': 'file_storage/function-call-8746704567039347738.json', 'var_function-call-8559390036236620901': [{'count(*)': '1405'}], 'var_function-call-16127451980327638428': 'file_storage/function-call-16127451980327638428.json'}

exec(code, env_args)
