code = """import json
import pandas as pd

# Load papers
with open(locals()['var_function-call-16861145491754002893'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-4378801704425368314'], 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

food_papers = []

for p in papers:
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    text = p.get('text', '')
    
    # Check title
    if 'food' in title.lower():
        food_papers.append(title)
        continue
        
    # Check keywords or abstract (heuristic: first 3000 chars)
    # The hint says "Fields like domain... may contain multiple values". 
    # Usually listed in Keywords.
    # We look for "food" in the first 3000 characters as a proxy for Abstract/Keywords.
    # To avoid matching "food" in "fast food" or "food [11]" if it's not the main topic, 
    # we might want to look for "Keywords" section.
    
    # Extract keywords section
    lower_text = text.lower()
    
    # Try to find keywords section
    keywords_start = lower_text.find('keywords')
    if keywords_start != -1:
        # scan next 500 chars for "food"
        keywords_section = lower_text[keywords_start:keywords_start+500]
        if 'food' in keywords_section:
            food_papers.append(title)
            continue

    # Fallback: if "food" appears in the first 500 characters (Title + part of abstract)
    # But title is already checked.
    # Let's check if "food" is in the Abstract.
    # Abstract usually follows "ABSTRACT".
    abstract_start = lower_text.find('abstract')
    if abstract_start != -1:
        abstract_section = lower_text[abstract_start:abstract_start+1000] # reasonable length
        if 'food' in abstract_section:
            # Check if it's just a reference? Hard to say. 
            # But usually if "food" is in abstract, it's relevant.
            # But the sample paper had "food [11]" in abstract and wasn't about food.
            # So maybe strictly rely on Keywords?
            # Or if "food" appears multiple times?
            pass

    # Let's rely on Keywords and Title primarily as per the problem type. 
    # If a paper is "food" domain, it should have "food" in keywords or title.
    # The sample paper had "food [11]" in abstract but keywords were "Physical Activity; Finances; Location."
    # So relying on Keywords is safer.
    
    # What if "food" is not in keywords but is the main topic?
    # Maybe check for "eating", "diet"? But query asked for 'food' domain specifically.
    
    # Let's stick to Title or Keywords.
    
    # Also, some papers might use "Author Keywords" or "Index Terms". 
    # My keywords search 'keywords' covers 'Author Keywords'.
    
    pass

# Filter citations
# Join on title
food_papers_set = set(food_papers)
matched_citations = df_citations[df_citations['title'].isin(food_papers_set)]

total_citations = matched_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "food_papers_count": len(food_papers_set),
    "food_papers_titles": list(food_papers_set),
    "total_citations": int(total_citations)
}))"""

env_args = {'var_function-call-5516583949260656826': 'file_storage/function-call-5516583949260656826.json', 'var_function-call-6649186005887820433': 'file_storage/function-call-6649186005887820433.json', 'var_function-call-16861145491754002893': 'file_storage/function-call-16861145491754002893.json', 'var_function-call-4378801704425368314': 'file_storage/function-call-4378801704425368314.json'}

exec(code, env_args)
