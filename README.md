# DSP_Python
DSP with python

Enable I2S on raspberry pi and change output device
1. https://www.mathworks.com/help/supportpkg/raspberrypi/ug/play-high-quality-audio-from-raspberry-pi-using-i2s-based-dac.html
2. https://github.com/respeaker/seeed-voicecard
3. https://github.com/respeaker/4mics_hat

4. https://makersportal.com/blog/audio-processing-with-the-quadmic-4-microphone-array-on-the-raspberry-pi?rq=quadmic
5. https://wiki.seeedstudio.com/ReSpeaker_4-Mic_Linear_Array_Kit_for_Raspberry_Pi/

Enable I2S Drivers on Raspberry Pi
    In the terminal, type sudo nano /boot/config.txt to edit the config.txt file.
    To enable the I2S interface in the Raspberry Pi device tree, uncomment the line dtparam=i2s=on in the hardware interface section of the file.
    To configure the HiFiBerry DAC, add dtoverlay=hifiberry-dacplus in the lirc-rpi module section of the file.
    To disable the onboard ALSA audio devices for Raspberry Pi, comment out the line dtparam=audio=on in the enable audio section
