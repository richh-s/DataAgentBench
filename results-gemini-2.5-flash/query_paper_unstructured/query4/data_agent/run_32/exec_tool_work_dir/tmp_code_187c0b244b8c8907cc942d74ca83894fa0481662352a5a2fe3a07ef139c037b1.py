code = """import pandas as pd
import re
import json

papers_data = json.loads(open(locals()['var_function-call-15170204365258580789'], 'r').read())
processed_papers = []

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # More flexible year extraction: looking for common publication patterns
    year_match = re.search(r'(?:19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None
    
    # Check for 'physical activity' as a substring in the entire text to determine domain
    domain = 'physical activity' if 'physical activity' in text.lower() else None
    
    processed_papers.append({
        'title': title,
        'year': year,
        'domain': domain
    })

df_papers = pd.DataFrame(processed_papers)

# Filter for papers published in 2016 and in the 'physical activity' domain
filtered_papers_df = df_papers[
    (df_papers['year'] == 2016) & 
    (df_papers['domain'] == 'physical activity')
]

# Get the titles of the filtered papers
paper_titles_2016_physical_activity = filtered_papers_df['title'].tolist()

# If there are no papers, return an empty list
if not paper_titles_2016_physical_activity:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    # Prepare the titles for the SQL IN clause
    titles_str = ', '.join([f"'{t.replace("'", "''")}'" for t in paper_titles_2016_physical_activity]) # Escape single quotes for SQL
    
    # SQL query to get citation count for these papers in 2016
    sql_query = f"SELECT title, SUM(citation_count) AS total_citations FROM Citations WHERE title IN ({titles_str}) GROUP BY title;"
    
    print('__RESULT__:')
    print(json.dumps({'sql_query': sql_query})) # Returning SQL query to be executed by the tool"""

env_args = {'var_function-call-7039050370988840032': ['paper_docs'], 'var_function-call-15170204365258580789': 'file_storage/function-call-15170204365258580789.json', 'var_function-call-9037997024857941593': [], 'var_function-call-12259466865263390457': [], 'var_function-call-2200803983775777383': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
