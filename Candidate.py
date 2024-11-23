import pandas as pd
def learn(concepts, target):
specific_h = concepts[0].copy()
print("\nInitialization ofj specific_h and general_h")
print("\nSpecific Boundary:", specific_h)
general_h = [["?" for _ in range(len(specific_h))]]
print("\nGeneral Boundary:", general_h)
for i, h in enumerate(concepts):
print("\nInstance", i + 1, "is", h)
if target[i] == "yes":
print("Instance is Positive")
for x in range(len(specific_h)):
if h[x] != specific_h[x]:
specific_h[x] = "?"
for g in general_h:
g[x] = "?"
general_h = [g for g in general_h if not all(x == '?' for x in g)]
elif target[i] == "no":
print("Instance is Negative")
general_h_new = []
for g in general_h:
if not all(x == '?' or x != h[x] for x, e in zip(g, h)):
general_h_new.append(g)
else:
for x in range(len(specific_h)):
if g[x] == '?':
new_g = g[:]
new_g[x] = h[x]
if new_g not in general_h_new:
general_h_new.append(new_g)
general_h = [g for g in general_h_new if not any(is_more_specific(g, other_g) for 
other_g in general_h_new if g != other_g)]
print("Specific Boundary after", i + 1, "Instance is", specific_h)
print("General Boundary after", i + 1, "Instance is", general_h)u
print("\n")
return specific_h, general_h
def is_more_specific(h1, h2):
return all(x == '?' or x == y for x, y in zip(h1, h2))
df = pd.read_csv('dataset.csv')
concepts = df.iloc[:, :-1].values 
target = df.iloc[:, -1].values 
specific_h, general_h = learn(concepts, target)
print("Final Specific Boundary (S):", specific_h)
print("Final General Boundary (G):", general_h)
