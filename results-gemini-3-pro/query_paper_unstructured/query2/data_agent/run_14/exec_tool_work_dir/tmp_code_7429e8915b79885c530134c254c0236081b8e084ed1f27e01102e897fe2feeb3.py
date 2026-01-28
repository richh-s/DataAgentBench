code = """import json

# Load citations
citation_file = locals()['var_function-call-12876420682816740159']
with open(citation_file, 'r') as f:
    citations = json.load(f)

# Load paper docs
paper_docs_file = locals()['var_function-call-11930424291751131995']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Create a lookup for paper text by title
# filename is "Title.txt"
paper_text_map = {}
for doc in paper_docs:
    fname = doc.get('filename', '')
    if fname.endswith('.txt'):
        title = fname[:-4]
        paper_text_map[title] = doc.get('text', '')

# Filter citations for ACM papers
acm_citations = []
missing_docs = 0
non_acm = 0

for cit in citations:
    title = cit['title']
    if title in paper_text_map:
        text = paper_text_map[title]
        # Check for ACM in the first 3000 characters
        # Heuristic: Look for "ACM" in header/copyright
        # Also check if "ACM" is in the text at all, but limit scope to avoid references
        header = text[:5000] # Increased to 5000 to be safe
        if "ACM" in header or "Association for Computing Machinery" in header:
            acm_citations.append(cit['citation_count'])
        else:
            non_acm += 1
    else:
        missing_docs += 1

# Calculate average
if acm_citations:
    # citation_count might be string or int
    counts = [int(c) for c in acm_citations]
    avg_citations = sum(counts) / len(counts)
else:
    avg_citations = 0

print(f"DEBUG: Total 2018 citations: {len(citations)}")
print(f"DEBUG: Matches found in paper_docs: {len(citations) - missing_docs}")
print(f"DEBUG: Missing docs: {missing_docs}")
print(f"DEBUG: Identified as ACM: {len(acm_citations)}")
print(f"DEBUG: Identified as Non-ACM: {non_acm}")
print(f"DEBUG: Average: {avg_citations}")

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-12876420682816740159': 'file_storage/function-call-12876420682816740159.json', 'var_function-call-12763598563475847231': 'file_storage/function-call-12763598563475847231.json', 'var_function-call-364809223448232169': {'count': 158, 'filenames_preview': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt']}, 'var_function-call-11930424291751131995': 'file_storage/function-call-11930424291751131995.json'}

exec(code, env_args)
