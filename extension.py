import glob
import os.path
from PIL import Image
import PIL

#이미지의 webp 확장자가 겹쳐진걸 해결하는 프로그램

path = "C:\\Users\\82109\\Desktop\\MYBOX\\"
before ="*.webp"
after =".png"
a= glob.glob(pathname=path+before)

print(a)

for x in a:
    if not os.path.isdir(x):
        filename = os.path.splitext(x)
        name = os.path.splitext(filename[0])

        if name[1] =="":
            os.rename(x, name[0]+after)
            print("확장자가 하나: {0} -> {1}".format(x,name[0]+after))
        else:
            os.rename(x, filename[0])
            print("확장자가 두개: {0} -> {1}".format(x,filename[0]))

