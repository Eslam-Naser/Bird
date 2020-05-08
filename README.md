
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
    "canonicalURI": "qemu:///system",
    "disks": {
        "sda": {
            "model": "ST2000DM008-2FR1",
            "size": "1.82 TiB",
            "size_bytes": 2000398934016,
            "vendor": "ATA"
        },
        "sdb": {
            "model": "WDC  WDS500G2B0A",
            "size": "465.76 GiB",
            "size_bytes": 500107862016,
            "vendor": "ATA"
        },
        "sdc": {
            "model": "Flash Reader",
            "size": "0 bytes",
            "size_bytes": 0,
            "vendor": "Multi"
        }
    },
    "dmi": {
        "bios": {
            "release_date": "11/13/2019",
            "vendor": "American Megatrends Inc.",
            "version": "5406"
        },
        "board": {
            "asset_tag": "Default string",
            "manufacturer": "ASUSTeK COMPUTER INC.",
            "product": "ROG STRIX X470-F GAMING"
        },
        "chassis": {
            "asset_tag": "Default string",
            "type": "Desktop"
        },
        "manufacturer": "System manufacturer",
        "product": {
            "name": "System Product Name"
        }
    },
    "facterversion": "3.10.0",
    "filesystems": "btrfs,ext2,ext3,ext4,squashfs,vfat",
    "fips_enabled": false,
    "identity": {
        "gid": 1000,
        "group": "eslam",
        "privileged": false,
        "uid": 1000,
        "user": "eslam"
    },
    "isConnectionAlive": true,
    "isConnectionEncrypted": false,
    "isConnectionSecure": true,
    "is_virtual": false,
    "kernel": "Linux",
    "kernelmajversion": "5.3",
    "kernelrelease": "5.3.0-51-generic",
    "kernelversion": "5.3.0",
    "libVersion": "4000000",
    "load_averages": {
        "15m": 0.32,
        "1m": 0.42,
        "5m": 0.33
    },
    "memory": {
        "swap": {
            "available": "1.86 GiB",
            "available_bytes": 1998581760,
            "capacity": "0%",
            "total": "1.86 GiB",
            "total_bytes": 1998581760,
            "used": "0 bytes",
            "used_bytes": 0
        },
        "system": {
            "available": "24.52 GiB",
            "available_bytes": 26332528640,
            "capacity": "21.72%",
            "total": "31.33 GiB",
            "total_bytes": 33640300544,
            "used": "6.81 GiB",
            "used_bytes": 7307771904
        }
    },
    "model": "x86_64",
    "mountpoints": {
        "/": {
            "available": "220.95 GiB",
            "available_bytes": 237248270336,
            "capacity": "29.61%",
            "device": "/dev/sdb5",
            "filesystem": "ext4",
            "options": [
                "rw",
                "relatime",
                "errors=remount-ro"
            ],
            "size": "313.91 GiB",
            "size_bytes": 337056657408,
            "used": "92.95 GiB",
            "used_bytes": 99808387072
        },
        "/boot/efi": {
            "available": "64.17 MiB",
            "available_bytes": 67286016,
            "capacity": "32.45%",
            "device": "/dev/sdb2",
            "filesystem": "vfat",
            "options": [
                "rw",
                "relatime",
                "fmask=0077",
                "dmask=0077",
                "codepage=437",
                "iocharset=iso8859-1",
                "shortname=mixed",
                "errors=remount-ro"
            ],
            "size": "95.00 MiB",
            "size_bytes": 99614720,
            "used": "30.83 MiB",
            "used_bytes": 32328704
        },
        "/dev/shm": {
            "available": "15.60 GiB",
            "available_bytes": 16754921472,
            "capacity": "0.39%",
            "device": "tmpfs",
            "filesystem": "tmpfs",
            "options": [
                "rw",
                "nosuid",
                "nodev"
            ],
            "size": "15.66 GiB",
            "size_bytes": 16820150272,
            "used": "62.21 MiB",
            "used_bytes": 65228800
        },
        "/media/eslam/620CBE0C0CBDDB6D": {
            "available": "98.57 GiB",
            "available_bytes": 105833750528,
            "capacity": "31.24%",
            "device": "/dev/sdb4",
            "filesystem": "fuseblk",
            "options": [
                "rw",
                "nosuid",
                "nodev",
                "relatime",
                "user_id=0",
                "group_id=0",
                "default_permissions",
                "allow_other",
                "blksize=4096"
            ],
            "size": "143.34 GiB",
            "size_bytes": 153908932608,
            "used": "44.77 GiB",
            "used_bytes": 48075182080
        },
        "/media/eslam/MyData1": {
            "available": "102.50 GiB",
            "available_bytes": 110057820160,
            "capacity": "89.99%",
            "device": "/dev/sda2",
            "filesystem": "fuseblk",
            "options": [
                "rw",
                "nosuid",
                "nodev",
                "relatime",
                "user_id=0",
                "group_id=0",
                "default_permissions",
                "allow_other",
                "blksize=4096"
            ],
            "size": "1.00 TiB",
            "size_bytes": 1099511623680,
            "used": "921.50 GiB",
            "used_bytes": 989453803520
        },
        "/media/eslam/MyData2": {
            "available": "479.61 GiB",
            "available_bytes": 514976186368,
            "capacity": "42.84%",
            "device": "/dev/sda3",
            "filesystem": "fuseblk",
            "options": [
                "rw",
                "nosuid",
                "nodev",
                "relatime",
                "user_id=0",
                "group_id=0",
                "default_permissions",
                "allow_other",
                "blksize=4096"
            ],
            "size": "839.00 GiB",
            "size_bytes": 900869386240,
            "used": "359.39 GiB",
            "used_bytes": 385893199872
        },
        "/run": {
            "available": "3.13 GiB",
            "available_bytes": 3356962816,
            "capacity": "0.21%",
            "device": "tmpfs",
            "filesystem": "tmpfs",
            "options": [
                "rw",
                "nosuid",
                "noexec",
                "relatime",
                "size=3285188k",
                "mode=755"
            ],
            "size": "3.13 GiB",
            "size_bytes": 3364032512,
            "used": "6.74 MiB",
            "used_bytes": 7069696
        },
        "/run/lock": {
            "available": "5.00 MiB",
            "available_bytes": 5238784,
            "capacity": "0.08%",
            "device": "tmpfs",
            "filesystem": "tmpfs",
            "options": [
                "rw",
                "nosuid",
                "nodev",
                "noexec",
                "relatime",
                "size=5120k"
            ],
            "size": "5.00 MiB",
            "size_bytes": 5242880,
            "used": "4.00 KiB",
            "used_bytes": 4096
        },
        "/run/user/1000": {
            "available": "3.13 GiB",
            "available_bytes": 3363991552,
            "capacity": "0.00%",
            "device": "tmpfs",
            "filesystem": "tmpfs",
            "options": [
                "rw",
                "nosuid",
                "nodev",
                "relatime",
                "size=3285184k",
                "mode=700",
                "uid=1000",
                "gid=1000"
            ],
            "size": "3.13 GiB",
            "size_bytes": 3364028416,
            "used": "36.00 KiB",
            "used_bytes": 36864
        },
        "/snap/core18/1705": {
            "available": "0 bytes",
            "available_bytes": 0,
            "capacity": "100%",
            "device": "/dev/loop5",
            "filesystem": "squashfs",
            "options": [
                "ro",
                "nodev",
                "relatime"
            ],
            "size": "55.00 MiB",
            "size_bytes": 57671680,
            "used": "55.00 MiB",
            "used_bytes": 57671680
        },
        "/snap/core18/1754": {
            "available": "0 bytes",
            "available_bytes": 0,
            "capacity": "100%",
            "device": "/dev/loop4",
            "filesystem": "squashfs",
            "options": [
                "ro",
                "nodev",
                "relatime"
            ],
            "size": "55.00 MiB",
            "size_bytes": 57671680,
            "used": "55.00 MiB",
            "used_bytes": 57671680
        },
        "/snap/gnome-3-28-1804/116": {
            "available": "0 bytes",
            "available_bytes": 0,
            "capacity": "100%",
            "device": "/dev/loop1",
            "filesystem": "squashfs",
            "options": [
                "ro",
                "nodev",
                "relatime"
            ],
            "size": "160.25 MiB",
            "size_bytes": 168034304,
            "used": "160.25 MiB",
            "used_bytes": 168034304
        },
        "/snap/gtk-common-themes/1506": {
            "available": "0 bytes",
            "available_bytes": 0,
            "capacity": "100%",
            "device": "/dev/loop3",
            "filesystem": "squashfs",
            "options": [
                "ro",
                "nodev",
                "relatime"
            ],
            "size": "62.13 MiB",
            "size_bytes": 65142784,
            "used": "62.13 MiB",
            "used_bytes": 65142784
        },
        "/snap/onenote-desktop/9": {
            "available": "0 bytes",
            "available_bytes": 0,
            "capacity": "100%",
            "device": "/dev/loop2",
            "filesystem": "squashfs",
            "options": [
                "ro",
                "nodev",
                "relatime"
            ],
            "size": "53.63 MiB",
            "size_bytes": 56229888,
            "used": "53.63 MiB",
            "used_bytes": 56229888
        },
        "/snap/snapd/7264": {
            "available": "0 bytes",
            "available_bytes": 0,
            "capacity": "100%",
            "device": "/dev/loop0",
            "filesystem": "squashfs",
            "options": [
                "ro",
                "nodev",
                "relatime"
            ],
            "size": "27.13 MiB",
            "size_bytes": 28442624,
            "used": "27.13 MiB",
            "used_bytes": 28442624
        },
        "/sys/fs/cgroup": {
            "available": "15.66 GiB",
            "available_bytes": 16820150272,
            "capacity": "0%",
            "device": "tmpfs",
            "filesystem": "tmpfs",
            "options": [
                "ro",
                "nosuid",
                "nodev",
                "noexec",
                "mode=755"
            ],
            "size": "15.66 GiB",
            "size_bytes": 16820150272,
            "used": "0 bytes",
            "used_bytes": 0
        }
    },
    "networking": {
        "domain": "linux.com",
        "fqdn": "Home.linux.com",
        "hostname": "Home",
        "interfaces": {
            "eth0": {
                "dhcp": "192.168.1.1",
                "mac": "04:d4:c4:58:df:d7",
                "mtu": 1500
            },
            "lo": {
                "bindings": [
                    {
                        "address": "127.0.0.1",
                        "netmask": "255.0.0.0",
                        "network": "127.0.0.0"
                    }
                ],
                "bindings6": [
                    {
                        "address": "::1",
                        "netmask": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                        "network": "::1"
                    }
                ],
                "ip": "127.0.0.1",
                "ip6": "::1",
                "mtu": 65536,
                "netmask": "255.0.0.0",
                "netmask6": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff",
                "network": "127.0.0.0",
                "network6": "::1"
            },
            "pnet0": {
                "bindings": [
                    {
                        "address": "192.168.1.15",
                        "netmask": "255.255.255.0",
                        "network": "192.168.1.0"
                    }
                ],
                "bindings6": [
                    {
                        "address": "fe80::6d4:c4ff:fe58:dfd7",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip": "192.168.1.15",
                "ip6": "fe80::6d4:c4ff:fe58:dfd7",
                "mac": "04:d4:c4:58:df:d7",
                "mtu": 1500,
                "netmask": "255.255.255.0",
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network": "192.168.1.0",
                "network6": "fe80::"
            },
            "pnet1": {
                "bindings6": [
                    {
                        "address": "fe80::b0bc:78ff:fe5d:aa69",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::b0bc:78ff:fe5d:aa69",
                "mac": "b2:bc:78:5d:aa:69",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "pnet2": {
                "bindings6": [
                    {
                        "address": "fe80::9c91:94ff:fef8:a07e",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::9c91:94ff:fef8:a07e",
                "mac": "9e:91:94:f8:a0:7e",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "pnet3": {
                "bindings6": [
                    {
                        "address": "fe80::1897:c2ff:fe01:b727",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::1897:c2ff:fe01:b727",
                "mac": "1a:97:c2:01:b7:27",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "pnet4": {
                "bindings6": [
                    {
                        "address": "fe80::a416:e9ff:fe96:cc7e",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::a416:e9ff:fe96:cc7e",
                "mac": "a6:16:e9:96:cc:7e",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "pnet5": {
                "bindings6": [
                    {
                        "address": "fe80::5064:9fff:fec6:bbb7",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::5064:9fff:fec6:bbb7",
                "mac": "52:64:9f:c6:bb:b7",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "pnet6": {
                "bindings6": [
                    {
                        "address": "fe80::589c:59ff:fea9:613d",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::589c:59ff:fea9:613d",
                "mac": "5a:9c:59:a9:61:3d",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "pnet7": {
                "bindings6": [
                    {
                        "address": "fe80::cc53:24ff:febc:4b7",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::cc53:24ff:febc:4b7",
                "mac": "ce:53:24:bc:04:b7",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "pnet8": {
                "bindings6": [
                    {
                        "address": "fe80::6068:54ff:feaf:74b",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::6068:54ff:feaf:74b",
                "mac": "62:68:54:af:07:4b",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "pnet9": {
                "bindings6": [
                    {
                        "address": "fe80::3cb8:9fff:fef0:e1d",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::3cb8:9fff:fef0:e1d",
                "mac": "3e:b8:9f:f0:0e:1d",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "virbr0": {
                "bindings": [
                    {
                        "address": "192.168.122.1",
                        "netmask": "255.255.255.0",
                        "network": "192.168.122.0"
                    }
                ],
                "ip": "192.168.122.1",
                "mac": "52:54:00:71:75:73",
                "mtu": 1500,
                "netmask": "255.255.255.0",
                "network": "192.168.122.0"
            },
            "virbr0-nic": {
                "mac": "52:54:00:71:75:73",
                "mtu": 1500
            },
            "vmnet1": {
                "bindings": [
                    {
                        "address": "192.168.224.1",
                        "netmask": "255.255.255.0",
                        "network": "192.168.224.0"
                    }
                ],
                "bindings6": [
                    {
                        "address": "fe80::250:56ff:fec0:1",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "dhcp": "192.168.224.254",
                "ip": "192.168.224.1",
                "ip6": "fe80::250:56ff:fec0:1",
                "mac": "00:50:56:c0:00:01",
                "mtu": 1500,
                "netmask": "255.255.255.0",
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network": "192.168.224.0",
                "network6": "fe80::"
            },
            "vmnet8": {
                "bindings": [
                    {
                        "address": "192.168.135.1",
                        "netmask": "255.255.255.0",
                        "network": "192.168.135.0"
                    }
                ],
                "bindings6": [
                    {
                        "address": "fe80::250:56ff:fec0:8",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "dhcp": "192.168.135.254",
                "ip": "192.168.135.1",
                "ip6": "fe80::250:56ff:fec0:8",
                "mac": "00:50:56:c0:00:08",
                "mtu": 1500,
                "netmask": "255.255.255.0",
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network": "192.168.135.0",
                "network6": "fe80::"
            },
            "vnet0": {
                "bindings6": [
                    {
                        "address": "fe80::fc54:ff:fe78:2f57",
                        "netmask": "ffff:ffff:ffff:ffff::",
                        "network": "fe80::"
                    }
                ],
                "ip6": "fe80::fc54:ff:fe78:2f57",
                "mac": "fe:54:00:78:2f:57",
                "mtu": 1500,
                "netmask6": "ffff:ffff:ffff:ffff::",
                "network6": "fe80::"
            },
            "vunl0_4_0": {
                "mac": "7e:7c:1a:bf:c0:96",
                "mtu": 9000
            },
            "vunl0_4_1": {
                "mac": "26:f5:f2:6d:f4:9b",
                "mtu": 9000
            },
            "vunl0_4_2": {
                "mac": "fa:56:56:f7:6d:b8",
                "mtu": 9000
            },
            "vunl0_4_3": {
                "mac": "6e:e1:94:b7:3c:fe",
                "mtu": 9000
            },
            "vunl0_4_4": {
                "mac": "e2:bf:bd:b2:fb:9e",
                "mtu": 9000
            },
            "vunl0_4_5": {
                "mac": "a6:b7:8a:08:2d:d4",
                "mtu": 9000
            },
            "vunl0_4_6": {
                "mac": "56:2b:53:e7:09:ab",
                "mtu": 9000
            },
            "vunl0_4_7": {
                "mac": "8e:76:34:d6:35:aa",
                "mtu": 9000
            },
            "vunl0_5_0": {
                "mac": "fa:4c:07:71:28:c9",
                "mtu": 9000
            },
            "vunl0_5_1": {
                "mac": "92:17:39:41:1d:0c",
                "mtu": 9000
            },
            "vunl0_5_2": {
                "mac": "aa:39:8d:9e:d6:87",
                "mtu": 9000
            },
            "vunl0_5_3": {
                "mac": "42:9b:99:a8:1e:81",
                "mtu": 9000
            }
        },
        "ip": "192.168.1.15",
        "ip6": "fe80::6d4:c4ff:fe58:dfd7",
        "mac": "04:d4:c4:58:df:d7",
        "mtu": 1500,
        "netmask": "255.255.255.0",
        "netmask6": "ffff:ffff:ffff:ffff::",
        "network": "192.168.1.0",
        "network6": "fe80::",
        "primary": "pnet0"
    },
    "os": {
        "architecture": "amd64",
        "distro": {
            "codename": "bionic",
            "description": "Ubuntu 18.04.4 LTS",
            "id": "Ubuntu",
            "release": {
                "full": "18.04",
                "major": "18.04"
            }
        },
        "family": "Debian",
        "hardware": "x86_64",
        "name": "Ubuntu",
        "release": {
            "full": "18.04",
            "major": "18.04"
        },
        "selinux": {
            "enabled": false
        }
    },
    "partitions": {
        "/dev/loop0": {
            "backing_file": "/var/lib/snapd/snaps/snapd_7264.snap",
            "mount": "/snap/snapd/7264",
            "size": "27.09 MiB",
            "size_bytes": 28405760
        },
        "/dev/loop1": {
            "backing_file": "/var/lib/snapd/snaps/gnome-3-28-1804_116.snap",
            "mount": "/snap/gnome-3-28-1804/116",
            "size": "160.15 MiB",
            "size_bytes": 167931904
        },
        "/dev/loop2": {
            "backing_file": "/var/lib/snapd/snaps/onenote-desktop_9.snap",
            "mount": "/snap/onenote-desktop/9",
            "size": "53.50 MiB",
            "size_bytes": 56102912
        },
        "/dev/loop3": {
            "backing_file": "/var/lib/snapd/snaps/gtk-common-themes_1506.snap",
            "mount": "/snap/gtk-common-themes/1506",
            "size": "62.09 MiB",
            "size_bytes": 65105920
        },
        "/dev/loop4": {
            "backing_file": "/var/lib/snapd/snaps/core18_1754.snap",
            "mount": "/snap/core18/1754",
            "size": "54.95 MiB",
            "size_bytes": 57618432
        },
        "/dev/loop5": {
            "backing_file": "/var/lib/snapd/snaps/core18_1705.snap",
            "mount": "/snap/core18/1705",
            "size": "54.95 MiB",
            "size_bytes": 57614336
        },
        "/dev/sda1": {
            "size": "15.98 MiB",
            "size_bytes": 16759808
        },
        "/dev/sda2": {
            "mount": "/media/eslam/MyData1",
            "size": "1.00 TiB",
            "size_bytes": 1099511627776
        },
        "/dev/sda3": {
            "mount": "/media/eslam/MyData2",
            "size": "839.00 GiB",
            "size_bytes": 900869390336
        },
        "/dev/sdb1": {
            "size": "529.00 MiB",
            "size_bytes": 554696704
        },
        "/dev/sdb2": {
            "mount": "/boot/efi",
            "size": "99.00 MiB",
            "size_bytes": 103809024
        },
        "/dev/sdb3": {
            "size": "16.00 MiB",
            "size_bytes": 16777216
        },
        "/dev/sdb4": {
            "mount": "/media/eslam/620CBE0C0CBDDB6D",
            "size": "143.34 GiB",
            "size_bytes": 153908936704
        },
        "/dev/sdb5": {
            "mount": "/",
            "size": "319.93 GiB",
            "size_bytes": 343522934784
        },
        "/dev/sdb6": {
            "size": "1.86 GiB",
            "size_bytes": 1998585856
        }
    },
    "path": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin",
    "processors": {
        "count": 16,
        "isa": "x86_64",
        "models": [
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor",
            "AMD Ryzen 7 3700X 8-Core Processor"
        ],
        "physicalcount": 1,
        "speed": "3.60 GHz"
    },
    "ruby": {
        "platform": "x86_64-linux-gnu",
        "sitedir": "/usr/local/lib/site_ruby/2.5.0",
        "version": "2.5.1"
    },
    "ssh": {
        "ecdsa": {
            "fingerprints": {
                "sha1": "SSHFP 3 1 ec78450520ce054469d8dba9ae07d6fb2a98b35a",
                "sha256": "SSHFP 3 2 158d2eed76e85ce31a7c71d4e282f27ac018f1000a633747b651e91819dd28d8"
            },
            "key": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKUEANptohGYMTGCyWu5rfe3jAsMk2nJH68Q4FVqAT+PBbUCEOFiGD5N5ScAYyR34orEZawQSI+x5ZBXJnvguNs="
        },
        "ed25519": {
            "fingerprints": {
                "sha1": "SSHFP 4 1 197ba97c1b02c4208b03adbd4780e5b8c6bf716c",
                "sha256": "SSHFP 4 2 c47e9fa21987cca3e4ff1d78d7db716c159b341af761ab5198a85c30ccd436fb"
            },
            "key": "AAAAC3NzaC1lZDI1NTE5AAAAII+gWPMRruZYRMoy+U3QHPg0rhRLZmmL0rm3bcSI6HIV"
        },
        "rsa": {
            "fingerprints": {
                "sha1": "SSHFP 1 1 f8e6cfcb09548510de84191244217cb3cc7ae06d",
                "sha256": "SSHFP 1 2 231e98d192293ef1708f04ac81f8228affe284552eb67bdbf11a3d6ef494a9fa"
            },
            "key": "AAAAB3NzaC1yc2EAAAADAQABAAABAQDHLk6Re3r7B+V3TD5RdOxt/aurBIShZ+iBwTkenwQNka0Y8KMbX8SrqipTm5XiYDyUr7+kZM9Y+0wVaJwM2zvPcJr9ASYHAJNzqXTdCRPsdWHbQXUJ51hORbgSay8hzt5Dw19nWOG/am6hPnJ/2jz2ORu6kffPt+Kz4Fj7I5CqR72UOKCtIHfiYl9LUNg2qtVx1bqKQ7vSZPqhJuDM5Za0hxmy1uZ+D7bzyKsR1k493nMpPAQlF/0TBzLZMSTOlz/KrLaqsCOEFBjZFmjyj7XOQY3lUJZ2scq2ZXkaDQWWimgJNN/e58fq0T1V1qRSFMhP7lkWp0pUfXh+UzhimdB1"
        }
    },
    "system_uptime": {
        "days": 0,
        "hours": 2,
        "seconds": 10569,
        "uptime": "2:56 hours"
    },
    "timezone": "EET",
    "virtual": "vmware_workstation",
    "virtualizationType": "QEMU"
}
```

