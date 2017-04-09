
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters related to bandwidth
configuration of TE tunnels
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__specification_type','__set_bandwidth','__signaled_bandwidth',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__specification_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AUTO': {}, u'SPECIFIED': {}},), default=unicode("SPECIFIED"), is_leaf=True, yang_name="specification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='te-bandwidth-type', is_config=False)
    self.__set_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="set-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)
    self.__signaled_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="signaled-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'bandwidth', u'state']

  def _get_specification_type(self):
    """
    Getter method for specification_type, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/specification_type (te-bandwidth-type)

    YANG Description: The method used for settign the bandwidth, either explicitly
specified or configured
    """
    return self.__specification_type
      
  def _set_specification_type(self, v, load=False):
    """
    Setter method for specification_type, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/specification_type (te-bandwidth-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_specification_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_specification_type() directly.

    YANG Description: The method used for settign the bandwidth, either explicitly
specified or configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AUTO': {}, u'SPECIFIED': {}},), default=unicode("SPECIFIED"), is_leaf=True, yang_name="specification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='te-bandwidth-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """specification_type must be of a type compatible with te-bandwidth-type""",
          'defined-type': "openconfig-network-instance:te-bandwidth-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AUTO': {}, u'SPECIFIED': {}},), default=unicode("SPECIFIED"), is_leaf=True, yang_name="specification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='te-bandwidth-type', is_config=False)""",
        })

    self.__specification_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_specification_type(self):
    self.__specification_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AUTO': {}, u'SPECIFIED': {}},), default=unicode("SPECIFIED"), is_leaf=True, yang_name="specification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='te-bandwidth-type', is_config=False)


  def _get_set_bandwidth(self):
    """
    Getter method for set_bandwidth, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/set_bandwidth (oc-mplst:bandwidth-kbps)

    YANG Description: set bandwidth explicitly, e.g., using
offline calculation
    """
    return self.__set_bandwidth
      
  def _set_set_bandwidth(self, v, load=False):
    """
    Setter method for set_bandwidth, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/set_bandwidth (oc-mplst:bandwidth-kbps)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_bandwidth() directly.

    YANG Description: set bandwidth explicitly, e.g., using
offline calculation
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="set-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_bandwidth must be of a type compatible with oc-mplst:bandwidth-kbps""",
          'defined-type': "oc-mplst:bandwidth-kbps",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="set-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)""",
        })

    self.__set_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_bandwidth(self):
    self.__set_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="set-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)


  def _get_signaled_bandwidth(self):
    """
    Getter method for signaled_bandwidth, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/signaled_bandwidth (oc-mplst:bandwidth-kbps)

    YANG Description: The currently signaled bandwidth of the LSP. In the case where
the bandwidth is specified explicitly, then this will match the
value of the set-bandwidth leaf; in cases where the bandwidth is
dynamically computed by the system, the current value of the
bandwidth should be reflected.
    """
    return self.__signaled_bandwidth
      
  def _set_signaled_bandwidth(self, v, load=False):
    """
    Setter method for signaled_bandwidth, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/signaled_bandwidth (oc-mplst:bandwidth-kbps)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_signaled_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_signaled_bandwidth() directly.

    YANG Description: The currently signaled bandwidth of the LSP. In the case where
the bandwidth is specified explicitly, then this will match the
value of the set-bandwidth leaf; in cases where the bandwidth is
dynamically computed by the system, the current value of the
bandwidth should be reflected.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="signaled-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """signaled_bandwidth must be of a type compatible with oc-mplst:bandwidth-kbps""",
          'defined-type': "oc-mplst:bandwidth-kbps",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="signaled-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)""",
        })

    self.__signaled_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_signaled_bandwidth(self):
    self.__signaled_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="signaled-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)

  specification_type = __builtin__.property(_get_specification_type)
  set_bandwidth = __builtin__.property(_get_set_bandwidth)
  signaled_bandwidth = __builtin__.property(_get_signaled_bandwidth)


  _pyangbind_elements = {'specification_type': specification_type, 'set_bandwidth': set_bandwidth, 'signaled_bandwidth': signaled_bandwidth, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/bandwidth/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters related to bandwidth
configuration of TE tunnels
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__specification_type','__set_bandwidth','__signaled_bandwidth',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__specification_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AUTO': {}, u'SPECIFIED': {}},), default=unicode("SPECIFIED"), is_leaf=True, yang_name="specification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='te-bandwidth-type', is_config=False)
    self.__set_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="set-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)
    self.__signaled_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="signaled-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'network-instances', u'network-instance', u'mpls', u'lsps', u'constrained-path', u'tunnels', u'tunnel', u'bandwidth', u'state']

  def _get_specification_type(self):
    """
    Getter method for specification_type, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/specification_type (te-bandwidth-type)

    YANG Description: The method used for settign the bandwidth, either explicitly
specified or configured
    """
    return self.__specification_type
      
  def _set_specification_type(self, v, load=False):
    """
    Setter method for specification_type, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/specification_type (te-bandwidth-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_specification_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_specification_type() directly.

    YANG Description: The method used for settign the bandwidth, either explicitly
specified or configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AUTO': {}, u'SPECIFIED': {}},), default=unicode("SPECIFIED"), is_leaf=True, yang_name="specification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='te-bandwidth-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """specification_type must be of a type compatible with te-bandwidth-type""",
          'defined-type': "openconfig-network-instance:te-bandwidth-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AUTO': {}, u'SPECIFIED': {}},), default=unicode("SPECIFIED"), is_leaf=True, yang_name="specification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='te-bandwidth-type', is_config=False)""",
        })

    self.__specification_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_specification_type(self):
    self.__specification_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'AUTO': {}, u'SPECIFIED': {}},), default=unicode("SPECIFIED"), is_leaf=True, yang_name="specification-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='te-bandwidth-type', is_config=False)


  def _get_set_bandwidth(self):
    """
    Getter method for set_bandwidth, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/set_bandwidth (oc-mplst:bandwidth-kbps)

    YANG Description: set bandwidth explicitly, e.g., using
offline calculation
    """
    return self.__set_bandwidth
      
  def _set_set_bandwidth(self, v, load=False):
    """
    Setter method for set_bandwidth, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/set_bandwidth (oc-mplst:bandwidth-kbps)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_bandwidth() directly.

    YANG Description: set bandwidth explicitly, e.g., using
offline calculation
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="set-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_bandwidth must be of a type compatible with oc-mplst:bandwidth-kbps""",
          'defined-type': "oc-mplst:bandwidth-kbps",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="set-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)""",
        })

    self.__set_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_bandwidth(self):
    self.__set_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="set-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)


  def _get_signaled_bandwidth(self):
    """
    Getter method for signaled_bandwidth, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/signaled_bandwidth (oc-mplst:bandwidth-kbps)

    YANG Description: The currently signaled bandwidth of the LSP. In the case where
the bandwidth is specified explicitly, then this will match the
value of the set-bandwidth leaf; in cases where the bandwidth is
dynamically computed by the system, the current value of the
bandwidth should be reflected.
    """
    return self.__signaled_bandwidth
      
  def _set_signaled_bandwidth(self, v, load=False):
    """
    Setter method for signaled_bandwidth, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/bandwidth/state/signaled_bandwidth (oc-mplst:bandwidth-kbps)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_signaled_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_signaled_bandwidth() directly.

    YANG Description: The currently signaled bandwidth of the LSP. In the case where
the bandwidth is specified explicitly, then this will match the
value of the set-bandwidth leaf; in cases where the bandwidth is
dynamically computed by the system, the current value of the
bandwidth should be reflected.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="signaled-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """signaled_bandwidth must be of a type compatible with oc-mplst:bandwidth-kbps""",
          'defined-type': "oc-mplst:bandwidth-kbps",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="signaled-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)""",
        })

    self.__signaled_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_signaled_bandwidth(self):
    self.__signaled_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="signaled-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-mplst:bandwidth-kbps', is_config=False)

  specification_type = __builtin__.property(_get_specification_type)
  set_bandwidth = __builtin__.property(_get_set_bandwidth)
  signaled_bandwidth = __builtin__.property(_get_signaled_bandwidth)


  _pyangbind_elements = {'specification_type': specification_type, 'set_bandwidth': set_bandwidth, 'signaled_bandwidth': signaled_bandwidth, }


