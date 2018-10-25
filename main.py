import json
from collections import OrderedDict

ITERM_COLORS = {
    "key": [
        "Ansi 0 Color",
        "Ansi 1 Color",
        "Ansi 10 Color",
        "Ansi 11 Color",
        "Ansi 12 Color",
        "Ansi 13 Color",
        "Ansi 14 Color",
        "Ansi 15 Color",
        "Ansi 2 Color",
        "Ansi 3 Color",
        "Ansi 4 Color",
        "Ansi 5 Color",
        "Ansi 6 Color",
        "Ansi 7 Color",
        "Ansi 8 Color",
        "Ansi 9 Color",
        "Background Color",
        "Badge Color",
        "Bold Color",
        "Cursor Color",
        "Cursor Guide Color",
        "Cursor Text Color",
        "Foreground Color",
        "Link Color",
        "Selected Text Color",
        "Selection Color",
        "Tab Color",
    ],
    "dict": [
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.15294118225574493",
                "0.086274512112140656",
                "0.0039215688593685627",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.42352941632270813",
                "0.54901963472366333",
                "0.9686274528503418",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.43137255311012268",
                "0.85490196943283081",
                "0.13333334028720856",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": ["1", "0.58431375026702881", "0.92156863212585449", "1"],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.89411765336990356",
                "0.65490198135375977",
                "0.36078432202339172",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.7607843279838562",
                "0.34117648005485535",
                "0.49411764740943909",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.65882354974746704",
                "0.78039216995239258",
                "0.12941177189350128",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": ["1", "1", "1", "1"],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.40392157435417175",
                "0.85882353782653809",
                "0.67843139171600342",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": ["1", "0.54509806632995605", "0.79607844352722168", "1"],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": ["1", "1", "0.66666668653488159", "0.50980395078659058"],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.91764706373214722",
                "0.57254904508590698",
                "0.78039216995239258",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.7921568751335144",
                "0.85882353782653809",
                "0.49803921580314636",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.83137255907058716",
                "0.77254903316497803",
                "0.7450980544090271",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.41960784792900085",
                "0.3490196168422699",
                "0.26666668057441711",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.31372550129890442",
                "0.32549020648002625",
                "0.93725490570068359",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.15294118225574493",
                "0.086274512112140656",
                "0.0039215688593685627",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": ["0.5", "0.42745095491409302", "0.17254889011383057", "1"],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": ["1", "1", "1", "1"],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.51372545957565308",
                "0.466666579246521",
                "0.43529421091079712",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "0.25",
                "0.86274629831314087",
                "0.98757690191268921",
                "0.082667849957942963",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.95294123888015747",
                "0.95294123888015747",
                "0.95294123888015747",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.92156863212585449",
                "0.87058824300765991",
                "0.83921569585800171",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.94117647409439087",
                "0.80000001192092896",
                "0.47058823704719543",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": ["1", "1", "1", "1"],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.46666666865348816",
                "0.46666666865348816",
                "0.38823530077934265",
            ],
            "string": "sRGB",
        },
        {
            "key": [
                "Alpha Component",
                "Blue Component",
                "Color Space",
                "Green Component",
                "Red Component",
            ],
            "real": [
                "1",
                "0.068835996091365814",
                "0.1000501736998558",
                "0.74730008840560913",
            ],
            "string": "sRGB",
        },
    ],
}


def arrToRgb(arr):
    rgb = arr[1:][::-1]
    rgb = [hex(int(float(n) * 255))[2:] for n in rgb]
    return f"#{''.join([n.zfill(2) for n in rgb])}"


colors = {}
palette = {}

for name, v in zip(*ITERM_COLORS.values()):
    rgb = arrToRgb(v["real"])

    if "Ansi" in name:
        palette[int(name.split(" ")[1])] = rgb
    else:
        colors[name] = rgb

theme = OrderedDict(
    {
        "name": "Night Owl",
        "comment": "Night Owl ported for Tilix",
        "foreground-color": colors["Foreground Color"],
        "background-color": colors["Background Color"],
        "use-theme-colors": False,
        "use-highlight-color": True,
        "highlight-foreground-color": colors["Selected Text Color"],
        "highlight-background-color": colors["Selection Color"],
        "use-cursor-color": True,
        "cursor-foreground-color": colors["Cursor Text Color"],
        "cursor-background-color": colors["Cursor Color"],
        "use-badge-color": True,
        "badge-color": colors["Badge Color"],
        "palette": [palette[i] for i in range(16)],
    }
)

with open("nightowl.json", "w") as fp:
    json.dump(theme, fp, indent=4)
