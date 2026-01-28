code = """import json
import re
import pandas as pd

def extract_info(text, filename):
    title = filename.replace(".txt", "")
    year = None
    domain = []

    # Try to extract year from filename (e.g., 'UbiComp '16.txt' -> 2016)
    filename_year_match = re.search(r'\\b(\'\\d{2}|\\d{4})\\b', filename)
    if filename_year_match:
        year_str = filename_year_match.group(1)
        if len(year_str) == 4: # YYYY format
            year = int(year_str)
        elif len(year_str) == 3 and year_str.startswith("'"): # 'YY format
            year = 2000 + int(year_str[1:])

    # If year not found in filename, try from copyright statement in text
    if year is None:
        copyright_year_match = re.search(r"Copyright\\s+(?:\\(c\\)|\\u00a9)?\\s*(\\d{4})", text, re.IGNORECASE)
        if copyright_year_match:
            year = int(copyright_year_match.group(1))

    # If year still not found, try more general year patterns in text
    if year is None:
        general_year_match = re.search(r'\\b(19|20)\\d{2}\\b', text)
        if general_year_match:
            year = int(general_year_match.group(0))

    # Extract domain (looking for common domains in the text)
    common_domains = ["food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"]
    text_lower = text.lower()
    for d in common_domains:
        pattern = r'\\b' + re.escape(d) + r'\\b'
        if re.search(pattern, text_lower):
            domain.append(d)

    return {"title": title, "year": year, "domain": list(set(domain))}

# Load MongoDB data
mongo_file_path = locals()['var_function-call-12752153450719007890']
with open(mongo_file_path, 'r') as f:
    mongo_data = json.load(f)

papers_info = []
for doc in mongo_data:
    papers_info.append(extract_info(doc['text'], doc['filename']))

# Filter papers for year 2016 and "physical activity" domain
filtered_papers = [
    p for p in papers_info 
    if p['year'] == 2016 and "physical activity" in [d.lower() for d in p['domain']]
]

# Get titles of filtered papers
filtered_titles = [p['title'] for p in filtered_papers]

# Load citation data
citations_file_path = locals()['var_function-call-16161537513363771660']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Filter citations by the titles of the 2016 "physical activity" papers
df_filtered_citations = df_citations[df_citations['title'].isin(filtered_titles)]

# Calculate total citation count for each paper
total_citations_per_paper = df_filtered_citations.groupby('title')['citation_count'].sum().reset_index()

# Convert to desired output format
result = total_citations_per_paper.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-16161537513363771660': 'file_storage/function-call-16161537513363771660.json', 'var_function-call-12752153450719007890': 'file_storage/function-call-12752153450719007890.json', 'var_function-call-866722953621056295': [], 'var_function-call-8171478659109438870': [], 'var_function-call-16770226383205343611': [], 'var_function-call-8439373108773590095': [], 'var_function-call-2542673735042371936': [], 'var_function-call-15077404571815829099': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'domain': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'domain': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'domain': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'domain': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'domain': []}], 'var_function-call-17221929207605378594': [], 'var_function-call-15462957610608874917': [], 'var_function-call-6016250029047767537': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domain': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domain': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domain': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domain': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'domain': []}]}

exec(code, env_args)
