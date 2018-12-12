#!/usr/bin/env python
import rospy
import json
from art_msgs.srv import GetRosparam, GetRosparamResponse


class RosparamServices:
    def __init__(self):
        self.get_rosparam_service = rospy.Service('/rosparam_get', GetRosparam, self.get_rosparam_cb)

    def get_rosparam_cb(self, req):
        success = False

        try:
            param = rospy.get_param(req.param_name)
            success = True
        except KeyError:
            param = {}

        return GetRosparamResponse(success=success, message=json.dumps(param))


if __name__ == "__main__":
    rospy.init_node('rosparam_service_node')

    try:
        node = RosparamServices()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
