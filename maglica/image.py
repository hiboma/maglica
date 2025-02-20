import libvirt
import maglica.config
import re
from xml.etree.ElementTree import *
import maglica.dispatcher

# Listing up inactive images
def list():
    config = maglica.config.load()
    images = []
    for host in config.hosts:
        conn = libvirt.open('remote://' + host)
        domains = conn.listDefinedDomains()
        for domain in domains:
            images.append({
                "name" : domain,
                "host" : host,
                })
    return images

def copy(args):
    maglica.dispatcher.dispatch({
        "type"   : "image",
        "action" : "copy",
        "name"   : args["name"],
        "dest"   : args["dest"],
    })
