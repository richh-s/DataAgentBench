import json
import pandas as pd
from pathlib import Path
import re

def load_sql_query():
    """Load SQL query from sql.json in the same folder."""
    sql_file = Path(__file__).parent / "sql.json"
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_query = json.load(f)
    return sql_query

def parse_sql_select(sql_query):
    """Parse SELECT clause to extract columns to return."""
    select_match = re.search(r'SELECT\s+(.+?)\s+FROM', sql_query, re.IGNORECASE | re.DOTALL)
    if not select_match:
        return []
    
    select_str = select_match.group(1).strip()
    # Split by comma and clean up column names
    columns = [col.strip() for col in select_str.split(',')]
    # Remove table aliases and extract column names
    clean_columns = []
    for col in columns:
        # Handle AS aliases
        if ' AS ' in col.upper():
            alias = col.split(' AS ')[-1].strip()
            clean_columns.append(alias)
        # Handle aggregate functions
        elif re.search(r'(SUM|AVG|COUNT|MAX|MIN)\s*\(', col, re.IGNORECASE):
            # Extract alias if present, otherwise use function name
            alias_match = re.search(r'AS\s+(\w+)', col, re.IGNORECASE)
            if alias_match:
                clean_columns.append(alias_match.group(1))
            else:
                # Extract the aggregate function name
                agg_match = re.search(r'(SUM|AVG|COUNT|MAX|MIN)', col, re.IGNORECASE)
                if agg_match:
                    clean_columns.append(agg_match.group(1).lower())
        else:
            # Remove table prefix (e.g., "p." or "c.")
            col = re.sub(r'^[cp]\.', '', col, flags=re.IGNORECASE)
            clean_columns.append(col.strip())
    
    return clean_columns

def parse_sql_conditions(sql_query):
    """Parse SQL query to extract semantic conditions."""
    # Extract WHERE conditions
    where_match = re.search(r'WHERE\s+(.+?)(?:\s+GROUP\s+BY|;|$)', sql_query, re.IGNORECASE | re.DOTALL)
    if not where_match:
        return {}
    
    conditions_str = where_match.group(1)
    conditions = {}
    
    # Parse domain = condition (e.g., p.domain = 'food')
    domain_eq_match = re.search(r"p\.domain\s*=\s*'([^']+)'", conditions_str, re.IGNORECASE)
    if domain_eq_match:
        conditions['domain'] = domain_eq_match.group(1).lower()
    
    # Parse domain LIKE condition (e.g., p.domain LIKE '%food%')
    domain_like_match = re.search(r"p\.domain\s+LIKE\s+'%([^%]+)%'", conditions_str, re.IGNORECASE)
    if domain_like_match:
        conditions['domain_contains'] = domain_like_match.group(1).lower()
    
    # Parse source = condition (e.g., p.source = 'ACM')
    source_eq_match = re.search(r"p\.source\s*=\s*'([^']+)'", conditions_str, re.IGNORECASE)
    if source_eq_match:
        conditions['source'] = source_eq_match.group(1).lower()
    
    # Parse venue = condition (e.g., p.venue = 'CHI')
    venue_eq_match = re.search(r"p\.venue\s*=\s*'([^']+)'", conditions_str, re.IGNORECASE)
    if venue_eq_match:
        conditions['venue'] = venue_eq_match.group(1).lower()
    
    # Parse contribution LIKE condition (e.g., p.contribution LIKE '%empirical%')
    contribution_like_match = re.search(r"p\.contribution\s+LIKE\s+'%([^%]+)%'", conditions_str, re.IGNORECASE)
    if contribution_like_match:
        conditions['contribution_contains'] = contribution_like_match.group(1).lower()
    
    # Parse year = condition (e.g., p.year = '2016')
    year_eq_match = re.search(r"p\.year\s*=\s*'([^']+)'", conditions_str, re.IGNORECASE)
    if year_eq_match:
        conditions['year'] = year_eq_match.group(1)
    
    # Parse year comparison (e.g., p.year > 2016)
    year_gt_match = re.search(r"p\.year\s*>\s*(\d+)", conditions_str, re.IGNORECASE)
    if year_gt_match:
        conditions['year_gt'] = int(year_gt_match.group(1))
    
    year_lt_match = re.search(r"p\.year\s*<\s*(\d+)", conditions_str, re.IGNORECASE)
    if year_lt_match:
        conditions['year_lt'] = int(year_lt_match.group(1))
    
    # Parse citation_year = condition (e.g., c.citation_year = 2018)
    citation_year_eq_match = re.search(r"c\.citation_year\s*=\s*(\d+)", conditions_str, re.IGNORECASE)
    if citation_year_eq_match:
        conditions['citation_year'] = int(citation_year_eq_match.group(1))
    
    # Parse citation_year = condition with quotes (e.g., c.citation_year = '2020')
    citation_year_eq_str_match = re.search(r"c\.citation_year\s*=\s*'(\d+)'", conditions_str, re.IGNORECASE)
    if citation_year_eq_str_match:
        conditions['citation_year'] = int(citation_year_eq_str_match.group(1))
    
    return conditions

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

def generate_ground_truth():
    """Generate ground truth answer by treating each paper as a tuple in papers_table."""
    # Load SQL query
    sql_query = load_sql_query()
    print(f"SQL Query: {sql_query}\n")
    
    # Parse SELECT clause to get columns
    select_columns = parse_sql_select(sql_query)
    print(f"Selected columns: {select_columns}\n")
    
    # Parse conditions from SQL
    conditions = parse_sql_conditions(sql_query)
    print(f"Parsed conditions: {conditions}\n")
    
    # Load citations table
    citations_file = Path(__file__).parent.parent / "ground_truth_labels" / "query_dataset_table" / "citations_table.csv"
    citations_df = pd.read_csv(citations_file)
    print(f"Loaded {len(citations_df)} citation records\n")
    
    # Load papers data (truths.csv) - treat this as papers_table
    truths_file = Path(__file__).parent.parent / "ground_truth_labels" / "truths.csv"
    with open(truths_file, 'r', encoding='utf-8') as f:
        papers_data = json.load(f)
    print(f"Loaded {len(papers_data)} papers from truths.csv (papers_table)\n")
    
    # Find all papers that match the conditions (treating each paper as a tuple)
    matching_paper_titles = []
    for paper_title, paper_data in papers_data.items():
        if check_paper_matches(paper_title, paper_data, conditions):
            matching_paper_titles.append(paper_title)
    
    print(f"Found {len(matching_paper_titles)} papers matching the conditions\n")
    
    # Generate records for each matching paper
    records = []
    all_matching_papers = []
    
    for paper_title in matching_paper_titles:
        # Join with citations_table
        paper_citations = citations_df[citations_df['title'] == paper_title]
        
        # Apply citation_year filter if present
        if 'citation_year' in conditions:
            paper_citations = paper_citations[paper_citations['citation_year'] == conditions['citation_year']]
        
        # Calculate aggregate (SUM in this case)
        if not paper_citations.empty:
            total_citations = int(paper_citations['citation_count'].sum())
            
            # Create record based on SELECT columns
            record = {}
            for col in select_columns:
                if col == 'title':
                    record['title'] = paper_title
                elif col == 'total_citations':
                    record['total_citations'] = total_citations
                # Add other columns as needed
            
            records.append(record)
            all_matching_papers.append(paper_title)
    
    print(f"Generated {len(records)} records\n")
    
    # Print all matching paper titles for verification
    print("\n" + "=" * 80)
    print("Matching Papers (for verification):")
    print("=" * 80)
    if all_matching_papers:
        for paper_title in all_matching_papers:
            print(f"  {paper_title}")
    else:
        print("  No papers match the SQL predicates.")
    print("=" * 80)
    
    # Store result as a list of records (since GROUP BY returns multiple rows)
    output_file = Path(__file__).parent / "ground_truth.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2)
    
    print(f"\n✅ Ground truth saved to {output_file}")
    print(f"Total records: {len(records)}")
    return records

if __name__ == "__main__":
    results = generate_ground_truth()
    print(f"\nTotal records: {len(results)}")

