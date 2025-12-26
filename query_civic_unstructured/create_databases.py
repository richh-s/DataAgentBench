"""
Script to create databases for query_civic_unstructured:
1. MongoDB collection with text files (filename, text)
2. SQLite database with Funding table (500 rows)

Run this script to set up the databases before running the agent.
"""

import json
import random
import sqlite3
from pathlib import Path
import os

# Set random seed for reproducibility
random.seed(42)

# Directories
BASE_DIR = Path(__file__).parent
TEXT_DIR = BASE_DIR / "query_dataset_text"
GROUND_TRUTH_DIR = BASE_DIR / "ground_truth_labels"
QUERY_DATASET_DIR = BASE_DIR / "query_dataset"

# Funding sources for synthetic table
FUNDING_SOURCES = [
    "Government Grant",
    "Private Sponsor",
    "International Aid",
    "Local NGO Fund",
    "Corporate Sponsorship",
    "Community Fund",
    "University Research Fund",
    "State Development Grant",
    "Environmental Grant",
    "Philanthropic Donation",
    "Crowdfunding",
    "Federal Assistance",
    "Development Bank Loan",
    "Research Institution Funding",
    "Social Impact Investment",
    "Green Energy Fund",
    "International Organization Grant",
    "Local Business Support",
    "Non-profit Organization Grant",
    "Municipal Fund",
    "Public-Private Partnership (PPP)",
    "National Foundation Fund",
    "Educational Sponsorship",
    "Technology Innovation Fund",
    "Infrastructure Bond",
    "Taxpayer Contribution",
    "Venture Capital Fund",
    "Impact Investment Fund",
    "Urban Renewal Fund",
    "Cultural Heritage Grant"
]


def extract_project_names():
    """Extract distinct project names from all ground truth label files."""
    project_names = set()

    for file_path in GROUND_TRUTH_DIR.glob("*.txt"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
                    project_names.update(data.keys())
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read {file_path}: {e}")
            continue

    return sorted(list(project_names))


def create_mongodb_dump():
    """Create MongoDB dump as BSON file for civic documents."""
    print("Creating MongoDB BSON dump for civic_docs collection...")

    try:
        import bson
    except ImportError:
        print("  Installing bson/pymongo for BSON support...")
        import subprocess
        subprocess.run(["pip", "install", "pymongo"], check=True)
        import bson

    # Create dump directory structure matching expected format
    dump_dir = QUERY_DATASET_DIR / "civic_docs_dump" / "civic_db"
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
    bson_file = dump_dir / "civic_docs.bson"
    with open(bson_file, 'wb') as f:
        for doc in documents:
            f.write(bson.BSON.encode(doc))

    print(f"  Created {len(documents)} documents in BSON dump")
    print(f"  Dump location: {bson_file}")

    return documents


def create_sqlite_database(k=500):
    """Create SQLite database with Funding table."""
    print("Creating SQLite database with Funding table...")

    db_path = QUERY_DATASET_DIR / "funding.db"

    # Remove existing database
    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create Funding table
    cursor.execute("""
        CREATE TABLE Funding (
            Funding_ID INTEGER PRIMARY KEY,
            Project_Name TEXT NOT NULL,
            Funding_Source TEXT NOT NULL,
            Amount INTEGER NOT NULL
        )
    """)

    # Extract distinct project names from ground truth labels
    distinct_project_names = extract_project_names()
    num_distinct = len(distinct_project_names)
    print(f"  Found {num_distinct} distinct project names from ground truth labels")

    # Generate table data
    table_data = []

    # First, ensure all distinct project names are covered
    for i, project_name in enumerate(distinct_project_names):
        funding_id = i + 1
        funding_source = random.choice(FUNDING_SOURCES)
        amount = random.randint(10, 100) * 1000
        table_data.append((funding_id, project_name, funding_source, amount))

    # Fill remaining entries with random project names
    remaining = k - num_distinct
    if remaining > 0:
        project_ids = random.sample(range(1, 501), remaining)
        for i in range(remaining):
            funding_id = num_distinct + i + 1
            project_name = f"project_{project_ids[i]}"
            funding_source = random.choice(FUNDING_SOURCES)
            amount = random.randint(10, 100) * 1000
            table_data.append((funding_id, project_name, funding_source, amount))

    # Insert all data
    cursor.executemany("""
        INSERT INTO Funding (Funding_ID, Project_Name, Funding_Source, Amount)
        VALUES (?, ?, ?, ?)
    """, table_data)

    conn.commit()

    # Print stats
    cursor.execute("SELECT COUNT(*) FROM Funding")
    count = cursor.fetchone()[0]
    print(f"  Created Funding table with {count} rows")
    print(f"  Database location: {db_path}")

    conn.close()

    return db_path


def generate_ground_truths():
    """Generate ground_truth.json for each query based on the data."""
    print("Generating ground truth files...")

    db_path = QUERY_DATASET_DIR / "funding.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Load all ground truth labels into a structure
    all_projects = {}
    for file_path in GROUND_TRUTH_DIR.glob("*.txt"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
                    for project_name, project_info in data.items():
                        if project_name not in all_projects:
                            all_projects[project_name] = project_info
        except (json.JSONDecodeError, IOError):
            continue

    # Query 1: Count capital projects with 'design' status and funding > 50000
    # SELECT COUNT(*) FROM Funding f JOIN CivicProjects p ON f.Project_Name = p.Project_Name
    # WHERE p.topic LIKE '%capital%' AND p.Status = 'design' AND f.Amount > 50000
    count = 0
    cursor.execute("SELECT Project_Name, Amount FROM Funding WHERE Amount > 50000")
    for row in cursor.fetchall():
        project_name, amount = row
        if project_name in all_projects:
            project = all_projects[project_name]
            if project.get('type', '').lower() == 'capital' and project.get('status', '').lower() == 'design':
                count += 1
    gt1 = {"count": count}
    with open(BASE_DIR / "query1" / "ground_truth.json", 'w') as f:
        json.dump(gt1, f, indent=2)
    print(f"  Query 1 ground truth: {count}")

    # Query 2: Total funding for park projects completed in 2022
    # WHERE p.topic LIKE '%park%' AND p.Status = 'completed' AND p.et BETWEEN '2022-01-01' AND '2022-12-31'
    total = 0
    cursor.execute("SELECT Project_Name, Amount FROM Funding")
    for row in cursor.fetchall():
        project_name, amount = row
        if project_name in all_projects:
            project = all_projects[project_name]
            topic = project.get('topic', '').lower()
            status = project.get('status', '').lower()
            et = project.get('et', '').lower()
            if 'park' in topic and status == 'completed' and '2022' in et:
                total += amount
    gt2 = {"total_funding": total}
    with open(BASE_DIR / "query2" / "ground_truth.json", 'w') as f:
        json.dump(gt2, f, indent=2)
    print(f"  Query 2 ground truth: {total}")

    # Query 3: Funding sources, amounts, and statuses of emergency/FEMA projects
    # WHERE p.topic LIKE '%emergency%' AND p.topic LIKE '%FEMA%'
    results = []
    cursor.execute("SELECT Project_Name, Funding_Source, Amount FROM Funding")
    for row in cursor.fetchall():
        project_name, funding_source, amount = row
        if project_name in all_projects:
            project = all_projects[project_name]
            topic = project.get('topic', '').lower()
            if 'emergency' in topic and 'fema' in topic:
                results.append({
                    "Project_Name": project_name,
                    "Funding_Source": funding_source,
                    "Amount": amount,
                    "Status": project.get('status', '')
                })
    gt3 = {"results": results}
    with open(BASE_DIR / "query3" / "ground_truth.json", 'w') as f:
        json.dump(gt3, f, indent=2)
    print(f"  Query 3 ground truth: {len(results)} projects")

    # Query 4: Count and total funding for projects starting in Spring 2022
    # WHERE p.st LIKE '%2022-Spring%'
    count = 0
    total = 0
    cursor.execute("SELECT Project_Name, Amount FROM Funding")
    for row in cursor.fetchall():
        project_name, amount = row
        if project_name in all_projects:
            project = all_projects[project_name]
            st = project.get('st', '').lower()
            if '2022' in st and 'spring' in st:
                count += 1
                total += amount
    gt4 = {"count": count, "total_funding": total}
    with open(BASE_DIR / "query4" / "ground_truth.json", 'w') as f:
        json.dump(gt4, f, indent=2)
    print(f"  Query 4 ground truth: count={count}, total={total}")

    # Query 5: Total funding for disaster projects starting in 2022
    # WHERE p.topic LIKE '%disaster%' AND p.st BETWEEN '2022-01-01' AND '2022-12-31'
    total = 0
    cursor.execute("SELECT Project_Name, Amount FROM Funding")
    for row in cursor.fetchall():
        project_name, amount = row
        if project_name in all_projects:
            project = all_projects[project_name]
            topic = project.get('topic', '').lower()
            ptype = project.get('type', '').lower()
            st = project.get('st', '').lower()
            if (ptype == 'disaster' or 'disaster' in topic) and '2022' in st:
                total += amount
    gt5 = {"total_funding": total}
    with open(BASE_DIR / "query5" / "ground_truth.json", 'w') as f:
        json.dump(gt5, f, indent=2)
    print(f"  Query 5 ground truth: {total}")

    conn.close()


def main():
    print("=" * 60)
    print("Setting up databases for query_civic_unstructured")
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
    create_sqlite_database(k=500)

    # Generate ground truths
    print("\n" + "-" * 40)
    generate_ground_truths()

    print("\n" + "=" * 60)
    print("Database setup complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
