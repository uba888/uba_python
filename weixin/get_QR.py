from PIL import Image
b = u'\u2588'
BLOCK=b
def print_cmd_qr(fileDir, size = 37, padding = 3,
        white = BLOCK, black = '  ', enableCmdQR = True):
    img     = Image.open(fileDir)
    times   = img.size[0] / (size + padding * 2)
    rgb     = img.convert('RGB')
    try:
        blockCount = int(enableCmdQR)
        assert(0 < abs(blockCount))
    except:
        blockCount = 1
    finally:
        white *= abs(blockCount)
        if blockCount < 0: white, black = black, white
    sys.stdout.write(' '*50 + '\r')
    sys.stdout.flush()
    qr = white * (size + 2) + '\n'
    startPoint = padding + 0.5
    for y in range(size):
        qr += white
        for x in range(size):
            r,g,b = rgb.getpixel(((x + startPoint) * times, (y + startPoint) * times))
            qr += white if r > 127 else black
        qr += white + '\n'
    qr += white * (size + 2) + '\n'
    sys.stdout.write(qr)
