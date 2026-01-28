code = """import json
import pandas as pd
import re

# Load citations data
citations_path = var_functions.query_db:5
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Load paper docs data
paper_docs_path = var_functions.query_db:6
with open(paper_docs_path, 'r') as f:
    paper_docs_data = json.load(f)

# Convert to DataFrames
citations_df = pd.DataFrame(citations_data)
paper_docs_df = pd.DataFrame(paper_docs_data)

# Extract title from filename (remove .txt extension)
paper_docs_df['title'] = paper_docs_df['filename'].str.replace('\.txt$', '', regex=True)

# Function to check if a paper is in the food domain
def is_food_domain(text):
    if pd.isna(text):
        return False
    
    # Look for food-related keywords and context
    # Common patterns: "food [", "food.", "food tracking", "food journal", "diet", "eating", etc.
    food_patterns = [
        r'\bfood\b',  # The word 'food'
        r'\bdiet\b',  # The word 'diet'
        r'\beating\b',  # The word 'eating'
        r'\bnutrition\b',  # The word 'nutrition'
        r'\bcalorie\b',  # The word 'calorie'
        r'food\s+tracking',
        r'food\s+journal',
        r'food\s+intake',
        r'dietary',
        r'eating\s+habits'
    ]
    
    text_lower = text.lower()
    for pattern in food_patterns:
        if re.search(pattern, text_lower):
            # Check if it's in a research context (not just a casual mention)
            # Look for tracking, self-tracking, informatics, etc. near food terms
            context_window = 200  # characters around the match
            for match in re.finditer(pattern, text_lower):
                start = max(0, match.start() - context_window)
                end = min(len(text_lower), match.end() + context_window)
                context = text_lower[start:end]
                
                # Check if context contains tracking/self-tracking/research terms
                if any(term in context for term in ['track', 'self-track', 'tracking', 'informatics', 
                                                   'self-monitoring', 'journal', 'log', 'logging',
                                                   'quantified', 'personal informatics']):
                    return True
    
    return False

# Apply food domain detection
paper_docs_df['is_food_domain'] = paper_docs_df['text'].apply(is_food_domain)

# Filter for food domain papers
food_papers = paper_docs_df[paper_docs_df['is_food_domain'] == True]
food_titles = set(food_papers['title'].tolist())

# Join with citations - filter for papers in food domain
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])
food_citations = citations_df[citations_df['title'].isin(food_titles)]

# Calculate total citation count
total_citations = food_citations['citation_count'].sum()

# Also get some stats
num_food_papers = len(food_titles)
num_citation_records = len(food_citations)

result = {
    'total_citation_count': int(total_citations),
    'num_food_papers': num_food_papers,
    'num_citation_records': num_citation_records
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
