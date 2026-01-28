code = """import json
import pandas as pd

# Load citations
citations_path = locals()['var_function-call-13191277041157486657']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load paper docs
papers_path = locals()['var_function-call-927678752965616416']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Convert to DataFrame
df_citations = pd.DataFrame(citations)
df_papers = pd.DataFrame(papers)

# Extract title and identify ACM papers
acm_titles = []
for index, row in df_papers.iterrows():
    text = row['text']
    filename = row['filename']
    title = filename.replace('.txt', '')
    
    # Check for ACM in the first 5000 characters to cover header and first page footer
    # looking for "ACM" as a distinct word or part of Copyright
    # Using a simple heuristic: "ACM" appears in the first page metadata.
    head_text = text[:5000]
    if "ACM" in head_text:
        acm_titles.append(title)

# Filter citations
# We want citations for papers published by ACM
# df_citations has 'title', 'citation_count', 'citation_year'
# We already filtered for citation_year = 2018 in the SQL query
# Ensure citations are filtered by title in acm_titles

# Filter df_citations
acm_citations_2018 = df_citations[df_citations['title'].isin(acm_titles)]

# Calculate average
if not acm_citations_2018.empty:
    # citation_count comes as string in the preview, need to convert to numeric
    # Wait, the preview showed: "citation_count": "95"
    acm_citations_2018['citation_count'] = pd.to_numeric(acm_citations_2018['citation_count'])
    average_citations = acm_citations_2018['citation_count'].mean()
else:
    average_citations = 0

print("__RESULT__:")
print(json.dumps(average_citations))"""

env_args = {'var_function-call-13191277041157486657': 'file_storage/function-call-13191277041157486657.json', 'var_function-call-927678752965616416': 'file_storage/function-call-927678752965616416.json'}

exec(code, env_args)
