; Auto-generated. Do not edit!


(cl:in-package srs_grasping-msg)


;//! \htmlinclude IKGoal.msg.html

(cl:defclass <IKGoal> (roslisp-msg-protocol:ros-message)
  ((pre_pose
    :reader pre_pose
    :initarg :pre_pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (g_pose
    :reader g_pose
    :initarg :g_pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass IKGoal (<IKGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IKGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IKGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name srs_grasping-msg:<IKGoal> is deprecated: use srs_grasping-msg:IKGoal instead.")))

(cl:ensure-generic-function 'pre_pose-val :lambda-list '(m))
(cl:defmethod pre_pose-val ((m <IKGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader srs_grasping-msg:pre_pose-val is deprecated.  Use srs_grasping-msg:pre_pose instead.")
  (pre_pose m))

(cl:ensure-generic-function 'g_pose-val :lambda-list '(m))
(cl:defmethod g_pose-val ((m <IKGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader srs_grasping-msg:g_pose-val is deprecated.  Use srs_grasping-msg:g_pose instead.")
  (g_pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IKGoal>) ostream)
  "Serializes a message object of type '<IKGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pre_pose) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'g_pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IKGoal>) istream)
  "Deserializes a message object of type '<IKGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pre_pose) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'g_pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IKGoal>)))
  "Returns string type for a message object of type '<IKGoal>"
  "srs_grasping/IKGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IKGoal)))
  "Returns string type for a message object of type 'IKGoal"
  "srs_grasping/IKGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IKGoal>)))
  "Returns md5sum for a message object of type '<IKGoal>"
  "be361c2f7296f2b7844f4d50c89e91ca")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IKGoal)))
  "Returns md5sum for a message object of type 'IKGoal"
  "be361c2f7296f2b7844f4d50c89e91ca")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IKGoal>)))
  "Returns full string definition for message of type '<IKGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%geometry_msgs/PoseStamped pre_pose~%geometry_msgs/PoseStamped g_pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IKGoal)))
  "Returns full string definition for message of type 'IKGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%geometry_msgs/PoseStamped pre_pose~%geometry_msgs/PoseStamped g_pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IKGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pre_pose))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'g_pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IKGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'IKGoal
    (cl:cons ':pre_pose (pre_pose msg))
    (cl:cons ':g_pose (g_pose msg))
))
