/* Auto-generated by genmsg_cpp for file /home/emisario/git/care-o-bot/srs/srs_grasping/msg/GraspResult.msg */
#ifndef SRS_GRASPING_MESSAGE_GRASPRESULT_H
#define SRS_GRASPING_MESSAGE_GRASPRESULT_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "srs_msgs/GraspConfiguration.h"

namespace srs_grasping
{
template <class ContainerAllocator>
struct GraspResult_ {
  typedef GraspResult_<ContainerAllocator> Type;

  GraspResult_()
  : grasp_configuration()
  {
  }

  GraspResult_(const ContainerAllocator& _alloc)
  : grasp_configuration(_alloc)
  {
  }

  typedef std::vector< ::srs_msgs::GraspConfiguration_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::srs_msgs::GraspConfiguration_<ContainerAllocator> >::other >  _grasp_configuration_type;
  std::vector< ::srs_msgs::GraspConfiguration_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::srs_msgs::GraspConfiguration_<ContainerAllocator> >::other >  grasp_configuration;


  ROS_DEPRECATED uint32_t get_grasp_configuration_size() const { return (uint32_t)grasp_configuration.size(); }
  ROS_DEPRECATED void set_grasp_configuration_size(uint32_t size) { grasp_configuration.resize((size_t)size); }
  ROS_DEPRECATED void get_grasp_configuration_vec(std::vector< ::srs_msgs::GraspConfiguration_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::srs_msgs::GraspConfiguration_<ContainerAllocator> >::other > & vec) const { vec = this->grasp_configuration; }
  ROS_DEPRECATED void set_grasp_configuration_vec(const std::vector< ::srs_msgs::GraspConfiguration_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::srs_msgs::GraspConfiguration_<ContainerAllocator> >::other > & vec) { this->grasp_configuration = vec; }
private:
  static const char* __s_getDataType_() { return "srs_grasping/GraspResult"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "f19658594ceb0d6a35cc8a7e3b06a8d2"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
srs_msgs/GraspConfiguration[] grasp_configuration\n\
\n\
================================================================================\n\
MSG: srs_msgs/GraspConfiguration\n\
int32 object_id\n\
string hand_type\n\
trajectory_msgs/JointTrajectory sconfiguration\n\
geometry_msgs/PoseStamped palm_pose\n\
geometry_msgs/PoseStamped pre_grasp\n\
string category\n\
float32 score\n\
\n\
================================================================================\n\
MSG: trajectory_msgs/JointTrajectory\n\
Header header\n\
string[] joint_names\n\
JointTrajectoryPoint[] points\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: trajectory_msgs/JointTrajectoryPoint\n\
float64[] positions\n\
float64[] velocities\n\
float64[] accelerations\n\
duration time_from_start\n\
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, grasp_configuration);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, grasp_configuration);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(grasp_configuration);
    return size;
  }

  typedef boost::shared_ptr< ::srs_grasping::GraspResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::srs_grasping::GraspResult_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct GraspResult
typedef  ::srs_grasping::GraspResult_<std::allocator<void> > GraspResult;

typedef boost::shared_ptr< ::srs_grasping::GraspResult> GraspResultPtr;
typedef boost::shared_ptr< ::srs_grasping::GraspResult const> GraspResultConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::srs_grasping::GraspResult_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::srs_grasping::GraspResult_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace srs_grasping

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::srs_grasping::GraspResult_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::srs_grasping::GraspResult_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::srs_grasping::GraspResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "f19658594ceb0d6a35cc8a7e3b06a8d2";
  }

  static const char* value(const  ::srs_grasping::GraspResult_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xf19658594ceb0d6aULL;
  static const uint64_t static_value2 = 0x35cc8a7e3b06a8d2ULL;
};

template<class ContainerAllocator>
struct DataType< ::srs_grasping::GraspResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "srs_grasping/GraspResult";
  }

  static const char* value(const  ::srs_grasping::GraspResult_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::srs_grasping::GraspResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
srs_msgs/GraspConfiguration[] grasp_configuration\n\
\n\
================================================================================\n\
MSG: srs_msgs/GraspConfiguration\n\
int32 object_id\n\
string hand_type\n\
trajectory_msgs/JointTrajectory sconfiguration\n\
geometry_msgs/PoseStamped palm_pose\n\
geometry_msgs/PoseStamped pre_grasp\n\
string category\n\
float32 score\n\
\n\
================================================================================\n\
MSG: trajectory_msgs/JointTrajectory\n\
Header header\n\
string[] joint_names\n\
JointTrajectoryPoint[] points\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: trajectory_msgs/JointTrajectoryPoint\n\
float64[] positions\n\
float64[] velocities\n\
float64[] accelerations\n\
duration time_from_start\n\
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
";
  }

  static const char* value(const  ::srs_grasping::GraspResult_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::srs_grasping::GraspResult_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.grasp_configuration);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GraspResult_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::srs_grasping::GraspResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::srs_grasping::GraspResult_<ContainerAllocator> & v) 
  {
    s << indent << "grasp_configuration[]" << std::endl;
    for (size_t i = 0; i < v.grasp_configuration.size(); ++i)
    {
      s << indent << "  grasp_configuration[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::srs_msgs::GraspConfiguration_<ContainerAllocator> >::stream(s, indent + "    ", v.grasp_configuration[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // SRS_GRASPING_MESSAGE_GRASPRESULT_H

