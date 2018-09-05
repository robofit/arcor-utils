#!/usr/bin/env python
import rospy
from art_msgs.srv import getARTableConfig, getARTableConfigResponse
from art_msgs.msg import ARTableConfig


class RosparamServices:
    def __init__(self):
        self.get_art_conf_srv = rospy.Service('/art/conf/get', getARTableConfig, self.art_rosparam_conf_get_cb)
        rospy.spin()

    def art_rosparam_conf_get_cb(self, req):
        conf = rospy.get_param("/art/conf")
        table_size = conf["table"]["size"].split(",")
        return getARTableConfigResponse(conf=ARTableConfig(table_size=table_size,world_frame=conf["world_frame"]))


if __name__ == "__main__":
    rospy.init_node('rosparam_service_node')

    try:
        node = RosparamServices()
    except rospy.ROSInterruptException:
        pass
