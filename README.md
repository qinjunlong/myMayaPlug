# myMayaPlug
自己的maya动画小插件

1 功能Founction01 maya相机导出到blender
首先第一个功能是maya相机导出到blender的时候由于坐标轴的不一样能产生的问题，在这个基础上如果相机有运动或者是有轨道移动和类似于万向节锁死的旋转问题的时候会更加麻烦，所以
用maya的bake相机方法还有全局loc以及相对loc两个做参照作为一个系统，导出的fbx文件放到blender上直接把相机旋转180度就可以实现了
