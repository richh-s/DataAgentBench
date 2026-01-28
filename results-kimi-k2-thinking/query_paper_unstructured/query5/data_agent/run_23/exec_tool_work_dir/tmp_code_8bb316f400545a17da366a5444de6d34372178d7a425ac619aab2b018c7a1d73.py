code = """import json
import re

# Check what variables are available in locals()
print("Available variables:")
for key in list(locals().keys()):
    if key.startswith('var_'):
        print(f"  {key}")

# Access the stored results
citations_data = locals()['var_query_db_5']
paper_data = locals()['var_query_db_9']

print(f"\nCitations data type: {type(citations_data)}")
print(f"Paper data type: {type(paper_data)}")
print(f"Citations count: {len(citations_data)}")
print(f"Paper count: {len(paper_data)}")

# Create citations dictionary for O(1) lookup
citations_dict = {}
for citation in citations_data:
    citations_dict[citation['title']] = int(citation['citation_count'])

print(f"\nCitations dictionary created with {len(citations_dict)} entries")
print(f"Example: {list(citations_dict.items())[:2]}")

# Find CHI papers by searching text for CHI conference mentions
chi_titles = []
chi_papers_with_years = []

for doc in paper_data:
    text = doc['text']
    # Look for CHI patterns
    if 'CHI' in text:
        title = doc['filename'].replace('.txt', '')
        chi_titles.append(title)
        
        # Try to extract year
        year_match = re.search(r'CHI\s*[\'"]?(\d{2,4})', text)
        if year_match:
            year_str = year_match.group(1)
            if len(year_str) == 2:
                year = int('20' + year_str) if int(year_str) < 50 else int('19' + year_str)
            else:
                year = int(year_str)
            chi_papers_with_years.append((title, year))

print(f"\nFound {len(chi_titles)} papers mentioning CHI")
print(f"With year extraction: {len(chi_papers_with_years)}")

# Match CHI papers with 2020 citations
total_citations = 0
matched_count = 0
matched_papers = []

for chi_title in chi_titles:
    if chi_title in citations_dict:
        count = citations_dict[chi_title]
        total_citations += count
        matched_count += 1
        matched_papers.append({
            'title': chi_title,
            'citations_2020': count
        })

print(f"\nMatched {matched_count} CHI papers with 2020 citations")
print(f"Total citations: {total_citations}")

# Sort by citation count and show top 5
matched_papers.sort(key=lambda x: x['citations_2020'], reverse=True)
print(f"\nTop 5 CHI papers by 2020 citations:")
for i, paper in enumerate(matched_papers[:5]):
    print(f"  {i+1}. {paper['title']}: {paper['citations_2020']} citations")

result = total_citations
print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
