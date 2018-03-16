import wpilib
from wpilib.drive import DifferentialDrive


class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        '''Robot initialization function'''
        
        # object that handles basic drive operations
        self.frontLeftMotor = wpilib.Spark(3)
        self.middleLeftMotor = wpilib.Spark(4)
        self.rearLeftMotor = wpilib.Spark(5)

        self.frontRightMotor = wpilib.Spark(0)
        self.middleRightMotor = wpilib.Spark(1)
        self.rearRightMotor = wpilib.Spark(2)

        self.ihigh_motor = wpilib.Spark(6)
        self.ilow_motor = wpilib.Spark(9)

        self.left = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.middleLeftMotor, self.rearLeftMotor)
        self.right = wpilib.SpeedControllerGroup(self.frontRightMotor, self.middleRightMotor, self.rearRightMotor)

        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)

        self.high = 0
        self.low = 0
        self.gameData = ''

        # joysticks 1 & 2 on the driver station
        self.Stick1 = wpilib.XboxController(0)
        self.Stick2 = wpilib.Joystick(1)
        
        self.aSolenoidLow = wpilib.DoubleSolenoid(2,3)
        self.aSolenoidHigh = wpilib.DoubleSolenoid(0,1)
        self.iSolenoid = wpilib.DoubleSolenoid(4,5)

    def autonomousInit(self):
        self.iSolenoid.set(2)
        self.aSolenoidLow.set(2)
        self.aSolenoidHigh.set(2)
        self.gameData = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        global timer
        timer = wpilib.Timer()
        timer.start()
        
    def autonomousPeriodic(self):
        if self.gameData[0:1] == "L":
            while timer.get() < 0.68:
                self.myRobot.tankDrive(-0.7,0.7)
                # while timer.get() <= 1:
                #     self.myRobot.tankDrive(0.6,0.6)                
                # while timer.get() <= 2:
                #     self.myRobot.tankDrive(0.6,-0.6)
                # while timer.get() <= 3:
                #     self.myRobot.tankDrive(0.6,0.6)
                # while timer.get() <= 4:
                #     self.myRobot.tankDrive(-0.6,0.6)
                # while timer.get() <= 6.5:
                #     self.myRobot.tankDrive(0.6,0.6)
                # while timer.get() <= 7.5:
                #     self.myRobot.tankDrive(-0.6,0.6)
                # while timer.get() <= 8:                   
                #     self.myRobot.tankDrive(0.6,0.6)
                # while timer.get() <= 9:
                #     self.myRobot.tankDrive(0.6,-0.6)
                # while timer.get() <= 9.5:
                #     self.myRobot.tankDrive(0.6,0.6)
                #     self.ihigh_motor.set(0.7)
                #     self.ilow_motor.set(-0.8)
                #     if timer.get() <= 9.2:
                #         self.aSolenoidLow.set(1)
                # while timer.get() > 11 and timer.get() <= 14:
                #     self.ihigh_motor.set(0.7)
                #     self.ilow_motor.set(-0.8)
                #     self.aSolenoidHigh.set(1)
                # while timer.get() >14 and timer.get() <15:
                #     self.iSolenoid.set(1)
                #     self.ihigh_motor.set(-1)
                #     self.ilow_motor.set(1)
                
                ''' Waiting to be tested'''
                # while timer.get() <= 1:
                #     self.myRobot.tankDrive(-0.6,0.6)
                # while timer.get() <= 1.5:                   
                #     self.myRobot.tankDrive(0.6,0.6)
                # while timer.get() <= 2.5:
                #     self.myRobot.tankDrive(0.6,-0.6)
                # while timer.get() <= 3:
                #     self.myRobot.tankDrive(0.6,0.6)
                #     self.ihigh_motor.set(0.7)
                #     self.ilow_motor.set(-0.8)
                #     if timer.get() <= 2.7:
                #         self.aSolenoidLow.set(1)
                # while timer.get() > 4.5 and timer.get() <= 7.5:
                #     self.ihigh_motor.set(0.7)
                #     self.ilow_motor.set(-0.8)
                #     self.aSolenoidHigh.set(1)
                # while timer.get() >7.5 and timer.get() <8.5:
                #     self.iSolenoid.set(1)
                #     self.ihigh_motor.set(-1)
                #     self.ilow_motor.set(1)


                

        elif self.gameData[0:1] == 'R':
            while timer.get() < 0.82:
                self.myRobot.tankDrive(0.7,-0.7)
                # while timer.get() <= 1:
                #     self.myRobot.tankDrive(0.6,0.6)                
                # while timer.get() <= 2:
                #     self.myRobot.tankDrive(-0.6,0.6)
                # while timer.get() <= 3:
                #     self.myRobot.tankDrive(0.6,0.6)
                # while timer.get() <= 4:
                #     self.myRobot.tankDrive(0.6,-0.6)
                # while timer.get() <= 6.5:
                #     self.myRobot.tankDrive(0.6,0.6)
                # while timer.get() <= 7.5:
                #     self.myRobot.tankDrive(0.6,-0.6)
                # while timer.get() <= 8:                   
                #     self.myRobot.tankDrive(0.6,0.6)
                # while timer.get() <= 9:
                #     self.myRobot.tankDrive(-0.6,0.6)
                # while timer.get() <= 9.5:
                #     self.myRobot.tankDrive(0.6,0.6)
                #     self.ihigh_motor.set(0.7)
                #     self.ilow_motor.set(-0.8)
                #     if timer.get() <= 9.2:
                #         self.aSolenoidLow.set(1)
                # while timer.get() > 11 and timer.get() <= 14:
                #     self.ihigh_motor.set(0.7)
                #     self.ilow_motor.set(-0.8)
                #     self.aSolenoidHigh.set(1)
                # while timer.get() >14 and timer.get() <15:
                #     self.iSolenoid.set(1)
                #     self.ihigh_motor.set(-1)
                #     self.ilow_motor.set(1)
                
                
                '''Waiting to be tested'''
                # while timer.get() <= 1:
                #     self.myRobot.tankDrive(0.6,-0.6)
                # while timer.get() <= 1.5:                   
                #     self.myRobot.tankDrive(0.6,0.6)
                # while timer.get() <= 2.5:
                #     self.myRobot.tankDrive(-0.6,0.6)
                # while timer.get() <= 3:
                #     self.myRobot.tankDrive(0.6,0.6)
                #     self.ihigh_motor.set(0.7)
                #     self.ilow_motor.set(-0.8)
                #     if timer.get() <= 2.7:
                #         self.aSolenoidLow.set(1)
                # while timer.get() > 4.5 and timer.get() <= 7.5:
                #     self.ihigh_motor.set(0.7)
                #     self.ilow_motor.set(-0.8)
                #     self.aSolenoidHigh.set(1)
                # while timer.get() >7.5 and timer.get() <8.5:
                #     self.iSolenoid.set(1)
                #     self.ihigh_motor.set(-1)
                #     self.ilow_motor.set(1)
        elif timer.get() < 0.2:
            self.myRobot.tankDrive(0.4,0.4)
        
    def disabledInit(self):
        self.myRobot.tankDrive(0,0)
        self.iSolenoid.set(0)
        self.aSolenoidLow.set(0)
        self.aSolenoidHigh.set(0)
    
    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        '''Execute at the start of teleop mode'''
        self.myRobot.setSafetyEnabled(True)
        self.iSolenoid.set(1)

    def teleopPeriodic(self):
        if self.isOperatorControl() and self.isEnabled():
            minv = 0.4
            maxv = 0.6
            forward = self.Stick1.getTriggerAxis(1)
            backward = self.Stick1.getTriggerAxis(0)
            sp = forward - backward
            steering = self.Stick1.getX(0)
            mod = minv + maxv*((1-abs(sp))**2)
            r = (steering**3)*mod
            if sp >= 0:
                self.myRobot.tankDrive(sp*0.85 - r, sp*0.85 + r)
            else:
                self.myRobot.tankDrive(sp*0.85 + r, (sp*0.85 - r))
            
            # intake and outtake
            if self.Stick2.getRawButton(11)==True: # intake
                self.ihigh_motor.set(0.6)
                self.ilow_motor.set(-0.95)
            if self.Stick2.getRawButton(11)==False and self.Stick2.getRawButton(12)==False:
                self.ihigh_motor.set(0)
                self.ilow_motor.set(0)
            if self.Stick2.getRawButton(12)==True: # outtake
                self.ihigh_motor.set(-0.8)
                self.ilow_motor.set(0.8)
            
            #test
            if self.Stick2.getRawButton(5)==True:
                timer.start()
                while timer.get() < 0.3:
                    self.myRobot.tankDrive(-0.4,0.4)
                timer.reset()
            if self.Stick2.getRawButton(6)==True:
                timer.start()
                while timer.get() < 0.5:
                    self.myRobot.tankDrive(-0.4,0.4)
                timer.reset()
            if self.Stick2.getRawButton(2)==True:
                timer.start()
                while timer.get() < 0.7:
                    self.myRobot.tankDrive(-0.4,0.4)
                timer.reset()
            
            if self.Stick2.getRawButton(9) == True: 
                self.aSolenoidLow.set(1)
                self.iSolenoid.set(1)
            if self.Stick2.getRawButton(10) == True: 
                self.aSolenoidLow.set(2)
            if self.Stick2.getRawButton(7) == True: 
                self.aSolenoidHigh.set(1) 
            if self.Stick2.getRawButton(8) == True:
                self.aSolenoidHigh.set(2)
            if self.Stick2.getRawButton(3) == True:
                self.iSolenoid.set(1) # push intake
            if self.Stick2.getRawButton(4) == True:
                self.iSolenoid.set(2) # pull intake
       
if __name__ == '__main__':
    wpilib.run(MyRobot)
