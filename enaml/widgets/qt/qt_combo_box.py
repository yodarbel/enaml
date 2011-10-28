#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .qt import QtGui
from .qt_control import QtControl

from ..combo_box import AbstractTkComboBox


class QtComboBox(QtControl, AbstractTkComboBox):
    """ A Qt implementation of ComboBox.

    Use a combo box to select a single item from a collection of items. 

    """
    #--------------------------------------------------------------------------
    # Setup methods
    #--------------------------------------------------------------------------
    def create(self):
        """ Creates a QComboBox.

        """
        self.widget = QtGui.QComboBox(self.parent_widget())

    def initialize(self):
        """ Intializes the widget with the attributes of this instance.

        """
        super(QtComboBox, self).initialize()
        self.update_items()

    def bind(self):
        """ Connects the event handlers for the combo box.

        """
        super(QtComboBox, self).bind()
        self.widget.currentIndexChanged.connect(self.on_selected)
        
    #--------------------------------------------------------------------------
    # Implementation
    #--------------------------------------------------------------------------
    def shell_value_changed(self, value):
        """ The change handler for the 'value' attribute on the 
        shell widget.

        """
        self.set_value(self.shell_obj.to_string(value))

    def shell_to_string_changed(self, value):
        """ The change handler for the 'string' attribute on the 
        shell widget.

        """
        self.update_items()
    
    def shell_items_changed(self, items):
        """ The change handler of the 'items' attribute on the shell
        widget.

        """
        self.update_items()

    def shell_items_items_changed(self, items):
        """ The change handler for the 'items' event of the 'items'
        attribute on the shell widget.
        
        """
        self.update_items()

    def update_items(self):
        """ Update the QComboBox with items from the shell widget.
        
        """
        shell = self.shell_obj
        self.set_items(shell._labels)
        self.set_selection(shell._index)

    def on_selected(self, index):
        """ The event handler for a combo box selection event.

        """
        shell = self.shell_obj
        value = shell.items[index]
        if value != shell.value:
            shell._index = index

    def set_items(self, str_items):
        """ Sets the items in the combo box.

        """
        widget = self.widget
        widget.clear()
        widget.addItems(str_items)

    def set_selection(self, index):
        """ Sets the value in the combo box, or resets the combo box
        if the value is not in the list of items.

        """
        widget = self.widget
        widget.setCurrentIndex(index)

