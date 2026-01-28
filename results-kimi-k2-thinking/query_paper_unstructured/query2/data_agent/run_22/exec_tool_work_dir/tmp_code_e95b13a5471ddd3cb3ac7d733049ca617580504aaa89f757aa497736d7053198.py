code = """import json
import re
import pandas as pd

# Load the full citation and papers data from files
citation_file = locals()['var_functions.execute_python:8']
print(f"Citation file path: {citation_file}")

with open(citation_file, 'r') as f:
    files_data = json.load(f)

citation_path = files_data['citation_file']
papers_path = files_data['papers_file']

print(f"Loading from: {citation_path} and {papers_path}")

with open(citation_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_path, 'r') as f:
    papers_data = json.load(f)

print(f"Total citations (2018): {len(citations_data)}")
print(f"Total papers: {len(papers_data)}")

# Process papers to extract metadata
papers_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    if not filename:
        continue
    
    # Extract title from filename
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    # Extract source/publisher information
    source = []
    text_upper = text.upper()
    
    if 'ACM' in text_upper or 'ASSOCIATION FOR COMPUTING MACHINERY' in text_upper:
        source.append('ACM')
    if 'IEEE' in text_upper:
        source.append('IEEE')
    if 'PUBMED' in text_upper or 'PUB MED' in text_upper:
        source.append('PubMed')
    
    # Extract publication year
    year_patterns = [
        r'copyright\s*(?:\d{4}\s*)?[\u00a9©]\s*(\d{4})',
        r'(?:\d{4}\s*)?[\u00a9©]\s*(\d{4})',
        r'(\d{4})\s*(?:ACM|IEEE)',
        r'20(?:1[0-9]|0[0-9])\b',
        r'19(?:9[0-9]|8[0-9]|7[0-9])\b'
    ]
    
    year = None
    for pattern in year_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            year_candidate = int(match.group(1))
            if 1970 <= year_candidate <= 2030:  # reasonable range
                year = year_candidate
                break
    
    # Extract venue
    venue_patterns = r'\b(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp/ISWC)\b'
    venue_match = re.search(venue_patterns, text)
    venue = venue_match.group(1) if venue_match else None
    
    papers_info.append({
        'title': title,
        'source': source,
        'year': year,
        'venue': venue
    })

# Create DataFrames
citations_df = pd.DataFrame(citations_data)
if not citations_df.empty:
    citations_df['citation_count'] = citations_df['citation_count'].astype(int)

papers_df = pd.DataFrame(papers_info)

# Find ACM papers
acm_mask = papers_df['source'].apply(lambda x: 'ACM' in x if isinstance(x, list) and x else False)
acm_papers = papers_df[acm_mask]

print(f"ACM papers found: {len(acm_papers)}")
if len(acm_papers) > 0:
    print("Sample ACM papers:", acm_papers['title'].head().tolist())

# Join with citations
if not citations_df.empty and not acm_papers.empty:
    merged_df = citations_df.merge(acm_papers[['title']], on='title', how='inner')
    print(f"ACM papers with 2018 citations: {len(merged_df)}")
    
    if not merged_df.empty:
        avg_citations = merged_df['citation_count'].mean()
        print(f"Average citation count: {avg_citations}")
        result = {
            'average_citation_count': round(avg_citations, 2),
            'acm_papers_with_citations': len(merged_df),
            'total_acm_papers': len(acm_papers)
        }
    else:
        print("No ACM papers found with 2018 citations")
        result = {'average_citation_count': 0, 'acm_papers_with_citations': 0, 'total_acm_papers': len(acm_papers)}
else:
    result = {'average_citation_count': 0, 'acm_papers_with_citations': 0, 'total_acm_papers': len(acm_papers) if not acm_papers.empty else 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'citation_file': 'file_storage/functions.query_db:0.json', 'papers_file': 'file_storage/functions.query_db:2.json', 'citation_count': 158, 'paper_count': 5}}

exec(code, env_args)
