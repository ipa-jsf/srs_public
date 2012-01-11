"""autogenerated by genmsg_py from IKActionGoal.msg. Do not edit."""
import roslib.message
import struct

import geometry_msgs.msg
import roslib.rostime
import actionlib_msgs.msg
import srs_grasping.msg
import std_msgs.msg

class IKActionGoal(roslib.message.Message):
  _md5sum = "31befda6e095087e2c46bb936cb4ca51"
  _type = "srs_grasping/IKActionGoal"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalID goal_id
IKGoal goal

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: srs_grasping/IKGoal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
geometry_msgs/PoseStamped pre_pose
geometry_msgs/PoseStamped g_pose

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['header','goal_id','goal']
  _slot_types = ['Header','actionlib_msgs/GoalID','srs_grasping/IKGoal']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       header,goal_id,goal
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(IKActionGoal, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = srs_grasping.msg.IKGoal()
    else:
      self.header = std_msgs.msg._Header.Header()
      self.goal_id = actionlib_msgs.msg.GoalID()
      self.goal = srs_grasping.msg.IKGoal()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.goal.pre_pose.header.seq, _x.goal.pre_pose.header.stamp.secs, _x.goal.pre_pose.header.stamp.nsecs))
      _x = self.goal.pre_pose.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d3I.pack(_x.goal.pre_pose.pose.position.x, _x.goal.pre_pose.pose.position.y, _x.goal.pre_pose.pose.position.z, _x.goal.pre_pose.pose.orientation.x, _x.goal.pre_pose.pose.orientation.y, _x.goal.pre_pose.pose.orientation.z, _x.goal.pre_pose.pose.orientation.w, _x.goal.g_pose.header.seq, _x.goal.g_pose.header.stamp.secs, _x.goal.g_pose.header.stamp.nsecs))
      _x = self.goal.g_pose.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.goal.g_pose.pose.position.x, _x.goal.g_pose.pose.position.y, _x.goal.g_pose.pose.position.z, _x.goal.g_pose.pose.orientation.x, _x.goal.g_pose.pose.orientation.y, _x.goal.g_pose.pose.orientation.z, _x.goal.g_pose.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = srs_grasping.msg.IKGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.goal.pre_pose.header.seq, _x.goal.pre_pose.header.stamp.secs, _x.goal.pre_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal.pre_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.goal.pre_pose.pose.position.x, _x.goal.pre_pose.pose.position.y, _x.goal.pre_pose.pose.position.z, _x.goal.pre_pose.pose.orientation.x, _x.goal.pre_pose.pose.orientation.y, _x.goal.pre_pose.pose.orientation.z, _x.goal.pre_pose.pose.orientation.w, _x.goal.g_pose.header.seq, _x.goal.g_pose.header.stamp.secs, _x.goal.g_pose.header.stamp.nsecs,) = _struct_7d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal.g_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.goal.g_pose.pose.position.x, _x.goal.g_pose.pose.position.y, _x.goal.g_pose.pose.position.z, _x.goal.g_pose.pose.orientation.x, _x.goal.g_pose.pose.orientation.y, _x.goal.g_pose.pose.orientation.z, _x.goal.g_pose.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.goal.pre_pose.header.seq, _x.goal.pre_pose.header.stamp.secs, _x.goal.pre_pose.header.stamp.nsecs))
      _x = self.goal.pre_pose.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d3I.pack(_x.goal.pre_pose.pose.position.x, _x.goal.pre_pose.pose.position.y, _x.goal.pre_pose.pose.position.z, _x.goal.pre_pose.pose.orientation.x, _x.goal.pre_pose.pose.orientation.y, _x.goal.pre_pose.pose.orientation.z, _x.goal.pre_pose.pose.orientation.w, _x.goal.g_pose.header.seq, _x.goal.g_pose.header.stamp.secs, _x.goal.g_pose.header.stamp.nsecs))
      _x = self.goal.g_pose.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.goal.g_pose.pose.position.x, _x.goal.g_pose.pose.position.y, _x.goal.g_pose.pose.position.z, _x.goal.g_pose.pose.orientation.x, _x.goal.g_pose.pose.orientation.y, _x.goal.g_pose.pose.orientation.z, _x.goal.g_pose.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = srs_grasping.msg.IKGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.goal.pre_pose.header.seq, _x.goal.pre_pose.header.stamp.secs, _x.goal.pre_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal.pre_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.goal.pre_pose.pose.position.x, _x.goal.pre_pose.pose.position.y, _x.goal.pre_pose.pose.position.z, _x.goal.pre_pose.pose.orientation.x, _x.goal.pre_pose.pose.orientation.y, _x.goal.pre_pose.pose.orientation.z, _x.goal.pre_pose.pose.orientation.w, _x.goal.g_pose.header.seq, _x.goal.g_pose.header.stamp.secs, _x.goal.g_pose.header.stamp.nsecs,) = _struct_7d3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal.g_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.goal.g_pose.pose.position.x, _x.goal.g_pose.pose.position.y, _x.goal.g_pose.pose.position.z, _x.goal.g_pose.pose.orientation.x, _x.goal.g_pose.pose.orientation.y, _x.goal.g_pose.pose.orientation.z, _x.goal.g_pose.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3I = struct.Struct("<3I")
_struct_7d = struct.Struct("<7d")
_struct_2I = struct.Struct("<2I")
_struct_7d3I = struct.Struct("<7d3I")
