import wx

ID_SPIN_DOMAIN = 1000
ID_SPIN_TYPE = 1001
ID_SPIN_LENGTH = 1002

ID_TOOL_ZOOM_OUT = 1101
ID_TOOL_ZOOM_IN = 1102

MAX_DOMAIN = 0x07
MAX_TYPE = 0xFF
MAX_LENGTH = 0xFF


class SpinnerPanel(wx.Panel):
    def __init__(self, parent, level_view_ref):
        super(SpinnerPanel, self).__init__(parent)

        self.level_view_ref = level_view_ref

        self.toolbar = wx.ToolBar(self)
        self.toolbar.AddTool(
            ID_TOOL_ZOOM_OUT,
            "Zoom out",
            wx.ArtProvider.GetBitmap(id=wx.ART_MINUS, client=wx.ART_TOOLBAR),
        )
        self.toolbar.AddTool(
            ID_TOOL_ZOOM_IN,
            "Zoom in",
            wx.ArtProvider.GetBitmap(id=wx.ART_PLUS, client=wx.ART_TOOLBAR),
        )

        self.toolbar.Realize()

        self.panel_sizer = wx.BoxSizer(wx.VERTICAL)

        self.spin_domain = wx.SpinCtrl(self, ID_SPIN_DOMAIN, max=MAX_DOMAIN)
        self.spin_domain.SetBase(16)
        self.spin_domain.Enable(False)
        self.spin_type = wx.SpinCtrl(self, ID_SPIN_TYPE, max=MAX_TYPE)
        self.spin_type.SetBase(16)
        self.spin_type.Enable(False)
        self.spin_length = wx.SpinCtrl(self, ID_SPIN_LENGTH, max=MAX_LENGTH)
        self.spin_length.SetBase(16)
        self.spin_length.Enable(False)

        spinner_sizer = wx.FlexGridSizer(cols=2, vgap=0, hgap=0)
        spinner_sizer.AddGrowableCol(0)

        spinner_sizer.Add(
            wx.StaticText(self, label="Bank/Domain: "),
            flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT,
        )
        spinner_sizer.Add(self.spin_domain)
        spinner_sizer.Add(
            wx.StaticText(self, label="Type: "),
            flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT,
        )
        spinner_sizer.Add(self.spin_type)
        spinner_sizer.Add(
            wx.StaticText(self, label="Length: "),
            flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT,
        )
        spinner_sizer.Add(self.spin_length)

        self.panel_sizer.Add(self.toolbar)
        self.panel_sizer.Add(spinner_sizer)

        self.SetSizerAndFit(self.panel_sizer)

        self.Bind(wx.EVT_TOOL, self.on_toolbox)

    def on_toolbox(self, event):
        tool_id = event.GetId()

        if tool_id == ID_TOOL_ZOOM_OUT:
            self.level_view_ref.zoom_out()
        elif tool_id == ID_TOOL_ZOOM_IN:
            self.level_view_ref.zoom_in()

    def get_type(self):
        return self.spin_type.GetValue()

    def set_type(self, type):
        self.spin_type.SetValue(type)

    def get_domain(self):
        return self.spin_domain.GetValue()

    def set_domain(self, domain):
        self.spin_domain.SetValue(domain)

    def get_length(self):
        return self.spin_length.GetValue()

    def set_length(self, length):
        self.spin_length.SetValue(length)

    def enable_type(self, enable, value=0):
        self.spin_type.SetValue(value)
        self.spin_type.Enable(enable)

    def enable_domain(self, enable, value=0):
        self.spin_domain.SetValue(value)
        self.spin_domain.Enable(enable)

    def enable_length(self, enable, value=0):
        self.spin_length.SetValue(value)
        self.spin_length.Enable(enable)

    def disable_all(self):
        self.enable_type(False)
        self.enable_domain(False)
        self.enable_length(False)

    def is_length_spinner(self, id):
        return id == ID_SPIN_LENGTH