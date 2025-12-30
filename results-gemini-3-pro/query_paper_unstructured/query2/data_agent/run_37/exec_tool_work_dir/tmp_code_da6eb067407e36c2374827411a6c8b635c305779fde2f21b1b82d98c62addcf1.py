code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-9421256355430255115']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create a lookup for citation count by title
# Filter is already applied for citation_year=2018
citation_map = {}
for item in citations_data:
    citation_map[item['title']] = item['citation_count']

# Load papers
papers_path = locals()['var_function-call-9421256355430255910']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

acm_citations = []

def get_source(text):
    # Simple heuristic based on hints and preview
    text_upper = text.upper()
    if "ACM" in text_upper or "ASSOCIATION FOR COMPUTING MACHINERY" in text_upper:
        # Check if IEEE is also present, might be a reference.
        # But usually copyright info is at the start or end.
        # Let's check for specific ACM markers
        if "ACM CLASSIFICATION KEYWORDS" in text_upper:
            return "ACM"
        if "COPYRIGHT" in text_upper and "ACM" in text_upper:
            return "ACM"
        if "PERMISSION" in text_upper and "ACM" in text_upper:
            return "ACM"
        # Fallback if just ACM is mentioned (could be risky if it's just in text)
        # But let's assume if it mentions ACM it's likely ACM unless IEEE is stronger.
        if "IEEE" not in text_upper:
            return "ACM"
            
    if "IEEE" in text_upper:
         if "COPYRIGHT" in text_upper and "IEEE" in text_upper:
            return "IEEE"
         if "ACM" not in text_upper:
             return "IEEE"
             
    # Default to unknown or ambiguous
    # If both are present, we might need a tie breaker, but for this specific task
    # let's count occurrences or look at the first 1000 chars.
    head = text_upper[:2000]
    if "ACM" in head and "IEEE" not in head:
        return "ACM"
    if "IEEE" in head and "ACM" not in head:
        return "IEEE"
        
    return "UNKNOWN"

count_acm_papers = 0
found_titles = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    
    # Check if this paper was cited in 2018
    if title in citation_map:
        text = paper.get('text', '')
        source = get_source(text)
        
        if source == "ACM":
            count = citation_map[title]
            # count might be a string or int depending on SQL result format? 
            # SQLite tool usually returns values as is, but let's ensure it's int.
            # Looking at the preview: "citation_count": "95" (it's a string!)
            # Wait, the preview shows strings. SQLite might return strings if not typed strictly?
            # Or the tool serialization makes it string?
            # Let's cast to int.
            acm_citations.append(int(count))
            found_titles.append(title)

# Calculate average
if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps({"average_citations": avg_citations, "count": len(acm_citations), "found_titles_sample": found_titles[:5]}))"""

env_args = {'var_function-call-9421256355430255115': 'file_storage/function-call-9421256355430255115.json', 'var_function-call-9421256355430255910': 'file_storage/function-call-9421256355430255910.json'}

exec(code, env_args)
