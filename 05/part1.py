file = open("input.txt", "r")

answer = 0
seeds = []
map_objs = []

class map_obj:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.maps = []
    
    def get_dest_id(self, source_id):
        for m in self.maps:
            
            if source_id >= m['source_start'] and source_id <  m['source_start'] + m['range']:
                return source_id - m['source_start'] + m['dest_start']
            
        return(source_id)
    

for line in file.readlines():
    if line.strip() == '':
        continue
    if line[0:6] == 'seeds:':
        seeds = list(map(int, line.strip().split(' ')[1:]))
        continue
    if ':' in line:
        source, destination = line.split('-')[0:3:2]
        map_objs.append(map_obj(source, destination.split(' ')[0]))
    else:
        keys = ['dest_start', 'source_start', 'range']
        values = map(int, line.strip().split(' '))
        d = dict(zip(keys, values))
        map_objs[-1].maps.append(d)

final_location = seeds.copy()

for id, seed in enumerate(seeds):
    dest = seed
    for m in map_objs:
        dest = m.get_dest_id(dest)
    final_location[id] = dest

print(min(final_location))

file.close()