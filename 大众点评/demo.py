from fontTools.ttLib import TTFont


# font = TTFont('demo.woff')
# font.saveXML('demo.xml')

font = TTFont('demo.woff')

# 各节点名称：font.keys()
kv = font.keys()
print(kv)

# 获取getGlyphOrder节点name值
print(font.getGlyphOrder())

# 获取cmap节点code与name值映射
print(font.getBestCmap())