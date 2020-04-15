# Launch dependency checker
![Tests](https://github.com/rosin-project/ros_launch_checker/workflows/Tests/badge.svg)

This checker validates that all `$(find <package-name>)` substitutions in all ROS `.launch` files of a package are declared in `package.xml`.


## Installation

```bash
pip install .
```

## Execution
Run with a path to a valid ROS package containing a `package.xml`.

Example:

```bash
python3 -m ros_launch_checker my_great_ros2_package/
```

## Testing

Some tests are included. In the root folder, run the following:

```bash
python3 -m unittest discover -b
```

The `-b` option supresses the standard input logging information.
