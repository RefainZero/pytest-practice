# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 22:27
# @Author  : longrong.lang
# @FileName: test_case1.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
def test_query_shop(query):
    shopName,size,colour=query
    print(f"\n返回查询商品信息：商品名称： {shopName} 颜色：{colour} 鞋号： {size}")