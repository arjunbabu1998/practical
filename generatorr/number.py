def testgener():
    yield 5
    yield 10
    yield 30
    yield 40

result=testgener()
#for item in result:
#   print(item)
print(result.__next__())
