code = """import json
import pandas as pd
import re

file_path = locals()['var_function-call-4700871027590263339']
with open(file_path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

# List of regex patterns for strict sports keywords
# Using \b to ensure whole word matches
sports_keywords = [
    r'\bolympic', r'\bolympics', r'\bathens', r'\bmedal', r'\bgold medal', r'\bsilver medal', r'\bbronze medal', 
    r'\bbaseball', r'\bmlb', r'\bred sox', r'\byankees', r'\bmets', r'\bcubs', r'\bdodgers', r'\bbraves', r'\bcardinals', 
    r'\bbasketball', r'\bnba', r'\blakers', r'\bpistons', r'\bspurs', r'\bshaq', r'\bkobe', r'\blebron', r'\bpacers', r'\bknicks',
    r'\bfootball', r'\bnfl', r'\bpatriots', r'\bcolts', r'\beagles', r'\bquarterback', r'\btouchdown', r'\bsuper bowl', r'\bdolphins', r'\bvikings', r'\bcowboys', r'\b49ers',
    r'\bsoccer', r'\bfifa', r'\buefa', r'\bmanchester', r'\barsenal', r'\bchelsea', r'\breal madrid', r'\bbarcelona', r'\bliverpool', r'\bac milan', r'\bjuventus', r'\bbayern', r'\bbeckham',
    r'\bhockey', r'\bnhl', r'\bstanley cup', r'\bmaple leafs', r'\bcanadiens', 
    r'\btennis', r'\bwimbledon', r'\bus open', r'\bfederer', r'\broddick', r'\bagassi', r'\bserena', r'\bvenus', r'\bsharapova', r'\bhenin', r'\bmauresmo',
    r'\bgolf', r'\bwoods', r'\bmickelson', r'\bpga', r'\bels',
    r'\bcycling', r'\barmstrong', r'\btour de france', r'\bullrich',
    r'\bracing', r'\bnascar', r'\bformula one', r'\bf1', r'\bschumacher', r'\bbarrichello',
    r'\bboxing', r'\bwrestling', r'\bcricket', r'\brugby', 
    r'\bathlete', r'\bchampionship', r'\btournament', r'\bworld cup', r'\bworld series', 
    r'\bdream team', r'\bdoping', r'\bsteroids', r'\bbalco',
    r'\bmarathon', r'\bsprint', r'\brelay', r'\bswimming', r'\bgymnastics', r'\bvolleyball'
]

# Compile regex
pattern = re.compile('|'.join(sports_keywords), re.IGNORECASE)

# Negative keywords
tech_keywords = [r'\bsoftware\b', r'\binternet\b', r'\bcomputer\b', r'\bmicrosoft\b', r'\bgoogle\b', r'\blinux\b']
tech_pattern = re.compile('|'.join(tech_keywords), re.IGNORECASE)

def get_match(text):
    if tech_pattern.search(text):
        return None
    match = pattern.search(text)
    if match:
        return match.group(0)
    return None

df['match_keyword'] = df.apply(lambda row: get_match(str(row['title']) + " " + str(row['description'])), axis=1)
sports_df = df[df['match_keyword'].notnull()]

sports_df['desc_len'] = sports_df['description'].apply(lambda x: len(str(x)))

top_5 = sports_df.sort_values('desc_len', ascending=False).head(5)

result = top_5[['title', 'match_keyword', 'desc_len', 'description']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10480147626898259871': ['articles'], 'var_function-call-10480147626898257344': ['authors', 'article_metadata'], 'var_function-call-13939615935546252294': [{'_id': '6944749d074f46943b49068a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944749d074f46943b49068b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944749d074f46943b49068c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944749d074f46943b49068d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944749d074f46943b49068e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-56986455496567506': [{'_id': '6944749d074f46943b49068a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944749d074f46943b49068b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944749d074f46943b49068c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944749d074f46943b49068d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944749d074f46943b49068e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4700871027590263339': 'file_storage/function-call-4700871027590263339.json', 'var_function-call-18339816460889542612': {'title': 'China Begins Countdown for Next Manned Space Flight', 'description_length': 580, 'description': 'By ELAINE KURTENBACH    SHANGHAI, China (AP) -- Chinese astronauts are in the final stages of preparing for a manned space mission that will orbit the globe 14 times before returning to Earth, a state-run newspaper reported Thursday.    The launch, expected sometime this month, will initially send a manned craft, the Shenzhou 5, into an oval orbit that at its closest will be 125 miles from Earth, the Liberation Daily reported, citing "relevant channels."    After circling the earth several times, the ship will enter an orbit at about 220 miles from earth, the report said...'}, 'var_function-call-14417579001079123824': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-5735159564906596604': [{'title': "Why Windows isn't Unix", 'match_keyword': 'run', 'desc_len': 708}, {'title': 'Pretty Log4J', 'match_keyword': 'win', 'desc_len': 708}, {'title': 'China Begins Countdown for Next Manned Space Flight', 'match_keyword': 'nba', 'desc_len': 580}, {'title': 'U.S. Bounces Back to Beat Greece 77-71', 'match_keyword': 'olympic', 'desc_len': 532}, {'title': 'DiMarco, Riley Play Way Into Ryder Cup (AP)', 'match_keyword': 'pga', 'desc_len': 483}]}

exec(code, env_args)
