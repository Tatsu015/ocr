try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# 日本語の画像ファイル
FILENAME = './PowerSghbel.png'

# デフォルト言語の英語で実行されるため意味なし
print(pytesseract.image_to_string(Image.open(FILENAME), lang='eng' ))

# # 日本語で文字出力
# print(pytesseract.image_to_string(Image.open(FILENAME), lang='jpn'))

# # ボックス(座標位置付き)出力
# print(pytesseract.image_to_boxes(Image.open(FILENAME), lang='jpn'))

# # TSV出力(多分、一番詳細情報あり)
# print(pytesseract.image_to_data(Image.open(FILENAME), lang='jpn'))

# # OSD(Orientation and script detection)
# print(pytesseract.image_to_osd(Image.open(FILENAME), lang='jpn'))

# # HOCR形式出力
# print(pytesseract.image_to_pdf_or_hocr(FILENAME, extension='hocr'))