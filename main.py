#MapPlot.py
#Name:
#Date:
#Assignment:

import csv
import matplotlib.pyplot as plt
trial = []
reactionTime = []
inFile = open("reaction_time_data.csv", "r")
reader = csv.DictReader(inFile)
for row in reader:
    trial.append(int(row["Trial"]))
    reactionTime.append(int(row["ReactionTime_ms"]))

cleanTrial = []
cleanReaction = []

for i in range(len(reactionTime)):
    if reactionTime[i] > 0:
        cleanTrial.append(trial[i])
        cleanReaction.append(reactionTime[i])

plt.plot(cleanTrial, cleanReaction, marker='o')
plt.xlabel("Trial Number")
plt.ylabel("Reaction Time (ms)")
plt.title("Reaction Time vs Trial Number")
plt.savefig("output.png")
