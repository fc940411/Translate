# encode:utf-8

import wx
import Translate
import requests


class MyFrame(wx.Frame):
    def __init__(self,parent,id=wx.ID_ANY,title='',
                 pos=wx.DefaultPosition,size=(800,300),
                 style=wx.DEFAULT_FRAME_STYLE,
                 name='MyFrame'):
        super(MyFrame,self).__init__(parent,id,title,pos,size,style,name)
        # 创建画板
        self.panel = wx.Panel(self)
        # 创建标题
        in_title = wx.StaticText(self.panel, label='中英文翻译', pos=(200, 20), style=wx.ALIGN_CENTER, size=(400, 20))
        font = wx.Font(18, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        in_title.SetFont(font)

        # 创建输入文本框
        words_title = wx.StaticText(self.panel, label='请输入需要翻译的内容:', pos=(200, 70), style=0, size=(400, 20))
        words_font = wx.Font(12, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        words_title.SetFont(words_font)
        self.words = wx.TextCtrl(self.panel, pos = (200, 100), size=(400,30), style=wx.TE_PROCESS_ENTER)
        self.words.Bind(wx.EVT_TEXT, self.Trans)

        # 创建输出结果
        answer_title = wx.StaticText(self.panel, label='翻译结果:', pos=(200, 170), style=0, size=(400, 20))
        answer_font = wx.Font(12, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        answer_title.SetFont(answer_font)
        self.answer = wx.StaticText(self.panel, label='', pos=(200, 220), style=wx.ALIGN_CENTER, size=(400, 20))
        self.answer.SetFont(answer_font)

        # 创建翻译按钮
        # self.button = wx.Button(self.panel, label='翻译', pos=(350,300), size=(100,40))
        # self.button.Bind(wx.EVT_BUTTON, self.Trans

    def Trans(self, event):
        '''创建翻译事件'''
        text = self.words.GetValue()
        res = Translate.YoudaoFanyi(text).run()
        if res:
            self.answer.SetLabel(res)
        else:
            self.answer.SetLabel('')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='翻译')
    frame.Show()
    app.MainLoop()
