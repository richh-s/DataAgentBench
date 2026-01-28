code = """import json

# Access the citation data file path
citations_file = locals()['var_functions.query_db:5']

with open(citations_file, 'r') as f:
    all_citations = json.load(f)

print(f"Total citation records: {len(all_citations)}")

# Access the paper documents file path  
papers_file = locals()['var_functions.query_db:6']

with open(papers_file, 'r') as f:
    all_papers = json.load(f)

print(f"Total paper documents: {len(all_papers)}")

# Create a dictionary to store papers by title
papers_dict = {}
for paper in all_papers:
    filename = paper.get('filename', '')
    # Extract title from filename (remove .txt extension)
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    papers_dict[title] = paper

print(f"Unique papers extracted: {len(papers_dict)}")

# Build a mapping from paper to domain
paper_domains = {}
for title, paper in papers_dict.items():
    text = paper.get('text', '').lower()
    
    # Look for domain indicators in the text
    # Common domains: food, physical activity, sleep, mental, finances, productivity, 
    # screen time, social interactions, location, chronic, diabetes, health_behavior
    
    # For food domain, look for specific keywords
    domain_keywords = {
        'food': ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie'],
        'physical activity': ['physical activity', 'exercise', 'fitness', 'workout', 'steps'],
        'sleep': ['sleep', 'bedtime', 'rest'],
        'mental': ['mental', 'stress', 'anxiety', 'mood'],
        'finances': ['finances', 'money', 'expense', 'budget'],
        'productivity': ['productivity', 'work', 'task', 'time management'],
        'location': ['location', 'gps', 'place'],
        'health_behavior': ['health behavior', 'wellness']
    }
    
    matched_domains = []
    for domain, keywords in domain_keywords.items():
        for keyword in keywords:
            if keyword in text:
                matched_domains.append(domain)
                break
    
    paper_domains[title] = matched_domains

# Find all food papers
food_papers = [title for title, domains in paper_domains.items() if 'food' in domains]
print(f"Papers in food domain: {len(food_papers)}")

# Build citation mapping
citation_counts = {}
for citation in all_citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_counts[title] = citation_counts.get(title, 0) + count

print(f"Unique papers with citation data: {len(citation_counts)}")

# Calculate total citations for food papers
total_citations = 0
matching_papers = 0
for paper_title in food_papers:
    if paper_title in citation_counts:
        total_citations += citation_counts[paper_title]
        matching_papers += 1
        print(f"  {paper_title}: {citation_counts[paper_title]} citations")

print(f"\nFood papers with citation data: {matching_papers}")
print(f"Total citations for food papers: {total_citations}")

# Prepare output result
result = {
    "total_citations": total_citations,
    "food_papers_with_citations": matching_papers,
    "total_food_papers": len(food_papers)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
