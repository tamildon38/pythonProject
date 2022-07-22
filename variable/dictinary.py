cameras={"sony":500,"nikon":600,"canon":700}
print(cameras)
cameras["canon"]=800
print(cameras)
cameras.keys()
cameras.values()
print(cameras.keys())
print(cameras.values())


demo=cameras.copy()
print(demo)
del cameras["sony"]
print(cameras)

cameras.clear()
print(cameras)


print("keys")
dic={"name":"tamil","age":"23"}
key=dic.keys(age)
print(key)


