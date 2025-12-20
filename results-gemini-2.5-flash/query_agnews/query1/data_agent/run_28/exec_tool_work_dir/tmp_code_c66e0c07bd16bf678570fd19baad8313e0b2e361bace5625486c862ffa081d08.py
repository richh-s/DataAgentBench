code = """import pandas as pd
import json

# Access the raw tool output
tool_output = locals()['var_function-call-1022612550516394984']

# Navigate to the list of strings that contains the query result
data_container_list = tool_output['query_db_response']['results']

# Extract the single string from the list
result_string = data_container_list[0]

# Find the start of the JSON array within the string
json_start_index = result_string.find('[')

# If a '[' is found, try to parse the JSON part
df = pd.DataFrame() # Initialize an empty DataFrame
if json_start_index != -1:
    json_data_string = result_string[json_start_index:]
    try:
        parsed_data = json.loads(json_data_string)
        df = pd.DataFrame(parsed_data)
    except json.JSONDecodeError as e:
        # Handle JSON parsing error if necessary
        pass

# Define sports keywords
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

# Filter for sports articles
sports_articles = pd.DataFrame()
if not df.empty:
    combined_filter = pd.Series([False] * len(df), index=df.index)
    for keyword in sports_keywords:
        title_matches = df['title'].str.contains(keyword, case=False, na=False) if 'title' in df.columns else combined_filter
        description_matches = df['description'].str.contains(keyword, case=False, na=False) if 'description' in df.columns else combined_filter
        combined_filter = combined_filter | title_matches | description_matches
    sports_articles = df[combined_filter].drop_duplicates()

# Determine the result
result = "No sports articles found." # Default result
if not sports_articles.empty:
    if 'description' in sports_articles.columns:
        sports_articles['description_length'] = sports_articles['description'].fillna('').str.len()
        if not sports_articles['description_length'].empty and sports_articles['description_length'].max() > 0:
            longest_description_article = sports_articles.loc[sports_articles['description_length'].idxmax()]
            result = longest_description_article['title']
        else:
            result = "No sports articles with non-empty descriptions found."
    else:
        result = "No description column found for sports articles."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-13890009462590654747': [{'_id': '6943c944083eb087172873bc', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c944083eb087172873bd', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c944083eb087172873be', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c944083eb087172873bf', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c944083eb087172873c0', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1022612550516394984': [{'_id': '6943c944083eb087172873bc', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c944083eb087172873bd', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c944083eb087172873be', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c944083eb087172873bf', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c944083eb087172873c0', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
