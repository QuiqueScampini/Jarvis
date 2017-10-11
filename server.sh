#!/bin/bash

workdir=`pwd`/app
 
start() {
    python3 -u Jarvis.py &
    echo "Server started."
}
 
stop() {
    pid=`ps -ef | grep 'Jarvis.py' | grep -v grep | awk '{ print $2 }'`
    echo $pid
    kill $pid
    sleep 2
    echo "Server killed."
}

cd $workdir

case "$1" in
  start)
    start
    ;;
  stop)
    stop   
    ;;
  restart)
    stop
    start
    ;;
  *)
    echo "Usage: jarvisServer {start|stop|restart}"
    exit 1
esac
exit 0
