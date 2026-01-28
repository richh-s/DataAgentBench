code = """import json

# Read the papers with empirical contribution and published after 2016
papers_file_path = locals()['var_functions.query_db:14']
with open(papers_file_path, 'r') as f:
    mongo_papers = json.load(f)

# Read the total citations data
citations_file_path = locals()['var_functions.query_db:12']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

print(f"Total papers from MongoDB: {len(mongo_papers)}")
print(f"Total citation records: {len(citations_data)}")

# Create a dictionary for quick lookup of citations by title
citations_dict = {}
for citation in citations_data:
    title = citation.get('title', '')
    total_citations = int(citation.get('total_citations', 0))
    citations_dict[title] = total_citations

print(f"Citations dictionary created with {len(citations_dict)} entries")

# Use the processed paper info from the previous step
import re
year_pattern = re.compile(r'(20(17|18|19|20|21|22|23|24|25))')

empirical_papers_after_2016 = []
for paper in mongo_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year_match = year_pattern.search(text)
    if year_match:
        year = int(year_match.group(1))
        if year > 2016:  # Published after 2016
            # Get citation count if available
            citation_count = citations_dict.get(title, 0)
            empirical_papers_after_2016.append({
                'title': title,
                'year': year,
                'total_citations': citation_count
            })

print(f"Empirical papers after 2016: {len(empirical_papers_after_2016)}")

# Sort by total citations in descending order (most cited first)
empirical_papers_after_2016.sort(key=lambda x: x['total_citations'], reverse=True)

# Prepare final result with just title and total_citations
final_result = []
for paper in empirical_papers_after_2016:
    final_result.append({
        'title': paper['title'],
        'total_citations': paper['total_citations']
    })

print(f"First 5 results: {final_result[:5]}")

# Output final result
result_json = json.dumps(final_result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2019}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'year': 2017}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}]}

exec(code, env_args)
