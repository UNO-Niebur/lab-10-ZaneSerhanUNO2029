#MapPlot.py
#Name:
#Date:
#Assignment:
import csv
import matplotlib as plt
trial = []
reactionTime = []

with open("reaction_time_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        trial.append(int(row["Trial"]))
        reactionTime.append(int(row["ReactionTime_ms"]))
