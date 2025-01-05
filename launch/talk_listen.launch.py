import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    weather_humidity_talk = launch_ros.actions.Node(
        package='mypkg',
        executable='weather_humidity_talker',
        )
    #listener = launch_ros.actions.Node(
        #package='mypkg',
        #executable='listener',
        #output='screen'
        #)

    return launch.LaunchDescription([weather_humidity_talk])

