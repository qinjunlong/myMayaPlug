import maya.cmds as cmds
class ExportCamer_C(object):
    def __init__(self,Q_tmie):
        self.BakeTime = Q_tmie
        print("ExportCamer_C_success!!")
        
    def CallBTN(self):
        lsOBJ = cmds.ls( selection=True )
        if(len(lsOBJ) == 0):
            print("ERROR!!! pleace select a camera!")
        else:
            loc = cmds.spaceLocator( p=(0, 0,0),n = 'global_LOC' )
            loc_cam = cmds.spaceLocator( p=(0, 0,0),n = 'cam_LOC')
            cmds.parent( 'cam_LOC', lsOBJ[0], relative=True )
            cmds.parent( 'cam_LOC', w=True )
            parentConstraint_loc = cmds.parentConstraint( lsOBJ[0], 'cam_LOC' ,mo=True)
            cmds.bakeResults('cam_LOC' ,t = (1,self.BakeTime) )
            cmds.delete(parentConstraint_loc[0])
            cmds.parent( 'cam_LOC', 'global_LOC')
            cameraName = cmds.camera(n='bake_'+lsOBJ[0])
            cmds.parent( cameraName, 'cam_LOC',relative=True)
            print('Success!!!')
