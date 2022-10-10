import easyocr


filename = "000005.png"


def ocr_process(filename):

    print("OCR Unit")
    print(f"Process .. {filename}")
    reader = easyocr.Reader(["en"])
    result = reader.readtext(filename)
    # print(result)

    var_out = []
    for a, b, c in result:
        # print(f"{b}", end="\n")
        var_out.append(b)

    # print(var_out)
    return var_out


r = ocr_process(filename)

for i in r:
    print(i)
