# The Blender Badgifier!
Create 3D Badges from SVGs with Blender

# Using the Badgifier
## Make an SVG
To get started, you will first need to get yourself an SVG file! Any file will do, but there are certain things to keep in mind. First, all strokes must be converted to curves! You can do this via the "Expand Stroke" option in Affinity Designer. If you are using Affinity, you will also want to convert shapes to curves. In fact, everything ought to be a curve for this to work properly!

## Make File Folders
Two File paths are necessary for this code--one to hold your SVG files, and one to store the gltf files. Add the file paths to the project in the necessary area.

## Naming Conventions
For this code to work properly, your curve objects must also follow some specific naming conventions. There are two main keywords:
"outline" -- This refers to the outline of your SVG. Naming a curve "outline" will cause the program to raise these objects slightly more than the others
"L1" -- This refers to the base color of your SVG, but it can apply to any layer that other layers are laid on top of. As of now, this code only allows one such layer. The code will not extrude this layer as much as other layers, preventing competition on equal layers

## Using Blender
To run this code, open Blender, delete all the objects, open the scripting panel, and press play! Just like that, you should find your gltf files in the destination folder!


# Troubleshooting Options

Convert all objects to curves. This can be done to strokes with the "Expand Stroke" command, and to shapes with "Convert to Curves"

Check your naming conventions.

Make sure all your collections on Blender are cleared.
