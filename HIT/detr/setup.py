from distutils.core import setup
from setuptools import find_packages

setup(
    name='detr',
    version='0.0.0',
    packages=find_packages(),
    license='MIT License',
    long_description=open('README.md').read(),
    install_requires=[
    # 列出你的依赖包, 为啥humanplus不自己把这些包放到这里
		# "pyquaternion",
		# "pyyaml",
		# "rospkg",
		# "pexpect",
		# "mujoco==2.3.7",
		# "dm_control==1.0.14",
		# "opencv-python",
		# "matplotlib",
		# "einops",
		# "packaging",
		# "h5py",
		# "ipython",
		# "getkey",
		# "wandb",
		# "chardet",
		# "h5py_cache"
      
    ]
)
