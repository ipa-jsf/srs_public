; Auto-generated. Do not edit!


(cl:in-package srs_grasping-msg)


;//! \htmlinclude IKFeedback.msg.html

(cl:defclass <IKFeedback> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass IKFeedback (<IKFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IKFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IKFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name srs_grasping-msg:<IKFeedback> is deprecated: use srs_grasping-msg:IKFeedback instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IKFeedback>) ostream)
  "Serializes a message object of type '<IKFeedback>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IKFeedback>) istream)
  "Deserializes a message object of type '<IKFeedback>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IKFeedback>)))
  "Returns string type for a message object of type '<IKFeedback>"
  "srs_grasping/IKFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IKFeedback)))
  "Returns string type for a message object of type 'IKFeedback"
  "srs_grasping/IKFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IKFeedback>)))
  "Returns md5sum for a message object of type '<IKFeedback>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IKFeedback)))
  "Returns md5sum for a message object of type 'IKFeedback"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IKFeedback>)))
  "Returns full string definition for message of type '<IKFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IKFeedback)))
  "Returns full string definition for message of type 'IKFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IKFeedback>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IKFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'IKFeedback
))
