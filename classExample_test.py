__author__='goldi'
class ObjType:
    def __init__(self):
        print("Printing Constructor")
    def createObj(self):
        print('creating object from parent class')
    def moveObj(self):
        print('move object from parent class')

class SubObjType(ObjType):
    def createObj(self):
        print('creating object of sub class')

def main():
        obj=ObjType()
        obj.createObj()
        obj.moveObj()

        subobj=SubObjType()
        subobj.createObj()
        subobj.moveObj()
main()