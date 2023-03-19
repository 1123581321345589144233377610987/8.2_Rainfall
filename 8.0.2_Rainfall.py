data = open('rainfall-totals.txt','r')
Data = data.readlines()
data.close()
total = 0
count = 0
for i in Data:
    i = i.strip("/n")
    I = i.split(" ")
    try:
        total += float(I[1])
        count += 1
    except ValueError:
        print(f"Bad numeric data found for entry: {i}")
print(f"{count} good values were found.")
print(f"The total was {total:.1f}.")
print(f"The average was {total/count:.1f}.")
