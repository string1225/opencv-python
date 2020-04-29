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
1. Install [Python 3.8](https://www.python.org/downloads/), [CUDA 10.2](https://developer.nvidia.com/cuda-downloads) and [cuDNN 7.5](https://developer.nvidia.com/rdp/cudnn-download) via the official website. VS integration option for CUDA isn't necessary here.
2. Install numpy and opencv-python via pip.
3. Replace the ***\{Your Python Installation Path\}\Lib\site-packages\cv2*** with the ***cv2*** of this repo. 
4. Run **test.py** and check the opencv version in the console.

Your python installation path may be ***C:\Users\\{Your_User\}\AppData\Local\Programs\Python\Python38*** for Windows.

## Compilation

Follow these steps if you want to compile the library by yourself:
1. You are using Windows 10.
2. Install [Python 3.8](https://www.python.org/downloads/), [CMake 3.17.1](https://cmake.org/download/), [Visual Studio 2019 Community](https://visualstudio.microsoft.com/zh-hans/vs/community/), [CUDA 10.2](https://developer.nvidia.com/cuda-downloads) and [cuDNN 7.5](https://developer.nvidia.com/rdp/cudnn-download) via the official website.
3. Install numpy via pip.
4. Download the source code of OpenCV 4.3.0 via [GitHub](https://github.com/opencv/opencv).
5. Run the CMake, indicate the folder of OpenCV source code and the target folder you want to place the built code.
6. Trigger the **configure** for the first time.
7. Check the options in the list. Make sure you have checked these options.
8. Configure again. Check the errors and fix them. Some downloading for ffmpeg or other lib from GitHub may be blocked by GFW. You need to download them manually and replace the cache in */.cache* in the target folder. You may use this (website)[https://d.serctl.com/?dl_start] to help you.
9. When you clear all errors, you could **generate** the project.
10. Click the **open project** to jump to VS or you could manually open the project from target folder.
11. Set the env as release on the top toolbar. 
12. Right click the ALL_BUILD in the right tree and start the generation. It may take 30~60 minutes here.
13. Right click the INSTALL in the right tree and start the generation. It may take 10 minutes here if you choose to build with all dependency.
14. The python lib will be created automatically after the code installation in VS. You could run the test.py and check the opencv version in the console now.

Refer to https://blog.csdn.net/hitpisces/article/details/104266030