code = """import json
import pandas as pd
import re

# Load citations
citations_file = locals()['var_function-call-9466384487046185468']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load papers
papers_file = locals()['var_function-call-18318904051356905988']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

food_papers = []

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Extract Author Keywords
    # Look for "Author Keywords" and take text until "ACM Classification" or "Introduction" or specific markers
    # normalize text a bit?
    # Simple regex to capture keywords block
    match = re.search(r"Author Keywords\s*([\s\S]*?)(?:\n\n|\r\n\r\n|ACM Classification|INTRODUCTION|ABSTRACT)", text, re.IGNORECASE)
    
    keywords = ""
    if match:
        keywords = match.group(1).lower()
    else:
        # Fallback: maybe just "Keywords"
        match2 = re.search(r"Keywords\s*([\s\S]*?)(?:\n\n|\r\n\r\n|ACM Classification|INTRODUCTION|ABSTRACT)", text, re.IGNORECASE)
        if match2:
            keywords = match2.group(1).lower()
    
    # Check if 'food' is in keywords
    if 'food' in keywords:
        food_papers.append(title)

# Filter citations
food_citations = citations_df[citations_df['title'].isin(food_papers)]
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "food_paper_count": len(food_papers),
    "food_papers": food_papers,
    "total_citations": int(total_citations)
}))"""

env_args = {'var_function-call-13469504004876319012': 'file_storage/function-call-13469504004876319012.json', 'var_function-call-18066522030501759191': 'file_storage/function-call-18066522030501759191.json', 'var_function-call-9466384487046185468': 'file_storage/function-call-9466384487046185468.json', 'var_function-call-18318904051356905988': 'file_storage/function-call-18318904051356905988.json'}

exec(code, env_args)
