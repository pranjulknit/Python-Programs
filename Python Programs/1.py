# string1 = "pranjul"
# print(string1[0])
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sm = reduce((lambda x, y: x + y), li)
# print (sm)



# tuple1 = ('Geeks')
# n = 5
# for i in range(int(n)):
#     tuple1 = (tuple1,)
#     print(tuple1)


class dog():
    species1="mamal"
    species2="dog"

    #sample method
    def fun(self):
        print("This is a", self.species1)
        print("This is a", self.species2)
#object intiation
rodger = dog()  
#acessing class attributes and method through objects
print(rodger.species1)
rodger.fun()