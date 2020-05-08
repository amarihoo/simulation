## installing requirements

using a ubuntu 16.04 environment with full ROS Kinectic, please install both the following: 

Gazebo: http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install

Sawyer Robot: https://sdk.rethinkrobotics.com/intera/Gazebo_Tutorial

## installing the package

dowload this github repo as a .zip

navigate to <your_workspace>/src/sawyer_simulator

replace the contents of the "sawyer_sim_examples" folder with the contents of the extracted .zip

run $catkin_make in your workspace folder

## run the package

$roslaunch sawyer_sim_examples sawyer_pick_and_place_demo.launch

(or in ROS Dev Studio, choose the launch file in the simulation launcher)

## other

code has only been tested in ROS Dev Studio

** note that all relevant work is in the scripts folder: -demo.py is complete adaptation, -test.py for simulation tests
** image processing in results
