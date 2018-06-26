from itertools import combinations
from numpy.random import choice
from random import shuffle
from prettytable import PrettyTable


stats = {'games': 0, 'won': 0, 'draw': 0, 'lost': 0,
         'gf': 0, 'ga': 0, 'diff': 0, 'points': 0}

groups = {
    'A': {'Egypt': stats, 'Russia': stats,
          'Saudi Arabia': stats, 'Uruguay': stats},
    'B': {'Iran': stats, 'Marocco': stats,
          'Portugal': stats, 'Spain': stats},
    'C': {'Australia': stats, 'Denmark': stats,
          'France': stats, 'Peru': stats},
    'D': {'Argentina': stats, 'Croatia': stats,
          'Iceland': stats, 'Nigeria': stats},
    'E': {'Brasil': stats, 'Croatia': stats,
          'Serbia': stats, 'Switherland': stats},
    'F': {'Germany': stats, 'Korea Republic': stats,
          'Mexico': stats, 'Sweden': stats},
    'G': {'Belgium': stats, 'England': stats,
          'Panama': stats, 'Tunisia': stats},
    'H': {'Colombia': stats, 'Japan': stats,
          'Poland': stats, 'Senegal': stats}
}

final_grid = [['A1', 'B2'], ['C1', 'D2'], ['E1', 'F2'], ['G1', 'H2'],
              ['B1', 'A2'], ['D1', 'C2'], ['F1', 'E2'], ['H1', 'G2']]


# Random number of goals taking into account the dispersion
def goals():
    goals = choice(range(0, 10), p=[0.37, 0.27, 0.2, 0.13, 0.021, 0.005,
                                    0.002, 0.0014, 0.0005, 0.0001])
    return goals


# Random number of penalty goals taking into account the dispersion
def penalty_goals():
    goals = choice(range(0, 6), p=[0.01, 0.02, 0.07, 0.1, 0.4, 0.4])
    return goals


# The result of a single match
def match(team_1, team_2):
    team_1_goals = goals()
    team_2_goals = goals()
    print(f'{team_1}:{team_2} - {team_1_goals}:{team_2_goals}')
    return [[team_1, team_1_goals, team_2_goals],
            [team_2, team_2_goals, team_1_goals]]


# Combinating all teams in a group, playing all matches in a group,
# printing all results with some statistic and returning two best teams
def group_results(group_name):
    group = groups[group_name]
    matches = [i for i in combinations(group.keys(), 2)]
    shuffle(matches)
    mini_group = {}
    place = 1
    for teams in matches:
        result_of_match = match(teams[0], teams[1])
        statistics(result_of_match, group_name)
    print('<----------------------->\n')
    print(f'GROUP {group_name}')
    t = PrettyTable(['Country', 'games', 'won', 'draw', 'lost',
                     'gf', 'ga', 'diff', 'points'])
    for k, v in sorted(group.items(),
                       key=lambda x: (x[1]['points'], x[1]['diff']),
                       reverse = True):
        t.add_row([k, v['games'], v['won'], v['draw'], v['lost'],
                      v['gf'], v['ga'], v['diff'], v['points']])
        if place < 3:
            mini_group[group_name + str(place)] = k
            place += 1
    print(t)
    return mini_group


# Iterating trougth all groups and returning all winners
def group_stage(groups):
    play_off_teams = {}
    for group in groups:
        play_off = group_results(group)
        print('\n<----------------------->')
        play_off_teams.update(play_off)
    return play_off_teams


# Counting goals, points, etc to define a winners
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


# Penalty statements
def penalties(team_1, team_2):
    while True:
        team_1_goals = penalty_goals()
        team_2_goals = penalty_goals()
        if team_1_goals != team_2_goals:
            print(f'Penalty:    {team_1_goals}:{team_2_goals} --------------->')
            if team_1_goals > team_2_goals:
                return team_1, team_2
            else:
                return team_2, team_1


# Overall statements to kick a team out
def kick_out(result):
    team_1 = result[0][0]
    team_2 = result[1][0]
    team_1_goals = result[0][1]
    team_2_goals = result[1][1]
    if team_1_goals != team_2_goals:
        if team_1_goals > team_2_goals:
            return team_1, team_2
        else:
            return team_2, team_1
    else:
        winner, loser = penalties(team_1, team_2)
        return winner, loser


# Quaterfinal iterating trougth the winner and the loser lists
# to choose a winner
def quaterfinal(mini_grid):
    winners = []
    losers = []
    a = PrettyTable(['Place', 'Country'])
    if len(mini_grid) == 8 or len(mini_grid) == 4:
        print(f'\n1/{len(mini_grid)//2} final')
        for teams in range(0, len(mini_grid), 2):
            result = match(mini_grid[teams], mini_grid[teams+1])
            winner, loser = kick_out(result)
            winners.append(winner)
            losers.append(loser)
        if len(mini_grid) == 4:
            print('\n3rd place game')
            result = match(losers[0], losers[1])
            third_place, loser = kick_out(result)
            print('\nFinal')
            result = match(winners[0], winners[1])
            first_place, second_place = kick_out(result)
            a.add_row([1, first_place])
            a.add_row([2, second_place])
            a.add_row([3, third_place])
            print('\n', a, '\n')
        else:
            quaterfinal(winners)


# Final stage games
def final_stage(final_grid, play_off_teams):
    winners = []
    losers = []
    print('\n1/8 final')
    for teams in final_grid:
        result = match(play_off_teams[teams[0]], play_off_teams[teams[1]])
        winner, loser = kick_out(result)
        winners.append(winner)
    quaterfinal(winners)


def main():
    play_off_teams = group_stage(groups)
    final_stage(final_grid, play_off_teams)


if __name__ == '__main__':
    main()
