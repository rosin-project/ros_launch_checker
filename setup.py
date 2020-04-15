from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ros_launch_checker", # Replace with your own username
    version="0.5.0",
    author="Francisco Martinez Lasaca",
    author_email="frml@itu.dk",
    description="A launch files checker for ROS1 packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rosin-project/ros_launch_checker",
    packages=find_packages(exclude=['test']),
    package_data= {
            # Include txt files
            "": ["*.txt"]
    },
    install_requires=[
        "setuptools",
        "lxml",
        "colorama>=0.4.3",
    ],
    entry_points = {
        'console_scripts':[
            'ros_launch_checker = ros_launch_checker.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)