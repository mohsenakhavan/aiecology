import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Organism:
    def __init__(self, x, y, energy, genome):
        self.x = x
        self.y = y
        self.energy = energy
        self.genome = genome
        self.age = 0

    def move(self):
        dx, dy = self.genome[:2]
        self.x = (self.x + dx) % WIDTH
        self.y = (self.y + dy) % HEIGHT
        self.energy -= 1

    def eat(self, amount):
        self.energy += amount

    def reproduce(self):
        if self.energy > REPRODUCTION_THRESHOLD:
            child_genome = self.genome + np.random.normal(0, MUTATION_RATE, size=4)
            child = Organism(self.x, self.y, INITIAL_ENERGY, child_genome)
            self.energy -= REPRODUCTION_COST
            return child
        return None

class AIEcosystem:
    def __init__(self):
        self.organisms = [Organism(np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT),
                                   INITIAL_ENERGY, np.random.normal(0, 1, size=4))
                          for _ in range(INITIAL_POPULATION)]
        self.food = np.random.randint(0, MAX_FOOD, size=(HEIGHT, WIDTH))
        self.generation = 0

    def update(self):
        new_organisms = []
        for org in self.organisms:
            org.move()
            org.eat(self.food[int(org.y), int(org.x)])
            self.food[int(org.y), int(org.x)] = 0
            child = org.reproduce()
            if child:
                new_organisms.append(child)
            org.age += 1

        self.organisms = [org for org in self.organisms if org.energy > 0 and org.age < MAX_AGE]
        self.organisms.extend(new_organisms)

        # Регенерация пищи
        self.food = np.minimum(self.food + FOOD_GROWTH_RATE, MAX_FOOD)
        self.generation += 1

    def get_stats(self):
        if not self.organisms:
            return 0, 0, 0
        energies = [org.energy for org in self.organisms]
        return len(self.organisms), np.mean(energies), np.max(energies)

# Глобальные параметры
WIDTH, HEIGHT = 100, 100
INITIAL_POPULATION = 100
INITIAL_ENERGY = 50
REPRODUCTION_THRESHOLD = 100
REPRODUCTION_COST = 50
MUTATION_RATE = 0.1
MAX_AGE = 100
MAX_FOOD = 100
FOOD_GROWTH_RATE = 1

# Инициализация экосистемы и графика
ecosystem = AIEcosystem()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
scatter = ax1.scatter([], [], s=5)
ax1.set_xlim(0, WIDTH)
ax1.set_ylim(0, HEIGHT)
ax1.set_title("AI Ecosystem")

generation_text = ax1.text(0.02, 0.98, '', transform=ax1.transAxes, verticalalignment='top')
population_text = ax1.text(0.02, 0.94, '', transform=ax1.transAxes, verticalalignment='top')
avg_energy_text = ax1.text(0.02, 0.90, '', transform=ax1.transAxes, verticalalignment='top')

generations = []
populations = []
avg_energies = []
line, = ax2.plot([], [])
ax2.set_xlabel("Generation")
ax2.set_ylabel("Population / Avg Energy")
ax2.set_title("Ecosystem Statistics")

def update(frame):
    ecosystem.update()
    x = [org.x for org in ecosystem.organisms]
    y = [org.y for org in ecosystem.organisms]
    scatter.set_offsets(np.c_[x, y])

    population, avg_energy, max_energy = ecosystem.get_stats()
    generation_text.set_text(f"Generation: {ecosystem.generation}")
    population_text.set_text(f"Population: {population}")
    avg_energy_text.set_text(f"Avg Energy: {avg_energy:.2f}")

    generations.append(ecosystem.generation)
    populations.append(population)
    avg_energies.append(avg_energy)

    ax2.clear()
    ax2.plot(generations, populations, label="Population")
    ax2.plot(generations, avg_energies, label="Avg Energy")
    ax2.legend()
    ax2.set_xlabel("Generation")
    ax2.set_ylabel("Value")
    ax2.set_title("Ecosystem Statistics")

    return scatter, generation_text, population_text, avg_energy_text

# Создание анимации
anim = FuncAnimation(fig, update, frames=1000, interval=50, blit=True)
plt.show()