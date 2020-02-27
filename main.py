import libvirt
import sys


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


