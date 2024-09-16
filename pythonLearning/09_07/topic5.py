# constins
# list = [1, 2, 3, 4]
# 4
# p - True, Np - False

def custom_constins(list, el):
    flag = False # can take flag = "No"
    for item in list:
        if item == el:
            flag = True  #flag = "Yes"
            break
    return flag 


res = custom_constins([1, 2, 3, 4], 2)
print(res)