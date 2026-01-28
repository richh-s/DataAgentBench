code = """import json

# Load citations data from 2020
citation_file_path = locals()['var_functions.query_db:0']
with open(citation_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Load all papers data
papers_file_path = locals()['var_functions.query_db:16']
with open(papers_file_path, 'r') as f:
    all_papers = json.load(f)

# Create a dictionary of citation counts for easy lookup
citation_dict = {c['title']: int(c['citation_count']) for c in citations_2020}

# Process papers to find CHI papers and their citations
chi_paper_citations = []

for paper in all_papers:
    # Check if this is a CHI paper by looking for "CHI" in the text
    text = paper.get('text', '').upper()
    if 'CHI' in text:
        # Extract title from filename (remove .txt)
        filename = paper.get('filename', '')
        if filename.endswith('.txt'):
            paper_title = filename[:-4]
            
            # Check if this paper has citations in 2020
            if paper_title in citation_dict:
                citation_count = citation_dict[paper_title]
                chi_paper_citations.append({
                    'title': paper_title,
                    'citation_count': citation_count
                })

# Calculate total citations
total_citations = sum(p['citation_count'] for p in chi_paper_citations)

result = {
    'chi_papers_found': len(chi_paper_citations),
    'chi_paper_details': chi_paper_citations,
    'total_citations_2020': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'total_count': 188, 'sample_records': [{'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}], 'titles_sample': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'total_titles': 188, 'titles_sample': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'citations_2020_count': 188, 'all_papers_count': 5, 'citation_titles_sample': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices'], 'paper_filenames_sample': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt']}}

exec(code, env_args)
