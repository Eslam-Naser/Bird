import libvirt
import sys
import json

class Main:
    """

    """

    def __init__(self):
        pass

    def connection(self, qemu_connection='qemu:///system'):
        conn = libvirt.open(qemu_connection)
        if conn is None:
            sys.stderr.write('Failed to open connection to: ' + qemu_connection)
            exit(1)
        else:
            return conn

    def runcommand(self, cmd):
        import subprocess
        info = {}
        proc = subprocess.Popen(cmd,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True,
                                universal_newlines=True)
        std_out, std_err = proc.communicate()
        info['exitstatus'] = proc.returncode
        info['stdout'] = std_out.rstrip()
        info['stderr'] = std_err.rstrip()
        ## Python's rstrip() method
        # strips all kinds of trailing whitespace by default, not just one newline

        return info
    # print(main.runcommand('ip a'))


class Namespace:
    """Class for Namespaces Methods"""

    def __init__(self):
        pass

    def ns_list(self):
        pass

    def ns_create(self):
        pass

    def ns_info(self):
        pass


class VM:
    """
    Class for vm operations
    """

    def __init__(self):
        pass

    connection = Main().connection()

    def list(self, connection=connection):
        list = connection.listDefinedDomains()
        return list

    def info(self, vm_name, connection=connection):
        from xml.dom import minidom
        info = {}
        vm_ = connection.lookupByName(vm_name)
        if vm_ == None:
            print('Failed to find the domain ' + vm_name, file=sys.stderr)

        raw_xml = vm_.XMLDesc(0)
        xml = minidom.parseString(raw_xml)
        info['memory'] = (xml.getElementsByTagName('memory')[0].firstChild.data)
        info['currentMemory'] = (xml.getElementsByTagName('currentMemory')[0].firstChild.data)
        info['vcpu'] = (xml.getElementsByTagName('vcpu')[0].firstChild.data)
        info['name'] = (xml.getElementsByTagName('name')[0].firstChild.data)
        info['uuid'] = (xml.getElementsByTagName('uuid')[0].firstChild.data)
        info['emulator']   = (xml.getElementsByTagName('emulator')[0].firstChild.data)
        info['cpuModel']   = (xml.getElementsByTagName('model')[0].firstChild.data)
        info['disks']      = []
        info['interfaces'] = []

        os = xml.getElementsByTagName('type')
        for o in os:
            info['arch'] = o.getAttribute('arch')

        os = xml.getElementsByTagName('graphics')
        for o in os:
            info['vncPort'] = o.getAttribute('port')
            info['vncListenAddress'] = o.getAttribute('listen')

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

print(json.dumps(vm.info('kube-2'), indent=4, sort_keys=True))

