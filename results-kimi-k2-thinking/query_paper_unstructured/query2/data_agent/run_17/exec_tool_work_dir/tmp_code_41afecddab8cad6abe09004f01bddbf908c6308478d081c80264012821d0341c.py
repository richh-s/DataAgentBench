code = """import json
import pandas as pd
import re

# Load citations data for 2018
citations_file = '/Users/Shared/wld9.json'
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

print(f"Loaded {len(citations_data)} citation records for 2018")
print("Sample citations:", citations_data[:3])

# Load paper documents
papers_file = '/Users/Shared/wld10.json'
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print(f"\nLoaded {len(papers_data)} paper documents")
print("Sample paper:", papers_data[0]['filename'])

# Create a mapping of paper title to source (publisher)
acm_papers = []
paper_sources = {}

for paper in papers_data:
    # Extract title from filename
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Search for ACM in the text to identify ACM papers
    text = paper.get('text', '')
    is_acm = 'ACM' in text or 'acm' in text
    
    if is_acm:
        paper_sources[title] = 'ACM'
        acm_papers.append(title)

print(f"\nFound {len(acm_papers)} ACM papers")
print("Sample ACM papers:", acm_papers[:5])

# Create DataFrames
citations_df = pd.DataFrame(citations_data)
print(f"\nCitations DataFrame shape: {citations_df.shape}")

# Filter citations for ACM papers
acm_citations = citations_df[citations_df['title'].isin(acm_papers)]
print(f"Found {len(acm_citations)} citations in 2018 for ACM papers")

if len(acm_citations) > 0:
    # Convert citation_count to numeric
    acm_citations['citation_count'] = pd.to_numeric(acm_citations['citation_count'])
    
    # Calculate average
    avg_citations = acm_citations['citation_count'].mean()
    print(f"Average citation count: {avg_citations:.2f}")
    
    # Also get some statistics
    print(f"Median: {acm_citations['citation_count'].median()}")
    print(f"Min: {acm_citations['citation_count'].min()}")
    print(f"Max: {acm_citations['citation_count'].max()}")
    print(f"Total papers: {len(acm_citations)}")
    
    result = {
        "average_citations": float(avg_citations),
        "total_papers": len(acm_citations),
        "median": float(acm_citations['citation_count'].median()),
        "min": int(acm_citations['citation_count'].min()),
        "max": int(acm_citations['citation_count'].max())
    }
else:
    print("No ACM papers found in 2018 citations")
    result = {"average_citations": 0, "total_papers": 0, "message": "No ACM papers found"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
