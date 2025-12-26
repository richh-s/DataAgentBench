# SQL queries with corresponding natural language questions
queries = [
    {
        "query": "SELECT SUM(c.citation_count) AS total_citations FROM citations_table c JOIN papers_table p ON c.title = p.title WHERE p.domain = 'food';",
        "natural_language_question": "What is the total citation count for papers in the 'food' domain?"
    },
    {
        "query": "SELECT AVG(c.citation_count) AS avg_citations FROM citations_table c JOIN papers_table p ON c.title = p.title WHERE p.source = 'ACM' AND c.citation_year = 2018;",
        "natural_language_question": "What is the average citation count for papers published by ACM cited in 2018?"
    },
    {
        "query": "SELECT p.title, SUM(c.citation_count) AS total_citations FROM citations_table c JOIN papers_table p ON c.title = p.title WHERE p.contribution LIKE '%empirical%' AND p.year > 2016 GROUP BY p.title;",
        "natural_language_question": "What is the title and total citation count for papers with an 'empirical' contribution published after 2016?"
    },
    {
        "query": "SELECT p.title, SUM(c.citation_count) AS total_citations FROM citations_table c JOIN papers_table p ON c.title = p.title WHERE p.year = '2016' AND p.domain = 'physical activity' GROUP BY p.title;",
        "natural_language_question": "What is the title and total citation count for papers published in 2016 in the 'physical activity' domain?"
    },
    {
        "query": "SELECT SUM(c.citation_count) AS total_citations FROM citations_table c JOIN papers_table p ON c.title = p.title WHERE p.venue = 'CHI' AND c.citation_year = '2020';",
        "natural_language_question": "What are total citation counts for all papers presented at CHI and cited in 2020?"
    }
]

import json
from pathlib import Path
from collections import Counter

# Create query folders and query.json/sql.json files
base_dir = Path(__file__).parent.parent  # Go up from ground_truth_labels to query_paper_unstructured
for i, query_data in enumerate(queries, start=1):
    query_dir = base_dir / f"query{i}"
    query_dir.mkdir(exist_ok=True)
    
    query_json_path = query_dir / "query.json"
    natural_language_question = query_data.get("natural_language_question", "")
    
    # Write the natural language question as a JSON string
    with open(query_json_path, 'w', encoding='utf-8') as f:
        json.dump(natural_language_question, f, indent=2)
    
    print(f"Created {query_json_path}")
    
    # Create sql.json with the SQL query
    sql_json_path = query_dir / "sql.json"
    sql_query = query_data.get("query", "")
    
    # Write the SQL query as a JSON string
    with open(sql_json_path, 'w', encoding='utf-8') as f:
        json.dump(sql_query, f, indent=2)
    
    print(f"Created {sql_json_path}")

# Count frequency of phrases in "domain" field from truths.csv
def count_domain_phrases():
    """Count the frequency of distinct phrases in the 'domain' field from truths.csv"""
    truths_file = Path(__file__).parent / "truths.csv"
    
    with open(truths_file, 'r', encoding='utf-8') as f:
        papers_data = json.load(f)
    
    domain_phrases = []
    
    for paper_key, paper_info in papers_data.items():
        # Get domain field - it might be a list
        domain_field = paper_info.get('domain', [])
        
        if isinstance(domain_field, list):
            # If it's a list, add all entries
            for domain in domain_field:
                if domain and domain.strip():
                    domain_phrases.append(domain.strip())
        elif isinstance(domain_field, str):
            # If it's a string, add it
            if domain_field.strip():
                domain_phrases.append(domain_field.strip())
    
    # Count frequencies
    phrase_counts = Counter(domain_phrases)
    
    # Print frequencies
    print("Frequency of phrases in 'domain' field:")
    print("=" * 60)
    for phrase, count in phrase_counts.most_common():
        print(f"{phrase}: {count}")
    print("=" * 60)
    print(f"Total distinct phrases: {len(phrase_counts)}")
    print(f"Total occurrences: {sum(phrase_counts.values())}")
    
    return phrase_counts

# Count frequency of phrases in "artifact_kind" field from truths.csv
def count_artifact_phrases():
    """Count the frequency of distinct phrases in the 'artifact_kind' field from truths.csv"""
    truths_file = Path(__file__).parent / "truths.csv"
    
    with open(truths_file, 'r', encoding='utf-8') as f:
        papers_data = json.load(f)
    
    artifact_phrases = []
    
    for paper_key, paper_info in papers_data.items():
        # Get artifact_kind field - it might be a list
        artifact_field = paper_info.get('artifact_kind', [])
        
        if isinstance(artifact_field, list):
            # If it's a list, add all entries
            for artifact in artifact_field:
                if artifact and str(artifact).strip():
                    artifact_phrases.append(str(artifact).strip())
        elif isinstance(artifact_field, str):
            # If it's a string, add it
            if artifact_field.strip():
                artifact_phrases.append(artifact_field.strip())
    
    # Count frequencies
    phrase_counts = Counter(artifact_phrases)
    
    # Print frequencies
    print("\nFrequency of phrases in 'artifact_kind' field:")
    print("=" * 60)
    for phrase, count in phrase_counts.most_common():
        print(f"{phrase}: {count}")
    print("=" * 60)
    print(f"Total distinct phrases: {len(phrase_counts)}")
    print(f"Total occurrences: {sum(phrase_counts.values())}")
    
    return phrase_counts

# Count frequency of phrases in "year" field from truths.csv
def count_year_phrases():
    """Count the frequency of distinct phrases in the 'year' field from truths.csv"""
    truths_file = Path(__file__).parent / "truths.csv"
    
    with open(truths_file, 'r', encoding='utf-8') as f:
        papers_data = json.load(f)
    
    year_phrases = []
    
    for paper_key, paper_info in papers_data.items():
        # Get year field - it might be a list
        year_field = paper_info.get('year', [])
        
        if isinstance(year_field, list):
            # If it's a list, add all entries
            for year in year_field:
                if year and str(year).strip():
                    year_phrases.append(str(year).strip())
        elif isinstance(year_field, str):
            # If it's a string, add it
            if year_field.strip():
                year_phrases.append(year_field.strip())
        elif isinstance(year_field, (int, float)):
            # If it's a number, convert to string
            year_phrases.append(str(year_field))
    
    # Count frequencies
    phrase_counts = Counter(year_phrases)
    
    # Print frequencies
    print("\nFrequency of phrases in 'year' field:")
    print("=" * 60)
    for phrase, count in sorted(phrase_counts.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0):
        print(f"{phrase}: {count}")
    print("=" * 60)
    print(f"Total distinct phrases: {len(phrase_counts)}")
    print(f"Total occurrences: {sum(phrase_counts.values())}")
    
    return phrase_counts

# Count frequency of phrases in "contribution" field from truths.csv
def count_contribution_phrases():
    """Count the frequency of distinct phrases in the 'contribution' field from truths.csv"""
    truths_file = Path(__file__).parent / "truths.csv"
    
    with open(truths_file, 'r', encoding='utf-8') as f:
        papers_data = json.load(f)
    
    contribution_phrases = []
    
    for paper_key, paper_info in papers_data.items():
        # Get contribution field - it might be a list
        contribution_field = paper_info.get('contribution', [])
        
        if isinstance(contribution_field, list):
            # If it's a list, add all entries
            for contribution in contribution_field:
                if contribution and str(contribution).strip():
                    contribution_phrases.append(str(contribution).strip())
        elif isinstance(contribution_field, str):
            # If it's a string, add it
            if contribution_field.strip():
                contribution_phrases.append(contribution_field.strip())
    
    # Count frequencies
    phrase_counts = Counter(contribution_phrases)
    
    # Print frequencies
    print("\nFrequency of phrases in 'contribution' field:")
    print("=" * 60)
    for phrase, count in phrase_counts.most_common():
        print(f"{phrase}: {count}")
    print("=" * 60)
    print(f"Total distinct phrases: {len(phrase_counts)}")
    print(f"Total occurrences: {sum(phrase_counts.values())}")
    
    return phrase_counts

# Count frequency of phrases in "venue" field from truths.csv
def count_venue_phrases():
    """Count the frequency of distinct phrases in the 'venue' field from truths.csv"""
    truths_file = Path(__file__).parent / "truths.csv"
    
    with open(truths_file, 'r', encoding='utf-8') as f:
        papers_data = json.load(f)
    
    venue_phrases = []
    
    for paper_key, paper_info in papers_data.items():
        # Get venue field - it might be a list
        venue_field = paper_info.get('venue', [])
        
        if isinstance(venue_field, list):
            # If it's a list, add all entries
            for venue in venue_field:
                if venue and str(venue).strip():
                    venue_phrases.append(str(venue).strip())
        elif isinstance(venue_field, str):
            # If it's a string, add it
            if venue_field.strip():
                venue_phrases.append(venue_field.strip())
    
    # Count frequencies
    phrase_counts = Counter(venue_phrases)
    
    # Print frequencies
    print("\nFrequency of phrases in 'venue' field:")
    print("=" * 60)
    for phrase, count in phrase_counts.most_common():
        print(f"{phrase}: {count}")
    print("=" * 60)
    print(f"Total distinct phrases: {len(phrase_counts)}")
    print(f"Total occurrences: {sum(phrase_counts.values())}")
    
    return phrase_counts

# Run the frequency counts
if __name__ == "__main__":
    domain_frequencies = count_domain_phrases()
    artifact_frequencies = count_artifact_phrases()
    year_frequencies = count_year_phrases()
    contribution_frequencies = count_contribution_phrases()
    venue_frequencies = count_venue_phrases()

# Save as JSON file (optional - commented out if path doesn't exist)
# file_path_nl_queries = "/mnt/data/sql_queries_with_nl_questions.json"
# with open(file_path_nl_queries, 'w') as f:
#     json.dump(queries, f, indent=4)
