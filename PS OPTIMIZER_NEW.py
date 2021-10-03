bl_info = {
    "name": "PS OPTIMIZER",
    "author": "Manuja Dilaksitha",
    "version": (1, 0),
    "blender": (2, 93),
    "description": "Switch particle system visibility on and off for optimized performance",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}



import bpy
from bpy import context


class PSOptimizerPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Switch Particle System Visibility"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'PS OPTIMIZER'

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Switch ON or OFF particle systems", icon='HIDE_OFF')


        row = layout.row()
        row.operator('particlesystem.switchoff')
        
        row = layout.row()
        row.operator('particlesystem.switchon')
        
        
        
####################      SWITCH OFF      #####################
        

class PARTICLE_VISIBILITY_SWITCH_OFF(bpy.types.Operator):
    
    bl_label = "Switch Off"
    bl_idname = 'particlesystem.switchoff'
    bl_options = {'REGISTER', 'UNDO'}
    
    
    
    def execute(self, context):
        
        #self.layout.operator(PARTICLE_VISIBILITY_SWITCHER.bl_idname)
    

        objects = bpy.context.scene.objects

        for obj in objects:
            name = obj.name

            for m in obj.modifiers:
                if(m.type == "PARTICLE_SYSTEM"):
                        bpy.data.objects[name].modifiers['ParticleSystem'].show_viewport = False
                     
        return{'FINISHED'}
    
    


####################      SWITCH ON      #####################



class PARTICLE_VISIBILITY_SWITCH_ON(bpy.types.Operator):
    
    bl_label = "Switch On"
    bl_idname = 'particlesystem.switchon'
    bl_options = {'REGISTER', 'UNDO'}
    
    
    
    def execute(self, context):
        
        objects = bpy.context.scene.objects
        
        
        for obj in objects:
            name = obj.name
            
            for mod in obj.modifiers:
                if(mod.type == "PARTICLE_SYSTEM"):
                    bpy.data.objects[name].modifiers['ParticleSystem'].show_viewport = True
                    
                    
                    
        return{'FINISHED'}



####################      REGISTER      #####################


classes = [PSOptimizerPanel, PARTICLE_VISIBILITY_SWITCH_OFF, PARTICLE_VISIBILITY_SWITCH_ON]

def register():
    
    bpy.utils.register_class(PSOptimizerPanel)
    bpy.utils.register_class(PARTICLE_VISIBILITY_SWITCH_OFF)
    bpy.utils.register_class(PARTICLE_VISIBILITY_SWITCH_ON)
    #bpy.types.append(execute)
    


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
