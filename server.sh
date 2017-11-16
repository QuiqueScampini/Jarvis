#!/bin/bash

workdir=`pwd`/app
 
start() {
    mv Jarvis.log Jarvis.old.log
	echo "Starting mjpg_streamer - `date '+%d/%m/%Y %H:%M:%S'`"
	/usr/local/bin/mjpg_streamer -i "/usr/local/lib/input_uvc.so" -o "/usr/local/lib/output_http.so -w /usr/local/www -p 8090" &
	echo "mjpg_streamer Started - `date '+%d/%m/%Y %H:%M:%S'`"
	echo "Starting pigpiod - `date '+%d/%m/%Y %H:%M:%S'`"
	sudo pigpiod
	echo "pigpiod Started - `date '+%d/%m/%Y %H:%M:%S'`"
	echo "Starting Server - `date '+%d/%m/%Y %H:%M:%S'`"
    python3 -u Jarvis.py &
    echo "Server started."
}

stop() {
    pid=`ps -ef | grep 'Jarvis.py' | grep -v grep | awk '{ print $2 }'`
    echo $pid
    kill $pid
    sleep 2
	echo "Stopping Server - `date '+%d/%m/%Y %H:%M:%S'`"
    echo "Server killed."

	pid=`ps -ef | grep 'mjpg_streamer' | grep -v grep | awk '{ print $2 }'`
	echo $pid
    kill $pid
	echo "Stopping mjpg_streamer - `date '+%d/%m/%Y %H:%M:%S'`"
    echo "mjpg_streamer killed."

	pid=`ps -ef | grep 'pigpiod' | grep -v grep | awk '{ print $2 }'`
	echo $pid
    sudo kill $pid
	echo "Stopping pigpiod - `date '+%d/%m/%Y %H:%M:%S'`"
    echo "pigpiod killed."
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
