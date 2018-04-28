import csv
import requests


def scrape(game='draftkings'):
    roto_grinders = ''.join([
        'https://rotogrinders.com',
        '/projected-stats/mlb-{}.csv?site={}'
    ])

    hold = [['playername', 'points']]
    for pos in ['hitter', 'pitcher']:
        url = roto_grinders.format(pos, game)
        content = requests.get(url).content.decode('utf-8')
        cr = csv.reader(content.splitlines(), delimiter=',')
        for p in list(cr):
            if len(p):
                hold.append([p[0], p[-1]])

    with open('data/current-projections.csv', 'w') as fp:
        w = csv.writer(fp, delimiter=',')
        w.writerows(hold)