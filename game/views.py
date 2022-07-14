from django.http import HttpResponse

def index(resquest):
    line1 = '<h1 style = "text-align: center">这就是白燕！！！</h1>'
    line3 = '<h1 style = "text-align: center">↓↓↓↓↓↓↓↓↓↓↓↓</h1>'
    line2 = '<img src = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fgss0.baidu.com%2F9vo3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2Fb999a9014c086e063c2ef9be09087bf40bd1cb45.jpg&refer=http%3A%2F%2Fgss0.baidu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1660381320&t=3907b908181a3badc1bdd02386039ff1" width = 1000>'
    return HttpResponse(line1 + line3 + line2)
