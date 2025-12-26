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
    
    # Parse type LIKE condition (e.g., p.type LIKE '%capital%')
    type_like_match = re.search(r"p\.type\s+LIKE\s+'%([^%]+)%'", conditions_str, re.IGNORECASE)
    if type_like_match:
        type_value = type_like_match.group(1).lower()
        conditions['type_contains'] = type_value
    
    # Parse type = condition (e.g., p.type = 'capital')
    type_eq_match = re.search(r"p\.type\s*=\s*'([^']+)'", conditions_str, re.IGNORECASE)
    if type_eq_match:
        conditions['type'] = type_eq_match.group(1).lower()
    
    # Parse topic LIKE condition (for backward compatibility)
    topic_match = re.search(r"p\.topic\s+LIKE\s+'%([^%]+)%'", conditions_str, re.IGNORECASE)
    if topic_match:
        topic_value = topic_match.group(1).lower()
        conditions['topic_contains'] = topic_value
    
    # Parse Status condition
    status_match = re.search(r"p\.Status\s*=\s*'([^']+)'", conditions_str, re.IGNORECASE)
    if status_match:
        conditions['status'] = status_match.group(1).lower()
    
    # Parse Amount condition
    amount_match = re.search(r"f\.Amount\s*>\s*(\d+)", conditions_str, re.IGNORECASE)
    if amount_match:
        conditions['amount_min'] = int(amount_match.group(1))
    
    return conditions

def process_ground_truth_file(file_path, funding_df, conditions):
    """Process a single ground truth labels file and return the count and matching project names."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return 0, []
            
            projects = json.loads(content)
            
            # Count projects matching the conditions and collect matching names
            count = 0
            matching_projects = []
            for project_name, project_data in projects.items():
                # Check type condition (exact match)
                type_match = True
                if 'type' in conditions:
                    project_type = project_data.get('type', '').lower()
                    type_match = project_type == conditions['type']
                
                # Check type LIKE condition (contains)
                type_contains_match = True
                if 'type_contains' in conditions:
                    project_type = project_data.get('type', '').lower()
                    type_contains_match = conditions['type_contains'] in project_type
                
                # Check topic condition (for backward compatibility)
                topic_match = True
                if 'topic_contains' in conditions:
                    topic = project_data.get('topic', '').lower()
                    topic_match = conditions['topic_contains'] in topic
                
                # Check status condition
                status_match = True
                if 'status' in conditions:
                    status = project_data.get('status', '').lower()
                    status_match = status == conditions['status']
                
                # Check funding amount condition
                funding_match = True
                if 'amount_min' in conditions:
                    # Find matching funding record
                    project_funding = funding_df[funding_df['Project Name'] == project_name]
                    if project_funding.empty:
                        funding_match = False
                    else:
                        amounts = project_funding['Amount'].values
                        funding_match = any(amount > conditions['amount_min'] for amount in amounts)
                
                # All conditions must match
                if type_match and type_contains_match and topic_match and status_match and funding_match:
                    count += 1
                    matching_projects.append(project_name)
            
            return count, matching_projects
            
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not process {file_path.name}: {e}")
        return 0, []

def verify_project_predicates(project_name, project_data, funding_df, conditions):
    """Verify if a project satisfies all SQL predicates."""
    verification = {
        'project_name': project_name,
        'all_pass': True,
        'checks': {}
    }
    
    # Check type condition (exact match)
    if 'type' in conditions:
        project_type = project_data.get('type', '').lower()
        type_match = project_type == conditions['type']
        verification['checks']['type'] = {
            'required': conditions['type'],
            'actual': project_type,
            'pass': type_match
        }
        verification['all_pass'] = verification['all_pass'] and type_match
    
    # Check type LIKE condition (contains)
    if 'type_contains' in conditions:
        project_type = project_data.get('type', '').lower()
        type_contains_match = conditions['type_contains'] in project_type
        verification['checks']['type_contains'] = {
            'required': f"contains '{conditions['type_contains']}'",
            'actual': project_type,
            'pass': type_contains_match
        }
        verification['all_pass'] = verification['all_pass'] and type_contains_match
    
    # Check topic condition
    if 'topic_contains' in conditions:
        topic = project_data.get('topic', '').lower()
        topic_match = conditions['topic_contains'] in topic
        verification['checks']['topic_contains'] = {
            'required': f"contains '{conditions['topic_contains']}'",
            'actual': topic,
            'pass': topic_match
        }
        verification['all_pass'] = verification['all_pass'] and topic_match
    
    # Check status condition
    if 'status' in conditions:
        status = project_data.get('status', '').lower()
        status_match = status == conditions['status']
        verification['checks']['status'] = {
            'required': conditions['status'],
            'actual': status,
            'pass': status_match
        }
        verification['all_pass'] = verification['all_pass'] and status_match
    
    # Check funding amount condition
    if 'amount_min' in conditions:
        project_funding = funding_df[funding_df['Project Name'] == project_name]
        if project_funding.empty:
            funding_match = False
            amounts_str = "No funding record found"
        else:
            amounts = project_funding['Amount'].values
            funding_match = any(amount > conditions['amount_min'] for amount in amounts)
            amounts_str = f"{', '.join(map(str, amounts))}"
        
        verification['checks']['amount'] = {
            'required': f"> {conditions['amount_min']}",
            'actual': amounts_str,
            'pass': funding_match
        }
        verification['all_pass'] = verification['all_pass'] and funding_match
    
    return verification

def verify_matching_projects(all_matching_projects, funding_df, conditions):
    """Verify that all output project names satisfy the SQL predicates."""
    print("\n" + "=" * 80)
    print("Verification: Checking if all output projects satisfy SQL predicates")
    print("=" * 80)
    
    ground_truth_dir = Path(__file__).parent.parent / "ground_truth_labels"
    
    # Group projects by file
    projects_by_file = {}
    for file_name, project_name in all_matching_projects:
        if file_name not in projects_by_file:
            projects_by_file[file_name] = []
        projects_by_file[file_name].append(project_name)
    
    all_verified = True
    
    for file_name in sorted(projects_by_file.keys()):
        file_path = ground_truth_dir / file_name
        if not file_path.exists():
            print(f"\n❌ File not found: {file_name}")
            all_verified = False
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    print(f"\n⚠️  Empty file: {file_name}")
                    continue
                
                projects = json.loads(content)
                file_projects = projects_by_file[file_name]
                
                print(f"\n📄 {file_name} ({len(file_projects)} projects):")
                print("-" * 80)
                
                for project_name in file_projects:
                    if project_name not in projects:
                        print(f"  ❌ {project_name}: NOT FOUND in file")
                        all_verified = False
                        continue
                    
                    verification = verify_project_predicates(
                        project_name, 
                        projects[project_name], 
                        funding_df, 
                        conditions
                    )
                    
                    if verification['all_pass']:
                        print(f"  ✅ {project_name}: All predicates satisfied")
                    else:
                        print(f"  ❌ {project_name}: FAILED predicates:")
                        all_verified = False
                        for check_name, check_result in verification['checks'].items():
                            status = "✅" if check_result['pass'] else "❌"
                            print(f"      {status} {check_name}: required={check_result['required']}, actual={check_result['actual']}")
        
        except (json.JSONDecodeError, IOError) as e:
            print(f"\n❌ Error processing {file_name}: {e}")
            all_verified = False
    
    print("\n" + "=" * 80)
    if all_verified:
        print("✅ VERIFICATION PASSED: All output projects satisfy the SQL predicates")
    else:
        print("❌ VERIFICATION FAILED: Some projects do not satisfy all predicates")
    print("=" * 80)
    
    return all_verified

def generate_ground_truth():
    """Generate ground truth answers for all files in ground_truth_labels."""
    # Load SQL query
    sql_query = load_sql_query()
    print(f"SQL Query: {sql_query}\n")
    
    # Parse conditions from SQL
    conditions = parse_sql_conditions(sql_query)
    print(f"Parsed conditions: {conditions}\n")
    
    # Load funding table
    funding_file = Path(__file__).parent.parent / "query_dataset_table" / "funding_table.csv"
    funding_df = pd.read_csv(funding_file)
    print(f"Loaded {len(funding_df)} funding records\n")
    
    # Process each ground truth labels file
    ground_truth_dir = Path(__file__).parent.parent / "ground_truth_labels"
    results = {}
    all_matching_projects = []
    
    for file_path in sorted(ground_truth_dir.glob("*.txt")):
        answer, matching_projects = process_ground_truth_file(file_path, funding_df, conditions)
        results[file_path.name] = answer
        all_matching_projects.extend([(file_path.name, pname) for pname in matching_projects])
        print(f"{file_path.name}: {answer}")
    
    # Print all matching project names for verification
    print("\n" + "=" * 80)
    print("Matching Projects (for verification):")
    print("=" * 80)
    if all_matching_projects:
        for file_name, project_name in all_matching_projects:
            print(f"  {file_name}: {project_name}")
    else:
        print("  No projects match the SQL predicates.")
    print("=" * 80)
    
    # Verify all matching projects satisfy the predicates
    if all_matching_projects:
        verify_matching_projects(all_matching_projects, funding_df, conditions)
    
    # Store results as JSON (doc name as key, answer as value)
    output_file = Path(__file__).parent / "ground_truth.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Ground truth saved to {output_file}")
    return results

if __name__ == "__main__":
    results = generate_ground_truth()
    print(f"\nTotal files processed: {len(results)}")

