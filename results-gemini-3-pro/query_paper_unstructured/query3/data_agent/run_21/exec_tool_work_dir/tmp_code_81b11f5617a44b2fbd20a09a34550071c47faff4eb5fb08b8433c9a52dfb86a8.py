code = """import json
import re

# Load papers
with open(locals()['var_function-call-8978544678357083899'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-9130584372251179173'], 'r') as f:
    citations = json.load(f)

# Helper to extract year
def extract_year(text):
    # Search in first 1000 characters
    head = text[:1000]
    matches = re.findall(r'\b(20\d{2})\b', head)
    if matches:
        # Return the first match.
        # However, sometimes copyright year might be different or multiple years appear.
        # Usually the first 4-digit number starting with 20 is the year.
        return int(matches[0])
    return None

# Helper to check empirical
def is_empirical(text):
    # Simple check
    return "empirical" in text.lower()

results = []

# Process papers
relevant_titles = set()
for p in papers:
    title = p['filename'].replace('.txt', '')
    year = extract_year(p['text'])
    
    # Check if empirical
    # Also check if year > 2016
    if year and year > 2016 and is_empirical(p['text']):
        relevant_titles.add(title)
        # Debug print
        print(f"Found relevant paper: {title} ({year})")

# Calculate total citations
citation_counts = {}
for c in citations:
    t = c['title']
    if t in relevant_titles:
        count = int(c['citation_count'])
        citation_counts[t] = citation_counts.get(t, 0) + count

final_output = []
for t in relevant_titles:
    final_output.append({
        "title": t,
        "citation_count": citation_counts.get(t, 0)
    })

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-15050569047067534700': 'file_storage/function-call-15050569047067534700.json', 'var_function-call-3142892684795704503': 'file_storage/function-call-3142892684795704503.json', 'var_function-call-8978544678357083899': 'file_storage/function-call-8978544678357083899.json', 'var_function-call-9130584372251179173': 'file_storage/function-call-9130584372251179173.json'}

exec(code, env_args)
