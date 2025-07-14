#!/usr/bin/python

# this script mounts all ntfs and ext4 partitions on your system
# you'll need sudo password will running this file.

import os


def get_disk_path(disk):
    """
    we know that the disk variable should look like this:

    /dev/sdd1: LABEL="T7" BLOCK_SIZE="512" UUID="CAB2A7C9B2A7B879" TYPE="ntfs" PARTUUID="1f0e53ae-01"
    so we need all what is before the ":"
    """ 

    disk_path = ""
    i=0
    while disk[i]!=':':
        disk_path += disk[i]
        i += 1
    
    return disk_path

def get_disk_name(disk):
    """
    we know that the disk.split('"') variable should look like this:

    ['/dev/sdd1: LABEL=', 'T7', ' BLOCK_SIZE=', '512', ' UUID=', 'CAB2A7C9B2A7B879', ' TYPE=', 'ntfs', ' PARTUUID=', '1f0e53ae-01', '']
    so we need all what is before the ":"
    """ 
    if "LABEL" in disk:
        # the 2nd index of it, without odd characters
        name = ''.join(e for e in disk.split('"')[1] if e.isalnum())
    else:
        name = ''.join(e for e in get_disk_path(disk) if e.isalnum())


    return name


# mount ntfs partitions
disk_info = os.popen('sudo blkid | grep ntfs').read().split('\n')[:-1]
disk_info = [(get_disk_path(disk), get_disk_name(disk)) for disk in disk_info]
for path,name in disk_info:
    os.system(f"sudo mkdir -p /media/{name}_mounted/")
    os.system(f"sudo mount -t ntfs-3g {path} /media/{name}_mounted/")


# mount ext4 partitions
disk_info = os.popen('sudo blkid | grep ext4').read().split('\n')[:-1]
disk_info = [(get_disk_path(disk), get_disk_name(disk)) for disk in disk_info]
for path,name in disk_info:
    os.system(f"sudo mkdir -p /media/{name}_mounted/")
    os.system(f"sudo mount -t ext4 {path} /media/{name}_mounted/")
