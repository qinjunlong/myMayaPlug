import maya.cmds as cmds
def CallBTN():
    loc = cmds.spaceLocator( p=(0, 0,0),n = 'loc_t' )
    loc_cam = cmds.spaceLocator( p=(0, 0,0),n = 'loc_cam_t')
    cmds.parent( 'loc_cam_t', 'Cam_02', relative=True )
    cmds.parent( 'loc_cam_t', w=True )
    parentConstraint_loc = cmds.parentConstraint( 'Cam_02', 'loc_cam_t' ,mo=True)
    cmds.bakeResults('loc_cam_t' ,t = (1,30) )
    cmds.delete(parentConstraint_loc[0])
    cmds.parent( 'loc_cam_t', 'loc_t')
    cameraName = cmds.camera(n='bake_camera')
    cmds.parent( 'bake_camera1', 'loc_cam_t',relative=True)  
    print('Success!!!')
