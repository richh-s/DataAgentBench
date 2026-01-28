code = """import json
import re

# Read all papers from MongoDB
all_papers_file = locals()['var_functions.query_db:22']
with open(all_papers_file, 'r') as f:
    all_papers = json.load(f)

print(f"Total papers in database: {len(all_papers)}")

# Get citations data
citations_file = locals()['var_functions.query_db:12']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Create citations dictionary
citations_dict = {}
for item in citations_data:
    title = item.get('title', '')
    citations = int(item.get('total_citations', 0))
    citations_dict[title] = citations

print(f"Total citation records: {len(citations_dict)}")

# Process papers: extract title, year, and check for empirical
empirical_papers = []
year_pattern = re.compile(r'(?:\b|\')((?:20)?(?:17|18|19|20|21|22|23|24|25))\b')

for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Check if paper has empirical contribution
    if 'empirical' in text.lower():
        # Extract title
        title = filename.replace('.txt', '')
        
        # Extract year
        year_match = year_pattern.search(text)
        if year_match:
            year_str = year_match.group(1)
            # Convert to 4-digit year
            if len(year_str) == 2:
                year = int('20' + year_str)
            else:
                year = int(year_str)
            
            # Check if published after 2016
            if year > 2016:
                citation_count = citations_dict.get(title, 0)
                empirical_papers.append({
                    'title': title,
                    'year': year,
                    'total_citations': citation_count
                })

print(f"Empirical papers after 2016: {len(empirical_papers)}")

# Sort by citations descending
empirical_papers.sort(key=lambda x: x['total_citations'], reverse=True)

# Prepare result with just title and citations
result = [{k: v for k, v in paper.items() if k in ['title', 'total_citations']} 
          for paper in empirical_papers]

print(f"First 10 results: {result[:10]}")
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2019}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'year': 2017}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:18': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
