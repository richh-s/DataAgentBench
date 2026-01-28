code = """import json
import re

# Access the citation data directly from storage
citations_data = locals()['var_functions.query_db:0']
print(f"Type of citations data: {type(citations_data)}")
print(f"Total citation records in 2018: {len(citations_data)}")

# Access the paper docs data directly
papers_data = locals()['var_functions.query_db:2']
print(f"Type of papers data: {type(papers_data)}")
print(f"Total paper documents: {len(papers_data)}")

# Extract paper metadata
papers_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Extract source (publisher) - looking for ACM, IEEE, PubMed
    source = []
    
    # Look for publisher information
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        source.append('ACM')
    if 'IEEE' in text:
        source.append('IEEE')
    if 'PubMed' in text or 'Pub Med' in text:
        source.append('PubMed')
    
    # Extract year - look for copyright year or publication year patterns
    year_pattern = r'(?:Copyright\s+(?:\d{4}\s+)?[\u00a9©]\s+|(?:\d{4}\s+)?[\u00a9©]\s+|\b)(\d{4})(?:\s+ACM|\s+IEEE|\b)'
    year_match = re.search(year_pattern, text)
    year = int(year_match.group(1)) if year_match else None
    
    # Look for venue patterns
    venue_pattern = r"(CHI|Ubicomp|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp/ISWC|UbiComp '15|CHI '1\d)"
    venue_match = re.search(venue_pattern, text)
    venue = venue_match.group(1) if venue_match else None
    
    # Extract venue from filename if not found in text
    if not venue:
        if 'CHI' in title:
            venue = 'CHI'
        elif 'UbiComp' in title or 'Ubicomp' in title:
            venue = 'Ubicomp'
        elif 'CSCW' in title:
            venue = 'CSCW'
    
    papers_info.append({
        'title': title,
        'source': source,
        'year': year,
        'venue': venue
    })

print(f"Processed {len(papers_info)} papers")

# Now join with citation data
import pandas as pd

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

# Create a DataFrame for papers
papers_df = pd.DataFrame(papers_info)

# Find papers that are ACM-published
acm_papers = papers_df[papers_df['source'].apply(lambda x: 'ACM' in x if x else False)]
print(f"ACM papers found: {len(acm_papers)}")

# Join with citations
merged_df = citations_df.merge(acm_papers[['title']], on='title', how='inner')
print(f"ACM papers with 2018 citations: {len(merged_df)}")

if not merged_df.empty:
    avg_citations = merged_df['citation_count'].mean()
    print(f"Average citation count for ACM papers in 2018: {avg_citations}")
else:
    avg_citations = 0
    print("No ACM papers found with 2018 citations")

# Print results in required format
result = {
    'total_citations_2018': len(citations_data),
    'acm_papers_found': len(acm_papers),
    'acm_papers_with_citations': len(merged_df),
    'average_citation_count': avg_citations
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
