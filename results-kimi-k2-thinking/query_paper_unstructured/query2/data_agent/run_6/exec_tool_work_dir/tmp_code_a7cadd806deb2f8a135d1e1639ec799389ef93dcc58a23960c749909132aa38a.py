code = """import json
import os
import re

# Assign the stored results to proper variables
citations_key = 'var_functions.query_db:0'
papers_key = 'var_functions.query_db:2'

citations_result = locals()[citations_key]
papers_result = locals()[papers_key]

# Load citations data
citations_data = []
if isinstance(citations_result, str) and citations_result.endswith('.json'):
    with open(citations_result, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_result

# Load papers data  
papers_data = []
if isinstance(papers_result, str) and papers_result.endswith('.json'):
    with open(papers_result, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_result

print(f"Total citations in 2018: {len(citations_data)}")
print(f"Total papers in database: {len(papers_data)}")

# Extract paper metadata
paper_info = []

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Extract source/publisher
    source = None
    text_lower = text.lower()
    if 'acm' in text_lower:
        source = 'ACM'
    elif 'ieee' in text_lower:
        source = 'IEEE'
    elif 'pubmed' in text_lower or 'nih' in text_lower:
        source = 'PubMed'
    
    # Extract year
    year = None
    header_text = text[:1000]
    year_matches = re.findall(r'\b(20\d{2})\b', header_text)
    
    if year_matches:
        current_year = 2024
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= current_year]
        if valid_years:
            year = min(valid_years)
    
    if not year:
        venue_patterns = [r'CHI\s*\'?\s*(20\d{2})', r'Ubicomp\s*\'?\s*(20\d{2})', r'CSCW\s*\'?\s*(20\d{2})',
                          r'DIS\s*\'?\s*(20\d{2})', r'PervasiveHealth\s*\'?\s*(20\d{2})', r'WWW\s*\'?\s*(20\d{2})',
                          r'IUI\s*\'?\s*(20\d{2})', r'OzCHI\s*\'?\s*(20\d{2})', r'TEI\s*\'?\s*(20\d{2})', r'AH\s*\'?\s*(20\d{2})']
        for pattern in venue_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                year_candidate = int(match.group(1))
                if 2000 <= year_candidate <= current_year:
                    year = year_candidate
                    break
    
    paper_info.append({
        'title': title,
        'source': source,
        'year': year,
    })

# Create lookup by title (lowercase)
paper_dict = {}
for p in paper_info:
    paper_dict[p['title'].lower().strip()] = p

# Filter ACM papers from citations
acm_citation_counts = []
matched_count = 0

for citation in citations_data:
    citation_title = citation.get('title', '').lower().strip()
    citation_count = int(citation.get('citation_count', 0))
    
    matching_paper = paper_dict.get(citation_title)
    if matching_paper:
        matched_count += 1
        if matching_paper['source'] == 'ACM':
            acm_citation_counts.append(citation_count)

print(f"Matched citations: {matched_count}")
print(f"ACM papers found: {len(acm_citation_counts)}")

# Calculate average
if acm_citation_counts:
    avg_citation = sum(acm_citation_counts) / len(acm_citation_counts)
    total_citations = sum(acm_citation_counts)
    result = f"Average citation count for ACM papers in 2018: {avg_citation:.2f} based on {len(acm_citation_counts)} papers with {total_citations} total citations"
else:
    result = "No ACM papers found in 2018 citations data"

print("\nSample ACM paper citations:")
count = 0
for citation in citations_data:
    if count >= 3:
        break
    citation_title = citation.get('title', '').lower().strip()
    citation_count = int(citation.get('citation_count', 0))
    paper = paper_dict.get(citation_title)
    if paper and paper['source'] == 'ACM':
        print(f"  {citation.get('title')[:50]}...: {citation_count}")
        count += 1

# Output final result
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
