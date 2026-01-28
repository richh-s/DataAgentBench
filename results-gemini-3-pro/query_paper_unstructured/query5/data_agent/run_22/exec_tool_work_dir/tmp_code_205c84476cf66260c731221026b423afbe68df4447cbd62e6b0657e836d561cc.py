code = """import json
import os
import re

# Load citations
citations_path = var_function_call_10316639782376099170
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create a dictionary for citations: title -> count
# Note: Titles in Citations table match filename without .txt
citation_map = {}
for item in citations_data:
    citation_map[item['title']] = int(item['citation_count'])

# Load papers
papers_path = var_function_call_3655541512535358306
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

chi_papers = []
total_citations = 0

# Regex for CHI
# Look for CHI followed by year, or 'CHI' as a venue name in header
# Common header formats: "CHI '15", "CHI 2015", "Proceedings of CHI", "Conference on Human Factors in Computing Systems"
# Also checking for "CHI" as a distinct word in the first few lines.
# To be safe, let's look for "CHI" in the first 1000 chars and verify it's likely the venue.
# Matches: "CHI '12", "CHI 2012", "CHI Conference", "CHI 2012...", "CHI '12..."
venue_pattern = re.compile(r"\bCHI\b.*(?:20\d\d|'\d\d)|Conference on Human Factors in Computing Systems", re.IGNORECASE) 
# Wait, "CHI" is usually uppercase in venue strings.
# The user hint says: Common venues include: "CHI".
# Let's try a simpler regex: "CHI" as a whole word in the first 500 characters.
# But we must avoid false positives like "China" or "machine". \bCHI\b handles that.
# Also "archiving", "architecture", etc.
# A strict regex: `\bCHI\b` in the first 500 chars.
# But "CHI" could be in the title or abstract.
# Usually venue is at the very top.

# Let's inspect a few papers' headers in the loop to be sure, but for now apply a heuristic.
# Heuristic: "\bCHI\b" AND ("Proceedings" OR "Conference" OR "20\d\d" OR "'\d\d") in first 500 chars.
# Or just "\bCHI '", "\bCHI 20".
# Let's use a pattern that catches standard ACM headers.
pattern = re.compile(r"\bCHI\s*(?:'|20)\d\d\b|\bCHI\s+Conference\b|Conference on Human Factors in Computing Systems", re.IGNORECASE)

# Let's refine: The example had "UBICOMP '15". So "CHI '15" is likely.
simple_pattern = re.compile(r"CHI\s*['\u2019]\d\d|CHI\s*20\d\d", re.IGNORECASE)
# \u2019 is smart quote.

count = 0
found_titles = []

for paper in papers_data:
    text_start = paper.get('text', '')[:1000] # Check first 1000 chars
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for CHI
    if simple_pattern.search(text_start) or "Conference on Human Factors in Computing Systems" in text_start:
        chi_papers.append(title)
        # Add citations if present
        if title in citation_map:
            total_citations += citation_map[title]
            count += 1
            found_titles.append(title)

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "chi_paper_count": len(chi_papers), "papers_with_citations": count, "sample_titles": found_titles[:5]}))"""

env_args = {'var_function-call-10316639782376097408': ['Citations', 'sqlite_sequence'], 'var_function-call-10316639782376098289': ['paper_docs'], 'var_function-call-10316639782376099170': 'file_storage/function-call-10316639782376099170.json', 'var_function-call-10316639782376095955': 'file_storage/function-call-10316639782376095955.json', 'var_function-call-3655541512535358306': 'file_storage/function-call-3655541512535358306.json'}

exec(code, env_args)
