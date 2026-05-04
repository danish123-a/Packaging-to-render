import os
import subprocess
from pdf_processor import convert_pdf_to_png

def run_pipeline():
    print("🚀 Starting 3D Packaging Render Pipeline...\n")
    
    # Ensure directories exist
    os.makedirs('input', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    # Define file paths
    pdf_input = "input/dieline.pdf"
    texture_output = os.path.abspath("output/texture.png")
    render_output = os.path.abspath("output/final_3d_render.png")
    blend_template = os.path.abspath("assets/template.blend")
    blender_script = os.path.abspath("blender_worker.py")
    
    # Make sure user put a PDF in the folder
    if not os.path.exists(pdf_input):
        print("❌ Please put a 'dieline.pdf' file inside the 'input/' folder!")
        return

    # Step 1: PDF to Image
    png_path = convert_pdf_to_png(pdf_input, texture_output)
    if not png_path: return
    
    print("\n🎥 Step 2: Waking up Blender in the background...")
    
    # Determine Blender path (You may need to change this based on your OS!)
    # Mac: "/Applications/Blender.app/Contents/MacOS/Blender"
    # Windows: "C:\\Program Files\\Blender Foundation\\Blender 4.0\\blender.exe"
    blender_executable = "blender" # Works if Blender is in your system PATH
    
    # Construct the headless Blender command
    # -b runs it in background, -P runs our python script, -- passes the variables
    blender_command = [
        blender_executable,
        "-b", blend_template,
        "-P", blender_script,
        "--", texture_output, render_output
    ]
    
    try:
        # Run Blender silently
        subprocess.run(blender_command, check=True)
        print(f"\n🎉 SUCCESS! Open your 'output' folder to see: {render_output}")
    except FileNotFoundError:
        print("\n❌ Error: Could not find Blender. Make sure Blender is installed and in your system PATH, or provide the exact path in main.py.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error during Blender render: {e}")

if __name__ == "__main__":
    run_pipeline()