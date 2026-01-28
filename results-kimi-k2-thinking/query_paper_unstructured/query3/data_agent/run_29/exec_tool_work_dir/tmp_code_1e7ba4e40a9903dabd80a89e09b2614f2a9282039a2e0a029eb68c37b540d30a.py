code = """import json, re

# The result file path is stored in a variable. The variable name is var_functions.query_db:5
# Actually we have access to the variable name as per instructions: locals()['var_functions.list_db:0'] etc
# The tool result is stored under key: var_functions.query_db:5
# Let's load it
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Function to extract year from text

def extract_year(text):
    # Look for patterns like "2017", "2018", etc. Usually the first occurrence near header
    # Look for a 4-digit number between 2010-2099
    match = re.search(r"(20\d{2})", text)
    if match:
        return int(match.group(1))
    return None

# Function to extract contribution type via regex, focusing on empirical

def has_empirical_contribution(text):
    # Look for keywords indicating empirical contribution
    # Could be in ABSTRACT, INTRODUCTION, or explicit mention of "empirical"
    # We'll search case-insensitively for "empirical"
    return bool(re.search(r"empirical", text, re.IGNORECASE))

# Build list of papers with fields
papers = []
for doc in docs:
    title = doc.get("filename", "").replace(".txt", "")
    text = doc.get("text", "")
    year = extract_year(text)
    empirical = has_empirical_contribution(text)
    if year and empirical and year > 2016:
        papers.append({"title": title, "year": year})

# Print number of candidate papers
print(f"Number of papers after 2016 with empirical contribution: {len(papers)}")
# Output the list of titles (for debugging)
#print([p['title'] for p in papers])

# Now we need to query citations database for these titles.

# Use query_db tool for each title? That would be many queries. Instead we can query all citations and then filter.

# We'll return the list of titles and counts via Python? Actually we need to query citations database which is SQLite.

# So we will use query_db to fetch all citations (title, citation_count).

# Since we cannot call another tool from within python, we will store the titles list to a variable and then later query.

# Let's prepare a JSON string of titles.
import json as js
titles_json = js.dumps([p['title'] for p in papers])

# Print the titles list as a JSON string in the required format.
print('__RESULT__:')
print(titles_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
