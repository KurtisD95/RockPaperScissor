# 99 bottle for loop
for i in range (99,-1,-1):
    if i > 0:
        print(i, "Bottles of beer on the wall,", i, " bottles of beer,")
        print("Take one down and pass it around,", i, "bottles of beer on the wall.\n")
    else:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")
