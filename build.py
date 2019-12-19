# -*- coding:utf-8 -*-
# Author : 我才是二亮 (unstring@163.com)
import sys, os.path
from FileParserClass import FileParser
from MarkdownBuildClass import MarkDownBuild

if __name__ == '__main__':

    md_dir = './md/'

    content = ''
    file = ''
    if (len(sys.argv) < 2):
        exit('请输入SQL文件路径')

    dir = sys.argv[1]
    try:
        file = open(dir)
    except IOError as e:
        exit(e)
    try:
        content = file.read()
    except:
        exit('文件读取失败')
    finally:
        file.close()

    file_parser = FileParser()
    # 将文件分离为每张表
    table_list = file_parser.separatTable(content)
    # 解析出表中表名及表详情
    table_name = file_parser.parserTableName(table_list)
    # 解析出每张表字段情况并与表名表详情组合
    table_data = file_parser.parserColumn(table_list, table_name)

    markdown_build = MarkDownBuild()

    text = markdown_build.buildMarkdown(table_data)
    file_name = os.path.basename(dir).split('.')[0] + '.md'
    # 写文件
    file_obj = ''
    try:
        file_obj = open(md_dir + file_name, 'w')
    except:
        exit('文件创建失败')

    try:
        file_obj.write(text)
    except:
        exit('文件写入失败')
    finally:
        file_obj.close()

    print('数据库文档已经成功创建,文件在md目录下.');


