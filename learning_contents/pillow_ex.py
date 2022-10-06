from PIL import Image
import os
import zipfile

# with zipfile.ZipFile('data/images.zip', 'r') as zip:
#     zip.extractall('data/images')

def dir_list(path:str) -> list and str:
    file_list = os.listdir(path)
    dir_len = len(file_list)
    return file_list, dir_len

def resize():
    img = Image.open('data/images/photo1.jpg').convert('L') # 흑백 변환
    print(type(img.height), img.width)
    crop_img = img.crop((0, 0, 100, 100))
    crop_img.show()
    # img = img.resize((300, 500)) # 튜플에 담기
    img.save('data/images/new_photo1.jpg')


def thumbnail(): # 서버에서 처리하는 로직 주로 사용
    img = Image.open('data/images/photo1.jpg')
    img.crop( (50, 50, 150, 150) ) #
    img.thumbnail((300, 500))
    img.save('data/images/new_thumbnail1.jpg', quality=15, progressive=True) # png 파일의 압축은 quantize 서치, png는 색상의 갯수로 용량이 결정되므로



a, b = dir_list('data/images')
print(a)
# resize()
# thumbnail()

