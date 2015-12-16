#!/bin/sh
OOO_HOST=
OOO_PORT="2002 2003 2004 2005"
USER_HOME=/tmp

_create_home() {
    port=$1
    home=/home/port${port}
    mkdir -p ${home}
    echo ${home}
}

_start_instances() {
    # Go to OOo program folder
    # Set IP address
    host=${OOO_HOST:-127.0.0.1}
    # All ports... default is standard port 2002
    for port in ${OOO_PORT:-2002}
    do
        # Set user home
        starthome=$(_create_home ${port})
        HOME=$starthome
        export HOME
        
        # Start OOo
        echo "Starting OpenOffice on ${host}:${port} using home directory ${HOME}"
        sock="socket,host=${host},port=${port},tcpNoDelay=1;urp;StarOffice.ServiceManager"
        opts="-nologo -nofirststartwizard -nodefault -nocrashreport -headless"
        nohup soffice -accept="${sock}" ${opts} 1>>soffice_${port}.log &
        #soffice -accept="${sock}" ${opts}
    done
}

_start_instances
exit 0
