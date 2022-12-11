#!/usr/bin/python3
#
# Advent of Code 2022
# Day 11, part 1
# https://github.com/krcs/aoc-2022
#
input = "./input.txt"

def read_lines(file):
    result = []

    with open(input,'r') as f:
        while True:
            line = f.readline()

            if len(line)>0:
                result.append(line.strip())

            if not line:
                break
    return result

lines = read_lines(input)

def parse_input(lines):
    idx = -1
    monkeys = []

    for line in lines:
        if line.startswith('Monkey'):
            idx += 1
            id = int(line[len('Monkey '):].replace(':',''))
            monkeys.append({
                'id' : id,
                'items': [],
                'operation': '',
                'test': { 
                    'div': 1, 
                    'true': -1, 
                    'false': -1 
                },
                'checks' : 0
            })

        if line.startswith('Starting items:'):
            items_str = line[len('Starting items: '):]
            monkeys[idx]['items'] = items_str.split(", ")

        if line.startswith('Operation:'):
            operation_str = line[len('Operation: new = '):]
            monkeys[idx]['operation'] = operation_str

        if line.startswith('Test:'):
            test = int(line[len('Test: divisible by '):])
            monkeys[idx]['test']['div'] = test

        if line.startswith('If true:'):
            true = int(line[len('If true: throw to monkey '):])
            monkeys[idx]['test']['true'] = true

        if line.startswith('If false:'):
            false = int(line[len('If false: throw to monkey '):])
            monkeys[idx]['test']['false'] = false 

    return monkeys



monkeys = parse_input(lines)
for round in range(20):
    for monkey in monkeys:
        for item in monkey['items']:
            wlevel = eval(monkey['operation'].replace('old',str(item)))
            wlevel //= 3
            if wlevel % monkey['test']['div'] == 0:
                monkeys[monkey['test']['true']]['items'].append(wlevel)
            else:
                monkeys[monkey['test']['false']]['items'].append(wlevel)
            monkey['checks'] += 1
        monkey['items'] = []

part1 = sorted([ monkey['checks'] for monkey in monkeys ], reverse=True)
print("Part 1:", part1[0]*part1[1])
