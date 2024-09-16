# Nested Loop 
# Loop within loop


"""
for i in range(start,stop,step): outer loop
    for j in range(start,stop,step): inner loop
        #code"""

# Grandfather
for grandfather in range(4):
    # Sam
    for sam in range(4):
        print("Collected apple from row ", grandfather, "column", sam)

#Example 2
for g in "ABCDE":
    for s in "ABCDE":
        print(g, s)

#Example 3
for paanipuriwala in range(1, 6):
    for family in range(1, 5):
        print(paanipuriwala, family)