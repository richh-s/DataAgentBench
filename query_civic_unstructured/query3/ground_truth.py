import json
import pandas as pd
from pathlib import Path
import re
from datetime import datetime

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
    # Remove table aliases (e.g., "f.Project_Name" -> "Project_Name")
    clean_columns = []
    for col in columns:
        # Handle AS aliases
        if ' AS ' in col.upper():
            col = col.split(' AS ')[-1].strip()
        # Remove table prefix (e.g., "f." or "p.")
        col = re.sub(r'^[fp]\.', '', col, flags=re.IGNORECASE)
        clean_columns.append(col)
    
    return clean_columns

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
    
    # Parse topic LIKE condition - handle multiple topic LIKE conditions with AND or OR
    topic_matches = list(re.finditer(r"p\.topic\s+LIKE\s+'%([^%]+)%'", conditions_str, re.IGNORECASE))
    if topic_matches:
        topic_values = [match.group(1).lower() for match in topic_matches]
        # Check if conditions are connected with OR (between topic conditions)
        # Look for OR between consecutive topic LIKE conditions
        topic_or = False
        if len(topic_values) > 1:
            # Check if there's an OR between the topic conditions
            # Find positions of topic LIKE conditions
            for i in range(len(topic_matches) - 1):
                start_pos = topic_matches[i].end()
                end_pos = topic_matches[i + 1].start()
                between_text = conditions_str[start_pos:end_pos]
                if re.search(r'\bOR\b', between_text, re.IGNORECASE):
                    topic_or = True
                    break
        
        if topic_or:
            conditions['topic_contains'] = {
                'values': topic_values,
                'operator': 'OR'
            }
        else:
            conditions['topic_contains'] = {
                'values': topic_values,
                'operator': 'AND'
            }
    
    # Parse Status condition
    status_match = re.search(r"p\.Status\s*=\s*'([^']+)'", conditions_str, re.IGNORECASE)
    if status_match:
        conditions['status'] = status_match.group(1).lower()
    
    # Parse Amount condition
    amount_match = re.search(r"f\.Amount\s*>\s*(\d+)", conditions_str, re.IGNORECASE)
    if amount_match:
        conditions['amount_min'] = int(amount_match.group(1))
    
    # Parse date BETWEEN condition (e.g., p.et BETWEEN '2022-01-01' AND '2022-12-31')
    date_between_match = re.search(r"p\.(\w+)\s+BETWEEN\s+'([^']+)'\s+AND\s+'([^']+)'", conditions_str, re.IGNORECASE)
    if date_between_match:
        date_field = date_between_match.group(1).lower()
        date_start = date_between_match.group(2)
        date_end = date_between_match.group(3)
        conditions['date_range'] = {
            'field': date_field,
            'start': date_start,
            'end': date_end
        }
    
    # Parse field LIKE condition (e.g., p.et LIKE '%2022%')
    handled_fields = {'topic', 'type', 'status'}
    field_like_matches = re.finditer(r"p\.(\w+)\s+LIKE\s+'%([^%]+)%'", conditions_str, re.IGNORECASE)
    for field_like_match in field_like_matches:
        field_name = field_like_match.group(1).lower()
        field_value = field_like_match.group(2).lower()
        if field_name not in handled_fields:
            conditions[f'field_like_{field_name}'] = field_value
    
    # Parse field comparison operators (e.g., p.et <= 2023, p.et >= 2022)
    comparison_patterns = [
        (r"p\.(\w+)\s*<=\s*(\d+)", '<='),
        (r"p\.(\w+)\s*>=\s*(\d+)", '>='),
        (r"p\.(\w+)\s*<\s*(\d+)", '<'),
        (r"p\.(\w+)\s*>\s*(\d+)", '>'),
        (r"p\.(\w+)\s*=\s*(\d+)", '=')
    ]
    
    for pattern, operator in comparison_patterns:
        comp_match = re.search(pattern, conditions_str, re.IGNORECASE)
        if comp_match:
            field_name = comp_match.group(1).lower()
            field_value = int(comp_match.group(2))
            if field_name not in handled_fields:
                conditions[f'field_comp_{field_name}'] = {
                    'operator': operator,
                    'value': field_value
                }
    
    return conditions

def process_ground_truth_file(file_path, funding_df, conditions, select_columns):
    """Process a single ground truth labels file and return matching records."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return [], []
            
            projects = json.loads(content)
            
            # Collect matching records
            matching_records = []
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
                
                # Check topic condition - handle multiple topic LIKE conditions with AND or OR
                topic_match = True
                if 'topic_contains' in conditions:
                    topic = project_data.get('topic', '').lower()
                    topic_condition = conditions['topic_contains']
                    
                    if isinstance(topic_condition, dict):
                        # New format with operator
                        topic_values = topic_condition['values']
                        operator = topic_condition['operator']
                        if operator == 'OR':
                            # At least one topic value must be in the topic string
                            topic_match = any(value in topic for value in topic_values)
                        else:  # AND
                            # All topic values must be in the topic string
                            topic_match = all(value in topic for value in topic_values)
                    elif isinstance(topic_condition, list):
                        # Legacy format - treat as AND for backward compatibility
                        topic_match = all(value in topic for value in topic_condition)
                    else:
                        # Single topic value
                        topic_match = topic_condition in topic
                
                # Check status condition
                status_match = True
                if 'status' in conditions:
                    status = project_data.get('status', '').lower()
                    status_match = status == conditions['status']
                
                # Check date range condition
                date_match = True
                if 'date_range' in conditions:
                    date_field = conditions['date_range']['field']
                    date_value = project_data.get(date_field, '')
                    date_match = check_date_in_range(
                        date_value,
                        conditions['date_range']['start'],
                        conditions['date_range']['end']
                    )
                
                # Check field LIKE conditions
                field_like_match = True
                for key, value in conditions.items():
                    if key.startswith('field_like_'):
                        field_name = key.replace('field_like_', '')
                        field_value = project_data.get(field_name, '').lower()
                        field_like_match = field_like_match and (value in field_value)
                
                # Check field comparison conditions
                field_comp_match = True
                for key, comp_info in conditions.items():
                    if key.startswith('field_comp_'):
                        field_name = key.replace('field_comp_', '')
                        operator = comp_info['operator']
                        comp_value = comp_info['value']
                        field_value = project_data.get(field_name, '')
                        
                        if field_value and field_value.lower() != 'none':
                            year_match = re.search(r'(\d{4})', field_value)
                            if year_match:
                                field_year = int(year_match.group(1))
                                if operator == '<=':
                                    field_comp_match = field_comp_match and (field_year <= comp_value)
                                elif operator == '>=':
                                    field_comp_match = field_comp_match and (field_year >= comp_value)
                                elif operator == '<':
                                    field_comp_match = field_comp_match and (field_year < comp_value)
                                elif operator == '>':
                                    field_comp_match = field_comp_match and (field_year > comp_value)
                                elif operator == '=':
                                    field_comp_match = field_comp_match and (field_year == comp_value)
                            else:
                                field_comp_match = False
                        else:
                            field_comp_match = False
                
                # Check funding amount condition
                funding_match = True
                if 'amount_min' in conditions:
                    project_funding = funding_df[funding_df['Project Name'] == project_name]
                    if project_funding.empty:
                        funding_match = False
                    else:
                        amounts = project_funding['Amount'].values
                        funding_match = any(amount > conditions['amount_min'] for amount in amounts)
                
                # All conditions must match
                if type_match and type_contains_match and topic_match and status_match and date_match and field_like_match and field_comp_match and funding_match:
                    # Get all funding records for this project
                    project_funding = funding_df[funding_df['Project Name'] == project_name]
                    if not project_funding.empty:
                        for _, funding_row in project_funding.iterrows():
                            record = {}
                            for col in select_columns:
                                if col == 'Project_Name':
                                    record[col] = project_name
                                elif col == 'Funding_Source':
                                    record[col] = funding_row['Funding Source']
                                elif col == 'Amount':
                                    record[col] = int(funding_row['Amount'])
                                elif col == 'Status':
                                    record[col] = project_data.get('status', '')
                                else:
                                    # Try to get from project_data or funding_row
                                    if col in project_data:
                                        record[col] = project_data[col]
                                    elif col in funding_row:
                                        record[col] = funding_row[col]
                            
                            matching_records.append(record)
                            matching_projects.append(project_name)
            
            return matching_records, matching_projects
            
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not process {file_path.name}: {e}")
        return [], []

def parse_date(date_str):
    """Parse date string in various formats to datetime object."""
    if not date_str or date_str.lower() == 'none':
        return None
    
    date_str_lower = date_str.lower()
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        return None
    
    year = int(year_match.group(1))
    
    if 'spring' in date_str_lower:
        try:
            return datetime(year, 4, 15)
        except:
            pass
    elif 'summer' in date_str_lower:
        try:
            return datetime(year, 7, 15)
        except:
            pass
    elif 'fall' in date_str_lower or 'autumn' in date_str_lower:
        try:
            return datetime(year, 10, 15)
        except:
            pass
    elif 'winter' in date_str_lower:
        try:
            return datetime(year, 1, 15)
        except:
            pass
    
    month_names = {
        'january': 1, 'jan': 1, 'february': 2, 'feb': 2,
        'march': 3, 'mar': 3, 'april': 4, 'apr': 4,
        'may': 5, 'june': 6, 'jun': 6, 'july': 7, 'jul': 7,
        'august': 8, 'aug': 8, 'september': 9, 'sep': 9, 'sept': 9,
        'october': 10, 'oct': 10, 'november': 11, 'nov': 11,
        'december': 12, 'dec': 12
    }
    
    for month_name, month_num in month_names.items():
        if month_name in date_str_lower:
            try:
                return datetime(year, month_num, 1)
            except:
                pass
    
    month_match = re.search(r'-(\d{1,2})(?:-|$)', date_str)
    if month_match:
        month = int(month_match.group(1))
        try:
            return datetime(year, month, 1)
        except:
            pass
    
    date_formats = ['%Y-%m-%d', '%Y-%m', '%Y', '%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S']
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str[:len(fmt.replace('%', '').replace('Y', 'YYYY').replace('m', 'MM').replace('d', 'DD'))], fmt)
        except:
            continue
    
    try:
        return datetime(year, 1, 1)
    except:
        pass
    
    return None

def check_date_in_range(date_str, date_start, date_end):
    """Check if a date string falls within the given range."""
    if not date_str or date_str.lower() == 'none':
        return False
    
    date_obj = parse_date(date_str)
    if not date_obj:
        return False
    
    start_obj = parse_date(date_start)
    end_obj = parse_date(date_end)
    
    if not start_obj or not end_obj:
        return False
    
    if len(date_end) == 4:
        end_obj = datetime(int(date_end), 12, 31)
    
    return start_obj <= date_obj <= end_obj

def verify_project_predicates(project_name, project_data, funding_df, conditions):
    """Verify if a project satisfies all SQL predicates."""
    verification = {
        'project_name': project_name,
        'all_pass': True,
        'checks': {}
    }
    
    if 'type' in conditions:
        project_type = project_data.get('type', '').lower()
        type_match = project_type == conditions['type']
        verification['checks']['type'] = {
            'required': conditions['type'],
            'actual': project_type,
            'pass': type_match
        }
        verification['all_pass'] = verification['all_pass'] and type_match
    
    if 'type_contains' in conditions:
        project_type = project_data.get('type', '').lower()
        type_contains_match = conditions['type_contains'] in project_type
        verification['checks']['type_contains'] = {
            'required': f"contains '{conditions['type_contains']}'",
            'actual': project_type,
            'pass': type_contains_match
        }
        verification['all_pass'] = verification['all_pass'] and type_contains_match
    
    if 'topic_contains' in conditions:
        topic = project_data.get('topic', '').lower()
        topic_condition = conditions['topic_contains']
        
        if isinstance(topic_condition, dict):
            # New format with operator
            topic_values = topic_condition['values']
            operator = topic_condition['operator']
            if operator == 'OR':
                topic_match = any(value in topic for value in topic_values)
                required_str = f"contains any of {topic_values} (OR)"
            else:  # AND
                topic_match = all(value in topic for value in topic_values)
                required_str = f"contains all of {topic_values} (AND)"
        elif isinstance(topic_condition, list):
            # Legacy format - treat as AND
            topic_match = all(value in topic for value in topic_condition)
            required_str = f"contains all of {topic_condition} (AND)"
        else:
            # Single topic value
            topic_match = topic_condition in topic
            required_str = f"contains '{topic_condition}'"
        
        verification['checks']['topic_contains'] = {
            'required': required_str,
            'actual': topic,
            'pass': topic_match
        }
        verification['all_pass'] = verification['all_pass'] and topic_match
    
    if 'status' in conditions:
        status = project_data.get('status', '').lower()
        status_match = status == conditions['status']
        verification['checks']['status'] = {
            'required': conditions['status'],
            'actual': status,
            'pass': status_match
        }
        verification['all_pass'] = verification['all_pass'] and status_match
    
    if 'date_range' in conditions:
        date_field = conditions['date_range']['field']
        date_value = project_data.get(date_field, '')
        date_match = check_date_in_range(
            date_value,
            conditions['date_range']['start'],
            conditions['date_range']['end']
        )
        verification['checks']['date_range'] = {
            'required': f"{date_field} BETWEEN '{conditions['date_range']['start']}' AND '{conditions['date_range']['end']}'",
            'actual': date_value,
            'pass': date_match
        }
        verification['all_pass'] = verification['all_pass'] and date_match
    
    for key, value in conditions.items():
        if key.startswith('field_like_'):
            field_name = key.replace('field_like_', '')
            field_value = project_data.get(field_name, '').lower()
            field_match = value in field_value
            verification['checks'][key] = {
                'required': f"{field_name} LIKE '%{value}%'",
                'actual': project_data.get(field_name, ''),
                'pass': field_match
            }
            verification['all_pass'] = verification['all_pass'] and field_match
    
    for key, comp_info in conditions.items():
        if key.startswith('field_comp_'):
            field_name = key.replace('field_comp_', '')
            operator = comp_info['operator']
            comp_value = comp_info['value']
            field_value = project_data.get(field_name, '')
            
            field_match = False
            extracted_year = None
            if field_value and field_value.lower() != 'none':
                year_match = re.search(r'(\d{4})', field_value)
                if year_match:
                    extracted_year = int(year_match.group(1))
                    if operator == '<=':
                        field_match = extracted_year <= comp_value
                    elif operator == '>=':
                        field_match = extracted_year >= comp_value
                    elif operator == '<':
                        field_match = extracted_year < comp_value
                    elif operator == '>':
                        field_match = extracted_year > comp_value
                    elif operator == '=':
                        field_match = extracted_year == comp_value
            
            verification['checks'][key] = {
                'required': f"{field_name} {operator} {comp_value}",
                'actual': f"{field_value} (year: {extracted_year if extracted_year is not None else 'N/A'})",
                'pass': field_match
            }
            verification['all_pass'] = verification['all_pass'] and field_match
    
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
    
    # Parse SELECT clause to get columns to return
    select_columns = parse_sql_select(sql_query)
    print(f"Selected columns: {select_columns}\n")
    
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
        records, matching_projects = process_ground_truth_file(file_path, funding_df, conditions, select_columns)
        results[file_path.name] = records
        all_matching_projects.extend([(file_path.name, pname) for pname in matching_projects])
        print(f"{file_path.name}: {len(records)} records")
    
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
    
    # Store results as JSON (doc name as key, list of records as value)
    output_file = Path(__file__).parent / "ground_truth.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Ground truth saved to {output_file}")
    return results

if __name__ == "__main__":
    results = generate_ground_truth()
    print(f"\nTotal files processed: {len(results)}")

