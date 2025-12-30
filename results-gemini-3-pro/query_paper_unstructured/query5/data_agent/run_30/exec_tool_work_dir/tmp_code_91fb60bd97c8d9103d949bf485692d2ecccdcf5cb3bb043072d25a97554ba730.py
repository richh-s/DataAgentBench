code = """import json
import re

with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-4121090962908109712'], 'r') as f:
    paper_docs_data = json.load(f)

paper_map = {}
for doc in paper_docs_data:
    if 'filename' in doc:
        title = doc['filename'].replace('.txt', '')
        paper_map[title] = doc['text']

total_citations = 0
chi_papers_count = 0
matched_titles = []

for record in citations_data:
    title = record['title']
    if title in paper_map:
        text = paper_map[title]
        # Search whole text for CHI venue indicators
        # Use simple string checks first
        if "CHI " in text[:2000] or "CHI '" in text[:2000] or "Conference on Human Factors in Computing Systems" in text[:2000]:
             # Additional check to ensure it's not just a random word
             # Look for "CHI" with boundaries using regex
             if re.search(r'\bCHI\b', text[:2000]):
                 count = int(record['citation_count'])
                 total_citations += count
                 chi_papers_count += 1
                 matched_titles.append(title)

result = {
    "total_citations": total_citations,
    "chi_papers_count": chi_papers_count,
    "matched_titles_preview": matched_titles[:3]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json', 'var_function-call-5326245820750148638': 16}

exec(code, env_args)
