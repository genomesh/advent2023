file = open("input.txt", "r")

seed_inits = []
seed_ranges = []
map_objs = []

class map_obj:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.maps = []
    
    def get_source_id(self, dest_id):
        for m in self.maps:
            if dest_id >= m['dest_start'] and dest_id <  m['dest_start'] + m['range']:
                return dest_id + m['source_start'] - m['dest_start']
        return dest_id

for line in file.readlines():
    if line.strip() == '':
        continue
    if line[0:6] == 'seeds:':
        seeds_and_ranges = list(map(int, line.strip().split(' ')[1:]))
        l = len(seeds_and_ranges)
        seed_inits = seeds_and_ranges[0:l:2]
        seed_ranges = seeds_and_ranges[1:l:2]
        continue
    if ':' in line:
        source, destination = line.split('-')[0:3:2]
        map_objs.append(map_obj(source, destination.split(' ')[0]))
    else:
        keys = ['dest_start', 'source_start', 'range']
        values = map(int, line.strip().split(' '))
        d = dict(zip(keys, values))
        map_objs[-1].maps.append(d)

def seed_exists(dest):
    seed = dest
    for m in reversed(map_objs):
        seed = m.get_source_id(seed)
    for seed_init, seed_range in zip(seed_inits, seed_ranges):
        if (seed_init <= seed and seed_init + seed_range > seed):
            return True
    return False

final_location = 0

while not seed_exists(final_location):
    final_location += 1
    if final_location % 100000 == 0:
        print(final_location)
print(final_location)

file.close()
