import random
import statistics

rock_cutter = {"A":4, "WS":4, "ND": 5, "CD":7, "CO":5}
rock_drill = {"A":4, "WS":3, "ND": 4, "CD":7, "CO": 6}
rock_saw = {"A":4, "WS":3, "ND": 5, "CD":6, "CO": 6}

def roll_attacks(weapon):
	damage_out = 0
	for i in range(weapon["A"]):
		weapon_skill = random.randint(1,6)
		if weapon_skill >= weapon["CO"]:
			damage_out += weapon["CD"]
			#print("Attack {0} crit on {1}".format(i, weapon_skill))
		elif weapon_skill >= weapon["WS"]:
			damage_out += weapon["ND"]
			#print("Attack {0} hit on {1}".format(i, weapon_skill))
	return damage_out




def main():
	for name, weapon in [("Rock Cutter", rock_cutter), ("Rock Drill", rock_drill), ("Rock Saw", rock_saw)]:
		average = []
		for i in range(1000000):
			average.append(roll_attacks(weapon))
		print("STATS FOR {0}".format(name))
		print("Mean:{0}".format(statistics.mean(average)))
		print("Median:{0}".format(statistics.median(average)))
		print("Mode: {0}".format(statistics.mode(average)))


if __name__ == '__main__':
	main()