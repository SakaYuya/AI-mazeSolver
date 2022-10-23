# cd [folder]
# chmod +x run.sh
# ./run.sh

#pip install matplotlib
#pip install ffmpeg-python

ls ./input/level_1/*.txt > level1_InputFilenames.txt
ls ./input/level_2/*.txt > level2_InputFilenames.txt
ls ./input/advance/*.txt > advance_InputFilenames.txt

python3 ./source/main.py $PWD