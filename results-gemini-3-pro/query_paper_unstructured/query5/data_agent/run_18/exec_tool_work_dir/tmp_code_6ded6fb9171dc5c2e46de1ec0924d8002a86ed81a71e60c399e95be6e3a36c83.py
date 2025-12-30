code = """import json
import re

# Load citations
with open(locals()['var_function-call-7586214257055398583'], 'r') as f:
    citations = json.load(f)

# Load paper docs
# The previous query result might be a list of docs.
try:
    with open(locals()['var_function-call-16114964338052687681'], 'r') as f:
        paper_docs = json.load(f)
except Exception as e:
    print(f"Error loading paper docs: {e}")
    paper_docs = []

print(f"Loaded {len(citations)} citation records.")
print(f"Loaded {len(paper_docs)} paper documents.")

# Index papers by filename
paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

chi_citation_count = 0
chi_papers = []

# Regex for CHI venue
# Matches "CHI '12", "CHI 2012", "CHI Conference", "Conference on Human Factors in Computing Systems"
# Avoids "NordiCHI", "OzCHI" by ensuring word boundary or start of line, but specifically looking for "CHI"
# \bCHI\b matches "CHI" word.
# We also want to ensure it's the venue. Usually appears near "Proceedings of", "Copyright", or at start.
# Let's search in the first 3000 chars.

venue_patterns = [
    r"CHI\s?'\d{2}",        # CHI '12
    r"CHI\s?20\d{2}",       # CHI 2012
    r"Conference on Human Factors in Computing Systems",
    r"CHI Conference"
]

# Negative patterns to avoid
negative_patterns = [
    r"NordiCHI",
    r"OzCHI"
]

count_found_docs = 0

for cit in citations:
    title = cit['title']
    fname = title + ".txt"
    if fname in paper_map:
        text = paper_map[fname]
        count_found_docs += 1
        
        # Check first 3000 chars
        header = text[:3000]
        
        is_chi = False
        # Check positive patterns
        for pat in venue_patterns:
            if re.search(pat, header, re.IGNORECASE): # venues can be "Chi '12" or "CHI '12"? usually ALL CAPS or Title Case
                # But wait, "Machine" contains "chi". \b is needed.
                # My patterns above don't have \b.
                # "Conference on..." is specific.
                # "CHI '12" is specific.
                # "CHI Conference" is specific.
                # But "CHI" could be matched by "Architect". No, "CHI" is space delimited in my regex? 
                # \s? matches space or not.
                # "CHI'12"
                # Let's refine regex
                pass

        # Refined check
        # Look for specific strings
        # "CHI '15", "CHI 2015", "CHI '09"
        # "Conference on Human Factors in Computing Systems"
        
        # Case insensitive search might be safer but "chi" is common.
        # "CHI" as venue is usually uppercase.
        
        # Let's use case sensitive for "CHI" part if possible, or check context.
        # But sample text had "UBICOMP '15" (uppercase).
        
        found_positive = False
        for pat in venue_patterns:
            if re.search(pat, header): # Case sensitive for CHI part in pattern?
                found_positive = True
                break
        
        # Also check if it's "NordiCHI" or "OzCHI"
        # If "NordiCHI" is found, it might also match "CHI" if I am not careful.
        # "NordiCHI '12" -> contains "CHI '12"? Yes if pattern is r"CHI\s?'\d{2}".
        # So I need to check if the match is preceded by letters.
        
        if found_positive:
            # Check negative
            # If "NordiCHI" is present in the same line or context?
            # Simpler: Check if the specific match is NOT preceded by alphabetical chars.
            # I'll implement a stricter regex.
            pass

def is_chi_paper(text):
    # Search in first 5000 chars
    header = text[:5000]
    
    # Pattern 1: "CHI 'YY" or "CHI 20YY"
    # Ensure not preceded by word char (e.g. NordiCHI)
    # \bCHI doesn't work if ' is next? \b matches between word and non-word.
    # CHI'12: I is word, ' is non-word. So \b matches.
    # NordiCHI'12: I is word, ' is non-word. \b matches after I.
    # But we want to ensure *before* C there is no word char.
    
    # Regex: (?<![a-zA-Z])CHI\s?['\u2019]?\s?(\d{2}|\d{4})
    # Note: ' might be fancy quote.
    
    p1 = r"(?<![a-zA-Z])CHI\s?['\u2019]?\s?(20\d{2}|\d{2})"
    
    # Pattern 2: "Conference on Human Factors in Computing Systems"
    p2 = r"Conference on Human Factors in Computing Systems"
    
    if re.search(p1, header) or re.search(p2, header, re.IGNORECASE):
        # Double check it is not NordiCHI or OzCHI
        # If we found p1, we need to verify the match wasn't part of NordiCHI.
        # The lookbehind (?<![a-zA-Z]) ensures it.
        # "NordiCHI" would fail the lookbehind.
        # "OzCHI" would fail.
        # "CHI" at start of line passes.
        # " CHI" passes.
        return True
    return False

total_citations = 0
matched_titles = []

for cit in citations:
    title = cit['title']
    fname = title + ".txt"
    if fname in paper_map:
        if is_chi_paper(paper_map[fname]):
            total_citations += int(cit['citation_count'])
            matched_titles.append(title)

print(f"Matched {len(matched_titles)} CHI papers.")
print(f"Total citations: {total_citations}")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-7586214257055398583': 'file_storage/function-call-7586214257055398583.json', 'var_function-call-979778011189952116': 'Sundroid: Solar Radiation Awareness with Smartphones', 'var_function-call-8522392465021198661': 'file_storage/function-call-8522392465021198661.json', 'var_function-call-7603458929060210194': 'file_storage/function-call-7603458929060210194.json', 'var_function-call-16114964338052687681': 'file_storage/function-call-16114964338052687681.json'}

exec(code, env_args)
