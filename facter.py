import subprocess
import json


def facter():
    """
    A Python function that returns a "dict" of system information from the "facter" command, which is similar in usage to "Puppet Facter"
    - For a List of the facts ==> "https://puppet.com/docs/facter/3.9/core_facts.html"
    - The "facter" command gets the vast majority of the facts but not all of it
    :return: dict of "facter" system info
    ############
    # Examples #
    ############
    facter()
    facter()['uptime']
    facter()['osfamily']
    facter()['os']['family']
    facter()['interfaces']
    facter()['ipaddress']
    facter()['memoryfree_mb']
    facter()['processors']['physicalcount']
    facter()['partitions']
    """

    info = {}
    proc = subprocess.Popen('facter --json',
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
    std_out, std_err = proc.communicate()
    info['rc'] = proc.returncode
    info['stdout'] = std_out.rstrip()
    info['stderr'] = std_err.rstrip()

    if info['rc'] != 0:
        print("[ Error ]" + info['stderr'])
        exit(1)

    f = info['stdout']
    f_json = json.loads(f)
    return f_json


### Examples:
#print(facter()['partitions'])
