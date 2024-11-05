itemincart=0
if itemincart!=2:
    pass
     #raise Exception("Product count is not matching")
assert (itemincart==0)

try:
    with open("file.tet") as f:
        f.read()
except:
    print("I am in except as because try block has failed")


try:
    with open("file.tet") as f:
        f.read()
except Exception as e:
    print(e)
finally:
    print("It's finally block")
