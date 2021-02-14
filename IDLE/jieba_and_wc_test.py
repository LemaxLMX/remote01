import jieba
from wordcloud import WordCloud as wc
from imageio import imread

s="浅复制模式只能独立第一层，\
也就是说原变量和继承变量在可迭代对象中依然会同步修改。"

print(s)

print(jieba.lcut(s)) #精确模式
print(jieba.lcut(s,cut_all=True)) #全模式
print(jieba.lcut_for_search(s)) #搜索引擎模式

temp=imread('3.png')
txt='蓝图上的落差终归只是理念上的区分，\
在实践场域的分野也未必明晰。\
譬如当我们追寻心之所向时，在途中涉足权力的玉墀，\
这究竟是伴随着期望的泯灭还是期望的达成？\
在我们塑造生活的同时，生活也在浇铸我们。\
既不可否认原生的家庭性与社会性，又承认自己的图景有轻狂的失真，\
不妨让体验走在言语之前。\
用不被禁锢的头脑去体味切斯瓦夫·米沃什的大海与风帆，\
并效维特根斯坦之言，对无法言说之事保持沉默。'
txt_list=jieba.lcut(txt)
new_txt=' '.join(txt_list)

pic=wc(scale=1.5,min_font_size=20,
       max_font_size=80,font_path='C:\Windows\Fonts\msyh.ttc',
       mask=temp,background_color='white').generate(new_txt)
pic.to_file('words.png')
