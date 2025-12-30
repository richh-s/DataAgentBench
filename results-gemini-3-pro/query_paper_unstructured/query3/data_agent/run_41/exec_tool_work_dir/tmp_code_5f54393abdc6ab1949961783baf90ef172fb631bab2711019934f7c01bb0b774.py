code = """import json
import re

# File paths from previous steps
papers_file = 'var_function-call-7300462932011158786.json'
citations_file = 'var_function-call-3385159612181082423.json'

# Load Citations
try:
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
    
    # Map title -> total citations
    # The SQL query already summed them by title, returning [{"title":..., "total_citations":...}]
    # But wait, the SQL query was: SELECT title, SUM(citation_count) as total_citations FROM Citations GROUP BY title;
    # So citations_data is a list of dicts.
    citation_map = {row['title']: row['total_citations'] for row in citations_data}
    
except Exception as e:
    print(f"Error loading citations: {e}")
    citation_map = {}

# Load Papers and Filter
results = []
try:
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
        
    print(f"Loaded {len(papers_data)} papers.")
    
    for doc in papers_data:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '')
        
        # 1. Check Year > 2016
        # Look in first 1000 chars for publication year
        header = text[:1000]
        
        # Regex for 2017-2029
        # \b20(1[7-9]|2[0-9])\b matches 2017, 2018, ... 2029
        match_full = re.search(r'\b20(1[7-9]|2[0-9])\b', header)
        
        # Regex for '17-'29
        # '\b(1[7-9]|2[0-9])\b matches '17, '18...
        match_short = re.search(r"'\b(1[7-9]|2[0-9])\b", header)
        
        is_after_2016 = False
        if match_full:
            is_after_2016 = True
        elif match_short:
            is_after_2016 = True
            
        # 2. Check Contribution == 'empirical'
        # Search for "empirical" in text (case insensitive)
        is_empirical = "empirical" in text.lower()
        
        if is_after_2016 and is_empirical:
            total_citations = citation_map.get(title, 0)
            results.append({
                "title": title,
                "citation_count": total_citations
            })
            
except Exception as e:
    print(f"Error processing papers: {e}")

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-12008909793186569857': ['paper_docs'], 'var_function-call-12008909793186566274': 'file_storage/function-call-12008909793186566274.json', 'var_function-call-12008909793186566787': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7300462932011158786': 'file_storage/function-call-7300462932011158786.json', 'var_function-call-3385159612181082423': 'file_storage/function-call-3385159612181082423.json', 'var_function-call-15182070709462479705': 'check_complete'}

exec(code, env_args)
