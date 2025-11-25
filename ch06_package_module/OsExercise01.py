import os

# 특정 디렉토리에 하위 디렉토리 여러 개 생성하기
targetFolder = 'd:\\' # \는 특수 문자라서 \\라고 표시해야 합니다.
parentPath = os.path.join(targetFolder, 'exercise')
print(parentPath)

try:
    os.mkdir(parentPath)

    folderList = ['alpha', 'bravo', 'delta', 'nova', 'terra', 'pixel', 'orbit', 'matrix', 'spark', 'fusion']

    for fold in folderList:
        newFolder = os.path.join(parentPath, fold)
        os.mkdir(newFolder)

except FileExistsError:
    print('해당 디렉토리가 이미 존재합니다.')
# end try