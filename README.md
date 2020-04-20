# opencv-python

This a repo for compiled OpenCV Python Lib with CUDA and cuDNN for Windows 10.

Please check your system and need with following version info:
 - Windows 10 V1909
 - OpenCV 4.3.0
 - Python 3.8.2
 - CUDA 10.2
 - cuDNN 7.5

## Installation

Follow these steps if you want to use the lib directly:
0. Make sure you are using Windows 10.
1. Install Python 3.8, CUDA 10.2 and cuDNN 7.5 via the official website.
2. Install numpy and opencv-python via pip.
3. Replace the *$Your_Python_Installation_Path\Lib\site-packages\cv2* with the *cv2* of this repo. Your python installation path may be *C:\Users\$Your_User\AppData\Local\Programs\Python\Python38*.
4. Run the test.py and check the opencv version in the console.

## Compilation

Follow these steps if you want to compile the library by yourself:
0. Make sure you are using Windows 10.
1. Install Python 3.8, CMake 3.17.1, Visual Studio 2019 Community, CUDA 10.2, cuDNN 7.5 via the official website.
2. Install numpy via pip.
3. Download the source code of OpenCV 4.3.0 via GitHub.
4. Run the CMake, indicate the folder of OpenCV source code and the target folder you want to place the built code.
5. Run the configure for the first time.
6. Check the options in the list. Make sure you have checked these options.
7. Configure again. Check the errors and fix them. Some downloading for ffmpeg or other lib from GitHub may be blocked by GFW. You need to download them manually and replace the cache in *.cache* in the target folder

