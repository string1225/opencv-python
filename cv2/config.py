import os

BINARIES_PATHS = [
    __file__.replace("__init__.py","bin"),
    os.path.join(os.getenv('CUDA_PATH', 'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v10.2'), 'bin')
] + BINARIES_PATHS