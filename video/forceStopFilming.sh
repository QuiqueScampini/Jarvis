#!/bin/bash

cd ${JARVIS_VIDEO}

actualProcessPid=${1}

kill -9 ${actualProcessPid}

if [ -f FILM_PID ]; then
    pid=`cat FILM_PID`
    kill ${pid}
    ps -ef | grep ${pid} | grep ffmpeg | grep -v grep
	while [ $? -eq 0 ];do
		ps -ef | grep ${pid} | grep ffmpeg | grep -v grep
	done
fi

if [ -f STITCH_PID ]; then
    pid=`cat STITCH_PID`
    kill ${pid}
    ps -ef | grep ${pid} | grep ffmpeg | grep -v grep
	while [ $? -eq 0 ];do
		ps -ef | grep ${pid} | grep ffmpeg | grep -v grep
	done
fi

if [ -f CONVERT_PID ]; then
    pid=`cat CONVERT_PID`
    kill ${pid}
    ps -ef | grep ${pid} | grep ffmpeg | grep -v grep
	while [ $? -eq 0 ];do
		ps -ef | grep ${pid} | grep ffmpeg | grep -v grep
	done
fi

rm -f FILM_PID STITCH_PID CONVERT_PID

exit 0