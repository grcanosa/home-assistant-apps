#!/bin/sh
#
# Put this file in /usr/local/etc/rc.d/btsync.sh

case "$1" in

stop)
    echo "Stop Dash Scanner"
    killall dash_scanner.py
    #kill "`cat /tmp/telegrambots.pid`"
    sleep 5
    killall -9 dash_scanner.py
    #killall -9 multilauncher.py
    ;;
start)
    symlink=$(readlink -f "$0")
	  path=$(dirname $symlink)
    . $path/pass_info.sh
    #echo "Creating folder in $path/../data/log"
    #mkdir -p $path/../data/log
	  $path/dash_scanner.py $HOMEASSISTANTPASS &
    #echo $! > /tmp/telegrambots.pid
    ;;
restart)
    $0 stop
    sleep 2
    $0 start
    ;;
*)
    echo "usage: $0 { start | stop | restart }" >&2
        exit 1
        ;;
esac
