#!/bin/bash

cd ${JARVIS_VIDEO}

lockPID="./filmDrive.pid"
# Check IF PROGRAM IS RUNNING
if [ -f ${lockPID} ]; then
	pid=`cat ${lockPID}`
	ps -ef | grep -v grep | grep " ${pid} " | grep "${0}" > /dev/null

	if [ $? -eq 0 ]; then
		# WE ARE RUNNING - WE FORCE STOP
		echo "WE FORCE FILMING"
		forceStopFilming.sh ${pid}
	fi
fi

#STARTING
echo $$ > ${lockPID}

#Delete old files
rm -f *.mp4
rm -f *.log

#Start Process
ffmpeg -f video4linux2 -i /dev/video1 -s 2000x1000 -c:v h264 -f mp4 lastdrive.mp4 </dev/null >/dev/null 2> lastdrive.log &
pid=$!
echo ${pid} > FILM_PID

wait ${pid}

#Start Stitching
ffmpeg  -i lastdrive.mp4 -i /home/pi/thetacam_workspace/zx.pgm -i /home/pi/thetacam_workspace/zy.pgm -filter_complex "remap"  stitcheado.mp4 </dev/null >/dev/null 2> stitcheado.log &
pid=$!
echo ${pid} > STITCH_PID

wait ${pid}

ffmpeg -i stitcheado.mp4 -c:v mpeg4 final.mp4 </dev/null >/dev/null 2> final.log &
pid=$!
echo ${pid} > CONVERT_PID

wait ${pid}

rm -f FILM_PID STITCH_PID CONVERT_PID

exit 0