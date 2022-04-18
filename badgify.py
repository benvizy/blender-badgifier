import bpy
from bpy import context
import bmesh
import builtins as __builtin__

from mathutils import Vector
from bmesh.types import BMVert

import os

## Necessary Functions
# Redefine print command for use in the Blender Console
def console_print(*args, **kwargs):
    for a in context.screen.areas:
        if a.type == 'CONSOLE':
            c = {}
            c['area'] = a
            c['space_data'] = a.spaces.active
            c['region'] = a.regions[-1]
            c['window'] = context.window
            c['screen'] = context.screen
            s = " ".join([str(arg) for arg in args])
            for line in s.split("\n"):
                bpy.ops.console.scrollback_append(c, text=line)

def print(*args, **kwargs):
    """Console print() function."""

    console_print(*args, **kwargs) # to py consoles
    __builtin__.print(*args, **kwargs) # to system console
    
# Select One Object
def select_one_object(obj):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

# Extrude Mesh
def extrude_mesh(scene, mesh, z):

    bm = bmesh.new()
    bm.from_mesh(mesh)
    bm.faces.ensure_lookup_table()
    faces = [bm.faces[0]]

    # Extrude
    extruded = bmesh.ops.extrude_face_region(bm, geom=faces)

    # Move extruded geometry
    translate_verts = [v for v in extruded['geom'] if isinstance(v, BMVert)]

    up = Vector((0,0,z))
    bmesh.ops.translate(bm, vec=up, verts=translate_verts)

    # Delete Old Faces
    bmesh.ops.delete(bm, geom=faces, context="FACES")

    # Remove Doubles, Just in Case
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.001)

    # Update mesh and free Bmesh
    bm.normal_update
    bm.to_mesh(mesh.data)
    bm.free()

# Export the new Object    
def export_badge(filepath):
    print("exporting...")
    bpy.ops.export_scene.gltf(filepath=filepath)
    


# Delete the Object
def delete_badge():
    print("deleting...")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(confirm=False)
    

## Necessary Variables
SVG_PATH = "YOUR/PATH/HERE"
GLB_PATH = "YOUR/PATH/HERE"
scene = bpy.context.scene

def badgify():
    svg_files = [f for f in os.listdir(SVG_PATH)]

    for file in svg_files:
        print(f"now we dealing with {file}")
        bpy.ops.import_curve.svg(filepath=f"{SVG_PATH}/{file}")
        
        # Scale up everything
        for obj in bpy.data.collections[file].all_objects:
            obj.select_set(True)
        bpy.ops.transform.resize(value=(5, 5, 1))




        # Extrude
        print(f"Here are our objects: {bpy.data.collections[file].all_objects}")
        for obj in bpy.data.collections[file].all_objects:
            print(f"now we dealing with {obj.name}")
            if "outline" in obj.name:
                select_one_object(obj)
                bpy.context.object.data.extrude = 0.015
            elif "L1" in obj.name:
                select_one_object(obj)
                bpy.context.object.data.extrude = 0.013
            else:
                select_one_object(obj)
                bpy.context.object.data.extrude = 0.014
        
        # Export
        file_name = file[0:-4]
        export_badge(filepath=f"{GLB_PATH}/{file_name}")
        delete_badge()





if __name__ == "__main__":
    badgify()
