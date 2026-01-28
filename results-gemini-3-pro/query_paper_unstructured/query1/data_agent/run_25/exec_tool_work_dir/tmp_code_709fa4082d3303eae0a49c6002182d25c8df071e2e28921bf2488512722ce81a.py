code = """import json
import re

# Load data
with open(locals()['var_function-call-17486704262329443494'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-9673377435246489263'], 'r') as f:
    papers_data = json.load(f)

# Aggregate citations by title
citation_sums = {}
for entry in citations_data:
    title = entry['title']
    count = entry['citation_count']
    # citation_count might be string or int based on preview
    if isinstance(count, str):
        count = int(count)
    citation_sums[title] = citation_sums.get(title, 0) + count

# Identify food papers
food_papers = []
total_citations = 0

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    title_from_file = filename.replace('.txt', '')
    
    # Extract domain
    # Try to find Author Keywords
    # Pattern: Author Keywords followed by text until next section
    # Next sections often: ACM Classification Keywords, INTRODUCTION, General Terms
    keywords_match = re.search(r'Author Keywords(.*?)(?:ACM Classification Keywords|INTRODUCTION|General Terms|$)', text, re.DOTALL | re.IGNORECASE)
    
    is_food = False
    
    if keywords_match:
        keywords = keywords_match.group(1).lower()
        if 'food' in keywords:
            is_food = True
    else:
        # Fallback to title
        if 'food' in title_from_file.lower():
            is_food = True
            
    # Also check if "food" is in the text if we want to be more inclusive as per hints?
    # Hint: "Fields like domain ... may contain multiple values ... use substring/contains matching"
    # But usually domain is a specific field.
    # Let's double check if we can parse "Domain" field?
    # The database description says: "For each paper, you may need to extract: ... domain: ..."
    # It doesn't say "Domain:" field exists. It lists it as a field to extract.
    # The sample text didn't have "Domain:". It had "Author Keywords".
    # Let's stick to Author Keywords and Title. 
    # Actually, looking at the sample, "Author Keywords" contained "Physical Activity; Finances; Location".
    # These are exactly the domains listed in the description. 
    # So "Author Keywords" is the primary source.
    
    # Just in case, if "food" is not in keywords but is in title, we count it.
    
    if is_food:
        food_papers.append(title_from_file)
        # Add citations if title matches
        if title_from_file in citation_sums:
            total_citations += citation_sums[title_from_file]

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-16442091982687073941': 'file_storage/function-call-16442091982687073941.json', 'var_function-call-8772526442893089747': 'file_storage/function-call-8772526442893089747.json', 'var_function-call-9673377435246489263': 'file_storage/function-call-9673377435246489263.json', 'var_function-call-17486704262329443494': 'file_storage/function-call-17486704262329443494.json'}

exec(code, env_args)
