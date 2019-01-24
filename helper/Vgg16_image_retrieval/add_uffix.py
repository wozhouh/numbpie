import os
path = './database/'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.')<0:
            newname=file+'.jpg'
            os.rename(os.path.join(path,file),os.path.join(path,newname))
print(file,'ok')