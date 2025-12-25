code = """import json
import pandas as pd

file_path = locals()['var_function-call-16123289365089937645']
with open(file_path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

# Scoring function
def sports_score(text):
    text = text.lower()
    score = 0
    # High value keywords (unambiguous)
    high_keywords = [
        'olympic', 'olympiad', 'athens 2004', 'athens games', 'gold medal', 'silver medal', 'bronze medal', 
        'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'us open', 'french open', 'australian open', 
        'formula one', 'nascar', 'pga', 'lpga', 'world cup', 'super bowl', 'stanley cup', 'world series', 
        'champions league', 'premier league', 'bundesliga', 'serie a', 'la liga', 'tour de france', 
        'red sox', 'yankees', 'lakers', 'pistons', 'spurs', 'pacers', 'patriots', 'eagles', 
        'arsenal', 'man utd', 'real madrid', 'barcelona', 'ac milan', 'juventus', 'bayern', 
        'schumacher', 'armstrong', 'phelps', 'williams sisters', 'federer', 'roddick', 'agassi', 
        'sharapova', 'woods', 'mickelson', 'annika sorenstam', 'ichiro', 'bonds'
    ]
    # Medium value keywords
    medium_keywords = [
        'basketball', 'baseball', 'football', 'soccer', 'tennis', 'hockey', 'golf', 'boxing', 'racing', 
        'volleyball', 'badminton', 'gymnastics', 'swimming', 'track and field', 'athletics', 'marathon', 
        'sprint', 'relay', 'wrestling', 'judo', 'taekwondo', 'fencing', 'archery', 'rowing', 'sailing', 
        'equestrian', 'triathlon', 'decathlon', 'heptathlon'
    ]
    # Low value keywords (need context)
    low_keywords = [
        'sport', 'game', 'match', 'team', 'coach', 'player', 'athlete', 'medal', 'gold', 'silver', 'bronze', 
        'cup', 'tournament', 'championship', 'league', 'score', 'win', 'loss', 'victory', 'defeat', 'draw', 
        'record', 'season', 'playoff', 'final', 'semi-final', 'quarter-final'
    ]
    
    for k in high_keywords:
        if k in text:
            score += 5
    for k in medium_keywords:
        if k in text:
            score += 3
    for k in low_keywords:
        if k in text:
            score += 1
            
    return score

df['sports_score'] = (df['title'] + " " + df['description']).apply(sports_score)
df['desc_len'] = df['description'].str.len()

# Filter candidates with score >= 3 (at least one medium or 3 low or 1 high)
candidates = df[df['sports_score'] >= 3].sort_values('desc_len', ascending=False)

# Get top 5
top_5 = candidates.head(5)[['title', 'description', 'desc_len', 'sports_score']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-11154296010328489628': [{'_id': '694474029b2a2bdeadbf31f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-171696771051611798': ['authors', 'article_metadata'], 'var_function-call-8576431502399489278': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-9575702754113021911': [{'_id': '694474029b2a2bdeadbf31f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694474029b2a2bdeadbf31f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694474029b2a2bdeadbf31f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694474029b2a2bdeadbf31f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694474029b2a2bdeadbf31fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16516747551938445962': [{'_id': '694474029b2a2bdeadbf31f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694474029b2a2bdeadbf31f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694474029b2a2bdeadbf31f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694474029b2a2bdeadbf31f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694474029b2a2bdeadbf31fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16123289365089937645': 'file_storage/function-call-16123289365089937645.json', 'var_function-call-12970982467575397726': {'title': 'Web-apps are the legacy apps of the future.', 'description_length': 808, 'description': "  Back in the days of stone knives and bearskins applications were  things that were written in cretinous languages like COBOL that  ran on wierd 71 bit architectures and used messed up file formats like  JCL and VSAM files or whatever.  What's a 'Data Division'?  Some whiny  80s band from Manchester?      Of course today we are so much  smarter.  If you look at the evolution, from ML, to branched languages  to structured programming to OOP, and from 3270 applications, to PC  apps to client server to web apps, you can clearly see how the  applications programmer transformed himself from knuckle dragging  simian to homo sapiens. That's the stereotype, right?    We have a name for all that old stuff, a pejorative name:  'legacy'.1   I'm here to tell you that the web application is the new  legacy.  "}, 'var_function-call-4892955506907030126': 'file_storage/function-call-4892955506907030126.json'}

exec(code, env_args)
