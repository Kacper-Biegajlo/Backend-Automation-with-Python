it = 10

while it > 1: # while loop
    if it == 9:
        it = it - 1 
        continue #skips current itteration and proceeds to next one
    if it == 3:
        break #break stops the loop
    print(it)
    it = it-1

print("while loop execution is done")

