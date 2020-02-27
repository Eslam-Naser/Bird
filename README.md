
# Bird [ Under Development ]

API Agent for Libvirt for easier management and extended functionalities 

```python
vm = VM()
print(json.dumps(vm.info('kube-2'), indent=4, sort_keys=True))
```

```json
{
    "arch": "x86_64",
    "cpuModel": "Broadwell-IBRS",
    "currentMemory": "4194304",
    "disks": [
        {
            "bus": "0x00",
            "dev": "vda",
            "device_": "disk",
            "domain": "0x0000",
            "file": "/var/lib/libvirt/images/kube-2/kube-2.qcow2",
            "function": "0x0",
            "name": "virtio-disk0",
            "slot": "0x07",
            "type": "pci",
            "type_": "file"
        },
        {
            "bus": "0x00",
            "dev": "vdb",
            "device_": "disk",
            "domain": "0x0000",
            "file": "/var/lib/libvirt/images/kube-2.img",
            "function": "0x0",
            "name": "virtio-disk1",
            "slot": "0x09",
            "type": "pci",
            "type_": "file"
        }
    ],
    "emulator": "/usr/bin/kvm-spice",
    "graphicsAutoport": "yes",
    "graphicsConnectionString": "spice://127.0.0.1:5906",
    "graphicsListenAddress": "127.0.0.1",
    "graphicsPort": "5906",
    "graphicsType": "spice",
    "id": "90",
    "interfaces": [
        {
            "address": "52:54:00:fa:ba:cb",
            "bridge": "virbr0",
            "bus": "0x00",
            "dev": "vnet6",
            "domain": "0x0000",
            "function": "0x0",
            "name": "net0",
            "network": "default",
            "slot": "0x03",
            "type": "pci",
            "type_": "network"
        },
        {
            "address": "52:54:00:09:65:5a",
            "bridge": "virbr0",
            "bus": "0x00",
            "dev": "vnet7",
            "domain": "0x0000",
            "function": "0x0",
            "name": "net1",
            "network": "default",
            "slot": "0x0b",
            "type": "pci",
            "type_": "network"
        }
    ],
    "memory": "4194304",
    "memoryStatus": {
        "actual": 4194304,
        "available": 4042772,
        "major_fault": 0,
        "minor_fault": 0,
        "rss": 1635256,
        "swap_in": 0,
        "swap_out": 0,
        "unused": 3977668
    },
    "name": "kube-2",
    "state": "running",
    "uuid": "26248c44-f414-493e-a60f-743e2e3b30e3",
    "vcpu": "4"
}
```

```python
print(json.dumps(host.info(), indent=4, sort_keys=True))
```

```json
{
    "CPUStats": {
        "idle": "2035276530000000",
        "iowait": "41330000000",
        "kernel": "8674350000000",
        "user": "19780430000000"
    },
    "CPUs": 32,
    "canonicalURI": "qemu:///system",
    "cellsFreeMemory": {
        "Node-0": "14164525056 bytes free memory",
        "Node-1": "21127049216 bytes free memory"
    },
    "freeMemory": 35291574272,
    "freePages": {
        "0": {
            "2048": 0
        },
        "1": {
            "2048": 0
        }
    },
    "hostname": "kvm.linux.com",
    "isConnectionAlive": true,
    "isConnectionEncrypted": false,
    "isConnectionSecure": true,
    "libVersion": "1003001",
    "maxVcpu": 16,
    "memorySize": "257565MB",
    "mhzOfCPUs": 3200,
    "model": "x86_64",
    "numberOfCPUCoresPerSocket": 8,
    "numberOfCPUSockets": 1,
    "numberOfCPUThreadsPerCore": 2,
    "numberOfCPUs": 32,
    "numberOfNUMANodes": 2,
    "securityModel": "apparmor 0",
    "version": "2005000",
    "virtualizationType": "QEMU"
}
```

