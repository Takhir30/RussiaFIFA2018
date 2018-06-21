from itertools import combinations
from numpy.random import choice
from random import shuffle


groups = {
    'A': {'Egypt': [], 'Russia': [], 'Saudi Arabia': [], 'Uruguay': []},
    'B': {'Iran': [], 'Marocco': [], 'Portugal': [], 'Spain': []},
    'C': {'Australia': [],'Denmark': [], 'France': [], 'Peru': []},
    'D': {'Argentina': [], 'Croatia': [], 'Iceland': [], 'Nigeria': []},
    'E': {'Brasil': [], 'Croatia': [], 'Serbia': [], 'Switherland': []},
    'F': {'Germany': [], 'Korea Republick': [], 'Mexico': [], 'Sweden': []},
    'G': {'Belgium': [], 'England': [], 'Panama': [], 'Tunisia': []},
    'H': {'Colombia': [], 'Japan': [], 'Poland': [], 'Senegal': []}
}


def goals_per_team():
    goals = choice(range(0, 10), p=[0.37, 0.27, 0.2, 0.13, 0.021, 0.005,
                                    0.002, 0.0014, 0.0005, 0.0001])
    return goals


def group_results(group_name):
    group = groups[group_name]
    matches = [i for i in combinations(group.keys(), 2)]
    shuffle(matches)
    for match_result in matches:
        print(f'{match_result[0]}:{match_result[1]} - {goals_per_team()}:{goals_per_team()}')


def group_stage_games(groups):
    for group in groups:
        group_results(group)
        print('<----------------------->')



group_stage_games(groups)
