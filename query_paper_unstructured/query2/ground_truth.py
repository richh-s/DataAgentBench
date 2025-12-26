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

def parse_sql_conditions(sql_query):
    """Parse SQL query to extract semantic conditions."""
    # Extract WHERE conditions
    where_match = re.search(r'WHERE\s+(.+?)(?:;|$)', sql_query, re.IGNORECASE | re.DOTALL)
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

def verify_paper_predicates(paper_title, paper_data, citations_df, conditions):
    """Verify if a paper satisfies all SQL predicates."""
    verification = {
        'paper_title': paper_title,
        'all_pass': True,
        'checks': {}
    }
    
    # Check domain condition
    if 'domain' in conditions:
        domain_values = get_field_value(paper_data, 'domain')
        domain_match = conditions['domain'] in domain_values
        verification['checks']['domain'] = {
            'required': conditions['domain'],
            'actual': domain_values,
            'pass': domain_match
        }
        verification['all_pass'] = verification['all_pass'] and domain_match
    
    if 'domain_contains' in conditions:
        domain_values = get_field_value(paper_data, 'domain')
        domain_match = any(conditions['domain_contains'] in d for d in domain_values)
        verification['checks']['domain_contains'] = {
            'required': f"contains '{conditions['domain_contains']}'",
            'actual': domain_values,
            'pass': domain_match
        }
        verification['all_pass'] = verification['all_pass'] and domain_match
    
    # Check source condition
    if 'source' in conditions:
        source_values = get_field_value(paper_data, 'source')
        source_match = conditions['source'] in source_values
        verification['checks']['source'] = {
            'required': conditions['source'],
            'actual': source_values,
            'pass': source_match
        }
        verification['all_pass'] = verification['all_pass'] and source_match
    
    # Check venue condition
    if 'venue' in conditions:
        venue_values = get_field_value(paper_data, 'venue')
        venue_match = conditions['venue'] in venue_values
        verification['checks']['venue'] = {
            'required': conditions['venue'],
            'actual': venue_values,
            'pass': venue_match
        }
        verification['all_pass'] = verification['all_pass'] and venue_match
    
    # Check contribution condition
    if 'contribution_contains' in conditions:
        contribution_values = get_field_value(paper_data, 'contribution')
        contribution_match = any(conditions['contribution_contains'] in c for c in contribution_values)
        verification['checks']['contribution_contains'] = {
            'required': f"contains '{conditions['contribution_contains']}'",
            'actual': contribution_values,
            'pass': contribution_match
        }
        verification['all_pass'] = verification['all_pass'] and contribution_match
    
    # Check year condition
    if 'year' in conditions:
        year_values = get_field_value(paper_data, 'year')
        year_match = conditions['year'] in [str(v) for v in year_values]
        verification['checks']['year'] = {
            'required': conditions['year'],
            'actual': year_values,
            'pass': year_match
        }
        verification['all_pass'] = verification['all_pass'] and year_match
    
    if 'year_gt' in conditions:
        year_values = get_field_value(paper_data, 'year')
        try:
            year_match = any(int(y) > conditions['year_gt'] for y in year_values if y.isdigit())
        except (ValueError, TypeError):
            year_match = False
        verification['checks']['year_gt'] = {
            'required': f"> {conditions['year_gt']}",
            'actual': year_values,
            'pass': year_match
        }
        verification['all_pass'] = verification['all_pass'] and year_match
    
    # Check citation_year condition
    if 'citation_year' in conditions:
        paper_citations = citations_df[citations_df['title'] == paper_title]
        citation_year_match = not paper_citations.empty and any(
            row['citation_year'] == conditions['citation_year'] 
            for _, row in paper_citations.iterrows()
        )
        citation_years = paper_citations['citation_year'].tolist() if not paper_citations.empty else []
        verification['checks']['citation_year'] = {
            'required': conditions['citation_year'],
            'actual': citation_years,
            'pass': citation_year_match
        }
        verification['all_pass'] = verification['all_pass'] and citation_year_match
    
    return verification

def verify_matching_papers(all_matching_papers, citations_df, papers_data, conditions):
    """Verify that all output paper titles satisfy the SQL predicates."""
    print("\n" + "=" * 80)
    print("Verification: Checking if all output papers satisfy SQL predicates")
    print("=" * 80)
    
    all_verified = True
    
    for file_name, paper_title in all_matching_papers:
        if paper_title not in papers_data:
            print(f"\n❌ Paper not found in truths.csv: {paper_title}")
            all_verified = False
            continue
        
        paper_data = papers_data[paper_title]
        
        verification = verify_paper_predicates(
            paper_title,
            paper_data,
            citations_df,
            conditions
        )
        
        if verification['all_pass']:
            print(f"  ✅ {file_name}: {paper_title} - All predicates satisfied")
        else:
            print(f"  ❌ {file_name}: {paper_title} - FAILED predicates:")
            all_verified = False
            for check_name, check_result in verification['checks'].items():
                status = "✅" if check_result['pass'] else "❌"
                print(f"      {status} {check_name}: required={check_result['required']}, actual={check_result['actual']}")
    
    print("\n" + "=" * 80)
    if all_verified:
        print("✅ VERIFICATION PASSED: All output papers satisfy the SQL predicates")
    else:
        print("❌ VERIFICATION FAILED: Some papers do not satisfy all predicates")
    print("=" * 80)
    
    return all_verified

def parse_sql_select_key(sql_query):
    """Parse SELECT clause to determine the key name in ground_truth.json."""
    select_match = re.search(r'SELECT\s+(.+?)\s+FROM', sql_query, re.IGNORECASE | re.DOTALL)
    if not select_match:
        return None
    
    select_str = select_match.group(1).strip()
    
    # Check for AS alias (e.g., AVG(...) AS avg_citations)
    alias_match = re.search(r'AS\s+(\w+)', select_str, re.IGNORECASE)
    if alias_match:
        return alias_match.group(1)
    
    # Check for aggregate functions without alias
    if re.search(r'SUM\s*\(', select_str, re.IGNORECASE):
        return 'total_citations'  # default for SUM
    elif re.search(r'AVG\s*\(', select_str, re.IGNORECASE):
        return 'avg_citations'  # default for AVG
    elif re.search(r'COUNT\s*\(', select_str, re.IGNORECASE):
        return 'count'  # default for COUNT
    elif re.search(r'MAX\s*\(', select_str, re.IGNORECASE):
        return 'max_value'  # default for MAX
    elif re.search(r'MIN\s*\(', select_str, re.IGNORECASE):
        return 'min_value'  # default for MIN
    
    return None

def generate_ground_truth():
    """Generate ground truth answer by treating each paper as a tuple in papers_table."""
    # Load SQL query
    sql_query = load_sql_query()
    print(f"SQL Query: {sql_query}\n")
    
    # Parse SELECT clause to get the key name
    result_key = parse_sql_select_key(sql_query)
    print(f"Result key: {result_key}\n")
    
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
    
    # Collect all citation_count values for matching papers
    all_citation_counts = []
    all_matching_papers = []
    
    for paper_title in matching_paper_titles:
        # Join with citations_table
        paper_citations = citations_df[citations_df['title'] == paper_title]
        
        # Apply citation_year filter if present
        if 'citation_year' in conditions:
            paper_citations = paper_citations[paper_citations['citation_year'] == conditions['citation_year']]
        
        # Collect citation_count values for this paper
        if not paper_citations.empty:
            citation_counts = paper_citations['citation_count'].tolist()
            all_citation_counts.extend(citation_counts)
            all_matching_papers.append(paper_title)
    
    # Calculate average
    if all_citation_counts:
        avg_value = sum(all_citation_counts) / len(all_citation_counts)
    else:
        avg_value = 0.0
    
    print(f"Average citation_count: {avg_value:.2f}\n")
    print(f"Total citation records: {len(all_citation_counts)}\n")
    
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
    
    # Verify all matching papers satisfy the predicates
    if all_matching_papers:
        all_matching_papers_with_files = [(f"{p}.txt", p) for p in all_matching_papers]
        verify_matching_papers(all_matching_papers_with_files, citations_df, papers_data, conditions)
    
    # Store result with the key from SQL SELECT clause
    output_file = Path(__file__).parent / "ground_truth.json"
    result = {result_key: avg_value} if result_key else {"avg_citations": avg_value}
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n✅ Ground truth saved to {output_file}")
    print(f"Result: {result}")
    return result

if __name__ == "__main__":
    results = generate_ground_truth()
    print(f"\nResult key: {list(results.keys())[0] if results else 'N/A'}")

