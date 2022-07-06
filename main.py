def doSomething():
    global data, data_s
    data = Quadruped.Ball_return(Ball_Position.X_AXIS)
    if data < 80:
        data_s = (80 - data) * Kp
        Quadruped.Control_a(Mov_ang.L_SWING, 0, 0)
    else:
        data_s = (data - 80) * Kp
        Quadruped.Control_a(Mov_ang.R_SWING, 0, 0)
def doSomething2():
    global data1
    data1 = Quadruped.Ball_return(Ball_Position.RE_EFFECT)
    if data1 < 1000:
        Quadruped.Control_s(Mov_dir.FOR, 7, 0)
    else:
        Quadruped.Control_s(Mov_dir.BAC, 0, 0)
STA = 0
data1 = 0
data_s = 0
data = 0
Kp = 0
Kp = 0.06
serial.redirect(SerialPin.P8, SerialPin.P0, BaudRate.BAUD_RATE115200)
Quadruped.Image_init()
Quadruped.on_toggle1(ColorID.BLUE, FunctionID1.BALL)
Quadruped.init()
Quadruped.start()
Quadruped.height(10)

def on_forever():
    global STA
    Quadruped.heartbeat()
    STA = Quadruped.Ball_return(Ball_Position.STATUS)
    if STA == 1:
        Quadruped.gait(gait.TROT)
        doSomething()
        doSomething2()
    else:
        Quadruped.reset()
        Quadruped.stand()
basic.forever(on_forever)
