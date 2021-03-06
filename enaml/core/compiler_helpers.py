#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .declarative import Declarative
from .enaml_def import EnamlDef


def _make_enamldef_helper_(name, base, description, f_globals):
    """ A compiler helper function for creating a new EnamlDef type.

    This function is called by the bytecode generated by the Enaml
    compiler when an enaml module is imported. It is used to make new
    types from the 'enamldef' keyword.

    This helper will raise an exception if the base type is of an
    incompatible type.

    Parameters
    ----------
    name : str
        The name to use when generating the new type.

    base : type
        The base class to use for the new type. This must be a subclass
        of Declarative.

    description : dict
        The description dictionay by the Enaml compiler. This dict will
        be used during instantiation to populate new instances with
        children and bound expressions.

    f_globals : dict
        The dictionary of globals for objects created by this class.

    Returns
    -------
    result : EnamlDef
        A new enamldef subclass of the given base class.

    """
    if not isinstance(base, type) or not issubclass(base, Declarative):
        msg = "can't derive enamldef from '%s'"
        raise TypeError(msg % base)
    dct = {
        '__module__': f_globals.get('__name__', ''),
        '__doc__': description.get('__doc__', ''),
    }
    decl_cls = EnamlDef(name, (base,), dct)
    decl_cls._descriptions += ((description, f_globals),)
    return decl_cls

