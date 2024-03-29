from copy import deepcopy

def process_grid(inp):
    
    grid = [['#']*len(inp[0]) for _ in inp]
    agents = []

    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == '#':
                continue
            elif inp[i][j] in ['G', 'E']:
                agents.append(Agent((i, j), inp[i][j]))

            grid[i][j] = ' '

    grid = ["".join(row) for row in grid]

    return grid, agents

def neighbours(i, j):
    yield i-1, j
    yield i, j-1
    yield i, j+1
    yield i+1, j

class Agent:
    def __init__(self, pos, t, hit_points=200):
        self.pos = pos
        self.t = t
        self.hit_points = hit_points

    def live(self):
        return self.hit_points > 0

    def __str__(self):
        return "{}({})".format(self.t, self.hit_points)

class Game:
    def __init__(self, grid, agents):
        self.grid = grid
        self.agents = deepcopy(agents)
        self.occupied = {agent.pos: i for i, agent in enumerate(agents)}
        self.round_counter = 0

    def move(self, agent_id, pos):
        old_pos = self.agents[agent_id].pos
        del self.occupied[old_pos]

        self.agents[agent_id].pos = pos
        self.occupied[pos] = agent_id

    def damage(self, agent_id, attack):
        self.agents[agent_id].hit_points -= attack

        if not self.agents[agent_id].live():
            del self.occupied[self.agents[agent_id].pos]

    def targets_remaining(self, t):
        return any(agent.live() and agent.t != t for agent in self.agents)

    def total_hitpoints(self):
        return sum(agent.hit_points for agent in self.agents if agent.live())

    def agent_ids(self):
        ids = sorted(range(len(self.agents)), key=lambda i: self.agents[i].pos)
        return ids

    def neighbouring_spaces(self, i, j):
        for i, j in neighbours(i, j):
            if self.grid[i][j] == ' ' and (i, j) not in self.occupied:
                yield i, j

    def target_squares(self, agent_id):
        t = self.agents[agent_id].t
        for agent in self.agents:
            if agent.t != t and agent.live():
                yield from self.neighbouring_spaces(*agent.pos)

    def nearby_enemies(self, agent_id):
        pos, t = self.agents[agent_id].pos, self.agents[agent_id].t

        for n in neighbours(*pos):
            n_agent_id = self.occupied.get(n, None)
            if n_agent_id is not None and self.agents[n_agent_id].t != t:
                yield n_agent_id

    def weakest_nearby_enemy(self, agent_id):
        return min(self.nearby_enemies(agent_id),
            key=lambda i: (self.agents[i].hit_points, self.agents[i].pos),
            default=None)

    def in_range(self, agent_id):
        g = self.nearby_enemies(agent_id)
        try:
            next(g)
        except StopIteration:
            return False
        return True

    def display_row(self, i):
        info_required = []

        for j in range(len(self.grid[0])):
            agent_id = self.occupied.get((i, j), None)
            if agent_id is not None:
                yield self.agents[agent_id].t
                info_required.append(agent_id)
            else:
                yield self.grid[i][j]

        for agent_id in info_required:
            yield " "
            yield str(self.agents[agent_id])

    def __str__(self):
        s = "Round: {}\n".format(self.round_counter)
        return s + "\n".join("".join(self.display_row(i)) for i in range(len(self.grid)))

def find_move(game, agent_id):

    targets = set(game.target_squares(agent_id))

    if not targets:
        return None

    distance = dict()

    start = game.agents[agent_id].pos
    distance[start] = 0
    pos = [start]
    d = 0

    found_targets = set()
    while not found_targets and pos:
        d += 1
        new_pos = []
        for p in pos:
            for n in game.neighbouring_spaces(*p):
                if n not in distance:
                    new_pos.append(n)
                    distance[n] = d

                if n in targets:
                    found_targets.add(n)

        pos = new_pos

    if not found_targets:
        return None

    target = min(found_targets)

    pos = set([target])

    while d > 1:
        new_pos = set()
        for p in pos:
            for n in neighbours(*p):
                if n in distance and distance[n] == d-1:
                    new_pos.add(n)

        pos = new_pos
        d -= 1

    destination = min(pos)

    return destination

def play(grid, agents, elf_attack=3, verbose=False):
    g = Game(grid, agents)

    while True:
        if verbose:
            print(g)

        for agent_id in g.agent_ids():
            if not g.agents[agent_id].live():
                continue

            if not g.targets_remaining(g.agents[agent_id].t):
                return g

            if not g.in_range(agent_id):
                destination = find_move(g, agent_id)
                if destination is not None:
                    g.move(agent_id, destination)

            w = g.weakest_nearby_enemy(agent_id)
            if w is not None:
                g.damage(w, elf_attack if g.agents[agent_id].t=='E' else 3)

        g.round_counter += 1

class PlayCache:
    def __init__(self, grid, agents):
        def f(elf_attack, **kwargs):
            return play(grid, agents, elf_attack=elf_attack, **kwargs)
        self.f = f
        self.cache = {}

    def __call__(self, elf_attack=3, **kwargs):
        if elf_attack not in self.cache:
            self.cache[elf_attack] = self.f(elf_attack, **kwargs)
        return self.cache[elf_attack]

def bisection(f, left, right):
    
    assert f(left) is False
    assert f(right) is True

    while right - left > 1:
        m = (left + right) // 2
        if f(m):
            right = m
        else:
            left = m

    return right

def part2(pc):
    def all_elves_survive(elf_attack):
        g = pc(elf_attack)
        return all(agent.live() for agent in g.agents if agent.t == 'E')

    elf_attack = bisection(all_elves_survive, 3, 50)
    game = pc(elf_attack)
    return elf_attack, game

if __name__=="__main__":
    with open("15.txt", 'r') as f:
        inp = [line.strip() for line in f]

    pc = PlayCache(*process_grid(inp))

    game = pc()
    print('Part 1:',game.round_counter * game.total_hitpoints())

    elf_attack, game = part2(pc)
    print('Part 2:',game.round_counter * game.total_hitpoints())