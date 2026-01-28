code = """import json

# Load citations
with open(locals()['var_function-call-4239113770536719479'], 'r') as f:
    citations = json.load(f)

# Load paper docs
# The previous query result might be in var_function-call-17837509656361549464
with open(locals()['var_function-call-17837509656361549464'], 'r') as f:
    papers = json.load(f)

# Create a map of filename -> text
paper_map = {p['filename']: p['text'] for p in papers}

total_citations = 0
missing_papers = []
chi_papers_count = 0

for citation in citations:
    title = citation['title']
    filename = title + ".txt"
    if filename in paper_map:
        text = paper_map[filename]
        # Check for CHI venue
        # Heuristic: Look for "CHI" in the first 500 characters, or "Proceedings of the ... CHI"
        # The sample text had "UBICOMP '15" at the start.
        # So CHI papers likely have "CHI '15" or similar.
        # Also check for "Conference on Human Factors in Computing Systems"
        
        # Normalize text for checking
        header = text[:1000].upper()
        if "CHI" in header or "HUMAN FACTORS IN COMPUTING SYSTEMS" in header:
            # Further validation: "CHI" might be part of a word like "CHINA" or "MACHINE".
            # Ensure it's a standalone word or part of the conference name.
            import re
            if re.search(r'\bCHI\b', header) or "HUMAN FACTORS IN COMPUTING SYSTEMS" in header:
                total_citations += citation['citation_count']
                chi_papers_count += 1
    else:
        missing_papers.append(title)

print(f"Processed {len(papers)} papers.")
print(f"Found {chi_papers_count} CHI papers among the cited ones.")
print(f"Missing {len(missing_papers)} papers from the doc store.")

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "missing_count": len(missing_papers)}))"""

env_args = {'var_function-call-4239113770536719479': 'file_storage/function-call-4239113770536719479.json', 'var_function-call-5140237096160835583': 'file_storage/function-call-5140237096160835583.json', 'var_function-call-13183044506038404940': 'file_storage/function-call-13183044506038404940.json', 'var_function-call-17837509656361549464': 'file_storage/function-call-17837509656361549464.json'}

exec(code, env_args)
