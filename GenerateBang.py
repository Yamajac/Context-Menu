DevkitBG = {
    "Config" : "Context Menu\ContextMenu",
    "File" : "Context Menu\@Resources\ContextMenuOptions.inc",
    "Prefix" : False,
    "Width"  : "160",
    "MouseOverColour" : "200,0,0,50",
    "SeparatorColour" : "255,0,0,255",
    "BackgroundColour" : "46,52,150,255",
    "BorderColour"  : "20,200,13,150",
    "FontColour" : "200,100,200,200",
    "ShadowColour" : "120,0,200,100",
    "Lines" : [{
        "Icon"      : False,
        "Text"      : "Dev Environment",
        "Style"     : "Bold",
        "Bang"      : False,
        "Separator" : "1"
    },
    {
        "Icon"      : "",
        "Text"      : "Sign out",
        "Style"     : False,
        "Bang"      : """[!ActivateConfig "LoginScreen\DEVKITUnloader"][!ActivateConfig "LoginScreen\LoginScreenLoader"][!DeactivateConfig]""",
        "Separator" : "1" 
    },
    {
        "Icon"      : "",
        "Text"      : "Manage",
        "Style"     : False,
        "Bang"      : """[!Manage][!DeactivateConfig]""",
        "Separator" : False
    },
    {
        "Icon"      : "",
        "Text"      : "Refresh",
        "Style"     : False,
        "Bang"      : """[!Refresh "DevKit\Wallpaper"][!DeactivateConfig]""",
        "Separator" : False
    }],
    "Suffix" : False

}
RainManager = {
    "Config" : "Context Menu\ContextMenu",
    "File" : "Context Menu\@Resources\ContextMenuOptions.inc",
    "Prefix" : """[!SetVariable MouseY "($MouseY$ / #Spacing#)"][!UpdateMeasureGroup Mousers][!UpdateMeasure ClickedConfig]""",
    "Width"  : "250",
    "MouseOverColour" : "200,200,0,50",
    "SeparatorColour" : "155,147,201,255",
    "BackgroundColour" : "46,52,68,255",
    "BorderColour"  : "20,13,30,150",
    "FontColour" : "200,200,200,200",
    "ShadowColour" : "0,0,0,100",
    "Lines" : [{
        "Icon"      : False,
        "Text"      : "[ClickedConfig]",
        "Style"     : "Bold",
        "Bang"      : False,
        "Separator" : "1"
    },
    {
        "Icon"      : "",
        "Text"      : "Manage",
        "Style"     : False,
        "Bang"      : """[!Manage Skins "[ClickedConfig]"][!DeactivateConfig]""",
        "Separator" : False
    },
    {
        "Icon"      : "",
        "Text"      : "Refresh",
        "Style"     : False,
        "Bang"      : """[!Refresh "[ClickedConfig]"][!DeactivateConfig]""",
        "Separator" : False
    },
    {
        "Icon"      : "",
        "Text"      : "Unload",
        "Style"     : False,
        "Bang"      : """[!DeactivateConfig "[ClickedConfig]"][!UpdateMeasure RainmeterSettings DevKit\RainManager][!DeactivateConfig]""",
        "Separator" : "1"
    },
    {
        "Icon"      : "",
        "Text"      : "Refresh",
        "Style"     : False,
        "Bang"      : """[!Refresh "DevKit\RainManager"][!DeactivateConfig]""",
        "Separator" : False
    }],
    "Suffix" : False

}



Options = DevkitBG


with open('output', 'w', encoding='utf-8') as f:
    bang = ""
    
    if Options['Prefix'] != False:
        bang += Options['Prefix']
    bang += """[!WriteKeyValue Variables Width {0} "#SKINSPATH#{1}"]""".format(Options['Width'],Options['File'])
    bang += """[!WriteKeyValue Variables Length {0} "#SKINSPATH#{1}"]""".format(len(Options['Lines']),Options['File'])
    bang += """[!WriteKeyValue Variables MouseOverColour {0} "#SKINSPATH#{1}"]""".format(Options['MouseOverColour'],Options['File'])
    bang += """[!WriteKeyValue Variables SeparatorColour {0} "#SKINSPATH#{1}"]""".format(Options['SeparatorColour'],Options['File'])
    bang += """[!WriteKeyValue Variables BackgroundColour {0} "#SKINSPATH#{1}"]""".format(Options['BackgroundColour'],Options['File'])
    bang += """[!WriteKeyValue Variables BorderColour {0} "#SKINSPATH#{1}"]""".format(Options['BorderColour'],Options['File'])
    bang += """[!WriteKeyValue Variables FontColour {0} "#SKINSPATH#{1}"]""".format(Options['FontColour'],Options['File'])
    bang += """[!WriteKeyValue Variables ShadowColour {0} "#SKINSPATH#{1}"]""".format(Options['ShadowColour'],Options['File'])
    
    for i in range(len(Options['Lines'])):
        for k,v in Options['Lines'][i].items():
            if v != False:
                print(k,v)
                bang += """[!WriteKeyValue Variables {0}{1} \"\"\"{2}"\"\" "#SKINSPATH#{3}"]""".format(k, i+1, v, Options['File'])
            else:
                print(k,v)
                bang += """[!WriteKeyValue Variables {0}{1} \"\"\"{2}"\"\" "#SKINSPATH#{3}"]""".format(k, i+1, " ", Options['File'])
            
    bang += """[!ActivateConfig "{0}"]""".format(Options['Config'])
    bang += """[!Move (#CURRENTCONFIGX#+$MouseX$) (#CURRENTCONFIGY#+$MouseY$) "{0}"]""".format(Options['Config'])
    bang += """[!Refresh "{0}"]""".format(Options['Config'])
    
    if Options['Suffix'] != False:
        bang += Options['Suffix']
    f.write(bang)




