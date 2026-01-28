code = """import json
import re

# Read all papers from MongoDB
all_papers_file = locals()['var_functions.query_db:22']
with open(all_papers_file, 'r') as f:
    all_papers = json.load(f)

# Read citations data
citations_file = locals()['var_functions.query_db:26']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Create citations dictionary for quick lookup
citations_dict = {}
for item in citations_data:
    title = item.get('title', '')
    try:
        citations = int(item.get('total_citations', 0))
    except (ValueError, TypeError):
        citations = 0
    citations_dict[title] = citations

print(f"Total papers: {len(all_papers)}")
print(f"Total citation records: {len(citations_dict)}")

# Process all papers to find those with empirical contribution and published after 2016
empirical_papers = []
year_pattern = re.compile(r'(201[7-9]|202[0-5])')

for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Check if paper mentions empirical (contribution)
    if 'empirical' in text.lower():
        title = filename.replace('.txt', '')
        
        # Extract year from text
        year_match = year_pattern.search(text)
        if year_match:
            year = int(year_match.group(1))
            if year > 2016:  # Published after 2016
                citation_count = citations_dict.get(title, 0)
                empirical_papers.append({
                    'title': title,
                    'year': year,
                    'total_citations': citation_count
                })

print(f"Empirical papers after 2016: {len(empirical_papers)}")

# Sort by citations in descending order
empirical_papers.sort(key=lambda x: x['total_citations'], reverse=True)

# Prepare final result with title and total_citations only
final_result = []
for paper in empirical_papers:
    final_result.append({
        'title': paper['title'],
        'total_citations': paper['total_citations']
    })

print(f"Top 5 most cited papers:")
for i, paper in enumerate(final_result[:5], 1):
    print(f"{i}. {paper['title']} - {paper['total_citations']} citations")

# Output final result
result_json = json.dumps(final_result, ensure_ascii=False)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2019}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'year': 2017}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:18': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
