code = """import json, re
from statistics import mean

# Load citation records from file
with open(var_call_9UEwXKrKCswT4nhQNJEesoH7, 'r') as f:
    citations = json.load(f)

# Build a map from title to citation_count for 2018
cit_counts_2018 = {rec['title']: int(rec['citation_count']) for rec in citations}

# Load paper docs
with open(var_call_9TL6uXBR79y7yAEEWpBRxCBX, 'r') as f:
    papers = json.load(f)

# Helper to check if a paper is ACM
acm_titles = set()
for doc in papers:
    text = doc.get('text', '')
    # Heuristic: look for 'Copyright' line mentioning ACM or publisher strings
    if re.search(r'Copyright\s+\d{4}.*ACM', text, re.IGNORECASE) or re.search(r'Permission to make digital or hard copies of all or part of this work', text):
        # Also look for venue lines like "CHI '", "Ubicomp", etc followed by ACM
        # But simplest is: if ACM appears near beginning
        if re.search(r'ACM', text[:2000], re.IGNORECASE):
            title = doc.get('filename', '').rsplit('.txt', 1)[0]
            if title:
                acm_titles.add(title)

# Get citation counts for ACM papers in 2018
acm_citations_2018 = [cit_counts_2018[title] for title in cit_counts_2018.keys() if title in acm_titles]

avg_citation = mean(acm_citations_2018) if acm_citations_2018 else 0

result = {"average_citation_count_acm_2018": avg_citation, "paper_count": len(acm_citations_2018)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9UEwXKrKCswT4nhQNJEesoH7': 'file_storage/call_9UEwXKrKCswT4nhQNJEesoH7.json', 'var_call_9TL6uXBR79y7yAEEWpBRxCBX': 'file_storage/call_9TL6uXBR79y7yAEEWpBRxCBX.json'}

exec(code, env_args)
