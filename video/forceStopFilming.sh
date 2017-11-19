#!/bin/bash

cd ${JARVIS_VIDEO}

actualProcessPid=${1}
kill -9 ${actualProcessPid}

if [ -f FILM_PID ]; then
    pid=`cat FILM_PID`
    kill ${pid}
    ps -ef | grep ${pid} | grep ffmpeg | grep -v grep > /dev/null
	while [ $? -eq 0 ];do
		ps -ef | grep ${pid} | grep ffmpeg | grep -v grep
	done

    rm -f FILM_PID
fi

if [ -f STITCH_PID ]; then
    pid=`cat STITCH_PID`
    kill ${pid}
    ps -ef | grep ${pid} | grep ffmpeg | grep -v grep > /dev/null
	while [ $? -eq 0 ];do
		ps -ef | grep ${pid} | grep ffmpeg | grep -v grep
	done

	rm -f STITCH_PID
fi

if [ -f CONVERT_PID ]; then
    pid=`cat CONVERT_PID`
    kill ${pid}
    ps -ef | grep ${pid} | grep ffmpeg | grep -v grep > /dev/null
	while [ $? -eq 0 ];do
		ps -ef | grep ${pid} | grep ffmpeg | grep -v grep
	done

	rm -f CONVERT_PID
fi

exit 0