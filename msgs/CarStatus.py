# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from wheel_control/CarStatus.msg. Do not edit."""
import codecs
import sys

python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CarStatus(genpy.Message):
    _md5sum = "40e809ffbae50f2069f28f48db847441"
    _type = "wheel_control/CarStatus"
    _has_header = False  # flag to mark the presence of a Header object
    _full_text = """
# channel: "BalanceCarStatus"

int64 timestamp
uint32 error_code_l     # error code, no explanation
uint32 error_code_r   # error code, no explanation
string error_message  # error code, no explanation
int8 control_mode    # 1-free control, 100-handle control,101-lcm control
int32 encoder_position_r  # 
int32 encoder_position_l  # 
float32 wheel_speed_R    # m/h
float32 wheel_speed_L    # m/h
float32 unit_convert_scale

# error own detect
bool has_follow_error_l
bool has_follow_error_r
float32 follow_error_integral_l
float32 follow_error_integral_r

# control info
float32 control_info_speed_left
float32 control_info_speed_right
int8 control_info_user_control_mode
int64 control_info_cmd_duration 
float32 control_info_acc
float32 control_info_dec
bool control_info_emergency
bool control_info_is_clear_error
bool control_info_planning_release_control

int8 control_mode_l 
int8 control_mode_r 
int8 active_sts_l 
int8 active_sts_r 
float32 wheel_spd_l 
float32 wheel_spd_r 
float32 wheel_acc_l
float32 wheel_acc_r
float32 wheel_dec_l
float32 wheel_dec_r

float32 current_max_l     #A
float32 current_max_r     #A

float32 phase_current_l     # unit: A 实际相电流
float32 phase_current_r     # unit: A 实际相电流

bool stop_flag_l
bool stop_flag_r

bool disconnectProtectionEnabledLeft
bool disconnectProtectionEnabledRight

int32 disconnectProtectDelayL
int32 disconnectProtectDelayR

int16 temperature_l 
int16 temperature_r 
int8 volt_l 
int8 volt_r 
"""
    __slots__ = [
        "timestamp",
        "error_code_l",
        "error_code_r",
        "error_message",
        "control_mode",
        "encoder_position_r",
        "encoder_position_l",
        "wheel_speed_R",
        "wheel_speed_L",
        "unit_convert_scale",
        "has_follow_error_l",
        "has_follow_error_r",
        "follow_error_integral_l",
        "follow_error_integral_r",
        "control_info_speed_left",
        "control_info_speed_right",
        "control_info_user_control_mode",
        "control_info_cmd_duration",
        "control_info_acc",
        "control_info_dec",
        "control_info_emergency",
        "control_info_is_clear_error",
        "control_info_planning_release_control",
        "control_mode_l",
        "control_mode_r",
        "active_sts_l",
        "active_sts_r",
        "wheel_spd_l",
        "wheel_spd_r",
        "wheel_acc_l",
        "wheel_acc_r",
        "wheel_dec_l",
        "wheel_dec_r",
        "current_max_l",
        "current_max_r",
        "phase_current_l",
        "phase_current_r",
        "stop_flag_l",
        "stop_flag_r",
        "disconnectProtectionEnabledLeft",
        "disconnectProtectionEnabledRight",
        "disconnectProtectDelayL",
        "disconnectProtectDelayR",
        "temperature_l",
        "temperature_r",
        "volt_l",
        "volt_r",
    ]
    _slot_types = [
        "int64",
        "uint32",
        "uint32",
        "string",
        "int8",
        "int32",
        "int32",
        "float32",
        "float32",
        "float32",
        "bool",
        "bool",
        "float32",
        "float32",
        "float32",
        "float32",
        "int8",
        "int64",
        "float32",
        "float32",
        "bool",
        "bool",
        "bool",
        "int8",
        "int8",
        "int8",
        "int8",
        "float32",
        "float32",
        "float32",
        "float32",
        "float32",
        "float32",
        "float32",
        "float32",
        "float32",
        "float32",
        "bool",
        "bool",
        "bool",
        "bool",
        "int32",
        "int32",
        "int16",
        "int16",
        "int8",
        "int8",
    ]

    def __init__(self, *args, **kwds):
        """
        Constructor. Any message fields that are implicitly/explicitly
        set to None will be assigned a default value. The recommend
        use is keyword arguments as this is more robust to future message
        changes.  You cannot mix in-order arguments and keyword arguments.

        The available fields are:
           timestamp,error_code_l,error_code_r,error_message,control_mode,encoder_position_r,encoder_position_l,wheel_speed_R,wheel_speed_L,unit_convert_scale,has_follow_error_l,has_follow_error_r,follow_error_integral_l,follow_error_integral_r,control_info_speed_left,control_info_speed_right,control_info_user_control_mode,control_info_cmd_duration,control_info_acc,control_info_dec,control_info_emergency,control_info_is_clear_error,control_info_planning_release_control,control_mode_l,control_mode_r,active_sts_l,active_sts_r,wheel_spd_l,wheel_spd_r,wheel_acc_l,wheel_acc_r,wheel_dec_l,wheel_dec_r,current_max_l,current_max_r,phase_current_l,phase_current_r,stop_flag_l,stop_flag_r,disconnectProtectionEnabledLeft,disconnectProtectionEnabledRight,disconnectProtectDelayL,disconnectProtectDelayR,temperature_l,temperature_r,volt_l,volt_r

        :param args: complete set of field values, in .msg order
        :param kwds: use keyword arguments corresponding to message field names
        to set specific fields.
        """
        if args or kwds:
            super(CarStatus, self).__init__(*args, **kwds)
            # message fields cannot be None, assign default values for those that are
            if self.timestamp is None:
                self.timestamp = 0
            if self.error_code_l is None:
                self.error_code_l = 0
            if self.error_code_r is None:
                self.error_code_r = 0
            if self.error_message is None:
                self.error_message = ""
            if self.control_mode is None:
                self.control_mode = 0
            if self.encoder_position_r is None:
                self.encoder_position_r = 0
            if self.encoder_position_l is None:
                self.encoder_position_l = 0
            if self.wheel_speed_R is None:
                self.wheel_speed_R = 0.0
            if self.wheel_speed_L is None:
                self.wheel_speed_L = 0.0
            if self.unit_convert_scale is None:
                self.unit_convert_scale = 0.0
            if self.has_follow_error_l is None:
                self.has_follow_error_l = False
            if self.has_follow_error_r is None:
                self.has_follow_error_r = False
            if self.follow_error_integral_l is None:
                self.follow_error_integral_l = 0.0
            if self.follow_error_integral_r is None:
                self.follow_error_integral_r = 0.0
            if self.control_info_speed_left is None:
                self.control_info_speed_left = 0.0
            if self.control_info_speed_right is None:
                self.control_info_speed_right = 0.0
            if self.control_info_user_control_mode is None:
                self.control_info_user_control_mode = 0
            if self.control_info_cmd_duration is None:
                self.control_info_cmd_duration = 0
            if self.control_info_acc is None:
                self.control_info_acc = 0.0
            if self.control_info_dec is None:
                self.control_info_dec = 0.0
            if self.control_info_emergency is None:
                self.control_info_emergency = False
            if self.control_info_is_clear_error is None:
                self.control_info_is_clear_error = False
            if self.control_info_planning_release_control is None:
                self.control_info_planning_release_control = False
            if self.control_mode_l is None:
                self.control_mode_l = 0
            if self.control_mode_r is None:
                self.control_mode_r = 0
            if self.active_sts_l is None:
                self.active_sts_l = 0
            if self.active_sts_r is None:
                self.active_sts_r = 0
            if self.wheel_spd_l is None:
                self.wheel_spd_l = 0.0
            if self.wheel_spd_r is None:
                self.wheel_spd_r = 0.0
            if self.wheel_acc_l is None:
                self.wheel_acc_l = 0.0
            if self.wheel_acc_r is None:
                self.wheel_acc_r = 0.0
            if self.wheel_dec_l is None:
                self.wheel_dec_l = 0.0
            if self.wheel_dec_r is None:
                self.wheel_dec_r = 0.0
            if self.current_max_l is None:
                self.current_max_l = 0.0
            if self.current_max_r is None:
                self.current_max_r = 0.0
            if self.phase_current_l is None:
                self.phase_current_l = 0.0
            if self.phase_current_r is None:
                self.phase_current_r = 0.0
            if self.stop_flag_l is None:
                self.stop_flag_l = False
            if self.stop_flag_r is None:
                self.stop_flag_r = False
            if self.disconnectProtectionEnabledLeft is None:
                self.disconnectProtectionEnabledLeft = False
            if self.disconnectProtectionEnabledRight is None:
                self.disconnectProtectionEnabledRight = False
            if self.disconnectProtectDelayL is None:
                self.disconnectProtectDelayL = 0
            if self.disconnectProtectDelayR is None:
                self.disconnectProtectDelayR = 0
            if self.temperature_l is None:
                self.temperature_l = 0
            if self.temperature_r is None:
                self.temperature_r = 0
            if self.volt_l is None:
                self.volt_l = 0
            if self.volt_r is None:
                self.volt_r = 0
        else:
            self.timestamp = 0
            self.error_code_l = 0
            self.error_code_r = 0
            self.error_message = ""
            self.control_mode = 0
            self.encoder_position_r = 0
            self.encoder_position_l = 0
            self.wheel_speed_R = 0.0
            self.wheel_speed_L = 0.0
            self.unit_convert_scale = 0.0
            self.has_follow_error_l = False
            self.has_follow_error_r = False
            self.follow_error_integral_l = 0.0
            self.follow_error_integral_r = 0.0
            self.control_info_speed_left = 0.0
            self.control_info_speed_right = 0.0
            self.control_info_user_control_mode = 0
            self.control_info_cmd_duration = 0
            self.control_info_acc = 0.0
            self.control_info_dec = 0.0
            self.control_info_emergency = False
            self.control_info_is_clear_error = False
            self.control_info_planning_release_control = False
            self.control_mode_l = 0
            self.control_mode_r = 0
            self.active_sts_l = 0
            self.active_sts_r = 0
            self.wheel_spd_l = 0.0
            self.wheel_spd_r = 0.0
            self.wheel_acc_l = 0.0
            self.wheel_acc_r = 0.0
            self.wheel_dec_l = 0.0
            self.wheel_dec_r = 0.0
            self.current_max_l = 0.0
            self.current_max_r = 0.0
            self.phase_current_l = 0.0
            self.phase_current_r = 0.0
            self.stop_flag_l = False
            self.stop_flag_r = False
            self.disconnectProtectionEnabledLeft = False
            self.disconnectProtectionEnabledRight = False
            self.disconnectProtectDelayL = 0
            self.disconnectProtectDelayR = 0
            self.temperature_l = 0
            self.temperature_r = 0
            self.volt_l = 0
            self.volt_r = 0

    def _get_types(self):
        """
        internal API method
        """
        return self._slot_types

    def serialize(self, buff):
        """
        serialize message into buffer
        :param buff: buffer, ``StringIO``
        """
        try:
            _x = self
            buff.write(
                _get_struct_q2I().pack(_x.timestamp, _x.error_code_l, _x.error_code_r)
            )
            _x = self.error_message
            length = len(_x)
            if python3 or type(_x) == unicode:
                _x = _x.encode("utf-8")
                length = len(_x)
            buff.write(struct.Struct("<I%ss" % length).pack(length, _x))
            _x = self
            buff.write(
                _get_struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b().pack(
                    _x.control_mode,
                    _x.encoder_position_r,
                    _x.encoder_position_l,
                    _x.wheel_speed_R,
                    _x.wheel_speed_L,
                    _x.unit_convert_scale,
                    _x.has_follow_error_l,
                    _x.has_follow_error_r,
                    _x.follow_error_integral_l,
                    _x.follow_error_integral_r,
                    _x.control_info_speed_left,
                    _x.control_info_speed_right,
                    _x.control_info_user_control_mode,
                    _x.control_info_cmd_duration,
                    _x.control_info_acc,
                    _x.control_info_dec,
                    _x.control_info_emergency,
                    _x.control_info_is_clear_error,
                    _x.control_info_planning_release_control,
                    _x.control_mode_l,
                    _x.control_mode_r,
                    _x.active_sts_l,
                    _x.active_sts_r,
                    _x.wheel_spd_l,
                    _x.wheel_spd_r,
                    _x.wheel_acc_l,
                    _x.wheel_acc_r,
                    _x.wheel_dec_l,
                    _x.wheel_dec_r,
                    _x.current_max_l,
                    _x.current_max_r,
                    _x.phase_current_l,
                    _x.phase_current_r,
                    _x.stop_flag_l,
                    _x.stop_flag_r,
                    _x.disconnectProtectionEnabledLeft,
                    _x.disconnectProtectionEnabledRight,
                    _x.disconnectProtectDelayL,
                    _x.disconnectProtectDelayR,
                    _x.temperature_l,
                    _x.temperature_r,
                    _x.volt_l,
                    _x.volt_r,
                )
            )
        except struct.error as se:
            self._check_types(
                struct.error(
                    "%s: '%s' when writing '%s'"
                    % (type(se), str(se), str(locals().get("_x", self)))
                )
            )
        except TypeError as te:
            self._check_types(
                ValueError(
                    "%s: '%s' when writing '%s'"
                    % (type(te), str(te), str(locals().get("_x", self)))
                )
            )

    def deserialize(self, str):
        """
        unpack serialized message in str into this message instance
        :param str: byte array of serialized message, ``str``
        """
        if python3:
            codecs.lookup_error("rosmsg").msg_type = self._type
        try:
            end = 0
            _x = self
            start = end
            end += 16
            (
                _x.timestamp,
                _x.error_code_l,
                _x.error_code_r,
            ) = _get_struct_q2I().unpack(str[start:end])
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
                self.error_message = str[start:end].decode("utf-8", "rosmsg")
            else:
                self.error_message = str[start:end]
            _x = self
            start = end
            end += 121
            (
                _x.control_mode,
                _x.encoder_position_r,
                _x.encoder_position_l,
                _x.wheel_speed_R,
                _x.wheel_speed_L,
                _x.unit_convert_scale,
                _x.has_follow_error_l,
                _x.has_follow_error_r,
                _x.follow_error_integral_l,
                _x.follow_error_integral_r,
                _x.control_info_speed_left,
                _x.control_info_speed_right,
                _x.control_info_user_control_mode,
                _x.control_info_cmd_duration,
                _x.control_info_acc,
                _x.control_info_dec,
                _x.control_info_emergency,
                _x.control_info_is_clear_error,
                _x.control_info_planning_release_control,
                _x.control_mode_l,
                _x.control_mode_r,
                _x.active_sts_l,
                _x.active_sts_r,
                _x.wheel_spd_l,
                _x.wheel_spd_r,
                _x.wheel_acc_l,
                _x.wheel_acc_r,
                _x.wheel_dec_l,
                _x.wheel_dec_r,
                _x.current_max_l,
                _x.current_max_r,
                _x.phase_current_l,
                _x.phase_current_r,
                _x.stop_flag_l,
                _x.stop_flag_r,
                _x.disconnectProtectionEnabledLeft,
                _x.disconnectProtectionEnabledRight,
                _x.disconnectProtectDelayL,
                _x.disconnectProtectDelayR,
                _x.temperature_l,
                _x.temperature_r,
                _x.volt_l,
                _x.volt_r,
            ) = _get_struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b().unpack(str[start:end])
            self.has_follow_error_l = bool(self.has_follow_error_l)
            self.has_follow_error_r = bool(self.has_follow_error_r)
            self.control_info_emergency = bool(self.control_info_emergency)
            self.control_info_is_clear_error = bool(self.control_info_is_clear_error)
            self.control_info_planning_release_control = bool(
                self.control_info_planning_release_control
            )
            self.stop_flag_l = bool(self.stop_flag_l)
            self.stop_flag_r = bool(self.stop_flag_r)
            self.disconnectProtectionEnabledLeft = bool(
                self.disconnectProtectionEnabledLeft
            )
            self.disconnectProtectionEnabledRight = bool(
                self.disconnectProtectionEnabledRight
            )
            return self
        except struct.error as e:
            raise genpy.DeserializationError(e)  # most likely buffer underfill

    def serialize_numpy(self, buff, numpy):
        """
        serialize message with numpy array types into buffer
        :param buff: buffer, ``StringIO``
        :param numpy: numpy python module
        """
        try:
            _x = self
            buff.write(
                _get_struct_q2I().pack(_x.timestamp, _x.error_code_l, _x.error_code_r)
            )
            _x = self.error_message
            length = len(_x)
            if python3 or type(_x) == unicode:
                _x = _x.encode("utf-8")
                length = len(_x)
            buff.write(struct.Struct("<I%ss" % length).pack(length, _x))
            _x = self
            buff.write(
                _get_struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b().pack(
                    _x.control_mode,
                    _x.encoder_position_r,
                    _x.encoder_position_l,
                    _x.wheel_speed_R,
                    _x.wheel_speed_L,
                    _x.unit_convert_scale,
                    _x.has_follow_error_l,
                    _x.has_follow_error_r,
                    _x.follow_error_integral_l,
                    _x.follow_error_integral_r,
                    _x.control_info_speed_left,
                    _x.control_info_speed_right,
                    _x.control_info_user_control_mode,
                    _x.control_info_cmd_duration,
                    _x.control_info_acc,
                    _x.control_info_dec,
                    _x.control_info_emergency,
                    _x.control_info_is_clear_error,
                    _x.control_info_planning_release_control,
                    _x.control_mode_l,
                    _x.control_mode_r,
                    _x.active_sts_l,
                    _x.active_sts_r,
                    _x.wheel_spd_l,
                    _x.wheel_spd_r,
                    _x.wheel_acc_l,
                    _x.wheel_acc_r,
                    _x.wheel_dec_l,
                    _x.wheel_dec_r,
                    _x.current_max_l,
                    _x.current_max_r,
                    _x.phase_current_l,
                    _x.phase_current_r,
                    _x.stop_flag_l,
                    _x.stop_flag_r,
                    _x.disconnectProtectionEnabledLeft,
                    _x.disconnectProtectionEnabledRight,
                    _x.disconnectProtectDelayL,
                    _x.disconnectProtectDelayR,
                    _x.temperature_l,
                    _x.temperature_r,
                    _x.volt_l,
                    _x.volt_r,
                )
            )
        except struct.error as se:
            self._check_types(
                struct.error(
                    "%s: '%s' when writing '%s'"
                    % (type(se), str(se), str(locals().get("_x", self)))
                )
            )
        except TypeError as te:
            self._check_types(
                ValueError(
                    "%s: '%s' when writing '%s'"
                    % (type(te), str(te), str(locals().get("_x", self)))
                )
            )

    def deserialize_numpy(self, str, numpy):
        """
        unpack serialized message in str into this message instance using numpy for array types
        :param str: byte array of serialized message, ``str``
        :param numpy: numpy python module
        """
        if python3:
            codecs.lookup_error("rosmsg").msg_type = self._type
        try:
            end = 0
            _x = self
            start = end
            end += 16
            (
                _x.timestamp,
                _x.error_code_l,
                _x.error_code_r,
            ) = _get_struct_q2I().unpack(str[start:end])
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            if python3:
                self.error_message = str[start:end].decode("utf-8", "rosmsg")
            else:
                self.error_message = str[start:end]
            _x = self
            start = end
            end += 121
            (
                _x.control_mode,
                _x.encoder_position_r,
                _x.encoder_position_l,
                _x.wheel_speed_R,
                _x.wheel_speed_L,
                _x.unit_convert_scale,
                _x.has_follow_error_l,
                _x.has_follow_error_r,
                _x.follow_error_integral_l,
                _x.follow_error_integral_r,
                _x.control_info_speed_left,
                _x.control_info_speed_right,
                _x.control_info_user_control_mode,
                _x.control_info_cmd_duration,
                _x.control_info_acc,
                _x.control_info_dec,
                _x.control_info_emergency,
                _x.control_info_is_clear_error,
                _x.control_info_planning_release_control,
                _x.control_mode_l,
                _x.control_mode_r,
                _x.active_sts_l,
                _x.active_sts_r,
                _x.wheel_spd_l,
                _x.wheel_spd_r,
                _x.wheel_acc_l,
                _x.wheel_acc_r,
                _x.wheel_dec_l,
                _x.wheel_dec_r,
                _x.current_max_l,
                _x.current_max_r,
                _x.phase_current_l,
                _x.phase_current_r,
                _x.stop_flag_l,
                _x.stop_flag_r,
                _x.disconnectProtectionEnabledLeft,
                _x.disconnectProtectionEnabledRight,
                _x.disconnectProtectDelayL,
                _x.disconnectProtectDelayR,
                _x.temperature_l,
                _x.temperature_r,
                _x.volt_l,
                _x.volt_r,
            ) = _get_struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b().unpack(str[start:end])
            self.has_follow_error_l = bool(self.has_follow_error_l)
            self.has_follow_error_r = bool(self.has_follow_error_r)
            self.control_info_emergency = bool(self.control_info_emergency)
            self.control_info_is_clear_error = bool(self.control_info_is_clear_error)
            self.control_info_planning_release_control = bool(
                self.control_info_planning_release_control
            )
            self.stop_flag_l = bool(self.stop_flag_l)
            self.stop_flag_r = bool(self.stop_flag_r)
            self.disconnectProtectionEnabledLeft = bool(
                self.disconnectProtectionEnabledLeft
            )
            self.disconnectProtectionEnabledRight = bool(
                self.disconnectProtectionEnabledRight
            )
            return self
        except struct.error as e:
            raise genpy.DeserializationError(e)  # most likely buffer underfill


_struct_I = genpy.struct_I


def _get_struct_I():
    global _struct_I
    return _struct_I


_struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b = None


def _get_struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b():
    global _struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b
    if _struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b is None:
        _struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b = struct.Struct(
            "<b2i3f2B4fbq2f3B4b10f4B2i2h2b"
        )
    return _struct_b2i3f2B4fbq2f3B4b10f4B2i2h2b


_struct_q2I = None


def _get_struct_q2I():
    global _struct_q2I
    if _struct_q2I is None:
        _struct_q2I = struct.Struct("<q2I")
    return _struct_q2I
