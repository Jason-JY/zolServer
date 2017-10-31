# coding: utf-8
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
class para:
    name="0"
    attr="0"
class detail(object):
    def getcpu_main(self):
        from zolServer import models
        box = models.cpu_list_test.objects.all()
        return box

    def getboard_main(self):
        from zolServer import models
        box = models.board_list_test.objects.all()
        return box

    def getmem_main(self):
        from zolServer import models
        box = models.mem_list_test.objects.all()
        return box

    def getgraphic_main(self):
        from zolServer import models
        box = models.graphic_list_test.objects.all()
        return box

    def getpower_main(self):
        from zolServer import models
        box = models.power_list_test.objects.all()
        return box
    def getradiator_main(self):
        from zolServer import models
        box = models.radiator_list_test.objects.all()
        return box
    def getcpu_detail(self,id):

        from zolServer import models
        box = models.cpu_detail_test.objects.get(id=id)
        test = []
        if box.id != " ":
            x = para()
            x.name = "id"
            x.attr = box.id
            test.append(x)
        if box.jbcs != " ":
            x = para()
            x.name = "基本参数"
            x.attr = box.jbcs
            test.append(x)
        if box.sylx != " ":
            x = para()
            x.name = "适用类型"
            x.attr = box.sylx
            test.append(x)
        if box.cpuxl != " ":
            x = para()
            x.name = "cpu系列"
            x.attr = box.cpuxl
            test.append(x)
        if box.zzgy != " ":
            x = para()
            x.name = "制作工艺"
            x.attr = box.zzgy
            test.append(x)
        if box.hxdh != " ":
            x = para()
            x.name = "核心代号"
            x.attr = box.hxdh
            test.append(x)
        if box.cpujg != " ":
            x = para()
            x.name = "cpu架构"
            x.attr = box.cpujg
            test.append(x)
        if box.cclx != " ":
            x = para()
            x.name = "插槽类型"
            x.attr = box.cclx
            test.append(x)
        if box.fzdx != " ":
            x = para()
            x.name = "封装大小"
            x.attr = box.fzdx
            test.append(x)
        if box.bzxs != " ":
            x = para()
            x.name = "包装形式"
            x.attr = box.bzxs
            test.append(x)
        if box.xncs != " ":
            x = para()
            x.name = "性能参数"
            x.attr = box.xncs
            test.append(x)
        if box.cpuzp != " ":
            x = para()
            x.name = "cpu主频"
            x.attr = box.cpuzp
            test.append(x)
        if box.dtjspl != " ":
            x = para()
            x.name = "动态加速频率"
            x.attr = box.dtjspl
            test.append(x)
        if box.hxsl != " ":
            x = para()
            x.name = "核心数量"
            x.attr = box.hxsl
            test.append(x)

        if box.xcsl != " ":
            x = para()
            x.name = "线程数量"
            x.attr = box.xcsl
            test.append(x)
        if box.sjhc != " ":
            x = para()
            x.name = "三级缓存"
            x.attr = box.sjhc
            test.append(x)
        if box.zxgg != " ":
            x = para()
            x.name = "总线规格"
            x.attr = box.zxgg
            test.append(x)
        if box.rsjgh != " ":
            x = para()
            x.name = "热设计功耗"
            x.attr = box.rsjgh
            test.append(x)
        if box.nccs != " ":
            x = para()
            x.name = "内存参数"
            x.attr = box.nccs
            test.append(x)
        if box.zczdnc != " ":
            x = para()
            x.name = "支持最大内存"
            x.attr = box.zczdnc
            test.append(x)
        if box.nclx != " ":
            x = para()
            x.name = "内存类型"
            x.attr = box.nclx
            test.append(x)

        if box.ncms != " ":
            x = para()
            x.name = "内存描述"
            x.attr = box.ncms
            test.append(x)
        if box.xkcs != " ":
            x = para()
            x.name = "显卡参数"
            x.attr = box.xkcs
            test.append(x)
        if box.jcxk != " ":
            x = para()
            x.name = "集成显卡"
            x.attr = box.jcxk
            test.append(x)
        if box.xkjbpl != " ":
            x = para()
            x.name = "显卡基本频率"
            x.attr = box.xkjbpl
            test.append(x)
        if box.xkdtpl != " ":
            x = para()
            x.name = "显卡动态频率"
            x.attr = box.xkdtpl
            test.append(x)
        if box.xkqttx != " ":
            x = para()
            x.name = "显卡其它特性"
            x.attr = box.xkqttx
            test.append(x)
        if box.jscs != " ":
            x = para()
            x.name = "技术参数"
            x.attr = box.jscs
            test.append(x)

        if box.rpjsjs != " ":
            x = para()
            x.name = "睿频加速技术"
            x.attr = box.rpjsjs
            test.append(x)
        if box.cxcjs != " ":
            x = para()
            x.name = "超线程技术"
            x.attr = box.cxcjs
            test.append(x)
        if box.xnhjs != " ":
            x = para()
            x.name = "虚拟化技术"
            x.attr = box.xnhjs
            test.append(x)
        if box.zlj != " ":
            x = para()
            x.name = "指令集"
            x.attr = box.zlj
            test.append(x)
        if box.clq_64 != " ":
            x = para()
            x.name = "64位处理器"
            x.attr = box.clq_64
            test.append(x)
        if box.qtjs != " ":
            x = para()
            x.name = "其它技术"
            x.attr = box.qtjs
            test.append(x)
        return test

    def getboard_detail(self,id):
        from zolServer import models
        box = models.board_detail_test.objects.get(id=id)
        test = []
        if box.id != " ":
            x = para()
            x.name = "id"
            x.attr = box.id
            test.append(x)
        if box.zbxp != " ":
            x = para()
            x.name = "主板芯片"
            x.attr = box.zbxp
            test.append(x)
        if box.jcxp != " ":
            x = para()
            x.name = "集成芯片"
            x.attr = box.jcxp
            test.append(x)
        if box.zxpz != " ":
            x = para()
            x.name = "主芯片组"
            x.attr = box.zxpz
            test.append(x)
        if box.xpzms != " ":
            x = para()
            x.name = "芯片组描述"
            x.attr = box.xpzms
            test.append(x)
        if box.xsxp != " ":
            x = para()
            x.name = "显示芯片"
            x.attr = box.xsxp
            test.append(x)
        if box.ypxp != " ":
            x = para()
            x.name = "音频芯片"
            x.attr = box.ypxp
            test.append(x)
        if box.wkxp != " ":
            x = para()
            x.name = "网卡芯片"
            x.attr = box.wkxp
            test.append(x)
        if box.clqgg != " ":
            x = para()
            x.name = "处理器规格"
            x.attr = box.clqgg
            test.append(x)
        if box.cpulx != " ":
            x = para()
            x.name = "CPU类型"
            x.attr = box.cpulx
            test.append(x)
        if box.cpucc != " ":
            x = para()
            x.name = "CPU插槽"
            x.attr = box.cpucc
            test.append(x)
        if box.cpums != " ":
            x = para()
            x.name = "CPU描述"
            x.attr = box.cpums
            test.append(x)
        if box.ncgg != " ":
            x = para()
            x.name = "内存规格"
            x.attr = box.ncgg
            test.append(x)
        if box.nclx != " ":
            x = para()
            x.name = "内存类型"
            x.attr = box.nclx
            test.append(x)
        if box.nccc != " ":
            x = para()
            x.name = "内存插槽"
            x.attr = box.nccc
            test.append(x)
        if box.zdncrl != " ":
            x = para()
            x.name = "最大内存容量"
            x.attr = box.zdncrl
            test.append(x)
        if box.ncms != " ":
            x = para()
            x.name = "内存描述"
            x.attr = box.ncms
            test.append(x)
        if box.kzcc != " ":
            x = para()
            x.name = "扩展插槽"
            x.attr = box.kzcc
            test.append(x)
        if box.pciebz != " ":
            x = para()
            x.name = "PCI_E标准"
            x.attr = box.pciebz
            test.append(x)
        if box.pciecc != " ":
            x = para()
            x.name = "PCI_E插槽"
            x.attr = box.pciecc
            test.append(x)
        if box.pcicc != " ":
            x = para()
            x.name = "PCI插槽"
            x.attr = box.pcicc
            test.append(x)
        if box.ccjk != " ":
            x = para()
            x.name = "存储接口"
            x.attr = box.ccjk
            test.append(x)
        if box.iojk != " ":
            x = para()
            x.name = "I_O接口"
            x.attr = box.iojk
            test.append(x)
        if box.usbjk != " ":
            x = para()
            x.name = "USB接口'"
            x.attr = box.usbjk
            test.append(x)
        if box.hdmijk != " ":
            x = para()
            x.name = "HDMI接口"
            x.attr = box.hdmijk
            test.append(x)
        if box.wdjk != " ":
            x = para()
            x.name = "外接端口"
            x.attr = box.wdjk
            test.append(x)
        if box.ps2jk != " ":
            x = para()
            x.name = "PS_2接口"
            x.attr = box.ps2jk
            test.append(x)
        if box.dyck != " ":
            x = para()
            x.name = "电源插口"
            x.attr = box.dyck
            test.append(x)
        if box.qtjk != " ":
            x = para()
            x.name = "其它接口"
            x.attr = box.qtjk
            test.append(x)
        if box.bx != " ":
            x = para()
            x.name = "板型"
            x.attr = box.bx
            test.append(x)
        if box.zbbx != " ":
            x = para()
            x.name = "主板板型"
            x.attr = box.zbbx
            test.append(x)
        if box.wxcc != " ":
            x = para()
            x.name = "外形尺寸"
            x.attr = box.wxcc
            test.append(x)
        if box.rjgl != " ":
            x = para()
            x.name = "软件管理"
            x.attr = box.rjgl
            test.append(x)
        if box.biosxn != " ":
            x = para()
            x.name = "BIOS性能"
            x.attr = box.biosxn
            test.append(x)
        if box.qtcs != " ":
            x = para()
            x.name = "其它参数"
            x.attr = box.qtcs
            test.append(x)
        if box.dxkjs != " ":
            x = para()
            x.name = "多显卡技术"
            x.attr = box.dxkjs
            test.append(x)
        if box.gdms != " ":
            x = para()
            x.name = "供电模式"
            x.attr = box.gdms
            test.append(x)
        if box.raidgn != " ":
            x = para()
            x.name = "RAID功能"
            x.attr = box.raidgn
            test.append(x)
        if box.qtxn != " ":
            x = para()
            x.name = "其它性能"
            x.attr = box.qtxn
            test.append(x)
        if box.ssrq != " ":
            x = para()
            x.name = "上市日期"
            x.attr = box.ssrq
            test.append(x)
        if box.zbfj != " ":
            x = para()
            x.name = "主板附件"
            x.attr = box.zbfj
            test.append(x)
        if box.bzqd != " ":
            x = para()
            x.name = "包装清单"
            x.attr = box.bzqd
            test.append(x)
        if box.bxxx != " ":
            x = para()
            x.name = "保修信息"
            x.attr = box.bxxx
            test.append(x)
        if box.bxzc != " ":
            x = para()
            x.name = "保修政策"
            x.attr = box.bxzc
            test.append(x)
        if box.zbsj != " ":
            x = para()
            x.name = "质保时间"
            x.attr = box.zbsj
            test.append(x)
        if box.zbbz != " ":
            x = para()
            x.name = "质保备注"
            x.attr = box.zbbz
            test.append(x)
        if box.dhbz != " ":
            x = para()
            x.name = "电话备注"
            x.attr = box.dhbz
            test.append(x)
        if box.xxnr != " ":
            x = para()
            x.name = "详细内容"
            x.attr = box.xxnr
            test.append(x)
        return test
    def getmem_detail(self,id):
        from zolServer import models
        box = models.mem_detail_test.objects.get(id=id)
        test = []
        if box.id != " ":
            x = para()
            x.name = "id"
            x.attr = box.id
            test.append(x)
        if box.jbcs != " ":
            x = para()
            x.name = "基本参数"
            x.attr = box.jbcs
            test.append(x)
        if box.sylx != " ":
            x = para()
            x.name = "适用类型"
            x.attr = box.sylx
            test.append(x)
        if box.ncrl != " ":
            x = para()
            x.name = "内存容量"
            x.attr = box.ncrl
            test.append(x)
        if box.rlms != " ":
            x = para()
            x.name = "容量描述"
            x.attr = box.rlms
            test.append(x)
        if box.nclx != " ":
            x = para()
            x.name = "内存类型"
            x.attr = box.nclx
            test.append(x)
        if box.nczp != " ":
            x = para()
            x.name = "内存主频"
            x.attr = box.nczp
            test.append(x)
        if box.csbz != " ":
            x = para()
            x.name = "传输标准"
            x.attr = box.csbz
            test.append(x)
        if box.zjs != " ":
            x = para()
            x.name = "针脚数"
            x.attr = box.zjs
            test.append(x)
        if box.cclx != " ":
            x = para()
            x.name = "插槽类型"
            x.attr = box.cclx
            test.append(x)
        if box.jscs != " ":
            x = para()
            x.name = "技术参数"
            x.attr = box.jscs
            test.append(x)
        if box.klpz != " ":
            x = para()
            x.name = "颗粒配置"
            x.attr = box.klpz
            test.append(x)

        if box.clyc != " ":
            x = para()
            x.name = "CL延迟"
            x.attr = box.clyc
            test.append(x)
        if box.zzgy != " ":
            x = para()
            x.name = "制作工艺"
            x.attr = box.zzgy
            test.append(x)
        if box.qtcs != " ":
            x = para()
            x.name = "其它参数"
            x.attr = box.qtcs
            test.append(x)
        if box.srp != " ":
            x = para()
            x.name = "散热片"
            x.attr = box.srp
            test.append(x)
        if box.gzdy != " ":
            x = para()
            x.name = "工作电压"
            x.attr = box.gzdy
            test.append(x)
        if box.qtxn != " ":
            x = para()
            x.name = "其它性能"
            x.attr = box.qtxn
            test.append(x)
        if box.qttd != " ":
            x = para()
            x.name = "其它特点"
            x.attr = box.qttd
            test.append(x)
        if box.bxxx != " ":
            x = para()
            x.name = "保修信息"
            x.attr = box.bxxx
            test.append(x)
        if box.bxzc != " ":
            x = para()
            x.name = "保修政策"
            x.attr = box.bxzc
            test.append(x)
        if box.zbsj != " ":
            x = para()
            x.name = "质保时间"
            x.attr = box.zbsj
            test.append(x)
        if box.zbbz != " ":
            x = para()
            x.name = "质保备注"
            x.attr = box.zbbz
            test.append(x)
        if box.dhbz != " ":
            x = para()
            x.name = "电话备注"
            x.attr = box.dhbz
            test.append(x)
        if box.xxnr != " ":
            x = para()
            x.name = "详细内容"
            x.attr = box.xxnr
            test.append(x)
        return test
    def getgraphic_detail(self,id):
        from zolServer import models
        box = models.graphic_detail_test.objects.get(id=id)
        test = []
        if box.id != " ":
            x = para()
            x.name = "id"
            x.attr = box.id
            test.append(x)
        if box.xkhx != " ":
            x = para()
            x.name = "id"
            x.attr = box.xkhx
            test.append(x)
        if box.xpcs != " ":
            x = para()
            x.name = "id"
            x.attr = box.xpcs
            test.append(x)
        if box.xkxp != " ":
            x = para()
            x.name = "id"
            x.attr = box.xkxp
            test.append(x)
        if box.xkxpxl != " ":
            x = para()
            x.name = "id"
            x.attr = box.xkxpxl
            test.append(x)
        if box.zzgy != " ":
            x = para()
            x.name = "id"
            x.attr = box.zzgy
            test.append(x)
        if box.hxdh != " ":
            x = para()
            x.name = "id"
            x.attr = box.hxdh
            test.append(x)
        if box.hxpl != " ":
            x = para()
            x.name = "id"
            x.attr = box.hxpl
            test.append(x)

        if box.cudahx != " ":
            x = para()
            x.name = "id"
            x.attr = box.cudahx
            test.append(x)
        if box.xcgg != " ":
            x = para()
            x.name = "id"
            x.attr = box.xcgg
            test.append(x)
        if box.xcpl != " ":
            x = para()
            x.name = "id"
            x.attr = box.xcpl
            test.append(x)
        if box.xclx != " ":
            x = para()
            x.name = "id"
            x.attr = box.xclx
            test.append(x)
        if box.xcrl != " ":
            x = para()
            x.name = "id"
            x.attr = box.xcrl
            test.append(x)
        if box.xcwk != " ":
            x = para()
            x.name = "id"
            x.attr = box.xcwk
            test.append(x)
        if box.zdfbl != " ":
            x = para()
            x.name = "id"
            x.attr = box.zdfbl
            test.append(x)
        if box.xkjk != " ":
            x = para()
            x.name = "id"
            x.attr = box.xkjk
            test.append(x)

        if box.jklx != " ":
            x = para()
            x.name = "id"
            x.attr = box.jklx
            test.append(x)
        if box.iojk != " ":
            x = para()
            x.name = "id"
            x.attr = box.iojk
            test.append(x)
        if box.dyjk != " ":
            x = para()
            x.name = "id"
            x.attr = box.dyjk
            test.append(x)
        if box.qtcs != " ":
            x = para()
            x.name = "id"
            x.attr = box.qtcs
            test.append(x)
        if box.xslx != " ":
            x = para()
            x.name = "id"
            x.attr = box.xslx
            test.append(x)
        if box.srfs != " ":
            x = para()
            x.name = "id"
            x.attr = box.srfs
            test.append(x)
        if box.api_3d != " ":
            x = para()
            x.name = "id"
            x.attr = box.api_3d
            test.append(x)
        if box.gdms != " ":
            x = para()
            x.name = "id"
            x.attr = box.gdms
            test.append(x)

        if box.zchdcp != " ":
            x = para()
            x.name = "id"
            x.attr = box.zchdcp
            test.append(x)
        if box.zdgh != " ":
            x = para()
            x.name = "id"
            x.attr = box.zdgh
            test.append(x)
        if box.jydy != " ":
            x = para()
            x.name = "id"
            x.attr = box.jydy
            test.append(x)
        if box.qttd != " ":
            x = para()
            x.name = "id"
            x.attr = box.qttd
            test.append(x)
        if box.sssj != " ":
            x = para()
            x.name = "id"
            x.attr = box.sssj
            test.append(x)
        if box.bxxx != " ":
            x = para()
            x.name = "id"
            x.attr = box.bxxx
            test.append(x)
        if box.bxzc != " ":
            x = para()
            x.name = "id"
            x.attr = box.bxzc
            test.append(x)
        if box.zbsj != " ":
            x = para()
            x.name = "id"
            x.attr = box.zbsj
            test.append(x)
        if box.zbbz != " ":
            x = para()
            x.name = "id"
            x.attr = box.zbbz
            test.append(x)
        if box.xxnr != " ":
            x = para()
            x.name = "id"
            x.attr = box.xxnr
            test.append(x)
        return test
    def getpower_detail(self,id):
        from zolServer import models
        box = models.power_detail_test.objects.get(id=id)
        test = []
        if box.id != " ":
            x = para()
            x.name = "id"
            x.attr = box.id
            test.append(x)
        if box.jbcs != " ":
            x = para()
            x.name = "基本参数"
            x.attr = box.jbcs
            test.append(x)
        if box.dylx != " ":
            x = para()
            x.name = "电源类型"
            x.attr = box.dylx
            test.append(x)
        if box.syfw != " ":
            x = para()
            x.name = "适用范围"
            x.attr = box.syfw
            test.append(x)
        if box.dybb != " ":
            x = para()
            x.name = "电梯版本"
            x.attr = box.dybb
            test.append(x)
        if box.cxlx != " ":
            x = para()
            x.name = "出线类型"
            x.attr = box.cxlx
            test.append(x)
        if box.edgl != " ":
            x = para()
            x.name = "额定功率"
            x.attr = box.edgl
            test.append(x)
        if box.fsms != " ":
            x = para()
            x.name = "风扇描述"
            x.attr = box.fsms
            test.append(x)
        if box.dycc != " ":
            x = para()
            x.name = "电源尺寸"
            x.attr = box.dycc
            test.append(x)
        if box.dyjk != " ":
            x = para()
            x.name = "电源接口"
            x.attr = box.dyjk
            test.append(x)
        if box.zbjk != " ":
            x = para()
            x.name = "主板接口"
            x.attr = box.zbjk
            test.append(x)
        if box.cpujk44 != " ":
            x = para()
            x.name = "cpu接口44"
            x.attr = box.cpujk44
            test.append(x)
        if box.cpujkf != " ":
            x = para()
            x.name = "cpu接口方"
            x.attr = box.cpujkf
            test.append(x)
        if box.xkjk62 != " ":
            x = para()
            x.name = "显卡接口62"
            x.attr = box.xkjk62
            test.append(x)
        if box.xkjk6 != " ":
            x = para()
            x.name = "显卡接口6"
            x.attr = box.xkjk6
            test.append(x)
        if box.ypjk != " ":
            x = para()
            x.name = "硬盘接口"
            x.attr = box.ypjk
            test.append(x)
        if box.rqjk != " ":
            x = para()
            x.name = "软驱接口"
            x.attr = box.rqjk
            test.append(x)
        if box.gdjk != " ":
            x = para()
            x.name = "供电接口"
            x.attr = box.gdjk
            test.append(x)
        if box.xncs != " ":
            x = para()
            x.name = "性能参数"
            x.attr = box.xncs
            test.append(x)
        if box.jlsc != " ":
            x = para()
            x.name = "交流输入"
            x.attr = box.jlsc
            test.append(x)
        if box.scdl3_3V != " ":
            x = para()
            x.name = "输出电流3_3V"
            x.attr = box.scdl3_3V
            test.append(x)
        if box.scdl5V != " ":
            x = para()
            x.name = "输出电流5V"
            x.attr = box.scdl5V
            test.append(x)
        if box.scdl5Vsb != " ":
            x = para()
            x.name = "输出电流5Vsb"
            x.attr = box.scdl5Vsb
            test.append(x)
        if box.scdl12V != " ":
            x = para()
            x.name = "输出电流12V"
            x.attr = box.scdl12V
            test.append(x)

        if box.scdl_12V != " ":
            x = para()
            x.name = "输出电流_12V"
            x.attr = box.scdl_12V
            test.append(x)
        if box.qtcs != " ":
            x = para()
            x.name = "其他参数"
            x.attr = box.qtcs
            test.append(x)
        if box.rfclx != " ":
            x = para()
            x.name = "PFC类型"
            x.attr = box.rfclx
            test.append(x)
        if box.bhgn != " ":
            x = para()
            x.name = "保护功能"
            x.attr = box.bhgn
            test.append(x)
        if box.zhxl != " ":
            x = para()
            x.name = "转换效率"
            x.attr = box.zhxl
            test.append(x)
        if box.plusrz != " ":
            x = para()
            x.name = "PLUS认证_80"
            x.attr = box.plusrz
            test.append(x)
        if box.agrz != " ":
            x = para()
            x.name = "安规认证"
            x.attr = box.agrz
            test.append(x)
        if box.dyfj != " ":
            x = para()
            x.name = "电源附件"
            x.attr = box.dyfj
            test.append(x)

        if box.dyqd != " ":
            x = para()
            x.name = "包装清单"
            x.attr = box.dyqd
            test.append(x)
        if box.bxxx != " ":
            x = para()
            x.name = "保修信息"
            x.attr = box.bxxx
            test.append(x)
        if box.bxzc != " ":
            x = para()
            x.name = "保修政策"
            x.attr = box.bxzc
            test.append(x)
        if box.zbsj != " ":
            x = para()
            x.name = "质保时间"
            x.attr = box.zbsj
            test.append(x)
        if box.zbbz != " ":
            x = para()
            x.name = "质保备注"
            x.attr = box.zbbz
            test.append(x)
        if box.dhbz != " ":
            x = para()
            x.name = "电话备注"
            x.attr = box.dhbz
            test.append(x)
        if box.xxnr != " ":
            x = para()
            x.name = "详细内容"
            x.attr = box.xxnr
            test.append(x)
        return test
    def getradiator_detail(self,id):
        from zolServer import models
        box = models.radiato_detail_test.objects.get(id=id)
        test = []
        if box.jbcs != " ":
            x = para()
            x.name = "基本参数"
            x.attr = box.id
            test.append(x)
        if box.srqlx != " ":
            x = para()
            x.name = "散热器类型"
            x.attr = box.srqlx
            test.append(x)
        if box.srfs != " ":
            x = para()
            x.name = "散热方式"
            x.attr = box.srfs
            test.append(x)
        if box.flcs != " ":
            x = para()
            x.name = "风冷参数"
            x.attr = box.flcs
            test.append(x)

        if box.fscc != " ":
            x = para()
            x.name = "风扇尺寸"
            x.attr = box.fscc
            test.append(x)
        if box.zclx != " ":
            x = para()
            x.name = "轴承类型"
            x.attr = box.zclx
            test.append(x)
        if box.zsms != " ":
            x = para()
            x.name = "转数描述"
            x.attr = box.zsms
            test.append(x)
        if box.zdfl != " ":
            x = para()
            x.name = "最大风量"
            x.attr = box.zdfl
            test.append(x)
        if box.fy != " ":
            x = para()
            x.name = "风压"
            x.attr = box.fy
            test.append(x)
        if box.zy != " ":
            x = para()
            x.name = "噪音"
            x.attr = box.zy
            test.append(x)
        if box.srqfj != " ":
            x = para()
            x.name = "散热器附件"
            x.attr = box.srqfj
            test.append(x)
        if box.bzqd != " ":
            x = para()
            x.name = "包装清单"
            x.attr = box.bzqd
            test.append(x)

        if box.bxxx != " ":
            x = para()
            x.name = "保修信息"
            x.attr = box.bxxx
            test.append(x)
        if box.bxzc != " ":
            x = para()
            x.name = "保修政策"
            x.attr = box.bxzc
            test.append(x)
        if box.zbsj != " ":
            x = para()
            x.name = "质保时间"
            x.attr = box.zbsj
            test.append(x)
        if box.zbbz != " ":
            x = para()
            x.name = "质保备注"
            x.attr = box.zbbz
            test.append(x)
        if box.dhbz != " ":
            x = para()
            x.name = "电话备注"
            x.attr = box.dhbz
            test.append(x)
        if box.xxnr != " ":
            x = para()
            x.name = "详细内容"
            x.attr = box.xxnr
            test.append(x)
        return test