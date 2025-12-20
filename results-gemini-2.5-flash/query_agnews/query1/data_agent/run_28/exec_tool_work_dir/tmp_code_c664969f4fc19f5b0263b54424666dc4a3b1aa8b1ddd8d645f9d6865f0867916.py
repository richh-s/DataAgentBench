code = """import pandas as pd
import json

# Access the raw tool output
tool_output = locals()['var_function-call-1022612550516394984']

# Navigate to the list of strings that contains the query result
data_container_list = tool_output['query_db_response']['results']

# Extract the single string from the list that contains the JSON data
result_string_with_preamble = data_container_list[0]

# Define the marker that precedes the actual JSON array string
json_data_start_marker = "The result is:\n"

# Find the index of the marker
start_index = result_string_with_preamble.find(json_data_start_marker)

df = pd.DataFrame() # Initialize an empty DataFrame

if start_index != -1:
    # Extract the part of the string after the marker
    json_part_raw = result_string_with_preamble[start_index + len(json_data_start_marker):]
    # Strip any leading/trailing whitespace, including newlines, to get the clean JSON array string
    json_array_string = json_part_raw.strip()

    try:
        parsed_data = json.loads(json_array_string)
        # Ensure parsed_data is a list before creating DataFrame
        if isinstance(parsed_data, list):
            df = pd.DataFrame(parsed_data)
        else:
            # If parsed_data is not a list (e.g., a single dict), wrap it in a list
            df = pd.DataFrame([parsed_data])
    except json.JSONDecodeError:
        # If JSON parsing fails, df remains empty.
        pass

# Define sports keywords for filtering
sports_keywords = [
    'Sports', 'Football', 'Basketball', 'Baseball', 'Tennis', 'Golf', 'Olympics',
    'World Series', 'Super Bowl', 'NBA Finals', 'Stanley Cup', 'Championship',
    'Games', 'Tournament', 'Athlete', 'Team', 'Player', 'Coach', 'Score', 'Victory',
    'Loss', 'Win', 'Defeat', 'Race', 'Match', 'Season', 'League', 'Cup', 'Medal',
    'Record', 'Fan', 'Stadium', 'Arena', 'Field', 'Court', 'Track', 'Pitch',
    'Boxing', 'UFC', 'MMA', 'Formula 1', 'Nascar', 'Cycling', 'Swimming', 'Athletics',
    'Skiing', 'Snowboarding', 'Surfing', 'Skateboarding', 'Gymnastics', 'Wrestling',
    'Volleyball', 'Hockey', 'Cricket', 'Rugby', 'Badminton', 'Table Tennis',
    'Fencing', 'Judo', 'Karate', 'Taekwondo', 'Weightlifting', 'Archery',
    'Shooting', 'Sailing', 'Rowing', 'Canoeing', 'Kayaking', 'Triathlon',
    'Biathlon', 'Pentathlon', 'Decathlon', 'Marathon', 'Sprint', 'Relay',
    'Freestyle', 'Backstroke', 'Breaststroke', 'Butterfly', 'Diving',
    'Figure Skating', 'Bobsled', 'Luge', 'Skeleton', 'Curling', 'Biathlon',
    'Playoffs', 'Draft', 'Trade', 'Contract', 'Injury', 'Retirement', 'Hall of Fame'
]

# Filter for sports articles based on keywords in title or description
sports_articles = pd.DataFrame() # Initialize an empty DataFrame for filtered articles

if not df.empty and 'title' in df.columns and 'description' in df.columns:
    # Initialize a boolean series for filtering, same length as df, all False initially
    combined_filter = pd.Series([False] * len(df), index=df.index)
    
    for keyword in sports_keywords:
        # Use .fillna('') to treat NaN values as empty strings for .str.contains
        title_matches = df['title'].fillna('').str.contains(keyword, case=False)
        description_matches = df['description'].fillna('').str.contains(keyword, case=False)
        
        # Combine the filters using element-wise OR operation
        combined_filter = combined_filter | title_matches | description_matches
    
    # Apply the combined filter to get sports articles and remove duplicates
    sports_articles = df[combined_filter].drop_duplicates()

# Determine the final result
result = "No sports articles found." # Default result if no sports articles are found

if not sports_articles.empty:
    if 'description' in sports_articles.columns:
        # Calculate the length of the description after filling NaN with empty strings
        sports_articles['description_length'] = sports_articles['description'].fillna('').str.len()
        
        # Filter for articles that actually have non-empty descriptions
        articles_with_valid_descriptions = sports_articles[sports_articles['description_length'] > 0]
        
        if not articles_with_valid_descriptions.empty:
            # Find the article with the maximum description length
            longest_description_article = articles_with_valid_descriptions.loc[articles_with_valid_descriptions['description_length'].idxmax()]
            result = longest_description_article['title']
        else:
            result = "No sports articles with non-empty descriptions found."
    else:
        result = "No description column found for sports articles."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-13890009462590654747': [{'_id': '6943c944083eb087172873bc', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c944083eb087172873bd', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c944083eb087172873be', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c944083eb087172873bf', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c944083eb087172873c0', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1022612550516394984': [{'_id': '6943c944083eb087172873bc', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c944083eb087172873bd', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c944083eb087172873be', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c944083eb087172873bf', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c944083eb087172873c0', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
