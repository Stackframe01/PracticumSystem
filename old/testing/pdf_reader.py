from wand.image import Image


def read_pdf():
    # 'https://fgos.ru/LMS/wm/wm_fgos.php?id=09_03_03(1)'
    pdf = Image(filename='fgos_ru_09_03_04(2).pdf', resolution=300)
    pdfImage = pdf.convert('jpeg')
    print(pdfImage)


if __name__ == '__main__':
    read_pdf()
