import glob

# file type for the image export (.jpg, .png, .tif, .tga)
filetype = ".png"
##

script = glob.glob('./*.pyde')
name = script[0][2:-5]

def mousePressed():
    # save file on mouse click in a YYYY_MM_DD subfolder
    y = year()
    mo = month()
    d = day()
    h = hour()
    m = minute()
    s = second()
    ms = millis()
    filename = "{:02d}_{:02d}_{:02d}/{}_{:02d}{:02d}{:02d}{}".format(y,mo,d,name,h,m,s,ms)
    print("SAVED : " + filename + filetype)
    save(filename + filetype)
    
    # Save parameters variables to a txt file
    p = [filename[11:].upper(), "-" * 18 + "\n"]
    with open(name + ".pyde", "r") as file:
        l = file.readlines()
        lines = l[l.index("# parameters\n")+1 : l.index("##\n")]
        p += [x[:-1] for x in lines]
    saveStrings(filename + ".txt", p)
    print("SAVED : " + filename + ".txt")
