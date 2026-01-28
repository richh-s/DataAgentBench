code = """import json
import os

# Load citations
with open(locals()['var_function-call-15646429060027290344'], 'r') as f:
    citations = json.load(f)

# Load papers
# The variable var_function-call-5884279522157261639 contains the result of the query {"collection": "paper_docs", "count": true}
# which seemingly returned the list of docs.
with open(locals()['var_function-call-5884279522157261639'], 'r') as f:
    papers = json.load(f)

print(f"Number of citations records: {len(citations)}")
print(f"Number of papers fetched: {len(papers)}")

# Create a lookup for citation counts
citation_map = {c['title']: int(c['citation_count']) for c in citations}

total_citations = 0
found_papers_count = 0

for paper in papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
        if title in citation_map:
            # Check for CHI in text
            text = paper.get('text', '')
            # Simple heuristic: Check if "CHI" appears in the first 1000 chars 
            # or check for "Proceedings of the ... CHI"
            # Being a bit more robust: look for "CHI" surrounded by spaces or punctuation, 
            # or "CHI '", or "CHI 20"
            # The sample text had "UBICOMP '15". So "CHI '20" or "CHI '19" etc.
            # Also "CHI Conference".
            
            # Let's look at the first few lines often containing the venue
            header = text[:1000]
            if "CHI" in header:
                # Double check it's not part of another word like "CHILD"
                # But "CHI" is usually capitalized fully in venue names.
                # Let's check if "CHI" is a distinct word.
                import re
                if re.search(r'\bCHI\b', header):
                    total_citations += citation_map[title]
                    found_papers_count += 1

print(f"Found {found_papers_count} papers presented at CHI.")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-173807103424142885': ['Citations', 'sqlite_sequence'], 'var_function-call-173807103424140732': ['paper_docs'], 'var_function-call-173807103424142675': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-173807103424140522': 'file_storage/function-call-173807103424140522.json', 'var_function-call-17670429279864850901': [{'COUNT(*)': '188'}], 'var_function-call-5884279522157261639': 'file_storage/function-call-5884279522157261639.json', 'var_function-call-15646429060027290344': 'file_storage/function-call-15646429060027290344.json', 'var_function-call-6914183761872541415': 'file_storage/function-call-6914183761872541415.json'}

exec(code, env_args)
