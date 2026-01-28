code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-15380122331926952136']
with open(citations_path, 'r') as f:
    citations_list = json.load(f)

# Create a dict for easy lookup: filename -> citation_count
# Note: citations_list contains titles. Filename is title + ".txt".
# Wait, the previous tool output for citations was a list of filenames (strings).
# Let's verify what `var_function-call-15380122331926952136` contains.
# The previous execute_python code printed filenames, but the *result* of the tool (which is saved in the file)
# is what was printed in the __RESULT__ block.
# The previous `execute_python` printed `json.dumps(filenames)`.
# So the file contains a list of strings (filenames).
# But I need the citation counts!
# The `citations_list` in the previous step was derived from `var_function-call-1858146419099260835`.
# I should reload the original citation data (with counts) from `var_function-call-1858146419099260835`.

citations_data_path = locals()['var_function-call-1858146419099260835']
with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)

# Map filename -> count
# filename = title + ".txt"
citation_map = {item['title'] + ".txt": item['citation_count'] for item in citations_data}

# Load paper docs
papers_path = locals()['var_function-call-9448533248759791427']
with open(papers_path, 'r') as f:
    papers = json.load(f)

total_citations = 0
chi_papers = []

for paper in papers:
    fname = paper.get('filename')
    if fname in citation_map:
        text = paper.get('text', '')
        # Check for CHI in the first 2000 characters
        header = text[:2000]
        
        # Heuristics for CHI venue
        # 1. "CHI 'xx"
        # 2. "CHI 20xx"
        # 3. "Conference on Human Factors in Computing Systems"
        # 4. "CHI Conference"
        # 5. Just "CHI" as a standalone word in uppercase in the header lines.
        
        is_chi = False
        if "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
        elif re.search(r"\bCHI\s+'?\d{2}\b", header): # Matches CHI '15, CHI 2015, CHI 15
            is_chi = True
        elif re.search(r"\bCHI\s+20\d{2}\b", header):
            is_chi = True
        elif re.search(r"Proceedings of the .*CHI", header, re.IGNORECASE):
            is_chi = True
        # Sometimes it's just "CHI 2016" at the top
        
        if is_chi:
            count = citation_map[fname]
            total_citations += count
            chi_papers.append(fname)

print(f"Found {len(chi_papers)} CHI papers.")
print(f"Total citations: {total_citations}")
print(f"First 5 CHI papers: {chi_papers[:5]}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json', 'var_function-call-15380122331926952136': 'file_storage/function-call-15380122331926952136.json', 'var_function-call-9448533248759791427': 'file_storage/function-call-9448533248759791427.json'}

exec(code, env_args)
