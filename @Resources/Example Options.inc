;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;   This is the options file I use for my RainManager
;   You can see I use a new variable here "Config"
;   Before updating the Context Menu, I overwrite the Config variable here
;   with the proper info so the rest of the menu displays properly.
;   
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

[Variables]
Width=250
Length=5
MouseOverColour = 200,200,0,50
SeparatorColour = 155,147,201,255
BackgroundColour = 46,52,68,255
BorderColour = 20,13,30,150
FontColour = 200,200,200,200
ShadowColour = 0,0,0,100
Config =DevKit\Wallpaper

Text1=#Config#
Style1=Bold
Separator1=1

Icon2=
Text2=Manage
Bang2=[!Manage Skins "#Config#"][!DeactivateConfig]

Icon3=
Text3=Refresh
Bang3=[!Manage Skins "#Config#"][!DeactivateConfig]

Icon4=
Text4=Unload
Bang4=[!DeactivateConfig "#Config#"][!UpdateMeasure RainmeterSettings DevKit\RainManager][!DeactivateConfig]
Separator4 = 1

Icon5=
Text5=Refresh
Bang5=[!Refresh "DevKit\RainManager"][!DeactivateConfig]
