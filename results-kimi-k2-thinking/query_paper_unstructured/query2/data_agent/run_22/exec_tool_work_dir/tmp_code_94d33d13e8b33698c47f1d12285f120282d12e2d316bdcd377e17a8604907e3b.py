code = """import json
import re
import pandas as pd

# Get the file information from previous execution
file_info = locals()['var_functions.execute_python:8']
print(f"File info type: {type(file_info)}")
print(f"File info content: {file_info}")

# The files_data is already loaded, use it directly
files_data = file_info

# Load the actual data from the file paths
citation_path = files_data['citation_file']
papers_path = files_data['papers_file']

print(f"Loading citations from: {citation_path}")
print(f"Loading papers from: {papers_path}")

with open(citation_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_path, 'r') as f:
    papers_data = json.load(f)

print(f"Total citations (2018): {len(citations_data)}")
print(f"Total papers: {len(papers_data)}")

# Process papers to extract metadata - look for ACM publisher
papers_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title from filename
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    # Check if this is an ACM paper
    text_upper = text.upper()
    is_acm = 'ACM' in text_upper or 'ASSOCIATION FOR COMPUTING MACHINERY' in text_upper
    
    if is_acm:
        papers_info.append({
            'title': title,
            'source': ['ACM'],
            'is_acm': True
        })
        print(f"Found ACM paper: {title}")

print(f"Total ACM papers found: {len(papers_info)}")

# Create DataFrames
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

if papers_info:
    papers_df = pd.DataFrame(papers_info)
    
    # Join citations with ACM papers
    merged_df = citations_df.merge(papers_df[['title']], on='title', how='inner')
    
    if not merged_df.empty:
        avg_citations = merged_df['citation_count'].mean()
        total_papers = len(merged_df)
        print(f"Found {total_papers} ACM papers with citations in 2018")
        print(f"Average citations: {avg_citations:.2f}")
        result = {
            'average_citation_count': round(avg_citations, 2),
            'total_acm_papers_cited': total_papers
        }
    else:
        print("No ACM papers found with 2018 citations")
        result = {'average_citation_count': 0, 'total_acm_papers_cited': 0}
else:
    print("No ACM papers found in the dataset")
    result = {'average_citation_count': 0, 'total_acm_papers_cited': 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'citation_file': 'file_storage/functions.query_db:0.json', 'papers_file': 'file_storage/functions.query_db:2.json', 'citation_count': 158, 'paper_count': 5}}

exec(code, env_args)
