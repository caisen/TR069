#coding:utf-8


# -----------------------------rpc --------------------------
import os
import sys

#debug
DEBUG_UNIT = False
if (DEBUG_UNIT):
    g_prj_dir = os.path.dirname(__file__)
    parent1 = os.path.dirname(g_prj_dir)
    parent2 = os.path.dirname(parent1)
    parent3 = os.path.dirname(parent2)
    parent4 = os.path.dirname(parent3)  # tr069v3\lib
    parent5 = os.path.dirname(parent4)  # tr069v3\
    sys.path.insert(0, parent4)
    sys.path.insert(0, os.path.join(parent4, 'common'))
    sys.path.insert(0, os.path.join(parent4, 'worklist'))
    sys.path.insert(0, os.path.join(parent4, 'usercmd'))
    sys.path.insert(0, os.path.join(parent5, 'vendor'))
from TR069.lib.common.event import *
from TR069.lib.common.error import *
from time import sleep
import TR069.lib.common.logs.log as log 

g_prj_dir = os.path.dirname(__file__)
parent1 = os.path.dirname(g_prj_dir)
parent2 = os.path.dirname(parent1) # dir is system
try:
    i = sys.path.index(parent2)
    if (i !=0):
        # stratege= boost priviledge
        sys.path.pop(i)
        sys.path.insert(0, parent2)
except Exception,e: 
    sys.path.insert(0, parent2)

import _Common
reload(_Common)
from _Common import *
import _VOIP
reload(_VOIP)
from _VOIP import VOIP

def test_script(obj):
    """
    """
    sn = obj.sn # 取得SN号
    DeviceType = "LAN"  # 绑定tr069模板类型.只支持ADSL\LAN\EPON三种
    AccessMode = 'DHCP'    # WAN接入模式,可选PPPoE_Bridge,PPPoE,DHCP,Static
    rollbacklist = []  # 存储工单失败时需回退删除的实例.目前缺省是不开启回退
    # 初始化日志
    obj.dict_ret.update(str_result=u"开始执行工单:%s........\n" %
                        os.path.basename(os.path.dirname(__file__)))
    
    # data传参
    ProxyServer = obj.dict_data.get("ProxyServer")[0]
    ProxyServerPort = obj.dict_data.get("ProxyServerPort")[0]
    RegistrarServer = obj.dict_data.get("RegistrarServer")[0]
    RegistrarServerPort = obj.dict_data.get("RegistrarServerPort")[0]
    OutboundProxy = obj.dict_data.get("OutboundProxy")[0]
    OutboundProxyPort = obj.dict_data.get("OutboundProxyPort")[0]
    X_CT_COM_Standby_ProxyServer = obj.dict_data.get("X_CT_COM_Standby_ProxyServer")[0]
    X_CT_COM_Standby_ProxyServerPort = obj.dict_data.get("X_CT_COM_Standby_ProxyServerPort")[0]
    X_CT_COM_Standby_RegistrarServer = obj.dict_data.get("X_CT_COM_Standby_RegistrarServer")[0]
    X_CT_COM_Standby_RegistrarServerPort = obj.dict_data.get("X_CT_COM_Standby_RegistrarServerPort")[0]
    X_CT_COM_Standby_OutboundProxy = obj.dict_data.get("X_CT_COM_Standby_OutboundProxy")[0]
    X_CT_COM_Standby_OutboundProxyPort = obj.dict_data.get("X_CT_COM_Standby_OutboundProxyPort")[0]
    AuthUserName1 = obj.dict_data.get("AuthUserName1")[0]
    AuthPassword1 = obj.dict_data.get("AuthPassword1")[0]
    PVC_OR_VLAN = obj.dict_data.get("PVC_OR_VLAN")[0]    # ADSL上行只关心PVC值,LAN和EPON上行则关心VLAN值
    X_CT_COM_ServiceList = obj.dict_data.get("X_CT_COM_ServiceList")[0]
    WANEnable_Switch = obj.dict_data.get("WANEnable_Switch")[0]
    
    # "InternetGatewayDevice.Services.VoiceService.1." 
    dict_voiceservice = {"VoiceProfile.1.SIP.ProxyServer":[1, ProxyServer],
                         "VoiceProfile.1.SIP.ProxyServerPort":[1, ProxyServerPort],
                         "VoiceProfile.1.SIP.ProxyServerTransport":[0, "Null"],
                         "VoiceProfile.1.SIP.RegistrarServer":[1, RegistrarServer],
                         "VoiceProfile.1.SIP.RegistrarServerPort":[1, RegistrarServerPort],
                         "VoiceProfile.1.SIP.RegistrarServerTransport":[0, "Null"],
                         "VoiceProfile.1.SIP.OutboundProxy":[1, OutboundProxy],
                         "VoiceProfile.1.SIP.OutboundProxyPort":[1, OutboundProxyPort],
                         "VoiceProfile.1.SIP.X_CT-COM_Standby-ProxyServer":[1, X_CT_COM_Standby_ProxyServer],
                         "VoiceProfile.1.SIP.X_CT-COM_Standby-ProxyServerPort":[1, X_CT_COM_Standby_ProxyServerPort],
                         "VoiceProfile.1.SIP.X_CT-COM_Standby-ProxyServerTransport":[0, "Null"],
                         "VoiceProfile.1.SIP.X_CT-COM_Standby-RegistrarServer":[1, X_CT_COM_Standby_RegistrarServer],
                         "VoiceProfile.1.SIP.X_CT-COM_Standby-RegistrarServerPort":[1, X_CT_COM_Standby_RegistrarServerPort],
                         "VoiceProfile.1.SIP.X_CT-COM_Standby-RegistrarServerTransport":[0, "Null"],
                         "VoiceProfile.1.SIP.X_CT-COM_Standby-OutboundProxy":[1, X_CT_COM_Standby_OutboundProxy],
                         "VoiceProfile.1.SIP.X_CT-COM_Standby-OutboundProxyPort":[1, X_CT_COM_Standby_OutboundProxyPort],
                         "VoiceProfile.1.SIP.UserAgentDomain":[0, "Null"],
                         "VoiceProfile.1.SIP.UserAgentPort":[0, "Null"],
                         "VoiceProfile.1.SIP.UserAgentTransport":[0, "Null"],
                         "VoiceProfile.1.SIP.VLANIDMark":[0, "Null"],
                         "VoiceProfile.1.SIP.X_CT-COM_802-1pMark":[0, "Null"],
                         "VoiceProfile.1.SIP.DSCPMark":[0, "Null"],  
                         "VoiceProfile.1.SIP.X_CT-COM_HeartbeatSwitch":[0, "Null"],
                         "VoiceProfile.1.SIP.X_CT-COM_HeartbeatCycle":[0, "Null"],
                         "VoiceProfile.1.SIP.X_CT-COM_HeartbeatCount":[0, "Null"],  
                         "VoiceProfile.1.SIP.X_CT-COM_SessionUpdateTimer":[0, "Null"],
                         "VoiceProfile.1.SIP.RegisterRetryInterval":[0, "Null"],
                         "VoiceProfile.1.SIP.RegisterExpires":[0, "Null"],
                         "VoiceProfile.1.SIP.ImplicitRegistrationEnable":[0, "Null"],                            
                         "VoiceProfile.1.Line.1.SIP.AuthUserName":[1, AuthUserName1],
                         "VoiceProfile.1.Line.1.SIP.AuthPassword":[1, AuthPassword1],
                         "VoiceProfile.1.Line.2.SIP.AuthUserName":[0, "Null"],
                         "VoiceProfile.1.Line.2.SIP.AuthPassword":[0, "Null"],
                         "VoiceProfile.1.Line.1.Enable":[1, "Enabled"],
                         "VoiceProfile.1.Line.2.Enable":[0, "Enabled"]}
    
    # 对X_CT_COM_LanInterface重新解析,兼容GUI或RF传参数LAN1,lan1格式
    #ret, X_CT_COM_LanInterface = ParseLANName(X_CT_COM_LanInterface)
    #if ret == ERR_FAIL:
    #    info = u'输入的X_CT_COM_LanInterface参数错误'
    #    obj.dict_ret.update(str_result=obj.dict_ret["str_result"] + info)
    #    return ret_res
    
    
    # WANDSLLinkConfig节点参数
    if PVC_OR_VLAN == "":
        PVC_OR_VLAN_flag = 0
    else:
        PVC_OR_VLAN_flag = 1
        
    dict_wanlinkconfig = {'X_CT-COM_Enable':[0, 'Null'],
                          'X_CT-COM_Mode':[PVC_OR_VLAN_flag, '2'],
                          'X_CT-COM_VLANIDMark':[PVC_OR_VLAN_flag, PVC_OR_VLAN],
                          'X_CT-COM_802-1pMark':[1, '0']}
    
    # WANPPPConnection节点参数
    # 注意:X_CT-COM_IPMode节点有些V4版本没有做,所以不能使能为1.实际贝曼工单也是没有下发的
    dict_wanpppconnection = {}
    
    # WANIPConnection节点参数
    dict_wanipconnection = {'Enable':[1, '1'],
                            'ConnectionType':[1, 'IP_Routed'], 
                            'Name':[0, 'Null'],
                            'NATEnabled':[0, 'Null'], 
                            'AddressingType':[1, 'DHCP'],
                            'ExternalIPAddress':[0, '10.10.10.10'], 
                            'SubnetMask':[0, '255.255.255.0'],
                            'DefaultGateway':[0, '10.10.10.1'], 
                            'DNSEnabled':[0, 'Null'],
                            'DNSServers':[0, '10.10.10.2'], 
                            'X_CT-COM_LanInterface':[0, "Null"], 
                            'X_CT-COM_ServiceList':[1, X_CT_COM_ServiceList]}
    
    # 执行VOIP开通工单
    ret, ret_data = VOIP(obj, sn, WANEnable_Switch, DeviceType, 
                        AccessMode, PVC_OR_VLAN,
                        dict_voiceservice,
                        dict_wanlinkconfig, 
                        dict_wanpppconnection, dict_wanipconnection,
                        rollbacklist=rollbacklist)
    
    # 将工单脚本执行结果返回到OBJ的结果中
    obj.dict_ret.update(str_result=obj.dict_ret["str_result"] + ret_data)
    
    # 如果执行失败，统一调用回退机制（缺省是关闭的）
    if ret == ERR_FAIL:
        ret_rollback, ret_data_rollback = rollback(sn, rollbacklist, obj)
        obj.dict_ret.update(str_result=obj.dict_ret["str_result"] + ret_data_rollback)
    
    info = u"工单:%s执行结束\n" % os.path.basename(os.path.dirname(__file__))
    obj.dict_ret.update(str_result=obj.dict_ret["str_result"] + info)    
    return ret

if __name__ == '__main__':
    log_dir = g_prj_dir
    log.start(name="nwf", directory=log_dir, level="DebugWarn")
    log.set_file_id(testcase_name="tr069")    
    
    obj = MsgWorklistExecute(id_="1")
    obj.sn = "2013012901"

    dict_data = {"ProxyServer":("172.24.55.67","1"),
                "ProxyServerPort":("5060","2"),
                "RegistrarServer":("172.24.55.67","3"),
                "RegistrarServerPort":("5060","4"),
                "OutboundProxy":("0.0.0.0","5"),
                "OutboundProxyPort":("5060","6"),
                "X_CT_COM_Standby_ProxyServer":("172.24.55.67","7"),
                "X_CT_COM_Standby_ProxyServerPort":("5060","8"),
                "X_CT_COM_Standby_RegistrarServer":("172.24.55.67","9"),
                "X_CT_COM_Standby_RegistrarServerPort":("5060","10"),
                "X_CT_COM_Standby_OutboundProxy":("0.0.0.0","11"),
                "X_CT_COM_Standby_OutboundProxyPort":("5060","12"),
                "AuthUserName1":("55511021","13"),
                "AuthPassword1":("55511021","14"),
                "AuthUserName2":("55511022","15"),
                "AuthPassword2":("55511022","16"),
                "PVC_OR_VLAN":("63", "17"),
                "X_CT_COM_ServiceList":("VOIP", "18"),
                "WANEnable_Switch":("1", "19")}

    obj.dict_data = dict_data
    try:
        ret = test_script(obj)
        if ret == ERR_SUCCESS:
            print u"测试成功"
        else:
            print u"测试失败"
        print "****************************************"
        print obj.dict_ret["str_result"]
    except Exception, e:
        print u"测试异常"