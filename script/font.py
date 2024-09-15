import os, json
from fontTools.ttLib import TTFont

字体文件名称 = "HarmonyOS_Sans_SC_Regular.ttf"
保存的字体文件名称 = "HarmonyOS_Sans_SC_Regular_" # 会在名称后加上第几个切片并以.woff2结尾
字体切片字数 = 2500 # 多少个字打包成一个文件
css_font_family = "HarmonyOS Sans SC Regular" # css的字体家族
css_font_family_first = 'local("HarmonyOS Sans SC Regular"), local("HarmonyOS Sans SC"), ' # 如果你不知道这是干什么的，请设置为""

print("正在加载字体文件......")
# 打开字体文件
with TTFont(字体文件名称 ) as font:
    # 获取字体文件的数据
    font_data = font.getGlyphOrder()
print("加载字体文件成功")

# 写入字体数据，方便调试
with open("data.json", "w", encoding="utf-8") as f:
    writer_json = json.dumps(font_data, ensure_ascii=False, indent=2)
    f.write(writer_json)

print("正在生成数据......")
# 字体所有文字
font_unicodes = []

# 遍历字体数据
for i in font_data:
    # 判断数据开头是不是uni
    if i.startswith("uni"):
        # 插入数据
        font_unicodes.append(i)

# 写入字体数据，方便调试
with open("data1.json", "w", encoding="utf-8") as f:
    writer_json = json.dumps(font_unicodes, ensure_ascii=False, indent=2)
    f.write(writer_json)
    writer_json = []

# 切割列表
font_unicodes = [font_unicodes[i:i + 字体切片字数] for i in range(0, len(font_unicodes), 字体切片字数)]

# 写入字体数据，方便调试
with open("data2.json", "w", encoding="utf-8") as f:
    writer_json = json.dumps(font_unicodes, ensure_ascii=False, indent=2)
    f.write(writer_json)
    writer_json = []

# 取刚刚生成的数据，列表中的列表的范围
unicodes = []
for i in font_unicodes:
    start_key = i[0].replace("uni", "")
    end_key = i[-1].replace("uni", "")
    unicodes.append(f"U+{start_key}-{end_key}")

with open("data3.json", "w", encoding="utf-8") as f:
    writer_json = json.dumps(unicodes, ensure_ascii=False, indent=2)
    f.write(writer_json)
    writer_json = []

print("数据生成成功，开始转换！")

列表长度 = len(unicodes)

print(f"列表长度: {列表长度}")

raw_css = ""

for i in range(列表长度):
    当前字符集 = unicodes[i]
    print(f"正在处理字符集 {当前字符集}")

    # if isinstance(当前字符集, list):
    #     print("正在合并当前子集......")
    #     当前字符集 = ','.join(map(str, 当前字符集))
    #     print(f"合并结果： {当前字符集}")

    字体保存目录 = f"./fonts/{保存的字体文件名称}{i}.woff2"
    命令 = f'pyftsubset {字体文件名称} --unicodes="{当前字符集}" --output-file="{字体保存目录}" --flavor="woff2'
    print(f"执行命令: {命令}")
    # U+........
    os.system(命令)

    raw_css = raw_css + f'''
@font-face {{
    font-family: "{css_font_family}";
    font-style: normal;
    /* font-weight: 400; */
    font-display: swap;
    src: {css_font_family_first}url("{字体保存目录}") format("woff2");
    unicode-range: {当前字符集}
}}
''' # css生成模板

raw_css = raw_css + f'''
body {{
    /* 设置字体 */
    font-family: "{css_font_family}", sans-serif !important;
}}
'''

with open("font.css", "w", encoding="utf-8") as f:
    f.write(raw_css)
  
