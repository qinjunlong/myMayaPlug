from MyPlug.QTdesigner import widget
import importlib

importlib.reload(widget)
UI = widget.TRSConnectorWindow()
UI.show()