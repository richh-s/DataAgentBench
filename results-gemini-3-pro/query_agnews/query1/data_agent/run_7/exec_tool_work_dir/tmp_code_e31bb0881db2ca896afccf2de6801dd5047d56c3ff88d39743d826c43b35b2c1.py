code = """import json
import pandas as pd
import re

file_path = locals()['var_function-call-5860854601306860093']
with open(file_path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

# Keywords (using substring matching)
keywords = {
    'Business': ['oil', 'price', 'stocks', 'market', 'wall st', 'economy', 'dollar', 'trade', 'profit', 'shares', 'company', 'inc', 'corp', 'bank', 'rate', 'fed', 'ipo', 'inflation', 'invest', 'fund', 'business', 'sales', 'gm', 'ford', 'boeing', 'airways', 'ceo'],
    'Sci/Tech': ['google', 'web', 'software', 'computer', 'technology', 'space', 'nasa', 'internet', 'microsoft', 'virus', 'science', 'study', 'research', 'phone', 'mobile', 'linux', 'apple', 'server', 'chip', 'network', 'spam', 'online', 'digital', 'search engine', 'intel', 'code', 'bug', 'windows', 'unix', 'java', 'class', 'developer', 'application', 'orbit', 'manned', 'launch'],
    'World': ['iraq', 'war', 'president', 'government', 'country', 'minister', 'official', 'united nations', 'police', 'kill', 'bomb', 'military', 'blast', 'palestinian', 'israel', 'china', 'russia', 'bush', 'kerry', 'election', 'troops', 'gaza', 'baghdad', 'afghanistan', 'iran', 'nuclear', 'attack', 'force', 'sudan', 'darfur', 'venezuela', 'chavez', 'putin'],
    'Sports': ['olympic', 'medal', 'gold', 'team', 'game', 'win', 'cup', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'athlete', 'champion', 'coach', 'player', 'score', 'victory', 'defeat', 'league', 'athens', 'sox', 'yankees', 'lakers', 'red sox', 'mets', 'bulls', 'knicks', 'rangers', 'race', 'swimming', 'gymnastics', 'marathon', 'silver', 'bronze', 'sports', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'dream team', 'phelps', 'roddick', 'agassi', 'venus', 'serena', 'williams', 'armstrong', 'tour de france', 'f1', 'formula one', 'cricket', 'rugby', 'boxing', 'match', 'title', 'tournament', 'qualifying', 'final', 'semi-final', 'quarter-final', 'racing', 'motor', 'driver', 'united', 'arsenal', 'chelsea', 'liverpool', 'real madrid', 'barcelona', 'ac milan', 'juventus', 'bayern', 'cup', 'open', 'masters', 'grand slam', 'touchdown', 'homerun', 'strikeout', 'quarterback']
}

def classify(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text:
                scores[cat] += 1
    
    # Heuristics:
    # If "code", "java", "software" in text -> likely Sci/Tech, penalize Sports (reduce score or boost Sci/Tech)
    # Actually, the count should handle it if keywords are good.
    # But "final" in "final static Logger" counts as Sports.
    # "game" in "SimCity" counts as Sports.
    # Let's trust the counts but inspect the scores if needed.
    
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return "Unknown"
    return max_cat

df['category'] = df.apply(classify, axis=1)

# Filter Sports
sports_df = df[df['category'] == 'Sports'].copy()

# Calc len
sports_df['desc_len'] = sports_df['description'].astype(str).apply(len)

# Sort
sports_df = sports_df.sort_values('desc_len', ascending=False)

# Get top 10
top_10 = sports_df.head(10)[['title', 'description', 'desc_len']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_10))"""

env_args = {'var_function-call-7527779804282538118': ['articles'], 'var_function-call-7527779804282539207': ['authors', 'article_metadata'], 'var_function-call-7980116427146039164': [{'_id': '69446821247247aa632a648a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-7980116427146037227': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-15646640609932424543': [{'_id': '69446821247247aa632a648a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446821247247aa632a648b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446821247247aa632a648c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446821247247aa632a648d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446821247247aa632a648e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5860854601306860093': 'file_storage/function-call-5860854601306860093.json', 'var_function-call-2079702809120062311': {'error': 'No sports articles found', 'sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'Stocks End Up, But Near Year Lows (Reuters)', 'Money Funds Fell in Latest Week (AP)', 'Fed minutes show dissent over inflation (USATODAY.com)', 'Safety Net (Forbes.com)', 'Wall St. Bears Claw Back Into the Black']}, 'var_function-call-4041239902053374677': {'total': 10000, 'counts': {'Business': 3260, 'Sports': 2292, 'World': 2098, 'Sci/Tech': 1417, 'Unknown': 933}, 'random_titles': ['Possible security breach seen at AOL', 'Mob sets train on fire in Bangladesh', 'Dollar Gains on Euro After Muted U.S. CPI', 'Treasuries Yields Near Recent Lows', 'Three tested for bird flu discharged from Malaysian hospital', 'Sanders excites Ravens', 'U.S. Aircraft Make New Attack on Rebels in Najaf', 'Hollywood battles DVD chip makers', 'MOTOR RACING: IT #39;S TWO IN A ROW FOR DARIO', 'Treasury Prices Falter Before Auctions']}, 'var_function-call-7756651647694311905': [], 'var_function-call-13781640416408893278': [{'title': 'Pretty Log4J', 'description': '\\\\I\'ve been a big fan of Log4J  for a while now but haven\'t migrated any code\\over for one central reason.  The following line of code:\\\\    final static Logger logger = Logger.getLogger( "some.name" );\\\\... is amazingly ugly and difficult to work with.\\\\Most people use Log4J with a logger based on the classname:\\\\So we would probably see:\\\\    static Logger logger = Logger.getLogger( "org.apache.commons.feedparser.locate.FeedLocator" );\\\\Which is amazingly verbose.  A lot of developers shorten this to:\\\\    static Logger logger = Logger.getLogger( FeedLocator.class );\\\\But this still leaves us with cut and paste errors.\\\\What if we could just reduce it to:\\\\    static Logger logger = Logger.g ...\\\\', 'desc_len': 708}, {'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\', 'desc_len': 708}, {'title': 'THECHAT', 'description': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;', 'desc_len': 631}, {'title': 'China Begins Countdown for Next Manned Space Flight', 'description': 'By ELAINE KURTENBACH    SHANGHAI, China (AP) -- Chinese astronauts are in the final stages of preparing for a manned space mission that will orbit the globe 14 times before returning to Earth, a state-run newspaper reported Thursday.    The launch, expected sometime this month, will initially send a manned craft, the Shenzhou 5, into an oval orbit that at its closest will be 125 miles from Earth, the Liberation Daily reported, citing "relevant channels."    After circling the earth several times, the ship will enter an orbit at about 220 miles from earth, the report said...', 'desc_len': 580}, {'title': 'U.S. Bounces Back to Beat Greece 77-71', 'description': "ATHENS, Greece - Lamar Odom made a key defensive play on Greece's Dimitris Pipanikoulaou, preventing him from getting a clean layup attempt that could have cut the United States' lead to two points, and the Americans won 77-71 Tuesday night in the second round of the Olympic men's basketball tournament.    In a much closer game than expected, the Americans bounced back from their embarrassing loss to Puerto Rico in their opener and avoided dropping to 0-2, which would have matched their loss total from the previous 68 years...", 'desc_len': 532}]}

exec(code, env_args)
