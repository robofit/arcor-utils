#!/usr/bin/env python
import rospy
import tf
from tf2_msgs.msg import TFMessage


class TFBroadcaster:
    def __init__(self):
        self.br = tf.TransformBroadcaster()
        self.device_tf_sub = rospy.Subscriber("remote_device_tf", TFMessage, self.device_tf_sub_cb)

    def device_tf_sub_cb(self, data):
        for transform in data.transforms:
            self.br.sendTransform((transform.transform.translation.x,
                                   transform.transform.translation.y,
                                   transform.transform.translation.z),
                                  (transform.transform.rotation.x,
                                   transform.transform.rotation.y,
                                   transform.transform.rotation.z,
                                   transform.transform.rotation.w),
                                  rospy.Time.now(),
                                  transform.child_frame_id,
                                  transform.header.frame_id)


if __name__ == "__main__":

    rospy.init_node('remote_device_tf_broadcaster')

    try:
        tf_broadcaster = TFBroadcaster()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
