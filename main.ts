function doSomething () {
    data = Quadruped.Ball_return(Ball_Position.X_axis)
    if (data < 80) {
        data_s = (80 - data) * Kp
        Quadruped.Control_a(Mov_ang.L_swing, 0, 0)
    } else {
        data_s = (data - 80) * Kp
        Quadruped.Control_a(Mov_ang.R_swing, 0, 0)
    }
}
function doSomething2 () {
    data1 = Quadruped.Ball_return(Ball_Position.Re_effect)
    if (data1 < 1000) {
        Quadruped.Control_s(Mov_dir.For, 7, 0)
    } else {
        Quadruped.Control_s(Mov_dir.Bac, 0, 0)
    }
}
let STA = 0
let data1 = 0
let data_s = 0
let data = 0
let Kp = 0
Kp = 0.06
serial.redirect(
SerialPin.P8,
SerialPin.P0,
BaudRate.BaudRate115200
)
Quadruped.Image_init()
Quadruped.OnToggle1(ColorID.Blue, FunctionID1.ball)
Quadruped.init()
Quadruped.Start()
Quadruped.Height(10)
basic.forever(function () {
    Quadruped.Heartbeat()
    STA = Quadruped.Ball_return(Ball_Position.status)
    if (STA == 1) {
        Quadruped.Gait(gait.Trot)
        doSomething()
        doSomething2()
    } else {
        Quadruped.Reset()
        Quadruped.Stand()
    }
})
