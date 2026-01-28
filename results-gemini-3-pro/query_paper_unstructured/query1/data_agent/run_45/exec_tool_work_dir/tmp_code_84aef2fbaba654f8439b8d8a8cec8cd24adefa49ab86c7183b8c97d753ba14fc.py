code = """import json
import pandas as pd

citations_file = locals()['var_function-call-9466384487046185468']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

papers_file = locals()['var_function-call-18318904051356905988']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

food_papers = []

for paper in papers_data:
    text = paper['text']
    title = paper['filename'].replace('.txt', '')
    
    lower_text = text.lower()
    # Check for Author Keywords or Keywords
    start_idx = lower_text.find('author keywords')
    if start_idx == -1:
        start_idx = lower_text.find('keywords')
    
    if start_idx != -1:
        # Extract 500 chars after keywords
        chunk = lower_text[start_idx:start_idx+1000]
        # Truncate at next section
        end_markers = ['acm classification', 'introduction', 'abstract', 'general terms', 'category']
        end_idx = 1000
        for marker in end_markers:
            m_idx = chunk.find(marker, 10) # start searching a bit after 'keywords'
            if m_idx != -1 and m_idx < end_idx:
                end_idx = m_idx
        
        keywords_section = chunk[:end_idx]
        if 'food' in keywords_section:
            food_papers.append(title)

# Filter citations
food_citations = citations_df[citations_df['title'].isin(food_papers)]
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "food_paper_count": len(food_papers),
    "total_citations": int(total_citations),
    "sample_food_papers": food_papers[:10]
}))"""

env_args = {'var_function-call-13469504004876319012': 'file_storage/function-call-13469504004876319012.json', 'var_function-call-18066522030501759191': 'file_storage/function-call-18066522030501759191.json', 'var_function-call-9466384487046185468': 'file_storage/function-call-9466384487046185468.json', 'var_function-call-18318904051356905988': 'file_storage/function-call-18318904051356905988.json'}

exec(code, env_args)
