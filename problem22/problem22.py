# project euler problem 22
# http://projecteuler.net/problem=22

def get_data_set():
    with open('names.txt', 'r') as f:
        data = f.read().split(',')
        return sorted(data)

total_score = 0
data = get_data_set()
for index, name in enumerate(data, 1):
    s = name.replace('"', '')
    total_score += index * (sum(map(lambda x:ord(x) - 64, s)))

print total_score
