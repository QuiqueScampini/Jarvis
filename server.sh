#!/bin/bash

workdir=`pwd`/app
 
start() {
	echo "Starting Server - `date '+%d/%m/%Y %H:%M:%S'`" >> ../log/jarvis-server.log
    python -u jarvis.py >> ../log/jarvis-server.log & 
    echo "Server started."
}
 
stop() {
    pid=`ps -ef | grep '[p]ython Jarvis.py' | awk '{ print $2 }'`
    echo $pid
    kill $pid
    sleep 2
	echo "Stopping Server - `date '+%d/%m/%Y %H:%M:%S'`" >> ../log/jarvis-server.log
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