from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_1.items=anvil.server.call('getticker')

    # Any code you write here will run before the form opens.

  def drop_down_1_show(self, **event_args):
    ticker=self.drop_down_1.selected_value
    self.text_box_1.text=ticker
    self.text_box_2.text=anvil.server.call('getPrice',ticker)
    """This method is called when the DropDown is shown on the screen"""
    #alert('you selected a stock' + " " +self.drop_down_1.selected_value)
