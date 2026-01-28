code = """import json
import re

# Load data from storage
paper_docs_file = locals()['var_functions.query_db:0']
citations_file = locals()['var_functions.query_db:3']

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Read citations
with open(citations_file, 'r') as f:
    citations = json.load(f)

print(f"Loaded {len(paper_docs)} paper documents")
print(f"Loaded {len(citations)} citation records")

# Process paper documents to extract title and domain
def extract_paper_info(doc):
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract domain by searching for domain keywords in text
    # Common domains: "food", "physical activity", "sleep", "mental", etc.
    domain_keywords = [
        'food', 'nutrition', 'diet', 'eating', 'meal', 'calorie',
        'physical activity', 'exercise', 'fitness', 'workout', 'steps', 
        'sleep', 'mental', 'finances', 'productivity', 'screen time',
        'social interactions', 'location', 'chronic', 'diabetes',
        'health_behavior', 'weight'
    ]
    
    # Look for domain mentions in the text (case-insensitive)
    found_domains = []
    text_lower = text.lower()
    
    # Check for multi-word domains first
    if 'physical activity' in text_lower:
        found_domains.append('physical activity')
    if 'social interactions' in text_lower:
        found_domains.append('social interactions')
    if 'screen time' in text_lower:
        found_domains.append('screen time')
    if 'health behavior' in text_lower:
        found_domains.append('health_behavior')
    
    # Check single-word domains
    for keyword in ['food', 'sleep', 'mental', 'location', 'chronic', 'diabetes']:
        if keyword in text_lower:
            found_domains.append(keyword)
    
    # Special cases
    if 'nutrition' in text_lower or 'diet' in text_lower or 'eating' in text_lower or 'meal' in text_lower or 'calorie' in text_lower:
        if 'food' not in found_domains:
            found_domains.append('food')
    
    if 'exercise' in text_lower or 'fitness' in text_lower or 'workout' in text_lower or 'steps' in text_lower:
        if 'physical activity' not in found_domains:
            found_domains.append('physical activity')
    
    # Remove duplicates and join
    domains = list(set(found_domains))
    domain_str = ','.join(domains) if domains else ''
    
    return title, domain_str

# Extract info from all papers
paper_info = []
for doc in paper_docs:
    title, domain = extract_paper_info(doc)
    if title:  # Only include if we have a title
        paper_info.append({
            'title': title,
            'domain': domain
        })

print(f"Processed {len(paper_info)} papers")

# Show some samples
print("\nSample papers with domains:")
for i, paper in enumerate(paper_info[:5]):
    print(f"  {i+1}. {paper['title'][:60]}... | Domains: {paper['domain']}")

# Create a dictionary for easy lookup by title
paper_dict = {p['title']: p['domain'] for p in paper_info}

# Identify food papers and their citations
food_papers = []
total_citations = 0
processed_titles = set()

for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    # Only process each title once (sum all citation years)
    if title not in processed_titles:
        domain = paper_dict.get(title, '')
        if 'food' in domain.lower():
            food_papers.append({
                'title': title,
                'domain': domain,
                'citations': count
            })
            total_citations += count
            processed_titles.add(title)
        # Also sum citations for food papers across years
        elif title in processed_titles and 'food' in domain.lower():
            total_citations += count

print(f"\nFound {len(food_papers)} unique food domain papers")
print(f"Total citation count for food domain papers: {total_citations}")

# Show food papers found
if food_papers:
    print("\nFood domain papers:")
    for paper in food_papers:
        print(f"  - {paper['title'][:60]}... ({paper['citations']} citations)")

# Also sum using a different approach to ensure we capture all citations
# Create mapping of title to total citations
title_to_total_citations = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    title_to_total_citations[title] = title_to_total_citations.get(title, 0) + count

# Sum citations for food papers
food_total_citations = 0
food_paper_titles = []

for title, domain in paper_dict.items():
    if 'food' in domain.lower():
        citations_count = title_to_total_citations.get(title, 0)
        if citations_count > 0:
            food_paper_titles.append(title)
            food_total_citations += citations_count

print(f"\nAlternative calculation:")
print(f"Found {len(food_paper_titles)} food papers with citations")
print(f"Total citation count for food domain: {food_total_citations}")

# Prepare result
result = {
    'total_citation_count': food_total_citations,
    'food_papers_count': len(food_paper_titles)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
