code = """import json
import os
import re

# Load the citation data from stored variable
citations_var = locals()['var_functions.query_db:0']
if isinstance(citations_var, str) and citations_var.endswith('.json'):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_var

# Load the paper documents from stored variable
papers_var = locals()['var_functions.query_db:2']
if isinstance(papers_var, str) and papers_var.endswith('.json'):
    with open(papers_var, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_var

print(f"Total citations in 2018: {len(citations_data)}")
print(f"Total papers in database: {len(papers_data)}")

# Extract paper information (title, source, year) from documents
paper_info = []

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
    else:
        title = filename
    
    # Extract source (publisher) from text
    source = None
    text_lower = text.lower()
    if 'acm' in text_lower and ('association for computing machinery' in text_lower or 'acm' in text_lower):
        source = 'ACM'
    elif 'ieee' in text_lower:
        source = 'IEEE'
    elif 'pubmed' in text_lower or 'nih' in text_lower or 'pub med' in text_lower:
        source = 'PubMed'
    
    # Extract year from text (look for common patterns)
    year = None
    
    # Look for year in the first part of the text (header area)
    header_text = text[:1000]  # First 1000 characters
    year_matches = re.findall(r'\b(20\d{2})\b', header_text)
    
    if year_matches:
        # Try to find the most reasonable year (not too old, not in the future)
        current_year = 2024
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= current_year]
        if valid_years:
            year = min(valid_years)  # Take the earliest reasonable year (publication year)
    
    # Also check for common venue patterns that might include year
    venue_patterns = [r'CHI\s*\'?\s*(20\d{2})', r'Ubicomp\s*\'?\s*(20\d{2})', r'CSCW\s*\'?\s*(20\d{2})',
                      r'DIS\s*\'?\s*(20\d{2})', r'PervasiveHealth\s*\'?\s*(20\d{2})', r'WWW\s*\'?\s*(20\d{2})',
                      r'IUI\s*\'?\s*(20\d{2})', r'OzCHI\s*\'?\s*(20\d{2})', r'TEI\s*\'?\s*(20\d{2})', r'AH\s*\'?\s*(20\d{2})']
    
    if not year:  # If we didn't find year yet
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
        'filename': filename
    })

# Create a dictionary for quick lookup by title (case-insensitive)
paper_dict = {p['title'].lower().strip(): p for p in paper_info}

# Join with citation data and filter for ACM papers
matched_citations = []
acm_citations = []

for citation in citations_data:
    citation_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Find matching paper (case-insensitive, strip whitespace)
    matching_paper = paper_dict.get(citation_title.lower().strip())
    
    if matching_paper:
        matched_citations.append({
            'citation_title': citation_title,
            'citation_count': citation_count,
            'paper_title': matching_paper['title'],
            'paper_source': matching_paper['source'],
            'paper_year': matching_paper['year']
        })
        
        if matching_paper['source'] == 'ACM':
            acm_citations.append(citation_count)

print(f"Total matched citations: {len(matched_citations)}")
print(f"ACM papers matched: {len(acm_citations)}")

# Calculate average citation count for ACM papers
if acm_citations:
    avg_citation = sum(acm_citations) / len(acm_citations)
    total_citations = sum(acm_citations)
    # Print results in the required format
    result_str = f"Average citation count for ACM papers in 2018: {avg_citation:.2f} (based on {len(acm_citations)} papers with {total_citations} total citations)"
else:
    result_str = "No ACM papers found in the 2018 citations data"

print("\nFirst few ACM matches for verification:")
acm_count = 0
for citation in matched_citations:
    if citation['paper_source'] == 'ACM':
        print(f"  {citation['citation_title'][:60]}... - {citation['citation_count']} citations")
        acm_count += 1
        if acm_count >= 5:
            break

# Print final result in required format
print("__RESULT__:")
print(json.dumps(result_str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
