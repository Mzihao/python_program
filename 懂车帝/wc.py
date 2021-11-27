from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open("car.txt", encoding='utf8').read()
# 使用WordCloud生成词云
word_cloud = WordCloud(font_path="fzmw.ttf",  # 设置词云字体
                       background_color="white", # 词云图的背景颜色
                       scale=10 #分辨率
                       )
wc = word_cloud.generate(text)
wc.to_file("cloud.jpg") #保存图片
# 运用matplotlib展现结果
plt.imshow(wc)
plt.axis("off")
plt.show()
