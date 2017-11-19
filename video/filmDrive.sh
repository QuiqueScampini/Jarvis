#!/bin/bash

cd ${JARVIS_VIDEO}

lockPID="./filmDrive.pid"
# Check IF PROGRAM IS RUNNING
if [ -f ${lockPID} ]; then
	pid=`cat ${lockPID}`
	ps -ef | grep -v grep | grep " ${pid} " | grep "${0}" > /dev/null

	if [ $? -eq 0 ]; then
		# WE ARE RUNNING - WE FORCE STOP
		forceStopFilming.sh ${pid}
	fi
fi

#STARTING
echo $$ > ${lockPID}

#Delete old files
rm -f *.mp4
rm -f *.log
rm -f ${LAST_DRIVE_PATH}/final.mp4

#Start Process
ffmpeg -f video4linux2 -i /dev/video1 -s 2000x1000 -c:v h264 -f mp4 lastdrive.mp4 </dev/null >/dev/null 2> lastdrive.log &
pid=$!
echo ${pid} > FILM_PID

wait ${pid}
rm FILM_PID

#Start Stitching
ffmpeg  -i lastdrive.mp4 -i /home/pi/thetacam_workspace/zx.pgm -i /home/pi/thetacam_workspace/zy.pgm -filter_complex "remap"  stitcheado.mp4 </dev/null >/dev/null 2> stitcheado.log &
pid=$!
echo ${pid} > STITCH_PID

wait ${pid}
rm STITCH_PID

ffmpeg -i stitcheado.mp4 -c:v mpeg4 final.mp4 </dev/null >/dev/null 2> final.log &
pid=$!
echo ${pid} > CONVERT_PID

wait ${pid}
rm CONVERT_PID

mv final.mp4 ${LAST_DRIVE_PATH}/.

exit 0