from main import Main
import libvirt
import json
from xml.dom import minidom


class VM:
    """
    Class for vm operations
    """

    def __init__(self, connection=Main().connection()):
        self.connection = connection

    def list(self):
        list = self.connection.listDefinedDomains()
        return list

    def exists(self):
        list = self.connection.listDefinedDomains()
        print(list)

    def info(self, vm_name):
        info = {}
        vm_ = self.connection.lookupByName(vm_name)
        if vm_ == None:
            print('Failed to find the domain ' + vm_name, file=sys.stderr)
            exit(1)

        state, reason = vm_.state()
        if state == libvirt.VIR_DOMAIN_NOSTATE:
            info['state'] = 'noState'
        elif state == libvirt.VIR_DOMAIN_RUNNING:
            info['state'] = 'running'
        elif state == libvirt.VIR_DOMAIN_BLOCKED:
            info['state'] = 'blocked'
        elif state == libvirt.VIR_DOMAIN_PAUSED:
            info['state'] = 'paused'
        elif state == libvirt.VIR_DOMAIN_SHUTDOWN:
            info['state'] = 'shutdown'
        elif state == libvirt.VIR_DOMAIN_SHUTOFF:
            info['state'] = 'shutoff'
        elif state == libvirt.VIR_DOMAIN_CRASHED:
            info['state'] = 'crashed'
        elif state == libvirt.VIR_DOMAIN_PMSUSPENDED:
            info['state'] = 'pmSuspended'
        else:
            info['state'] = 'unknown'
            #print('The reason code is ' + str(reason))


        raw_xml = vm_.XMLDesc(0)
        xml = minidom.parseString(raw_xml)
        info['memory'] = (xml.getElementsByTagName('memory')[0].firstChild.data)
        info['currentMemory'] = (xml.getElementsByTagName('currentMemory')[0].firstChild.data)
        info['vcpu'] = (xml.getElementsByTagName('vcpu')[0].firstChild.data)
        info['name'] = (xml.getElementsByTagName('name')[0].firstChild.data)
        info['uuid'] = (xml.getElementsByTagName('uuid')[0].firstChild.data)
        info['memoryStatus']    = vm_.memoryStats()
        info['emulator']   = (xml.getElementsByTagName('emulator')[0].firstChild.data)
        #info['cpuModel']   = (xml.getElementsByTagName('model')[0].firstChild)  ## Needs to be fixed
        info['disks']      = []
        info['interfaces'] = []

        id = vm_.ID()
        if id == -1:
            info['id'] = ''
        else:
            info['id'] = str(vm_.ID())

        os = xml.getElementsByTagName('type')
        for o in os:
            info['arch'] = o.getAttribute('arch')

        os = xml.getElementsByTagName('graphics')
        for o in os:
            info['graphicsType'] = o.getAttribute('type')
            info['graphicsPort'] = o.getAttribute('port')
            info['graphicsAutoport'] = o.getAttribute('autoport')
            info['graphicsListenAddress'] = o.getAttribute('listen')
            info['graphicsConnectionString'] = 'spice://' + info['graphicsListenAddress'] +':' + info['graphicsPort']

        disk_types = (xml.getElementsByTagName('disk'))
        for disk in disk_types:
            disk_nodes = disk.childNodes
            h = {}
            for disk_node in disk_nodes:
                if disk_node.nodeName[0:1] != '#':
                    for attr in disk_node.attributes.keys():
                        h[disk_node.attributes[attr].name] = disk_node.attributes[attr].value
                        h['type_'] = disk.getAttribute('type')
                        h['device_'] = disk.getAttribute('device')
            info['disks'].append(h)

        net_interfaces = (xml.getElementsByTagName('interface'))
        for int in net_interfaces:
            int_nodes = int.childNodes
            h = {}
            for int_node in int_nodes:
                if int_node.nodeName[0:1] != '#':
                    for attr in int_node.attributes.keys():
                        h[int_node.attributes[attr].name] = int_node.attributes[attr].value
                        h['type_'] = int.getAttribute('type')
            info['interfaces'].append(h)

        # https://libvirt.org/docs/libvirt-appdev-guide-python/en-US/html/libvirt_application_development_guide_using_python-Guest_Domains-Device_Config.html
        return info

### Examples ###


vm = VM()
#print(vm.list())
#print(vm.info('kube-2'))
#print(vm.info('kube-2').get('disks')[0])
#(vm.info('kube-2').get('interfaces'))
#print(vm.info('kube-2').get('vncPort'))

print(json.dumps(vm.info('CentOS-7-1907'), indent=4, sort_keys=True))

