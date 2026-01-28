"""
Script to create databases for query_paper_unstructured:
1. MongoDB collection with text files (filename, text)
2. SQLite database with citations table (title, citation_count, citation_year)

Run this script to set up the databases before running the agent.
"""

import json
import random
import sqlite3
from pathlib import Path
import pandas as pd

# Set random seed for reproducibility
random.seed(42)

# Directories
BASE_DIR = Path(__file__).parent
TEXT_DIR = BASE_DIR / "query_dataset_text"
GROUND_TRUTH_DIR = BASE_DIR / "ground_truth_labels"
QUERY_DATASET_DIR = BASE_DIR / "query_dataset"


def load_papers_data():
    """Load paper metadata from truths.csv (which is actually JSON)."""
    truths_file = GROUND_TRUTH_DIR / "truths.csv"
    with open(truths_file, 'r', encoding='utf-8') as f:
        papers_data = json.load(f)
    return papers_data


def create_mongodb_dump():
    """Create MongoDB dump as BSON file for paper documents."""
    print("Creating MongoDB BSON dump for paper_docs collection...")

    try:
        import bson
    except ImportError:
        print("  Installing bson/pymongo for BSON support...")
        import subprocess
        subprocess.run(["pip", "install", "pymongo"], check=True)
        import bson

    # Create dump directory structure matching expected format
    dump_dir = QUERY_DATASET_DIR / "paper_docs_dump" / "paper_db"
    dump_dir.mkdir(parents=True, exist_ok=True)

    # Read all text files and create documents
    documents = []
    text_files = sorted(TEXT_DIR.glob("*.txt"))

    for i, text_file in enumerate(text_files):
        with open(text_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        doc = {
            "_id": bson.ObjectId(),
            "filename": text_file.name,
            "text": content
        }
        documents.append(doc)

    # Write as BSON file
    bson_file = dump_dir / "paper_docs.bson"
    with open(bson_file, 'wb') as f:
        for doc in documents:
            f.write(bson.BSON.encode(doc))

    print(f"  Created {len(documents)} documents in BSON dump")
    print(f"  Dump location: {bson_file}")

    return documents


def create_sqlite_database():
    """Create SQLite database with Citations table."""
    print("Creating SQLite database with Citations table...")

    db_path = QUERY_DATASET_DIR / "citations.db"

    # Remove existing database
    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create Citations table
    cursor.execute("""
        CREATE TABLE Citations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            citation_count INTEGER NOT NULL,
            citation_year INTEGER NOT NULL
        )
    """)

    # Load papers data from truths.csv
    papers_data = load_papers_data()

    # Generate citations table data
    citations_data = []

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

        # Generate k_years (random number from 1-10) for years after publication
        k_years = random.randint(1, 10)

        # Calculate end year (publication_year + k_years, but no larger than 2025)
        end_year = min(publication_year + k_years, 2025)

        # Generate citation records for each year AFTER publication_year
        for citation_year in range(publication_year + 1, end_year + 1):
            # Generate random citation_count (1-100)
            citation_count = random.randint(1, 100)

            citations_data.append((title, citation_count, citation_year))

    # Insert all data
    cursor.executemany("""
        INSERT INTO Citations (title, citation_count, citation_year)
        VALUES (?, ?, ?)
    """, citations_data)

    conn.commit()

    # Print stats
    cursor.execute("SELECT COUNT(*) FROM Citations")
    count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(DISTINCT title) FROM Citations")
    distinct_titles = cursor.fetchone()[0]
    print(f"  Created Citations table with {count} rows")
    print(f"  Covering {distinct_titles} distinct papers")
    print(f"  Database location: {db_path}")

    conn.close()

    return db_path


def get_field_value(paper_data, field_name):
    """Get field value from paper data, handling both list and string formats."""
    field_value = paper_data.get(field_name, [])
    if isinstance(field_value, list):
        return [str(v).lower() if v else '' for v in field_value]
    elif isinstance(field_value, str):
        return [field_value.lower()]
    else:
        return [str(field_value).lower()] if field_value else []


def check_paper_matches(paper_title, paper_data, conditions):
    """Check if a paper matches all SQL conditions."""
    # Check domain condition
    domain_match = True
    if 'domain' in conditions:
        domain_values = get_field_value(paper_data, 'domain')
        domain_match = conditions['domain'] in domain_values

    if 'domain_contains' in conditions:
        domain_values = get_field_value(paper_data, 'domain')
        domain_match = any(conditions['domain_contains'] in d for d in domain_values)

    # Check source condition
    source_match = True
    if 'source' in conditions:
        source_values = get_field_value(paper_data, 'source')
        source_match = conditions['source'] in source_values

    # Check venue condition
    venue_match = True
    if 'venue' in conditions:
        venue_values = get_field_value(paper_data, 'venue')
        venue_match = conditions['venue'] in venue_values

    # Check contribution condition
    contribution_match = True
    if 'contribution_contains' in conditions:
        contribution_values = get_field_value(paper_data, 'contribution')
        contribution_match = any(conditions['contribution_contains'] in c for c in contribution_values)

    # Check year condition
    year_match = True
    if 'year' in conditions:
        year_values = get_field_value(paper_data, 'year')
        year_match = conditions['year'] in [str(v) for v in year_values]

    if 'year_gt' in conditions:
        year_values = get_field_value(paper_data, 'year')
        try:
            year_match = any(int(y) > conditions['year_gt'] for y in year_values if y.isdigit())
        except (ValueError, TypeError):
            year_match = False

    if 'year_lt' in conditions:
        year_values = get_field_value(paper_data, 'year')
        try:
            year_match = any(int(y) < conditions['year_lt'] for y in year_values if y.isdigit())
        except (ValueError, TypeError):
            year_match = False

    return domain_match and source_match and venue_match and contribution_match and year_match


def generate_ground_truths():
    """Generate ground_truth.json for each query based on the data."""
    print("Generating ground truth files...")

    db_path = QUERY_DATASET_DIR / "citations.db"
    conn = sqlite3.connect(db_path)

    # Load papers data
    papers_data = load_papers_data()

    # Query 1: Total citation count for papers in the 'food' domain
    # Conditions: domain = 'food'
    conditions = {'domain': 'food'}
    total = 0
    for paper_title, paper_data in papers_data.items():
        if check_paper_matches(paper_title, paper_data, conditions):
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(citation_count) FROM Citations WHERE title = ?", (paper_title,))
            result = cursor.fetchone()[0]
            if result:
                total += result
    gt1 = {"total_citations": total}
    with open(BASE_DIR / "query1" / "ground_truth.json", 'w') as f:
        json.dump(gt1, f, indent=2)
    print(f"  Query 1 ground truth: total_citations={total}")

    # Query 2: Average citation count for papers published by ACM cited in 2018
    # Conditions: source = 'acm', citation_year = 2018
    conditions = {'source': 'acm'}
    citation_year = 2018
    total_citations = 0
    paper_count = 0
    for paper_title, paper_data in papers_data.items():
        if check_paper_matches(paper_title, paper_data, conditions):
            cursor = conn.cursor()
            cursor.execute(
                "SELECT SUM(citation_count) FROM Citations WHERE title = ? AND citation_year = ?",
                (paper_title, citation_year)
            )
            result = cursor.fetchone()[0]
            if result:
                total_citations += result
                paper_count += 1
    avg = round(total_citations / paper_count, 2) if paper_count > 0 else 0
    gt2 = {"avg_citations": avg}
    with open(BASE_DIR / "query2" / "ground_truth.json", 'w') as f:
        json.dump(gt2, f, indent=2)
    print(f"  Query 2 ground truth: avg_citations={avg}")

    # Query 3: Title and total citation count for papers with 'empirical' contribution published after 2016
    # Conditions: contribution_contains = 'empirical', year_gt = 2016
    conditions = {'contribution_contains': 'empirical', 'year_gt': 2016}
    results = []
    for paper_title, paper_data in papers_data.items():
        if check_paper_matches(paper_title, paper_data, conditions):
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(citation_count) FROM Citations WHERE title = ?", (paper_title,))
            result = cursor.fetchone()[0]
            if result:
                results.append({
                    "title": paper_title,
                    "total_citations": result
                })
    gt3 = results
    with open(BASE_DIR / "query3" / "ground_truth.json", 'w') as f:
        json.dump(gt3, f, indent=2)
    print(f"  Query 3 ground truth: {len(results)} papers")

    # Query 4: Title and total citation count for papers published in 2016 in the 'physical activity' domain
    # Conditions: year = '2016', domain = 'physical activity'
    conditions = {'year': '2016', 'domain': 'physical activity'}
    results = []
    for paper_title, paper_data in papers_data.items():
        if check_paper_matches(paper_title, paper_data, conditions):
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(citation_count) FROM Citations WHERE title = ?", (paper_title,))
            result = cursor.fetchone()[0]
            if result:
                results.append({
                    "title": paper_title,
                    "total_citations": result
                })
    gt4 = results
    with open(BASE_DIR / "query4" / "ground_truth.json", 'w') as f:
        json.dump(gt4, f, indent=2)
    print(f"  Query 4 ground truth: {len(results)} papers")

    # Query 5: Total citation counts for all papers presented at CHI and cited in 2020
    # Conditions: venue = 'chi', citation_year = 2020
    conditions = {'venue': 'chi'}
    citation_year = 2020
    total = 0
    for paper_title, paper_data in papers_data.items():
        if check_paper_matches(paper_title, paper_data, conditions):
            cursor = conn.cursor()
            cursor.execute(
                "SELECT SUM(citation_count) FROM Citations WHERE title = ? AND citation_year = ?",
                (paper_title, citation_year)
            )
            result = cursor.fetchone()[0]
            if result:
                total += result
    gt5 = {"total_citations": total}
    with open(BASE_DIR / "query5" / "ground_truth.json", 'w') as f:
        json.dump(gt5, f, indent=2)
    print(f"  Query 5 ground truth: total_citations={total}")

    conn.close()


def main():
    print("=" * 60)
    print("Setting up databases for query_paper_unstructured")
    print("=" * 60)

    # Ensure query_dataset directory exists
    QUERY_DATASET_DIR.mkdir(exist_ok=True)

    # Get list of text files
    text_files = list(TEXT_DIR.glob("*.txt"))
    print(f"\nFound {len(text_files)} text files")

    # Create MongoDB dump
    print("\n" + "-" * 40)
    create_mongodb_dump()

    # Create SQLite database
    print("\n" + "-" * 40)
    create_sqlite_database()

    # Generate ground truths
    print("\n" + "-" * 40)
    generate_ground_truths()

    print("\n" + "=" * 60)
    print("Database setup complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
