
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/global/lsp-bit/attached-bit/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state for Link State PDU Bit.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ignore_bit','__suppress_bit',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__suppress_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__ignore_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'lsp-bit', u'attached-bit', u'state']

  def _get_ignore_bit(self):
    """
    Getter method for ignore_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit/state/ignore_bit (boolean)

    YANG Description: When set to true, if the attached bit is set on an incoming Level 1
IS-IS, the local system ignores it. In this case the local system
does not set a default route to the L1L2 router advertising the PDU
with the attached bit set.
    """
    return self.__ignore_bit
      
  def _set_ignore_bit(self, v, load=False):
    """
    Setter method for ignore_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit/state/ignore_bit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ignore_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ignore_bit() directly.

    YANG Description: When set to true, if the attached bit is set on an incoming Level 1
IS-IS, the local system ignores it. In this case the local system
does not set a default route to the L1L2 router advertising the PDU
with the attached bit set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ignore_bit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__ignore_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ignore_bit(self):
    self.__ignore_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_suppress_bit(self):
    """
    Getter method for suppress_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit/state/suppress_bit (boolean)

    YANG Description: When set to true, if the local IS acts as a L1L2 router, then the
attached bit is not advertised in locally generated PDUs.
    """
    return self.__suppress_bit
      
  def _set_suppress_bit(self, v, load=False):
    """
    Setter method for suppress_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit/state/suppress_bit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_bit() directly.

    YANG Description: When set to true, if the local IS acts as a L1L2 router, then the
attached bit is not advertised in locally generated PDUs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_bit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__suppress_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_bit(self):
    self.__suppress_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  ignore_bit = __builtin__.property(_get_ignore_bit)
  suppress_bit = __builtin__.property(_get_suppress_bit)


  _pyangbind_elements = {'ignore_bit': ignore_bit, 'suppress_bit': suppress_bit, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/global/lsp-bit/attached-bit/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state for Link State PDU Bit.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ignore_bit','__suppress_bit',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__suppress_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    self.__ignore_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'global', u'lsp-bit', u'attached-bit', u'state']

  def _get_ignore_bit(self):
    """
    Getter method for ignore_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit/state/ignore_bit (boolean)

    YANG Description: When set to true, if the attached bit is set on an incoming Level 1
IS-IS, the local system ignores it. In this case the local system
does not set a default route to the L1L2 router advertising the PDU
with the attached bit set.
    """
    return self.__ignore_bit
      
  def _set_ignore_bit(self, v, load=False):
    """
    Setter method for ignore_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit/state/ignore_bit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ignore_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ignore_bit() directly.

    YANG Description: When set to true, if the attached bit is set on an incoming Level 1
IS-IS, the local system ignores it. In this case the local system
does not set a default route to the L1L2 router advertising the PDU
with the attached bit set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ignore_bit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__ignore_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ignore_bit(self):
    self.__ignore_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_suppress_bit(self):
    """
    Getter method for suppress_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit/state/suppress_bit (boolean)

    YANG Description: When set to true, if the local IS acts as a L1L2 router, then the
attached bit is not advertised in locally generated PDUs.
    """
    return self.__suppress_bit
      
  def _set_suppress_bit(self, v, load=False):
    """
    Setter method for suppress_bit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/global/lsp_bit/attached_bit/state/suppress_bit (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_bit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_bit() directly.

    YANG Description: When set to true, if the local IS acts as a L1L2 router, then the
attached bit is not advertised in locally generated PDUs.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_bit must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__suppress_bit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_bit(self):
    self.__suppress_bit = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="suppress-bit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

  ignore_bit = __builtin__.property(_get_ignore_bit)
  suppress_bit = __builtin__.property(_get_suppress_bit)


  _pyangbind_elements = {'ignore_bit': ignore_bit, 'suppress_bit': suppress_bit, }


