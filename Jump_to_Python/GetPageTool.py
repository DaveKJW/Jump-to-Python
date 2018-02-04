"""2. 게시판 페이징하기"""

def GetPageTool(i, j):
    if i % j == 0:
        page = (i // j)
    else:
        page = (i // j) + 1
    return "필요한 페이지는 {0}page입니다.".format(page)
print(GetPageTool(32,10))