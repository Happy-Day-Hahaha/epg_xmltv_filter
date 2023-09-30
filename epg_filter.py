
### 下载文件

#import wget
#url = 'https://epg.pw/xmltv/epg.xml'  
#path = './'
#wget.download(url,path)

### 设置
#file_name = "https://epg.pw/xmltv/epg.xml" # 下载文件名
file_name = "http://64.225.52.167:37524/down/Heyd59OmdfGd.xml"
filter_tvgroup = ['ViuTV'] # 需要下载的电视台名
result_file_name = "epg_filtered.xml" # 生成的结果文件名

### 读取原始文件

import pandas
xml = pandas.read_xml(file_name)

xml_programme = xml.query('id.isnull()')
xml_p_new = xml_programme[['channel', 'start', 'stop', 'title', 'date','audio']]
xml_p_new = xml_p_new.rename(columns={'channel': 'id'})

xml_tvstation = xml.query('channel.isnull()')
xml_t_new = xml_tvstation[['id','display-name']]

xml_total = xml_t_new.merge(xml_p_new, on='id')

filtered_xml_total = xml_total.loc[xml_total['display-name'].isin(filter_tvgroup)]

# 电视频道总表filtered_tv，电视节目总表filtered_xml_total
filtered_xml_total = filtered_xml_total.drop(['display-name'], axis=1)
filtered_tv = xml_t_new.loc[xml_t_new['display-name'].isin(filter_tvgroup)]

# 获取原始文件前两行

f=open(file_name,'r')
str_head = ""
for i in range(2):
    str_head += f.readline().strip() + '\n'
#print(str_head)

# 输出文件（channel部分）
with open(result_file_name,"w") as file:
    file.write(str_head)

    for row in filtered_tv.itertuples():
        print("\t<channel id=\"" + str(int(row.id)) + "\">\n")
        print("\t\t<display-name lang=\"TW\">" + row._2 +"</display-name>\n")
        print("\t</channel>\n")

# 输出文件（epg部分）
with open(result_file_name,"a") as file:
    for row in filtered_xml_total.itertuples():
        print("\t<programme channel=\"" + str(int(row.id)) + "\" start=\"" + str(row.start) + "\" stop=\"" + str(row.stop) + "\">\n")
        print("\t\t<title lang=\"zh\">" + str(row.title) + "</title>\n")   
        print("\t\t<date>" + str(int(row.date)) + "</date>\n" )
        print("\t\t<audio>\n")
        print("\t\t\t<stereo>stereo</stereo>\n")
        print("\t\t</audio>\n")
        print("\t</programme>\n")

