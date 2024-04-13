print('间隔时长为发送间隔')
from pynput.keyboard import Key, Controller
import time
text = input("内容:")
keyboard = Controller()
TimeInterval = float(input('间隔时长:'))
Send = int(input('发送次数:'))
OperationTime = int(input('操作时间：'))
for a in range(OperationTime):
    print(OperationTime)
    time.sleep(1)
    OperationTime -= 1
for s in range(Send):
    keyboard.type(text)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
   
print('运行成功！')


