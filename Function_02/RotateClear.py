import maya.cmds as cmds
class RotateClear(object):
    def __init__(self,check_X,check_Y,check_Z):
        self.X = check_X
        self.Y = check_Y
        self.Z = check_Z
        print("RotateClear_success!!")
        
    def Clear(self):
        #print(self.X,self.Y,self.Z)
        lsOBJ = cmds.ls( selection=True )
        if(len(lsOBJ) == 0):
            print("ERROR!!! pleace select a Object!")
        else:
            if(self.X == 0 and self.Y == 0 and self.Z == 0):
                print("please check")
            elif(self.X == 0 and self.Y == 0 and self.Z == 1):
                cmds.setAttr(lsOBJ[0]+".rotateZ",0)
            elif(self.X == 0 and self.Y == 1 and self.Z == 0):
                cmds.setAttr(lsOBJ[0]+".rotateY",0)
            elif(self.X == 0 and self.Y == 1 and self.Z == 1):
                cmds.setAttr(lsOBJ[0]+".rotateY",0)
                cmds.setAttr(lsOBJ[0]+".rotateZ",0)
            elif(self.X == 1 and self.Y == 0 and self.Z == 0):
                cmds.setAttr(lsOBJ[0]+".rotateX",0)
            elif(self.X == 1 and self.Y == 0 and self.Z == 1):
                cmds.setAttr(lsOBJ[0]+".rotateX",0)
                cmds.setAttr(lsOBJ[0]+".rotateZ",0)
            elif(self.X == 1 and self.Y == 1 and self.Z == 0):
                cmds.setAttr(lsOBJ[0]+".rotateX",0)
                cmds.setAttr(lsOBJ[0]+".rotateY",0)
            elif(self.X == 1 and self.Y == 1 and self.Z == 1):
                cmds.setAttr(lsOBJ[0]+".rotateX",0)
                cmds.setAttr(lsOBJ[0]+".rotateY",0)
                cmds.setAttr(lsOBJ[0]+".rotateZ",0)
    