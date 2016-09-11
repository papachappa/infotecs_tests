# -*- coding: utf-8 -*-
import pywinauto
from pywinauto import application
import pywinauto.handleprops as _handleprops
import pywinauto.win32functions as _win32functions
import time
#c:\totalcmd\totalcmd.exe
path = 'cmd'
app=application.Application()
app.Start(path)

w_handle = pywinauto.findwindows.find_windows(title_re=u'.*')[0]
window = app.window_()[0]
print w_handle
print window

#hwnd = _win32functions.GetForegroundWindow()
#print "Active Window title is %s"%(_handleprops.text(w_handle))
#print "Application name is %s"%(pywinauto.application.process_module(_handleprops.processid(hwnd)))
# time.sleep(1)
# app.dialogs.MenuSelect("File->Exit")
# #app.dlg.MenuSelect("Document->Open")
# window.MenuItem(u'Файл->Выход').Click()

