VERSION 5.00
Begin VB.Form frmMain 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "白菜白光三线式调温电路设计软件 [cdhigh]"
   ClientHeight    =   9900
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   12420
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   9900
   ScaleWidth      =   12420
   StartUpPosition =   2  '屏幕中心
   Tag             =   "p@icon=icon.gif"
   Begin VB.Frame frameDesgin 
      Caption         =   "参数设计"
      Height          =   5055
      Left            =   5880
      TabIndex        =   2
      Top             =   4680
      Width           =   6375
      Begin VB.ComboBox cmbSortPolicy 
         Height          =   300
         ItemData        =   "frmMain.frx":0000
         Left            =   4080
         List            =   "frmMain.frx":0013
         Style           =   2  'Dropdown List
         TabIndex        =   26
         Tag             =   "p@bindcommand=<<ComboboxSelected>>"
         Top             =   1440
         Width           =   2055
      End
      Begin VB.ListBox lstBestChoices 
         Height          =   3120
         Left            =   4080
         TabIndex        =   25
         Tag             =   "p@bindcommand=<Double-Button-1>"
         Top             =   1800
         Width           =   2055
      End
      Begin VB.CommandButton cmdBestChoices 
         Caption         =   "为我推荐"
         Height          =   495
         Left            =   4080
         TabIndex        =   24
         Top             =   840
         Width           =   2055
      End
      Begin VB.ComboBox cmbTempFormula 
         Height          =   300
         ItemData        =   "frmMain.frx":0074
         Left            =   2400
         List            =   "frmMain.frx":007E
         Style           =   2  'Dropdown List
         TabIndex        =   23
         Top             =   4680
         Width           =   1335
      End
      Begin VB.TextBox txtMinVol 
         Height          =   270
         Left            =   2400
         TabIndex        =   15
         Top             =   2705
         Width           =   1335
      End
      Begin VB.TextBox txtMaxVol 
         Height          =   270
         Left            =   2400
         TabIndex        =   16
         Top             =   3198
         Width           =   1335
      End
      Begin VB.CommandButton cmdDrawCurve 
         Caption         =   "绘制调温曲线"
         Height          =   495
         Left            =   4080
         TabIndex        =   19
         Top             =   240
         Width           =   2055
      End
      Begin VB.TextBox txtMaxTemp 
         Height          =   270
         Left            =   2400
         TabIndex        =   18
         Top             =   4184
         Width           =   1335
      End
      Begin VB.TextBox txtMinTemp 
         Height          =   270
         Left            =   2400
         TabIndex        =   17
         Top             =   3691
         Width           =   1335
      End
      Begin VB.TextBox txtR10 
         Height          =   270
         Left            =   2400
         TabIndex        =   14
         Text            =   "56k"
         Top             =   2212
         Width           =   1335
      End
      Begin VB.TextBox txtR9 
         Height          =   270
         Left            =   2400
         TabIndex        =   13
         Text            =   "51"
         Top             =   1719
         Width           =   1335
      End
      Begin VB.TextBox txtR8 
         Height          =   270
         Left            =   2400
         TabIndex        =   12
         Text            =   "43k"
         Top             =   1226
         Width           =   1335
      End
      Begin VB.TextBox txtRT 
         Height          =   270
         Left            =   2400
         TabIndex        =   11
         Text            =   "10k"
         Top             =   733
         Width           =   1335
      End
      Begin VB.TextBox txtVCC 
         Height          =   270
         Left            =   2400
         TabIndex        =   10
         Text            =   "5.0"
         Top             =   240
         Width           =   1335
      End
      Begin VB.Label lblTempFormula 
         Alignment       =   1  'Right Justify
         Caption         =   "温度计算公式"
         Height          =   255
         Left            =   240
         TabIndex        =   22
         Top             =   4680
         Width           =   1935
      End
      Begin VB.Label lblMinVol 
         Alignment       =   1  'Right Justify
         Caption         =   "最小参考电压 (mV)"
         Height          =   255
         Left            =   240
         TabIndex        =   21
         Top             =   2705
         Width           =   1935
      End
      Begin VB.Label lblMaxVol 
         Alignment       =   1  'Right Justify
         Caption         =   "最大参考电压 (mV)"
         Height          =   255
         Left            =   240
         TabIndex        =   20
         Top             =   3198
         Width           =   1935
      End
      Begin VB.Label lblMaxTemp 
         Alignment       =   1  'Right Justify
         Caption         =   "最高温度 (c)"
         Height          =   255
         Left            =   240
         TabIndex        =   9
         Top             =   4184
         Width           =   1935
      End
      Begin VB.Label lblMinTemp 
         Alignment       =   1  'Right Justify
         Caption         =   "最低温度 (c)"
         Height          =   255
         Left            =   240
         TabIndex        =   8
         Top             =   3691
         Width           =   1935
      End
      Begin VB.Label lblR10 
         Alignment       =   1  'Right Justify
         Caption         =   "电阻R10 (ohm)"
         Height          =   255
         Left            =   240
         TabIndex        =   7
         Top             =   2212
         Width           =   1935
      End
      Begin VB.Label lblR9 
         Alignment       =   1  'Right Justify
         Caption         =   "电阻R9 (ohm)"
         Height          =   255
         Left            =   240
         TabIndex        =   6
         Top             =   1719
         Width           =   1935
      End
      Begin VB.Label lblR8 
         Alignment       =   1  'Right Justify
         Caption         =   "电阻R8 (ohm)"
         Height          =   255
         Left            =   240
         TabIndex        =   5
         Top             =   1226
         Width           =   1935
      End
      Begin VB.Label lblRT 
         Alignment       =   1  'Right Justify
         Caption         =   "电位器RT (ohm)"
         Height          =   255
         Left            =   240
         TabIndex        =   4
         Top             =   733
         Width           =   1935
      End
      Begin VB.Label lblVCC 
         Alignment       =   1  'Right Justify
         Caption         =   "运放电压VCC (V)"
         Height          =   255
         Left            =   240
         TabIndex        =   3
         Top             =   240
         Width           =   1935
      End
   End
   Begin VB.PictureBox cavCurve 
      Height          =   4935
      Left            =   120
      ScaleHeight     =   4875
      ScaleWidth      =   5595
      TabIndex        =   1
      Top             =   4800
      Width           =   5655
   End
   Begin VB.PictureBox cavSch 
      Height          =   4470
      Left            =   120
      Picture         =   "frmMain.frx":009B
      ScaleHeight     =   4410
      ScaleWidth      =   12000
      TabIndex        =   0
      Top             =   120
      Width           =   12060
   End
End
Attribute VB_Name = "frmMain"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
