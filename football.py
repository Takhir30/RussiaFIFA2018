from itertools import combinations
from numpy.random import choice
from random import shuffle
from prettytable import PrettyTable


groups = {
    'A': {
    'Egypt': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Russia': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Saudi Arabia': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Uruguay': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}
    },
    'B': {
    'Iran': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Marocco': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Portugal': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Spain': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}
    },
    'C': {
    'Australia': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Denmark': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'France': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Peru': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}
    },
    'D': {
    'Argentina': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Croatia': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Iceland': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Nigeria': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}
    },
    'E': {
    'Brasil': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Croatia': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Serbia': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Switherland': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}
    },
    'F': {
    'Germany': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Korea Republic': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Mexico': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Sweden': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}
    },
    'G': {
    'Belgium': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'England': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Panama': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Tunisia': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}
    },
    'H': {
    'Colombia': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Japan': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Poland': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0},
    'Senegal': {'games': 0, 'won': 0, 'draw': 0, 'lost': 0, 'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}
    }
}


def goals_per_team():
    goals = choice(range(0, 10), p=[0.37, 0.27, 0.2, 0.13, 0.021, 0.005,
                                    0.002, 0.0014, 0.0005, 0.0001])
    return goals


def group_results(group_name):
    group = groups[group_name]
    matches = [i for i in combinations(group.keys(), 2)]
    shuffle(matches)
    t = PrettyTable(['Country', 'games', 'won', 'draw', 'lost', 'gf', 'ga', 'diff', 'points'])
    for teams in matches:
        team_1_goals = goals_per_team()
        team_2_goals = goals_per_team()
        print(f'{teams[0]}:{teams[1]} - {team_1_goals}:{team_2_goals}')
        result_of_match = [[teams[0], team_1_goals, team_2_goals],
                           [teams[1], team_2_goals, team_1_goals]]
        statistics(result_of_match, group_name)
    print('<----------------------->\n')
    print(f'GROUP {group_name}')
    for k, v in sorted(group.items(), key=lambda x: (x[1]['points'], x[1]['diff']), reverse = True):
        t.add_row([k, v['games'], v['won'], v['draw'], v['lost'], v['gf'], v['ga'], v['diff'], v['points']])
    print(t)


def group_stage_games(groups):
    for group in groups:
        group_results(group)
        print('\n<----------------------->')


def statistics(result, group):
    for i in result:
        groups[group][i[0]]['games'] += 1
        groups[group][i[0]]['gf'] += i[1]
        groups[group][i[0]]['ga'] += i[2]
        groups[group][i[0]]['diff'] += i[1] - i[2]
        if i[1] > i[2]:
            groups[group][i[0]]['won'] += 1
            groups[group][i[0]]['points'] += 3
        elif i[1] == i[2]:
            groups[group][i[0]]['draw'] += 1
            groups[group][i[0]]['points'] += 1
        else:
            groups[group][i[0]]['lost'] += 1


group_stage_games(groups)
