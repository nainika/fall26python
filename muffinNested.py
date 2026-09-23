
buying = input('do you want a muffin or cupcake?')
muffins = 2
cupcakes = 2

while buying != "0":
        if buying == "muffin" and muffins > 0:
                muffins = muffins -1
                if buying == "muffin" and muffins == 0:
                        print("Muffins Out of stock")
        if buying == "cupcake" and cupcakes  > 0:
                cupcakes = cupcakes -1
                if buying == "cupcake" and cupcakes == 0:
                        print("cupcakes Out of stock")
        buying = input('do you want a muffin or cupcake?')
	
print("muffins:", muffins, "cupcakes:", cupcakes)
