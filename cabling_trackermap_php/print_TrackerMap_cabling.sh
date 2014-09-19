# !/bin/bash

export SCRAM_ARCH=slc5_amd64_gcc481
source /afs/cern.ch/cms/cmsset_default.sh

cd /afs/cern.ch/work/j/jmejiagu/public/servcice_work/andresa_trackermap/CMSSW_7_0_4/src
eval `scramv1 runtime -sh`

cd $OLDPWD

# if [ "${1}" == "1" ]; then
# 	python todos1.py -f $2 -y TEC --yf $3
# elif [ "${1}" == "2" ]; then
# 	python todos1.py -f $2 -b $4 $5 --bf $3
# elif [ "${1}" == "3" ]; then
# 	python todos1.py -f $2 -v TEC --vf $3
# # elif [ "${1}" == "4" ]; then
# # 	python todos1.py -f $2 -y subdetector
# fi

#mkdir temp
#ls > loco1.txt

#python todos3.py -f $1 $2  $3 $4 $5 $6 $7 $8 
#python todos2.py -f $1 $2 $5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} $3 $4 2>&1
#python todos4.py -f $1 $2 $5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} $3 $4 2>&1
#python todos4.py -f $1 $2 $3 $4 $5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} 2>&1
#python todos5.py -f $1 $2 $3 $4 $5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} 2>&1
#python todos6.py $1 $2 $3 $4 $5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} 2>&1
python todos_get_cabling.py $1 $2 $3 $4 $5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} 2>&1


#mv loco.txt temp/
# printf "python todos2.py -f $1 $2 $5 $6 $7 $8 $9 ${10} ${11} ${12} ${13} ${14} $3 $4 \n" > aver.txt

# echo $1 $2 $3 
