import json
from pathlib import Path
from collections import Counter, defaultdict

queries = [
    {
        "query": "SELECT COUNT(*) AS Num_Capital_Design_Projects FROM Funding f JOIN CivicProjects p ON f.Project_Name = p.Project_Name WHERE p.topic LIKE '%capital%' AND p.Status = 'design' AND f.Amount > 50000;",
        "natural_language_question": "How many capital projects with a 'design' status have funding greater than $50,000?"
    },
    {
        "query": "SELECT SUM(f.Amount) AS Total_Park_Funding_Completed_2022 FROM Funding f JOIN CivicProjects p ON f.Project_Name = p.Project_Name WHERE p.topic LIKE '%park%' AND p.Status = 'completed' AND p.et BETWEEN '2022-01-01' AND '2022-12-31';",
        "natural_language_question": "What is the total funding for park-related projects that were completed in 2022?"
    },
    {
        "query": "SELECT f.Project_Name, f.Funding_Source, f.Amount, p.Status FROM Funding f JOIN CivicProjects p ON f.Project_Name = p.Project_Name WHERE p.topic LIKE '%emergency%' AND p.topic LIKE '%FEMA%';",
        "natural_language_question": "What are the funding sources, amounts, and statuses of emergency warning projects related to FEMA?"
    },
    {
        "query": "SELECT COUNT(*), SUM(f.Amount) AS Total_Funding_Spring_2022 FROM Funding f JOIN CivicProjects p ON f.Project_Name = p.Project_Name WHERE p.st LIKE '%2022-Spring%';",
        "natural_language_question": "How many projects started in Spring 2022, and what is their total funding?"
    },
    {
        "query": "SELECT SUM(f.Amount) AS Total_Funding FROM Funding f JOIN CivicProjects p ON f.Project_Name = p.Project_Name WHERE p.topic LIKE '%disaster%' AND p.st BETWEEN '2022-01-01' AND '2022-12-31';",
        "natural_language_question": "What is the total funding for disaster-related projects that started in 2022?"
    }
]

# Save as JSON file in current folder
file_path = Path(__file__).parent / "sql_queries.json"
with open(file_path, 'w') as f:
    json.dump(queries, f, indent=4)

print(f"SQL queries saved to: {file_path}")

# Create query folders and query.json files
base_dir = Path(__file__).parent
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


def count_topic_phrase_frequencies():
    """
    Count the frequency of distinct phrases in the 'topic' field for each file 
    in ground_truth_labels, and aggregate the frequencies over all files.
    
    Returns:
        dict: A dictionary with two keys:
            - 'per_file': dict mapping filename to Counter of phrase frequencies
            - 'aggregated': Counter of aggregated phrase frequencies across all files
    """
    ground_truth_dir = Path(__file__).parent / "ground_truth_labels"
    per_file_frequencies = {}
    aggregated_counter = Counter()
    
    # Process each file in ground_truth_labels
    for file_path in sorted(ground_truth_dir.glob("*.txt")):
        file_counter = Counter()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
                    
                    # Extract topics from each project
                    for project_name, project_data in data.items():
                        if 'topic' in project_data and project_data['topic']:
                            topic_str = project_data['topic']
                            # Split by comma and process each phrase
                            phrases = [phrase.strip() for phrase in topic_str.split(',')]
                            # Filter out empty phrases and normalize
                            phrases = [p.lower() for p in phrases if p]
                            
                            # Count phrases for this file
                            file_counter.update(phrases)
                            # Also add to aggregated counter
                            aggregated_counter.update(phrases)
            
            per_file_frequencies[file_path.name] = file_counter
            
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read {file_path}: {e}")
            continue
    
    return {
        'per_file': per_file_frequencies,
        'aggregated': aggregated_counter
    }


if __name__ == "__main__":
    # Count topic phrase frequencies
    frequencies = count_topic_phrase_frequencies()
    
    print("\n" + "=" * 80)
    print("Topic Phrase Frequency Analysis")
    print("=" * 80)
    
    # Print aggregated frequencies (top 20)
    print("\nTop 20 Most Frequent Phrases (Aggregated across all files):")
    print("-" * 80)
    for phrase, count in frequencies['aggregated'].most_common(20):
        print(f"  {phrase:<50} {count:>5}")
    
    # Print per-file summary
    print(f"\n\nPer-file statistics:")
    print("-" * 80)
    for filename, counter in sorted(frequencies['per_file'].items()):
        print(f"  {filename:<50} {len(counter):>5} distinct phrases")
    
    print(f"\nTotal distinct phrases across all files: {len(frequencies['aggregated'])}")
    print("=" * 80)

    
