code = """import json
import pandas as pd

file_path = locals()['var_function-call-4700871027590263339']
with open(file_path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

sports_keywords = [
    'olympic', 'olympics', 'athens', 'medal', 'gold medal', 'silver medal', 'bronze medal', 
    'baseball', 'mlb', 'red sox', 'yankees', 'mets', 'cubs', 'dodgers', 'braves', 'cardinals', 'giants',
    'basketball', 'nba', 'lakers', 'pistons', 'spurs', 'heat', 'shaq', 'kobe', 'lebron', 'pacers', 'knicks',
    'football', 'nfl', 'patriots', 'colts', 'eagles', 'quarterback', 'touchdown', 'super bowl', 'dolphins', 'vikings', 'cowboys', '49ers',
    'soccer', 'fifa', 'uefa', 'manchester', 'arsenal', 'chelsea', 'real madrid', 'barcelona', 'liverpool', 'ac milan', 'juventus', 'bayern', 'beckham',
    'hockey', 'nhl', 'stanley cup', 'maple leafs', 'canadiens', 'rangers',
    'tennis', 'wimbledon', 'us open', 'federer', 'roddick', 'agassi', 'serena', 'venus', 'sharapova', 'henin', 'mauresmo',
    'golf', 'woods', 'mickelson', 'pga', 'singh', 'els',
    'cycling', 'armstrong', 'tour de france', 'ullrich',
    'racing', 'nascar', 'formula one', 'f1', 'schumacher', 'button', 'barrichello',
    'boxing', 'wrestling', 'cricket', 'rugby', 
    'athlete', 'championship', 'tournament', 'world cup', 'world series', 
    'dream team', 'doping', 'steroids', 'balco'
]

# Words that might trigger false positives if used alone or in wrong context
ambiguous_keywords = ['race', 'run', 'win', 'loss', 'victory', 'defeat', 'game', 'match', 'team', 'coach', 'score', 'cup', 'club', 'field', 'strike']

# Negative keywords (if these are present, likely NOT sports, unless strong keywords exist)
tech_keywords = ['space', 'orbit', 'nasa', 'astronaut', 'satellite', 'galaxy', 'moon', 'mars', 'software', 'internet', 'broadband', 'microsoft', 'google', 'intel', 'linux', 'virus', 'spam', 'hacker', 'ipod']
business_keywords = ['stock', 'market', 'economy', 'oil', 'price', 'dollar', 'euro', 'bank', 'investor', 'profit', 'revenue', 'earnings', 'dow jones', 'nasdaq', 'wall st', 'fed', 'inflation', 'trade', 'deficit']
world_keywords = ['iraq', 'iran', 'palestinian', 'israel', 'gaza', 'baghdad', 'bomb', 'blast', 'killed', 'troops', 'soldier', 'rebel', 'president', 'bush', 'kerry', 'election', 'poll', 'parliament', 'minister']

def get_matching_keyword(text):
    text_lower = text.lower()
    
    # Check negative keywords first? 
    # If "space" and "race" -> "space race" -> Not sports.
    # If "presidential" and "race" -> Not sports.
    
    is_tech = any(k in text_lower for k in tech_keywords)
    is_biz = any(k in text_lower for k in business_keywords)
    is_world = any(k in text_lower for k in world_keywords)
    
    match = None
    
    # Check strong keywords
    for kw in sports_keywords:
        if kw in text_lower:
            # Exceptions
            if kw == 'athens' and ('treaty' in text_lower or 'eu' in text_lower): continue 
            # If strong keyword is present, it's likely sports even if other topics are mentioned (e.g. "Stocks fall as Olympics begin" - maybe Business? But "Olympic athlete wins" is sports)
            # Let's count it as sports for now if a strong keyword is there.
            return kw
            
    # Check ambiguous keywords only if no negative context
    if not (is_tech or is_biz or is_world):
        for kw in ambiguous_keywords:
            if kw in text_lower:
                # Extra checks
                if kw == 'race' and 'presidential' in text_lower: continue
                if kw == 'field' and ('magnetic' in text_lower or 'oil' in text_lower): continue
                if kw == 'strike' and ('union' in text_lower or 'air' in text_lower): continue
                return kw
                
    return None

df['match_keyword'] = df.apply(lambda row: get_matching_keyword(str(row['title']) + " " + str(row['description'])), axis=1)
sports_df = df[df['match_keyword'].notnull()]

sports_df['desc_len'] = sports_df['description'].apply(lambda x: len(str(x)))

# Get top 5 longest
top_5 = sports_df.sort_values('desc_len', ascending=False).head(5)

result = top_5[['title', 'match_keyword', 'desc_len']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10480147626898259871': ['articles'], 'var_function-call-10480147626898257344': ['authors', 'article_metadata'], 'var_function-call-13939615935546252294': [{'_id': '6944749d074f46943b49068a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944749d074f46943b49068b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944749d074f46943b49068c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944749d074f46943b49068d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944749d074f46943b49068e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-56986455496567506': [{'_id': '6944749d074f46943b49068a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944749d074f46943b49068b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944749d074f46943b49068c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944749d074f46943b49068d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944749d074f46943b49068e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4700871027590263339': 'file_storage/function-call-4700871027590263339.json', 'var_function-call-18339816460889542612': {'title': 'China Begins Countdown for Next Manned Space Flight', 'description_length': 580, 'description': 'By ELAINE KURTENBACH    SHANGHAI, China (AP) -- Chinese astronauts are in the final stages of preparing for a manned space mission that will orbit the globe 14 times before returning to Earth, a state-run newspaper reported Thursday.    The launch, expected sometime this month, will initially send a manned craft, the Shenzhou 5, into an oval orbit that at its closest will be 125 miles from Earth, the Liberation Daily reported, citing "relevant channels."    After circling the earth several times, the ship will enter an orbit at about 220 miles from earth, the report said...'}, 'var_function-call-14417579001079123824': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}]}

exec(code, env_args)
