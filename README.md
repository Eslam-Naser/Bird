
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
    "name": "kube-2",
    "uuid": "26248c44-f414-493e-a60f-743e2e3b30e3",
    "vcpu": "4",
    "vncListenAddress": "127.0.0.1",
    "vncPort": "5906"
}
```