import string
import sys


print()
print("Provide a list of DRIVE LETTERS to be shown on RainMeter Disks")
# print("Enter \"end\" to terminate and generate file")
print("Example: CDEFGH")

drives = []
filename = ""

# while True:
  # drive = input("DRIVE LETTER: ")
  # if (drive == "end") : break
filename = input("DRIVE LETTERS: ")
for drive in filename:
  if (len(drive)==1):
    drives.append ({
      "letter": drive,
      "var": "drive_" + drive,
      "used": "used_" + drive,
      "total": "total_" + drive,
    })
    # filename += drive
# filename=drives

if not drives:
  exit("\nExit: empty drive list")



print("Generating configuration file for drives:")
for drive in drives:
  print(drive['letter'], end=" ")

print()

file = open(filename + ".ini", "w")
 




file.write("""
[Rainmeter]
Update=1000
Background=#@#Background.png
BackgroundMode=3
BackgroundMargins=0,34,0,14

[Metadata]
Name=Disk
Author=poiru
Information=Displays disk usage.
License=Creative Commons BY-NC-SA 3.0
Version=1.0.0

[Variables]
fontName=Trebuchet MS
textSize=8
colorBar=235,170,0,255
colorText=255,255,255,205
""")




# VARIABLE

for drive in drives:
  file.write(drive['var'] + " = " + drive['letter'] + ':\n')







file.write("""

; ----------------------------------
; MEASURES return some kind of value
; ----------------------------------
""")



# MEASURE
# 
for drive in drives:
  file.write("""
[""" + drive['total'] + """]
Measure=FreeDiskSpace
Drive = #""" + drive['var'] + """#
Total=1
UpdateDivider=120

[""" + drive['used'] + """]
; Returns inverted value of free disk space (i.e. used disk space)
Measure=FreeDiskSpace
Drive= #""" + drive['var'] + """#
InvertMeasure=1
UpdateDivider=120

""")



file.write(
"""

; ----------------------------------
; STYLES are used to "centralize" options
; ----------------------------------

[styleTitle]
StringAlign=Center
StringCase=Upper
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,50
FontColor=#colorText#
FontFace=#fontName#
FontSize=10
AntiAlias=1
ClipString=1

[styleLeftText]
StringAlign=Left
; Meters using styleLeftText will be left-aligned.
StringCase=None
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontColor=#colorText#
FontFace=#fontName#
FontSize=#textSize#
AntiAlias=1
ClipString=1

[styleRightText]
StringAlign=Right
StringCase=None
StringStyle=Bold
StringEffect=Shadow
FontEffectColor=0,0,0,20
FontColor=#colorText#
FontFace=#fontName#
FontSize=#textSize#
AntiAlias=1
ClipString=1

[styleBar]
BarColor=#colorBar#
BarOrientation=HORIZONTAL
SolidColor=255,255,255,15

; ----------------------------------
; METERS display images, text, bars, etc.
; ----------------------------------

[meterTitle]
Meter=String
MeterStyle=styleTitle
; Using MeterStyle=styleTitle will basically "copy" the
; contents of the [styleTitle] section here during runtime.
X=100
Y=12
W=190
H=18
Text=Disk
; Even though the text is set to Disk, Rainmeter will display
; it as DISK, because styleTitle contains StringCase=Upper.




""")


# DISPLAY

labelY = 40
barY = 55


for drive in drives:
  file.write("""
[meterLabel""" + drive['letter'] + """]
Meter=String
MeterStyle=styleLeftText
X=10
Y = """ + str(labelY) + """
W=190
H=14
Text = #""" + drive['var'] + """#\\

[meterValue""" + drive['letter'] + """]
Meter=String
MeterStyle=styleRightText
MeasureName = """ + drive['used'] + """
MeasureName2 = """ + drive['total'] + """
X=200
Y=0r
W=190
H=14
Text=%1B / %2B
NumOfDecimals=0
AutoScale=1
LeftMouseUpAction=["#""" + drive['var'] + """#\\"]

[meterBar""" + drive['letter'] + """]
Meter=Bar
MeterStyle=styleBar
MeasureName = """ + drive['used'] + """
X=10
Y = """ + str(barY) + """
W=190
H=1

""")
  labelY += 30
  barY += 30













file.close() 
print("Generated as " + filename + ".ini")
