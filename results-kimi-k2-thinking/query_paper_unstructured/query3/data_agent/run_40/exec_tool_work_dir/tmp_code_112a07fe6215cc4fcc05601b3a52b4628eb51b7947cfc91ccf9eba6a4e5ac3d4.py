code = """import json
import re

# Read the full MongoDB query results
mongo_file_path = locals()['var_functions.query_db:14']
with open(mongo_file_path, 'r') as f:
    mongo_papers = json.load(f)

print(f"Total papers with 'empirical' in text from MongoDB: {len(mongo_papers)}")

# Extract paper information: title and year
paper_info = []
year_pattern = re.compile(r'(20(17|18|19|20|21|22|23|24|25))')

for paper in mongo_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year_match = year_pattern.search(text)
    if year_match:
        year = int(year_match.group(1))
        if year > 2016:  # Published after 2016
            paper_info.append({
                'title': title,
                'year': year
            })

print(f"Papers with year > 2016: {len(paper_info)}")

# Output the paper information
result = json.dumps(paper_info)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2019}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'year': 2017}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
