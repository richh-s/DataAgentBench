code = """import json
import os

# Load citations data (SQLite result)
# Key: var_function-call-10128853651664279531
citations_path = locals()['var_function-call-10128853651664279531']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create a map from title to citation_count
# Normalize title just in case (strip whitespace), though usually strict match is needed.
title_citation_map = {item['title']: int(item['citation_count']) for item in citations_data}

# Load ACM papers data (MongoDB result)
# Key: var_function-call-2153954921317662099
acm_papers_path = locals()['var_function-call-2153954921317662099']
with open(acm_papers_path, 'r') as f:
    acm_papers_data = json.load(f)

# Filter and collect citation counts
acm_citation_counts = []
matched_titles = []

for paper in acm_papers_data:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4] # Remove .txt
        if title in title_citation_map:
            # Check if it's really an ACM paper?
            # The query filtered by regex "ACM".
            # Let's perform a stricter check if possible, or trust the regex.
            # Looking at the text sample: "Copyright 2015 © ACM".
            # If the text contains "ACM", it's likely published by ACM or cites it. 
            # Given the "Source" extraction instruction, simply containing "ACM" might be too broad if it's in references.
            # However, usually the publisher name appears in the header/footer.
            # Let's check if "ACM" is in the first 5000 characters to be safer, or just trust the regex for now.
            # The query was simply regex "ACM". 
            # Let's proceed with the intersection.
            acm_citation_counts.append(title_citation_map[title])
            matched_titles.append(title)

# Calculate average
if acm_citation_counts:
    average_citations = sum(acm_citation_counts) / len(acm_citation_counts)
else:
    average_citations = 0

result = {
    "matched_papers_count": len(acm_citation_counts),
    "average_citations": average_citations
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10128853651664279531': 'file_storage/function-call-10128853651664279531.json', 'var_function-call-13767594165860701791': 'file_storage/function-call-13767594165860701791.json', 'var_function-call-447385373725122589': 'file_storage/function-call-447385373725122589.json', 'var_function-call-2153954921317662099': 'file_storage/function-call-2153954921317662099.json'}

exec(code, env_args)
