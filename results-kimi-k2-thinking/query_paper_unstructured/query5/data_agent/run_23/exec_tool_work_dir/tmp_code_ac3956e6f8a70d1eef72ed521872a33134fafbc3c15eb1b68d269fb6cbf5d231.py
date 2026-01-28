code = """import json

# Load the 2020 citations data
citations_2020_path = 'var_functions.query_db:5'
with open(citations_2020_path, 'r') as f:
    citations_2020 = json.load(f)

print(f"Total 2020 citations records: {len(citations_2020)}")

# Load the paper docs data  
paper_docs_path = 'var_functions.query_db:9'
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total paper documents: {len(paper_docs)}")

# Create a dictionary mapping paper titles to their docs for easier lookup
paper_dict = {}
for doc in paper_docs:
    # Extract title from filename (remove .txt extension)
    title = doc['filename'].replace('.txt', '')
    paper_dict[title] = doc

print(f"Number of papers mapped: {len(paper_dict)}")

# Now let's search for CHI papers in the text
chi_papers = []
for doc in paper_docs:
    text = doc['text']
    # Look for CHI conference mentions
    if 'CHI' in text or 'chi' in text:
        # Extract title
        title = doc['filename'].replace('.txt', '')
        chi_papers.append({
            'title': title,
            'filename': doc['filename']
        })

print(f"Potential CHI papers found: {len(chi_papers)}")
print(f"First few CHI papers: {chi_papers[:3] if chi_papers else 'None'}")"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
