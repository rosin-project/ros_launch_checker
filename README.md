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

## Acknowledgements

<!--
    ROSIN acknowledgement from the ROSIN press kit
    @ https://github.com/rosin-project/press_kit
-->

<a href="http://rosin-project.eu">
  <img src="https://raw.githubusercontent.com/rosin-project/press_kit/master/img/rosin_ack_logo_wide.png" alt="rosin_logo" height="60">
</a>

Supported by ROSIN - ROS-Industrial Quality-Assured Robot Software Components.
More information: <a href="http://rosin-project.eu">rosin-project.eu</a>

<img src="https://raw.githubusercontent.com/rosin-project/press_kit/master/img/rosin_eu_flag.jpg" alt="eu_flag" height="45" align="left" >

This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement no. 732287.

