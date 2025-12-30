code = """import json
import re
import pandas as pd

# Load citations
citations_data = json.load(open('var_function-call-8765785804266823925.json'))
# citations_data is a list of dicts: {"title": "...", "citation_count": "..."}
# Convert citation_count to int and group by title
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])
citations_map = citations_df.groupby('title')['citation_count'].sum().to_dict()

# Load papers
papers_data = json.load(open('var_function-call-10316404265600385483.json'))
# papers_data is a list of dicts: {"filename": "...", "text": "..."}

results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 4-digit year in the first 1000 chars
    header_text = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header_text)
    
    # Heuristic: The publication year is usually the first 4-digit number starting with 20 in the header.
    # However, sometimes there are other dates (e.g. copyright 2015, conference 2015).
    # If multiple years are found, usually they are the same or close.
    # I'll take the most frequent or the first?
    # Let's take the first one found.
    if years:
        year = int(years[0])
    else:
        # Fallback: try to find 'YY (e.g. '15)
        short_years = re.findall(r"'\d{2}", header_text)
        if short_years:
            # Assuming 20xx
            y = int(short_years[0].replace("'", ""))
            year = 2000 + y
        else:
            year = 0 # Unknown
            
    # Extract Contribution
    # Check for "empirical" in text (case insensitive)
    is_empirical = "empirical" in text.lower()
    
    # Apply filters
    if year > 2016 and is_empirical:
        # Get citation count
        count = citations_map.get(title, 0)
        results.append({
            "title": title,
            "total_citation_count": count
        })

# Sort by citation count desc (optional but good for display)
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2080358657401428239': 'file_storage/function-call-2080358657401428239.json', 'var_function-call-4922993133298785860': ['paper_docs'], 'var_function-call-4922993133298782503': ['Citations', 'sqlite_sequence'], 'var_function-call-15480292294165083401': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10316404265600385483': 'file_storage/function-call-10316404265600385483.json', 'var_function-call-8350695654712224507': [{'count(*)': '1405'}], 'var_function-call-8765785804266825960': 'file_storage/function-call-8765785804266825960.json', 'var_function-call-8765785804266823925': 'file_storage/function-call-8765785804266823925.json'}

exec(code, env_args)
