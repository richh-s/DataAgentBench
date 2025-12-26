citations_table = [
    "title",          # Refers to the title of the paper, joining key
    "citation_count", # Number of citations for a specific year
    "citation_year",  # Year the paper was cited
]

import json
import random
import pandas as pd
from pathlib import Path

def generate_citations_table():
    """Generate citations_table from truths.csv"""
    # Read truths.csv (which is actually JSON)
    truths_file = Path(__file__).parent / "truths.csv"
    with open(truths_file, 'r', encoding='utf-8') as f:
        papers_data = json.load(f)
    
    # Create a lookup dictionary: title -> publication_year from truths.csv
    title_to_year = {}
    papers = []
    for paper_key, paper_info in papers_data.items():
        # Get title - if it's a list, get first entry
        title_field = paper_info.get('title', [])
        if isinstance(title_field, list) and len(title_field) > 0:
            title = title_field[0]
        elif isinstance(title_field, str):
            title = title_field
        else:
            continue  # Skip if no valid title
        
        # Get publication year - if it's a list, get first entry
        year_field = paper_info.get('year', [])
        if isinstance(year_field, list) and len(year_field) > 0:
            try:
                publication_year = int(year_field[0])
            except (ValueError, TypeError):
                continue  # Skip if year is not valid
        elif isinstance(year_field, str):
            try:
                publication_year = int(year_field)
            except (ValueError, TypeError):
                continue
        else:
            continue  # Skip if no valid year
        
        # Store in lookup dictionary
        title_to_year[title] = publication_year
        papers.append({
            'title': title,
            'publication_year': publication_year
        })
    
    # Generate citations table - generate for all distinct papers from truths.csv
    citations_data = []
    
    # Generate citation records for all years after publication_year for each paper
    for paper in papers:
        title = paper['title']
        
        # Look up publication_year from truths.csv
        publication_year = title_to_year[title]
        
        # Generate k_years (random number from 1-10) for years after publication
        k_years = random.randint(1, 10)
        
        # Calculate end year (publication_year + k_years, but no larger than 2025)
        end_year = min(publication_year + k_years, 2025)
        
        # Generate citation records for each year AFTER publication_year
        for citation_year in range(publication_year + 1, end_year + 1):
            # Generate random citation_count (1-100)
            citation_count = random.randint(1, 100)
            
            # Don't include publication_year in the output table
            citations_data.append({
                'title': title,
                'citation_count': citation_count,
                'citation_year': citation_year
            })
    
    # Convert to DataFrame
    citations_df = pd.DataFrame(citations_data)
    
    # Save to CSV
    output_dir = Path(__file__).parent / "query_dataset_table"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "citations_table.csv"
    citations_df.to_csv(output_file, index=False)
    
    print(f"Generated {len(citations_data)} citation records for {len(papers)} distinct papers")
    print(f"Citations table saved to: {output_file}")
    
    return citations_df

if __name__ == "__main__":
    citations_table = generate_citations_table()
    print(f"\nFirst few rows:")
    print(citations_table.head(10))
