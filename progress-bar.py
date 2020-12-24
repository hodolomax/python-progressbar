import tqdm

max = 400000000 # Buraya ne kadar çok sıfır koyarsan o kadar uzun sürer bar
start = 0
batch_size = 10
# moduleId=['220']
docs =-1
calculate = []

for start in tqdm.tqdm(range(0, max + batch_size, batch_size)):
    batch_size +=  10
    docs += 1


print("{0} entities have been changed".format(docs))
