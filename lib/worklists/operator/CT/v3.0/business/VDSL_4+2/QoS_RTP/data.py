#coding:utf-8


# -----------------------------doc--------------------------
# 工单 描述
WORKLIST_DOC = """
功能描述：生成一个基于业务的QoS保障测试-RTP工单

    参数：
    | Min            | 222.66.65.58 | 最小取值，可以和Max 取值一样。默认222.66.65.58 |
    | Max            | 222.66.65.58 | 最大取值,默认222.66.65.58  |
    | DSCPMarkValue  | 3 | DSCP值,默认3  |
    | M802_1_P_Value | 3 | 802.1p值,默认3 |
    | ClassQueue     | 1 | 有四个队列可选:1,2,3,4,缺省值:1 |
    
        
    
    注意:平台不做值的判断,统一由CPE决定值是否合法.
"""


# -----------------------------args--------------------------
# 工单 参数
WORKLIST_ARGS = {
"Min":("222.66.65.58", "1"),
"Max":("222.66.65.58", "2"),
"DSCPMarkValue":("3", "3"),
"M802_1_P_Value":("3", "4"),
"ClassQueue":("1", "5")
}

