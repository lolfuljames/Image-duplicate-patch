# Image-duplicate-patch
Copy images patch by patch, setup up patch size and source file. Ability to choose amount of duplicate pixels per patch file to increase resolution.

## INSTALLATION
```
pip install numpy
pip install scipy
pip install PIL
```
## USAGE

1. Insert an image into the same folder as copy.py.
2. Enter souce file and edit the follow code:
      `nameOfFile = "imagename.JPG"`
      
## PARAMETERS

      `Enter patching size: (-1 to exit)`

Value entered is the length of the patches to be used to duplicate the pixels.
-1 exits the program.


      `Enter duplicate count:`
      
Value entered is the number of pixels to be duplicated by patch.


An image is shown to explain the parameters with patch size 2 and  duplicate count 1. 
Numbers show are the patch sequences.

![alt text](https://i.imgur.com/ExACOJK.jpg "Image patch size 2 duplicate count 1 on a 4x4 matrix")
