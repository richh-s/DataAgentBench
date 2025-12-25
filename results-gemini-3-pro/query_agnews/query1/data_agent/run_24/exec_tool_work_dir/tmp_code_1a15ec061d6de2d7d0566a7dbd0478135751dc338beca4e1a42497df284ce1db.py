code = """import json
import pandas as pd

# Load the data
file_path = locals()['var_function-call-651803786089082059']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(articles)

# Calculate description length
df['desc_len'] = df['description'].apply(lambda x: len(x) if x else 0)

# Sort by length descending
df = df.sort_values('desc_len', ascending=False)

# Heuristic for Sports
def is_sports(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    
    # Positive keywords
    sports_keywords = [
        "sport", "olympic", "football", "basketball", "baseball", "soccer", 
        "hockey", "tennis", "golf", "medal", "athlete", "coach", "team", 
        "game", "tournament", "championship", "cup", "league", "nfl", "nba", 
        "mlb", "nhl", "fifa", "uefa", "racing", "driver", "match", "score"
    ]
    
    # Negative keywords (Business, Sci/Tech, World)
    # Be careful not to exclude "Sports Business" if that's considered Business (which it is).
    # But "Sports" category articles should focus on the sport.
    negative_keywords = [
        "stock", "market", "economy", "profit", "earnings", "revenue", "wall st", 
        "nasdaq", "dow jones", "investment", "shares", "company", "corp", "inc.", 
        "software", "computer", "technology", "microsoft", "google", "internet", 
        "space", "nasa", "scientist", "research", "biology", "physics", "video game",
        "console", "xbox", "playstation", "nintendo", "iraq", "president", "election",
        "minister", "bomb", "war", "security", "police"
    ]
    
    # Check if any positive keyword exists
    has_sport = any(k in text for k in sports_keywords)
    if not has_sport:
        return False
        
    # Check if negative keywords dominate or present context
    # If "game" refers to video game? "video game" is in negative.
    # If "team" refers to "research team"? "research" is in negative.
    
    has_negative = any(k in text for k in negative_keywords)
    
    # Refinement: If it has "olympic" it's almost certainly sports unless it's "Olympic security" (World/SciTech)
    # "Satellite boosts Olympic security" -> Sci/Tech.
    
    if has_negative:
        # Strong indicators that override negative?
        # Maybe not. Safety first.
        return False
        
    return True

# Apply filter
df['is_sports'] = df.apply(is_sports, axis=1)
sports_articles = df[df['is_sports']]

# Print top 10 candidates
print("__RESULT__:")
print(json.dumps(sports_articles[['title', 'description', 'desc_len']].head(10).to_dict(orient='records')))"""

env_args = {'var_function-call-1269522164093293289': ['articles'], 'var_function-call-1269522164093293944': ['authors', 'article_metadata'], 'var_function-call-12568169212486124168': [{'_id': '69447576476c718f6f0093a1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-12568169212486124789': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-4405237224219135175': [{'_id': '69447576476c718f6f0093a1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447576476c718f6f0093a2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447576476c718f6f0093a3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447576476c718f6f0093a4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447576476c718f6f0093a5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-234107968116991982': [{'_id': '69447576476c718f6f0093a1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447576476c718f6f0093a2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447576476c718f6f0093a3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447576476c718f6f0093a4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447576476c718f6f0093a5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3273741264274490333': [{'count(*)': '127600'}], 'var_function-call-8996360726762549650': [{'region': 'Asia'}, {'region': 'North America'}, {'region': 'South America'}, {'region': 'Europe'}, {'region': 'Africa'}], 'var_function-call-13771527386880163785': [{'author_id': '0', 'name': 'Felicia Miles'}, {'author_id': '1', 'name': 'Stacy Hunt'}, {'author_id': '2', 'name': 'Carol Reed'}, {'author_id': '3', 'name': 'Dr. Daniel Brown'}, {'author_id': '4', 'name': 'Andre Lam MD'}, {'author_id': '5', 'name': 'Meredith Collins'}, {'author_id': '6', 'name': 'Richard Owen'}, {'author_id': '7', 'name': 'Nathaniel Jones'}, {'author_id': '8', 'name': 'Ethan Bates'}, {'author_id': '9', 'name': 'Timothy Blevins'}], 'var_function-call-15592861099041803343': [], 'var_function-call-9580912821089221151': [{'_id': '69447576476c718f6f009466', 'article_id': '197', 'title': "'Invisible' technology for Olympics", 'description': 'Getting the technology in place for Athens 2004 is an Olympic task in itself.'}, {'_id': '69447576476c718f6f009467', 'article_id': '198', 'title': 'Satellite boosts Olympic security', 'description': 'An enhanced satellite location system aims to help Olympic security guards react more quickly to emergencies.'}, {'_id': '69447576476c718f6f0094a5', 'article_id': '260', 'title': 'Ancient Olympics Mixed Naked Sports, Pagan Partying', 'description': 'Nude athletes, performance-enhancing lizard meat, and animal sacrifices are just a few of the things that separate the ancient Olympics from the modern games, says the author of &lt;i&gt;The Naked Olympics.&lt;/i&gt;'}, {'_id': '69447576476c718f6f0094c4', 'article_id': '291', 'title': 'Olympics Could Call Out the Couch Potatoes', 'description': 'As the 2004 Summer Olympics officially get underway Friday with an international broadcast of the opening ceremonies, health experts expect the Athens games to inspire couch potatoes to become more active. But, experts caution, amateurs, particularly sedentary ones, should not jump into a new sports activity without sufficient preparation.'}, {'_id': '69447576476c718f6f00950a', 'article_id': '361', 'title': 'Olympic IT security requires advance planning', 'description': "If there's one thing the Atos Origin SA team understands as lead contractor for the Olympic IT infrastructure, it's that you must learn from your mistakes."}], 'var_function-call-651803786089082059': 'file_storage/function-call-651803786089082059.json'}

exec(code, env_args)
