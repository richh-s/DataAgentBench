code = """import json
import re

# Load previous results
with open(locals()['var_function-call-16127451980327638428'], 'r') as f:
    citations_data = json.load(f)
with open(locals()['var_function-call-8746704567039347738'], 'r') as f:
    papers_data = json.load(f)

# Build citation map: title -> total_count
citation_map = {}
for row in citations_data:
    t = row['title'].strip()
    c = int(row['citation_count'])
    citation_map[t] = citation_map.get(t, 0) + c

food_papers = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '').strip()
    
    is_food = False
    
    # Check 1: Title
    if 'food' in title.lower():
        is_food = True
    
    if not is_food:
        lower_text = text.lower()
        # Check Keywords
        # Try to find "Author Keywords" or "Keywords" or "Index Terms"
        # We will look for these headers and check the text immediately following them.
        # We'll take a window of text after the header.
        keywords_headers = ["author keywords", "index terms", "keywords", "general terms"]
        
        for header in keywords_headers:
            idx = lower_text.find(header)
            if idx != -1:
                # Look at the text after the header, say 500 characters
                snippet = lower_text[idx+len(header):idx+500]
                # Stop at the next likely header to avoid reading too far
                # Common next headers: "introduction", "acm classification", "abstract" (unlikely after), "1. introduction"
                end_markers = ["introduction", "acm classification", "1.", "\n\n\n"]
                min_end = len(snippet)
                for end_marker in end_markers:
                    end_idx = snippet.find(end_marker)
                    if end_idx != -1 and end_idx < min_end:
                        min_end = end_idx
                
                valid_snippet = snippet[:min_end]
                if "food" in valid_snippet:
                    is_food = True
                break
    
    # Check 3: Abstract (if not found in keywords)
    # Some papers might not have explicit keywords but are about food.
    # We can check the Abstract. Abstract usually comes after "ABSTRACT" and before "INTRODUCTION".
    if not is_food:
        lower_text = text.lower()
        abs_idx = lower_text.find("abstract")
        if abs_idx != -1:
            snippet = lower_text[abs_idx+8:abs_idx+2000] # 2000 chars window
            # Stop at Introduction
            intro_idx = snippet.find("introduction")
            if intro_idx != -1:
                snippet = snippet[:intro_idx]
            
            # Check for food in abstract
            # But we must be careful. "food" might be mentioned as an example.
            # "study of food tracking" -> YES
            # "similar to food tracking" -> MAYBE NOT
            # To be safe, let's rely on Keywords and Title primarily. 
            # If I miss some, it's better than false positives.
            # However, the hint "Common domains include: 'food'" suggests it's a category.
            # If I only check Title/Keywords, I might miss papers.
            # Let's count how many I found so far.
            pass

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
    else:
        # Try case insensitive match?
        # The DB description says title matches filename.
        # But let's try.
        pass

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "count_food_papers": len(food_papers), "matched_citations": found_count, "sample_titles": matched_titles[:5]}))"""

env_args = {'var_function-call-15196932222380505955': ['paper_docs'], 'var_function-call-15196932222380506622': ['Citations', 'sqlite_sequence'], 'var_function-call-6668322733122569881': 'file_storage/function-call-6668322733122569881.json', 'var_function-call-14852506911843357885': 'file_storage/function-call-14852506911843357885.json', 'var_function-call-8746704567039347738': 'file_storage/function-call-8746704567039347738.json', 'var_function-call-8559390036236620901': [{'count(*)': '1405'}], 'var_function-call-16127451980327638428': 'file_storage/function-call-16127451980327638428.json'}

exec(code, env_args)
