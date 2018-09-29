import wx

class MyFrame(wx.Frame):
	def _init_(self):
		wx.Frame._init_(self,None,
			pos=wx.DefaultPosition, size=wx.Size(450, 100),
			style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
			wx.CLOSE_BOX | wx.CLIP_CHILDREN,
			title="GUI")
		panel = wx.Panel(self)
		my_sizer = wx.BoxSizer(wx.VERTICAL)
		lbl = wx.StaticText(panel,
		label = "Hello, This is Nandishwar's Python Based Digital Assistant. How can I help you?")
		my_sizer.Add(lbl,0,wx.ALL, 5)
		self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
		self.txt.SetFocus()
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
		my_sizer.Add(self.txt,0,wx.ALL, 5)
		panel.SetSizer(my_sizer)
		self.Show()

	def OnEnter(self, event):
		input = self.txt.GetValue()
		input = input.lower()
		print("Hurrah! It worked.")

if __name__ == "__main__":
	app = wx.App(True)
	frame = MyFrame()
	app.MainLoop()
