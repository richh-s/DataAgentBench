code = """import json
import pandas as pd

# Load papers
with open(locals()['var_function-call-789985204037697992'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-10038520539297588104'], 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

food_titles = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.append(title)
        continue

    # Extract Keywords
    # Look for "Author Keywords"
    is_food = False
    lower_text = text.lower()
    
    # Helper to extract section
    def check_section(header, end_markers):
        start_idx = lower_text.find(header)
        if start_idx != -1:
            # Find the end of this section
            section_content = lower_text[start_idx + len(header):]
            end_idx = len(section_content)
            for marker in end_markers:
                idx = section_content.find(marker)
                if idx != -1 and idx < end_idx:
                    end_idx = idx
            
            content = section_content[:end_idx]
            if 'food' in content:
                return True
        return False

    # Check Author Keywords
    # It usually ends before "ACM Classification Keywords" or "INTRODUCTION" or double newline
    if check_section("author keywords", ["acm classification keywords", "introduction", "\n\n\n"]):
        is_food = True
    
    # Check ACM Classification Keywords if not found yet
    if not is_food and check_section("acm classification keywords", ["introduction", "general terms", "\n\n\n"]):
        is_food = True
        
    if is_food:
        food_titles.append(title)

# Filter citations
food_citations = df_citations[df_citations['title'].isin(food_titles)]
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps(int(total_citations)))"""

env_args = {'var_function-call-4706990439072147394': 'file_storage/function-call-4706990439072147394.json', 'var_function-call-4706990439072147581': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-789985204037697992': 'file_storage/function-call-789985204037697992.json', 'var_function-call-10038520539297588104': 'file_storage/function-call-10038520539297588104.json'}

exec(code, env_args)
