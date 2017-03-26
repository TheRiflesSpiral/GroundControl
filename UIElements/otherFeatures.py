from kivy.uix.screenmanager                 import Screen
from kivy.properties                        import ObjectProperty
from DataStructures.makesmithInitFuncs      import MakesmithInitFuncs


class OtherFeatures(Screen, MakesmithInitFuncs):
    viewmenu = ObjectProperty(None) #make viewmenu object accessible at this scope
    cancel   = ObjectProperty(None)
    
    def setUpData(self, data):
        self.data = data
        self.viewmenu.setUpData(data)
        self.connectmenu.setUpData(data)
        self.diagnostics.setUpData(data)
        self.connectmenu.updatePorts()