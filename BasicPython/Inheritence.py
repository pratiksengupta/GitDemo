from oopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 5)

    def getCompleteData(self):
        return self.num2 + self.num + self.add()


child = ChildImpl()
print(child.getCompleteData())