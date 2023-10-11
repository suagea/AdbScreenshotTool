# -*- coding: utf-8 -*-
# @Time : 2023/10/11 14:50
# @Author : LiangBoQing
# @File : AdbScreenshotTool
import os
import sys
import datetime
import subprocess
from time import sleep

dir_path = 'captures'

if getattr(sys, 'frozen', False):
  adb_tool = rf'.\_internal\adb_tool\adb.exe'
else:
  adb_tool = rf'.\adb_tool\adb.exe'

if not os.path.exists(dir_path):
  os.makedirs(dir_path)


def capture_screen(name, dev_name=''):
  file_name = rf'captures/{name}_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
  temp_file_name = 'temp_screenshot.png'

  if dev_name:
    cap_cmd = rf'{adb_tool} -s {dev_name} shell screencap -p /sdcard/{temp_file_name}'
    pul_cmd = rf'{adb_tool} -s {dev_name} pull /sdcard/{temp_file_name} {file_name}'
    del_cmd = rf'{adb_tool} -s {dev_name} shell rm /sdcard/{temp_file_name}'
  else:
    cap_cmd = rf'{adb_tool} shell screencap -p /sdcard/{temp_file_name}'
    pul_cmd = rf'{adb_tool} pull /sdcard/{temp_file_name} {file_name}'
    del_cmd = rf'{adb_tool} shell rm /sdcard/{temp_file_name}'

  subprocess.check_call(cap_cmd, shell=True, stdout=subprocess.PIPE)
  subprocess.check_call(pul_cmd, shell=True, stdout=subprocess.PIPE)
  subprocess.check_call(del_cmd, shell=True, stdout=subprocess.PIPE)


def get_connected_devices():
  try:
    result = subprocess.check_output([adb_tool, 'devices'], universal_newlines=True)
    lines = result.strip().split("\n")
    devices = [line.split("\t")[0] for line in lines[1:]]
    return devices
  except Exception as e:
    print(f"Error: {e}")
    return []


def select_device():
  devs = get_connected_devices()
  devs_quantity = len(devs)

  if devs_quantity == 0:
    print("No device connected")
    input('Press Enter key to finish.')
    exit(1)
  elif devs_quantity == 1:
    return devs[0]
  else:
    while True:
      try:
        for index, dev in enumerate(devs):
          print(f'{index}\t{dev}')
        return devs[int(input('Select device:'))]
      except Exception as e:
        print('Err:', e)


def capture_loop(dev_name):
  print(f"Selected device: {dev_name}")
  print('Input file name "?" to exit.')
  while True:
    try:
      f_name = input('File name:')
      if f_name == "?":
        break
      capture_screen(f_name, dev_name)
    except Exception as e:
      print(e)


def main():
  print("Welcome to the ADB Screenshot Tool!")
  dev_name = select_device()
  capture_loop(dev_name)
  print('Bye~')
  sleep(1)


if __name__ == '__main__':
  main()
