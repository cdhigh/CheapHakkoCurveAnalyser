VERSION 5.00
Begin VB.Form frmMain 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "白菜白光三线式调温电路分析软件 [cdhigh]"
   ClientHeight    =   9630
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   12555
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   9630
   ScaleWidth      =   12555
   StartUpPosition =   2  '屏幕中心
   Tag             =   "p@icon=icon.gif"
   Begin VB.Frame frameDesgin 
      Caption         =   "参数设计"
      Height          =   4695
      Left            =   6000
      TabIndex        =   2
      Top             =   4800
      Width           =   6375
      Begin VB.ComboBox cmbTempFormula 
         Height          =   300
         ItemData        =   "frmMain.frx":0000
         Left            =   2400
         List            =   "frmMain.frx":000A
         Style           =   2  'Dropdown List
         TabIndex        =   24
         Top             =   4320
         Width           =   1335
      End
      Begin VB.TextBox txtTips 
         BackColor       =   &H00C0FFFF&
         BorderStyle     =   0  'None
         Height          =   3735
         Left            =   4080
         Locked          =   -1  'True
         MultiLine       =   -1  'True
         TabIndex        =   22
         Top             =   840
         Width           =   2055
      End
      Begin VB.TextBox txtMinVol 
         Height          =   270
         Left            =   2400
         TabIndex        =   15
         Top             =   2505
         Width           =   1335
      End
      Begin VB.TextBox txtMaxVol 
         Height          =   270
         Left            =   2400
         TabIndex        =   16
         Top             =   2958
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
         Top             =   3864
         Width           =   1335
      End
      Begin VB.TextBox txtMinTemp 
         Height          =   270
         Left            =   2400
         TabIndex        =   17
         Top             =   3411
         Width           =   1335
      End
      Begin VB.TextBox txtR10 
         Height          =   270
         Left            =   2400
         TabIndex        =   14
         Text            =   "56000"
         Top             =   2052
         Width           =   1335
      End
      Begin VB.TextBox txtR9 
         Height          =   270
         Left            =   2400
         TabIndex        =   13
         Text            =   "51"
         Top             =   1599
         Width           =   1335
      End
      Begin VB.TextBox txtR8 
         Height          =   270
         Left            =   2400
         TabIndex        =   12
         Text            =   "43000"
         Top             =   1146
         Width           =   1335
      End
      Begin VB.TextBox txtRT 
         Height          =   270
         Left            =   2400
         TabIndex        =   11
         Text            =   "10000"
         Top             =   693
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
         TabIndex        =   23
         Top             =   4320
         Width           =   1935
      End
      Begin VB.Label lblMinVol 
         Alignment       =   1  'Right Justify
         Caption         =   "最小参考电压 (mV)"
         Height          =   255
         Left            =   240
         TabIndex        =   21
         Top             =   2505
         Width           =   1935
      End
      Begin VB.Label lblMaxVol 
         Alignment       =   1  'Right Justify
         Caption         =   "最大参考电压 (mV)"
         Height          =   255
         Left            =   240
         TabIndex        =   20
         Top             =   2958
         Width           =   1935
      End
      Begin VB.Label lblMaxTemp 
         Alignment       =   1  'Right Justify
         Caption         =   "最高温度 (c)"
         Height          =   255
         Left            =   240
         TabIndex        =   9
         Top             =   3864
         Width           =   1935
      End
      Begin VB.Label lblMinTemp 
         Alignment       =   1  'Right Justify
         Caption         =   "最低温度 (c)"
         Height          =   255
         Left            =   240
         TabIndex        =   8
         Top             =   3411
         Width           =   1935
      End
      Begin VB.Label lblR10 
         Alignment       =   1  'Right Justify
         Caption         =   "电阻R10 (ohm)"
         Height          =   255
         Left            =   240
         TabIndex        =   7
         Top             =   2052
         Width           =   1935
      End
      Begin VB.Label lblR9 
         Alignment       =   1  'Right Justify
         Caption         =   "电阻R9 (ohm)"
         Height          =   255
         Left            =   240
         TabIndex        =   6
         Top             =   1599
         Width           =   1935
      End
      Begin VB.Label lblR8 
         Alignment       =   1  'Right Justify
         Caption         =   "电阻R8 (ohm)"
         Height          =   255
         Left            =   240
         TabIndex        =   5
         Top             =   1146
         Width           =   1935
      End
      Begin VB.Label lblRT 
         Alignment       =   1  'Right Justify
         Caption         =   "电位器RT (ohm)"
         Height          =   255
         Left            =   240
         TabIndex        =   4
         Top             =   693
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
      Height          =   4695
      Left            =   240
      ScaleHeight     =   4635
      ScaleWidth      =   5595
      TabIndex        =   1
      Top             =   4800
      Width           =   5655
   End
   Begin VB.PictureBox cavSch 
      Height          =   4500
      Left            =   240
      Picture         =   "frmMain.frx":0027
      ScaleHeight     =   4440
      ScaleWidth      =   11985
      TabIndex        =   0
      Top             =   120
      Width           =   12045
   End
End
Attribute VB_Name = "frmMain"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

