#!/usr/bin/env python
#-*- coding:utf-8 -*-
""" 此程序用于三线式调温白菜白光的曲线分析和电阻网络阻值选取。
    灵感来自 <http://bbs.mydigit.cn/read.php?tid=985779>
    由网友 <master0123> 写的 《白光T12三线式控温（616控制器）分析》
    
    GUI界面采用Python内置的Tkinter标准库，使用作者自己的TkinterDesigner工具自动生成界面代码。
    <https://github.com/cdhigh/tkinter-designer>
    
    Author：
        cdhigh <https://github.com/cdhigh>
    License:
        The MIT License (MIT)
    第一版完成日期：
        2015-08-13
"""

__Version__ = '0.1'

import os, sys
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()


#N型电压转温度系数 
#用于通过电压计算温度
Var_VtoT_N = ( 
    (0, 3.8436847e1, 1.1010485, 5.2229312, 7.2060525, 5.8488586, 
        2.7754916, 7.7075166/1e1, 1.1582665/1e1, 7.3138868/1e3), 
    (0, 3.86896e1, -1.08267, 4.70205/1e2, -2.12169/1e6, -1.17272/1e4,
        5.39280/1e6, -7.98156/1e8), 
    (1.972485e1, 3.300943e1, -3.915159/1e1, 9.855391/1e3, 
        -1.274371/1e4, 7.767022/1e7),)
    
#白菜白光电路图GIF数据
schData = """
            R0lGODlhHwMoAfcAAAAAAIAAAACAAICAAAAAgIAAgACAgICAgMDcwKbK8Co/qio//ypf
            ACpfVSpfqipf/yp/ACp/VSp/qip//yqfACqfVSqfqiqf/yq/ACq/VSq/qiq//yrfACrf
            VSrfqirf/yr/ACr/VSr/qir//1UAAFUAVVUAqlUA/1UfAFUfVVUfqlUf/1U/AFU/VVU/
            qlU//1VfAFVfVVVfqlVf/1V/AFV/VVV/qlV//1WfAFWfVVWfqlWf/1W/AFW/VVW/qlW/
            /1XfAFXfVVXfqlXf/1X/AFX/VVX/qlX//38AAH8AVX8Aqn8A/38fAH8fVX8fqn8f/38/
            AH8/VX8/qn8//39fAH9fVX9fqn9f/39/AH9/VX9/qn9//3+fAH+fVX+fqn+f/3+/AH+/
            VX+/qn+//3/fAH/fVX/fqn/f/3//AH//VX//qn///6oAAKoAVaoAqqoA/6ofAKofVaof
            qqof/6o/AKo/Vao/qqo//6pfAKpfVapfqqpf/6p/AKp/Vap/qqp//6qfAKqfVaqfqqqf
            /6q/AKq/Vaq/qqq//6rfAKrfVarfqqrf/6r/AKr/Var/qqr//9QAANQAVdQAqtQA/9Qf
            ANQfVdQfqtQf/9Q/ANQ/VdQ/qtQ//9RfANRfVdRfqtRf/9R/ANR/VdR/qtR//9SfANSf
            VdSfqtSf/9S/ANS/VdS/qtS//9TfANTfVdTfqtTf/9T/ANT/VdT/qtT///8AVf8Aqv8f
            AP8fVf8fqv8f//8/AP8/Vf8/qv8///9fAP9fVf9fqv9f//9/AP9/Vf9/qv9///+fAP+f
            Vf+fqv+f//+/AP+/Vf+/qv+////fAP/fVf/fqv/f////Vf//qszM///M/zP//2b//5n/
            /8z//wB/AAB/VQB/qgB//wCfAACfVQCfqgCf/wC/AAC/VQC/qgC//wDfAADfVQDfqgDf
            /wD/VQD/qioAACoAVSoAqioA/yofACofVSofqiof/yo/ACo/Vf/78KCgpICAgP8AAAD/
            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
            l15+CWaYYgZpyJhmnommiwEBADs"""
   
class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('白菜白光三线式调温电路分析软件 [cdhigh]')
        self.master.resizable(0,0)
        self.icondata = """
            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"""
        self.iconimg = PhotoImage(data=self.icondata)
        self.master.tk.call('wm', 'iconphoto', self.master._w, self.iconimg)
        # To center the window on the screen.
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (837 / 2)
        y = (hs / 2) - (642 / 2)
        self.master.geometry('%dx%d+%d+%d' % (837,642,x,y))
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.frameDesgin = LabelFrame(self.top, text='参数设计')
        self.frameDesgin.place(relx=0.478, rely=0.498, relwidth=0.508, relheight=0.488)

        self.cavCurve = Canvas(self.top, takefocus=1)
        self.cavCurve.place(relx=0.019, rely=0.498, relwidth=0.45, relheight=0.488)

        self.cavSch = Canvas(self.top, takefocus=1)
        self.cavSch.place(relx=0.019, rely=0.012, relwidth=0.959, relheight=0.467)

        self.txtTips = Text(self.frameDesgin, bg='#FFFFC0')
        self.txtTips.place(relx=0.64, rely=0.179, relwidth=0.322, relheight=0.796)
        self.txtTips.insert('1.0','')

        self.txtMinVolVar = StringVar(value='')
        self.txtMinVol = Entry(self.frameDesgin, textvariable=self.txtMinVolVar)
        self.txtMinVol.place(relx=0.376, rely=0.534, relwidth=0.209, relheight=0.058)

        self.txtMaxVolVar = StringVar(value='')
        self.txtMaxVol = Entry(self.frameDesgin, textvariable=self.txtMaxVolVar)
        self.txtMaxVol.place(relx=0.376, rely=0.63, relwidth=0.209, relheight=0.058)

        self.cmdDrawCurve = Button(self.frameDesgin, text='绘制调温曲线', command=self.cmdDrawCurve_Cmd)
        self.cmdDrawCurve.place(relx=0.64, rely=0.051, relwidth=0.322, relheight=0.105)

        self.txtMaxTempVar = StringVar(value='')
        self.txtMaxTemp = Entry(self.frameDesgin, textvariable=self.txtMaxTempVar)
        self.txtMaxTemp.place(relx=0.376, rely=0.823, relwidth=0.209, relheight=0.058)

        self.txtMinTempVar = StringVar(value='')
        self.txtMinTemp = Entry(self.frameDesgin, textvariable=self.txtMinTempVar)
        self.txtMinTemp.place(relx=0.376, rely=0.727, relwidth=0.209, relheight=0.058)

        self.txtR10Var = StringVar(value='56000')
        self.txtR10 = Entry(self.frameDesgin, textvariable=self.txtR10Var)
        self.txtR10.place(relx=0.376, rely=0.437, relwidth=0.209, relheight=0.058)

        self.txtR9Var = StringVar(value='51')
        self.txtR9 = Entry(self.frameDesgin, textvariable=self.txtR9Var)
        self.txtR9.place(relx=0.376, rely=0.341, relwidth=0.209, relheight=0.058)

        self.txtR8Var = StringVar(value='43000')
        self.txtR8 = Entry(self.frameDesgin, textvariable=self.txtR8Var)
        self.txtR8.place(relx=0.376, rely=0.244, relwidth=0.209, relheight=0.058)

        self.txtRTVar = StringVar(value='10000')
        self.txtRT = Entry(self.frameDesgin, textvariable=self.txtRTVar)
        self.txtRT.place(relx=0.376, rely=0.148, relwidth=0.209, relheight=0.058)

        self.txtVCCVar = StringVar(value='5.0')
        self.txtVCC = Entry(self.frameDesgin, textvariable=self.txtVCCVar)
        self.txtVCC.place(relx=0.376, rely=0.051, relwidth=0.209, relheight=0.058)

        self.style.configure('TlblMinVol.TLabel', anchor='e')
        self.lblMinVol = Label(self.frameDesgin, text='最小参考电压 (mV)', style='TlblMinVol.TLabel')
        self.lblMinVol.place(relx=0.038, rely=0.534, relwidth=0.304, relheight=0.054)

        self.style.configure('TlblMaxVol.TLabel', anchor='e')
        self.lblMaxVol = Label(self.frameDesgin, text='最大参考电压 (mV)', style='TlblMaxVol.TLabel')
        self.lblMaxVol.place(relx=0.038, rely=0.63, relwidth=0.304, relheight=0.054)

        self.style.configure('TlblMaxTemp.TLabel', anchor='e')
        self.lblMaxTemp = Label(self.frameDesgin, text='最高温度 (c)', style='TlblMaxTemp.TLabel')
        self.lblMaxTemp.place(relx=0.038, rely=0.823, relwidth=0.304, relheight=0.054)

        self.style.configure('TlblMinTemp.TLabel', anchor='e')
        self.lblMinTemp = Label(self.frameDesgin, text='最低温度 (c)', style='TlblMinTemp.TLabel')
        self.lblMinTemp.place(relx=0.038, rely=0.727, relwidth=0.304, relheight=0.054)

        self.style.configure('TlblR10.TLabel', anchor='e')
        self.lblR10 = Label(self.frameDesgin, text='电阻R10 (ohm)', style='TlblR10.TLabel')
        self.lblR10.place(relx=0.038, rely=0.437, relwidth=0.304, relheight=0.054)

        self.style.configure('TlblR9.TLabel', anchor='e')
        self.lblR9 = Label(self.frameDesgin, text='电阻R9 (ohm)', style='TlblR9.TLabel')
        self.lblR9.place(relx=0.038, rely=0.341, relwidth=0.304, relheight=0.054)

        self.style.configure('TlblR8.TLabel', anchor='e')
        self.lblR8 = Label(self.frameDesgin, text='电阻R8 (ohm)', style='TlblR8.TLabel')
        self.lblR8.place(relx=0.038, rely=0.244, relwidth=0.304, relheight=0.054)

        self.style.configure('TlblRT.TLabel', anchor='e')
        self.lblRT = Label(self.frameDesgin, text='电位器RT (ohm)', style='TlblRT.TLabel')
        self.lblRT.place(relx=0.038, rely=0.148, relwidth=0.304, relheight=0.054)

        self.style.configure('TlblVCC.TLabel', anchor='e')
        self.lblVCC = Label(self.frameDesgin, text='运放电压VCC (V)', style='TlblVCC.TLabel')
        self.lblVCC.place(relx=0.038, rely=0.051, relwidth=0.304, relheight=0.054)

        self.style.configure('TlblTempFormula.TLabel', anchor='e')
        self.lblTempFormula = Label(self.frameDesgin, text='温度计算公式', style='TlblTempFormula.TLabel')
        self.lblTempFormula.place(relx=0.038, rely=0.92, relwidth=0.304, relheight=0.054)

        self.cmbTempFormulaList = ['线性化计算','0.0157mV/℃',]
        self.cmbTempFormulaVar = StringVar(value='线性化计算')
        self.cmbTempFormula = Combobox(self.frameDesgin, state='readonly', text='线性化计算', textvariable=self.cmbTempFormulaVar, values=self.cmbTempFormulaList)
        self.cmbTempFormula.place(relx=0.376, rely=0.92, relwidth=0.209)

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.master.title('白菜白光三线式调温电路分析软件 v%s [cdhigh]' % __Version__)
        self.cmbTempFormula.current(0)
        self.schImg = PhotoImage(data=schData)
        self.cavSch.create_image(0,0, image=self.schImg, anchor=NW)
        self.txtTips.insert('1.0','1. 运放电压、电位器、几个电阻的值必须填写；\n'
            '2. 红线为理想的调温曲线，黑线为实际的调温曲线；\n'
            '3. 横坐标为电位器旋转角度，纵坐标为T12热电偶温度；\n'
            '4. 温度计算假定室温为零度；\n'
            '5. 因T12热电偶类型不明，温度值仅供参考，关注参考电压值即可。')
        self.txtTips['state'] = 'disabled'
        
    def cmdCalR8R9R10_Cmd(self, event=None):
        self.DrawCurveInCanvas(list(range(120, 500, 1)))
    
    #根据各项参数设置，绘出调温曲线
    def cmdDrawCurve_Cmd(self, event=None):
        try:
            VCC = float(self.txtVCCVar.get())
            Rt = int(self.txtRTVar.get())
            R8 = int(self.txtR8Var.get())
            R9 = int(self.txtR9Var.get())
            R10 = int(self.txtR10Var.get())
        except Exception as e:
            showinfo('出错啦', '请先正确填写各项参数值：\n\n' + str(e))
            self.txtRT.focus_set()
            return
        
        vrefList = CalVrefList(VCC, Rt, R8, R9, R10)
        maxVref = max(vrefList)
        if maxVref >= 0.047533:
            showinfo('出错啦', '你设置的参数可能有误，计算出的最高温度已经超过热电偶的最大工作温度！')
        
        if self.cmbTempFormula.current() == 0:
            t12TempList = list(map(N_VtoT, vrefList))
        else:
            t12TempList = list(map(N_VtoT_Liner, vrefList))
        self.txtMinVolVar.set('%0.1f' % (min(vrefList) * 1000))
        self.txtMaxVolVar.set('%0.1f' % (maxVref * 1000))
        self.txtMinTempVar.set(str(int(min(t12TempList))))
        self.txtMaxTempVar.set(str(int(max(t12TempList))))
        self.DrawCurveInCanvas(t12TempList)
    
    #在Canvas上画出电压和电位器旋转角度的函数曲线图
    #传入参数中的列表为按照一定固定步进的从小到大的温度值
    def DrawCurveInCanvas(self, t12TempList):
        TextMargin = 10 #坐标文字离边缘距离
        MarginX = 20 #X坐标轴离canvas边缘像素距离
        MarginY = 40 #Y坐标轴离canvas边缘像素距离
        
        cav = self.cavCurve
        cav.delete('all')
        cavW = int(cav.winfo_width())
        cavH = int(cav.winfo_height())
        
        minTemp = min(t12TempList)
        maxTemp = max(t12TempList)
        
        #先画X/Y坐标轴
        orgX = MarginY
        orgY = cavH - MarginX
        YAxisLength = cavH - TextMargin - MarginX
        XAxisLength = cavW - TextMargin - MarginY
        cav.create_rectangle(orgX, TextMargin, cavW - TextMargin, orgY, outline='gray')
        
        #画坐标刻度
        #温度刻度间隔为50度，初始温度设定为最低温度下取整为一百度的值
        #最高温度刻度设定为最大温度上取整为一百度的值
        tempStart = int(minTemp / 100) * 100
        tempEnd = (int(maxTemp / 100) + 1) * 100
        tempPixelsStep = YAxisLength / ((tempEnd - tempStart) / 50)
        pixelsPerDegree = YAxisLength / (tempEnd - tempStart)
        tempRulerY = orgY
        for tmp in range(tempStart, tempEnd + 49, 50):
            cav.create_line(orgX, tempRulerY, orgX + XAxisLength, tempRulerY, fill='gray', dash=(2,5))
            cav.create_text(TextMargin, tempRulerY, text=str(int(tmp)), anchor=W)
            tempRulerY -= tempPixelsStep
        
        #角度刻度固定为10分度，每个刻度为0.1步进
        anglePixelsStep = XAxisLength / 10
        angleRulerX = orgX
        for angle in ('0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0'):
            cav.create_line(angleRulerX, orgY, angleRulerX, orgY - YAxisLength, fill='gray', dash=(2,5))
            cav.create_text(angleRulerX, cavH - TextMargin, text=angle, anchor=CENTER)
            angleRulerX += anglePixelsStep
        
        #内嵌函数，给定一个温度（在合法区间内），返回对应的Y轴坐标位置
        def tempY(temp):
            return orgY - (temp - tempStart) * pixelsPerDegree
        
        #内嵌函数，给定一个电位器旋转角度（0.0~1.0浮点），返回对应的X轴坐标位置
        def angleX(angle):
            return orgX + angle * XAxisLength
            
        #画一条理想调温直线，连接开始温度和结束温度
        cav.create_line(orgX, tempY(minTemp), angleX(1), tempY(maxTemp), fill='red')
        
        #开始画实际的调温曲线
        step = (100 / len(t12TempList)) / 100
        angle = 0.0
        prevX = orgX
        prevY = tempY(minTemp)
        for temp in t12TempList:
            currX = angleX(angle)
            currY = tempY(temp)
            cav.create_line(prevX, prevY, currX, currY)
            angle += step
            prevX = currX
            prevY = currY
        
        #最后一段
        cav.create_line(prevX, prevY, angleX(1), tempY(maxTemp))
        
#根据输入的电压和电阻阻值，将电位器从最小到最大按1%步进时各档的热电偶对应温度值计算出来，
#返回一个包含101个元素的列表
def CalT12TempList(VCC, Rt, R8, R9, R10):
    VrefList = CalVrefList(VCC, Rt, R8, R9, R10)
    return list(map(N_VtoT, VrefList))
    
#根据输入的电压和电阻阻值，将电位器从最小到最大步进1%的各档参考电压计算出来，
#返回一个包含101个元素的列表
def CalVrefList(VCC, Rt, R8, R9, R10):
    VrefList = []
    Rdown = Rup = 0.0 #分别为串并联后的上电阻和下电阻
    for pos in range(0, 101):
        Rt1 = Rt * pos / 100 #电位器中点到地电阻
        Rt2 = Rt - Rt1
        if Rt1 == 0:
            Rdown = R8 * R9 / (R8 + R9)
            Rup = R10
        elif Rt2 == 0:
            Rdown = R9
            Rup = R8 * R10 / (R8 + R10)
        else:
            RSumProduct = Rt1 * R8 + R8 * Rt2 + Rt1 * Rt2
            Rw1 = RSumProduct / Rt1
            Rw2 = RSumProduct / Rt2
            Rdown = Rw2 * R9 / (Rw2 + R9)
            Rup = Rw1 * R10 / (Rw1 + R10)
        
        Vref = VCC * Rdown / (Rdown + Rup)
        VrefList.append(Vref)
    return VrefList

#简单的按照一个常量（0.0157mV/℃）转换电压到温度，（假定室温为0度）
def N_VtoT_Liner(Vref):
    return Vref * 1000 / 0.0157
    
#N型热电偶电压转温度（假定室温为0度）
def N_VtoT(Vref):
    mV = Vref * 1000 #转成毫伏
    if -4.365 <= mV < 0:
        value = Var_VtoT_N[0][9]
        for i in range(9, 0, -1):
            value = mV * value + Var_VtoT_N[0][i - 1]
    elif 0 <= mV < 20.613:
        value = Var_VtoT_N[1][7]
        for i in range(7, 0, -1):
            value = mV * value + Var_VtoT_N[1][i - 1] 
    elif 20.613 <= mV <= 47.533:
        value = Var_VtoT_N[2][5]
        for i in range(5, 0, -1):
            value = mV * value + Var_VtoT_N[2][i - 1] 
    else:
        value = 1300 #简单的容错而已，此范围的温度已经超过了热电偶工作温度
        
    return value
    
if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

