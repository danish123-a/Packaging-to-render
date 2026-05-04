import bpy
import sys
import os

def render_packaging():
    print("🎨 [Blender Inside] Swapping textures and rendering...")
    
    # 1. Grab arguments passed from main.py (everything after "--")
    argv = sys.argv
    try:
        argv = argv[argv.index("--") + 1:] 
        texture_path = argv[0]
        output_path = argv[1]
    except ValueError:
        print("Error: Missing arguments for Blender script.")
        return

    # 2. Find the material on our 3D box (Must be named 'PackagingMaterial' in Blender)
    mat = bpy.data.materials.get("PackagingMaterial")
    if not mat:
        print("Error: Could not find 'PackagingMaterial' in the .blend file.")
        return
        
    # 3. Find the Image node and swap the image
    nodes = mat.node_tree.nodes
    tex_node = nodes.get("Image Texture") # The node must be named this
    
    if tex_node:
        # Load our new PNG and assign it
        new_image = bpy.data.images.load(filepath=texture_path)
        tex_node.image = new_image
    else:
        print("Error: Could not find 'Image Texture' node in the material.")
        return

    # 4. Render Settings (Make it pretty and transparent)
    bpy.context.scene.render.engine = 'CYCLES' # Use Cycles for photorealism
    bpy.context.scene.cycles.samples = 128     # Quality level
    bpy.context.scene.render.film_transparent = True # Transparent background
    
    # Set output file path
    bpy.context.scene.render.filepath = output_path
    
    # 5. Render the image!
    bpy.ops.render.render(write_still=True)
    print("🎉 [Blender Inside] Render complete!")

if __name__ == "__main__":
    render_packaging()