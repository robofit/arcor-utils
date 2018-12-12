from art_utils.art_api_helper import ArtApiHelper, ArtApiException
from art_utils.api_definition import APIGroup, Topic, Service, Action, ArtAPI
from art_utils.object_helper import ObjectHelper

import rospy


def wait_for_param(param, sleep=0.5):

    while not rospy.has_param(param):

        if rospy.is_shutdown():
            raise rospy.ROSInterruptException()

        rospy.loginfo("Waiting for param: " + param)
        rospy.sleep(sleep)


def array_from_param(param, target_type=str, expected_length=None, default=None, wait=False):

    if wait:
        wait_for_param(param)

    try:
        par = rospy.get_param(param)
    except KeyError as e:

        if default is None:
            raise KeyError(e)
        else:
            return default

    if not par:
        return []

    tmp = []

    for s in par.split(","):
        tmp.append(target_type(s.strip()))

    if expected_length is not None:
        if len(tmp) != expected_length:
            raise ValueError

    return tmp
