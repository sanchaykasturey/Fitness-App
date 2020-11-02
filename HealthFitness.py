import tkinter
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from datetime import date
import csv
##      Defining class
class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Calculator")
        self.root.geometry("1920x1080+0+0")
        self.root.configure(background="Gray")
        mainframe = Frame(self.root, bd=20, width=1920, height=1080, padx=10, pady=10, bg="Gray", relief=RIDGE)
        mainframe.grid()
##       Making Frames under main frame to take input and then display result
        leftframe = Frame(mainframe, bd=10, width=960, height=1080, padx=10, pady=13, bg="Gray", relief=RIDGE)
        leftframe.pack(side=LEFT)

        rightframe = Frame(mainframe, bd=10, width=960, height=1080, padx=10, pady=13, bg="Gray", relief=RIDGE)
        rightframe.pack(side=RIGHT)

        #####################################################################################
##       subframes under leftframe and right frame so that we can put data in categorised manner
        leftframe0 = Frame(leftframe, bd=5, width=900, height=900, padx=5, relief=RIDGE)
        leftframe0.grid(row=0, column=0)

        leftframe1 = Frame(leftframe, bd=5, width=900, height=60, padx=5, pady=6, relief=RIDGE)
        leftframe1.grid(row=1, column=0)

        leftframe2 = Frame(leftframe, bd=5, width=900, height=60, padx=5, pady=6, relief=RIDGE)
        leftframe2.grid(row=2, column=0)

        rightframe0 = Frame(rightframe, bd=5, width=900, height=1080, padx=5, bg="light coral", relief=RIDGE)
        rightframe0.grid(row=0, column=0)
##       Declaring variables to take inputs
        name = StringVar()
        age = IntVar()
        Systolic= IntVar()
        Diastolic= IntVar()
        PulseRate= IntVar()
        RBC_count= IntVar()
        WBC_count= IntVar()
        Platelets= IntVar()
        Haemoglobin= IntVar()
        UricAcid= IntVar()
        Cholesterol= IntVar()
        kg = IntVar()
        CMs = IntVar()
##       making functions for the suitable calculations and categorising the results
        def BmiDisplay():
            Calc_height=(CMs.get())
            m=(kg.get())
            h=Calc_height/100
            BMI_val=(m / (h * h))
            self.txtBMIResult.insert(END, BMI_val)
        def RbcDisplay():
            Calc_rbc=(RBC_count.get())
            if (Calc_rbc>=850):
                CalculatedRBC = "High"
            elif (Calc_rbc<=550):
                CalculatedRBC = "Low"
            else:
                CalculatedRBC = "Normal"
            self.txtRBCResult.insert(END, CalculatedRBC)
        def WbcDisplay():
            Calc_wbc=(WBC_count.get())
            if ( Calc_wbc >=17000):
                CalculatedWBC = "High"
            elif (Calc_wbc<=6000):
                CalculatedWBC = "Low"
            else:
                CalculatedWBC = "Normal"
            self.txtWBCResult.insert(END, CalculatedWBC)
        def PlateletsDisplay():
            Calc_platelets=(Platelets.get())
            if (Calc_platelets >=600):
                CalculatedPlatelets = "High"
            elif (Calc_platelets<=120):
                CalculatedPlatelets = "Low"
            else:
                CalculatedPlatelets = "Normal"
            self.txtPlateletsResult.insert(END, CalculatedPlatelets)
        def HaemoglobinDisplay():
            Calc_haemoglobin=(Haemoglobin.get())
            if (Calc_haemoglobin >=18):
                CalculatedHaemoglobin = "High"
            elif (Calc_haemoglobin<=10):
                CalculatedHaemoglobin = "Low"
            else:
                CalculatedHaemoglobin = "Normal"
            self.txthaemoglobinResult.insert(END, CalculatedHaemoglobin)
        def UricAcidDiscplay():
            Calc_uricAcid=(UricAcid.get())
            if ( Calc_uricAcid>=6):
                CalculatedUricAcid = "High"
            elif (Calc_uricAcid<=5):
                CalculatedUricAcid = "Low(Safe)"
            else:
                CalculatedUricAcid = "Normal"
            self.txtUricAcidResult.insert(END, CalculatedUricAcid)
        def CholestrolDisplay():
            Calc_cholestrol=(Cholesterol.get())
            if ( Calc_cholestrol>=239):
                CalculatedCholestrol = "High"
            elif (Calc_cholestrol<=200):
                CalculatedCholestrol = "Low"
            else:
                CalculatedCholestrol = "Normal"
            self.txtCholesterolResult.insert(END, CalculatedCholestrol)
        def pulseCalc():
            Calc_pulse=(PulseRate.get())
            Calc_age=(age.get())
            if (1<=Calc_age<=2) & (80<=Calc_pulse<=140):
                CalculatedPulse = "Normal"
            elif (3<=Calc_age<=5) & (80<=Calc_pulse<=110):
                CalculatedPulse = "Normal"
            elif (5<=Calc_age<=17) & (75<=Calc_pulse<=100):
                CalculatedPulse = "Normal"
            elif (17<=Calc_age<=22) & (60<=Calc_pulse<=90):
                CalculatedPulse = "Normal"
            elif (22<=Calc_age<=100) & (60<=Calc_pulse<=100):
                CalculatedPulse = "Normal"
            else:
                CalculatedPulse = "Abnormal"
            self.txtPulseResult.insert(END, CalculatedPulse)
        def BPCalculator():
            BPhigh = (Systolic.get())
            BPlow = (Diastolic.get())
            if (80<=BPhigh<=120) & (70<=BPlow<=86):
                BP="Normal"
            elif (80<=BPhigh<=120) & (BPlow<=70):
                BP="Low"
            else:
                BP="High"
            self.txtBPResult.insert(END, BP)
##          main() driver function for putting command
        def main():
            BmiDisplay()
            RbcDisplay()
            WbcDisplay()
            PlateletsDisplay()
            BPCalculator()
            UricAcidDiscplay()
            pulseCalc()
            CholestrolDisplay()
            HaemoglobinDisplay()
            self.btnExport.config(state=NORMAL, bg='goldenrod', relief="raised")
##          function to export the recorded files in CSV
        def export_CSV():
            try:
                CSV_name = (name.get())
                CSV_age = (age.get())
                CSV_CMs = (CMs.get())
                CSV_kg = (kg.get())
                CSV_BP = self.txtBPResult.get("1.0", 'end-1c')
                CSV_RBC = self.txtRBCResult.get("1.0", 'end-1c')
                CSV_WBC = self.txtWBCResult.get("1.0", 'end-1c')
                CSV_Platelets = self.txtPlateletsResult.get("1.0", 'end-1c')
                CSV_UricAcid = self.txtUricAcidResult.get("1.0", 'end-1c')
                CSV_Haemoglobin= self.txthaemoglobinResult.get("1.0", 'end-1c')
                CSV_Cholesterol = self.txtCholesterolResult.get("1.0", 'end-1c')
                CSV_Pulse= self.txtPulseResult.get("1.0", 'end-1c')
                CSV_BMI = self.txtBMIResult.get("1.0", 'end-1c')
                current_day = date.today()
                current_time = datetime.now().time()

                with open('fitness_result.csv', 'w', newline='') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(['Name', 'Age', 'BMI' , 'RBC', 'WBC', 'Platelets', 'Haemoglobin', 'UricAcid', 'Cholesterol', 'Pulse', 'BloodPressure'])
                    thewriter.writerow([CSV_name, CSV_age, CSV_BMI, CSV_RBC, CSV_WBC, CSV_Platelets, CSV_Haemoglobin, CSV_UricAcid, CSV_Cholesterol, CSV_Pulse, CSV_BP])
                    thewriter.writerow([])

                    thewriter.writerow([])
                    thewriter.writerow(['Date: {}'.format(current_day)])
                    thewriter.writerow(['Time: {}'.format(current_time)])

                tkinter.messagebox.showinfo("Body Mass Index", "Your results have been saved to a CSV file!")

            except NameError:
                tkinter.messagebox.showwarning("Body Mass Index", "Missing information, Please fill all fields.")
#        reset function for resetting all the values to null
        def reset():
            kg.set("")
            CMs.set("")
            name.set("")
            age.set("")
            Systolic.set("")
            Diastolic.set("")
            Platelets.set("")
            PulseRate.set("")
            RBC_count.set("")
            WBC_count.set("")
            Haemoglobin.set("")
            UricAcid.set("")
            Cholesterol.set("")
            self.txtBMIResult.delete("1.0", END)
            self.txtCholesterolResult.delete("1.0", END)
            self.txtPulseResult.delete("1.0", END)
            self.txtWBCResult.delete("1.0", END)
            self.txtRBCResult.delete("1.0", END)
            self.txtUricAcidResult.delete("1.0", END)
            self.txtPlateletsResult.delete("1.0", END)
            self.txtBPResult.delete("1.0", END)
            self.txthaemoglobinResult.delete("1.0", END)
            self.btnExport.config(state=DISABLED, bg='gray', relief="sunken")
#        exit function for exiting the program
        def exit():
            global root
            root.quit()

        # ===========================    LEFT FRAMES    ==================================
        self.lbName = Label(leftframe0, text="Name:", font=('arial', 17, 'bold'), width=19, bd=2, )
        self.lbName.grid(row=0, column=0)
        self.txtName = Entry(leftframe0, textvariable=name, font=('arial', 17, 'bold'), bd=5, width=20, justify=LEFT)
        self.txtName.grid(row=0, column=1)
        self.lbAge = Label(leftframe0, text="Age:", font=('arial', 17, 'bold'), bd=2)
        self.lbAge.grid(row=1, column=0)
        self.txtAge = Entry(leftframe0, textvariable=age, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtAge.grid(row=1, column=1)
        self.lbBPs = Label(leftframe0, text="Blood Pressure(Systolic):", font=('arial', 17, 'bold'), width=19, bd=2, )
        self.lbBPs.grid(row=2, column=0)
        self.txtBPs = Entry(leftframe0, textvariable=Systolic, font=('arial', 17, 'bold'), bd=5, width=20, justify=LEFT)
        self.txtBPs.grid(row=2, column=1)
        self.lbBPd = Label(leftframe0, text="Blood Pressure(Diastolic):", font=('arial', 17, 'bold'), bd=2)
        self.lbBPd.grid(row=3, column=0)
        self.txtBPd = Entry(leftframe0, textvariable=Diastolic, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtBPd.grid(row=3, column=1)
        self.lbPulseRate = Label(leftframe0, text="Pulse Rate", font=('arial', 17, 'bold'), width=19, bd=2, )
        self.lbPulseRate.grid(row=4, column=0)
        self.txtPulseRate = Entry(leftframe0, textvariable=PulseRate, font=('arial', 17, 'bold'), bd=5, width=20, justify=LEFT)
        self.txtPulseRate.grid(row=4, column=1)
        self.lbRBC = Label(leftframe0, text="RBC count (m/mm^3)", font=('arial', 17, 'bold'), bd=2)
        self.lbRBC.grid(row=5, column=0)
        self.txtRBC = Entry(leftframe0, textvariable=RBC_count, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtRBC.grid(row=5, column=1)
        self.lbWBC = Label(leftframe0, text="WBC count (m/mm^3)", font=('arial', 17, 'bold'), width=19, bd=2, )
        self.lbWBC.grid(row=6, column=0)
        self.txtWBC = Entry(leftframe0, textvariable=WBC_count, font=('arial', 17, 'bold'), bd=5, width=20, justify=LEFT)
        self.txtWBC.grid(row=6, column=1)
        self.lbPlatelets = Label(leftframe0, text="Platelets (m/mm^3)", font=('arial', 17, 'bold'), bd=2)
        self.lbPlatelets.grid(row=7, column=0)
        self.txtPlatelets = Entry(leftframe0, textvariable=Platelets, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtPlatelets.grid(row=7, column=1)
        self.lbHaemoglobin = Label(leftframe0, text="Haemoglobin (g/dl)", font=('arial', 17, 'bold'), bd=2)
        self.lbHaemoglobin.grid(row=8, column=0)
        self.txtHaemoglobin = Entry(leftframe0, textvariable=Haemoglobin, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtHaemoglobin.grid(row=8, column=1)
        self.lbUricAcid = Label(leftframe0, text="Uric Acid (mg/dl)", font=('arial', 17, 'bold'), bd=2)
        self.lbUricAcid.grid(row=9, column=0)
        self.txtUricAcid = Entry(leftframe0, textvariable=UricAcid, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtUricAcid.grid(row=9, column=1)
        self.lbCholesterol = Label(leftframe0, text="Cholestrol", font=('arial', 17, 'bold'), bd=2)
        self.lbCholesterol.grid(row=10, column=0)
        self.txtCholesterol = Entry(leftframe0, textvariable=Cholesterol, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtCholesterol.grid(row=10, column=1)
        self.lbWeight = Label(leftframe0, text="Weight (in KGs)", font=('arial', 17, 'bold'), bd=2)
        self.lbWeight.grid(row=11, column=0)
        self.txtWeight = Entry(leftframe0, textvariable=kg, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtWeight.grid(row=11, column=1)
        self.lbHeight = Label(leftframe0, text="Height (in CMs)", font=('arial', 17, 'bold'), bd=2)
        self.lbHeight.grid(row=12, column=0)
        self.txtHeight = Entry(leftframe0, textvariable=CMs, font=('arial', 17, 'bold'), bd=5, width=15, justify=LEFT)
        self.txtHeight.grid(row=12, column=1)
########################################################leftframe2################################################
        self.btnBMI = Button(leftframe1, text="Show Results", padx=4, pady=2, bd=4, width=19,
                             font=('arial', 17, 'bold'), height=1, bg='dodgerblue', command=main)
        self.btnBMI.bind('<Return>', main)
        self.btnBMI.grid(row=0, column=0)
        self.btnExport = Button(leftframe1, text="Export(as CSV)", padx=4, pady=2, bd=4, width=16, state=DISABLED,
                                bg='gray', relief="sunken",
                                font=('arial', 17, 'bold'), height=1, command=export_CSV)
        self.btnExport.grid(row=0, column=2)
#######################################################leftframe3################################################
        self.btnReset = Button(leftframe2, text="Reset", padx=4, pady=2, bd=4, width=19, font=('arial', 17, 'bold'),
                               height=1, command=reset)
        self.btnReset.grid(row=0, column=1, )
        self.btnExit = Button(leftframe2, text="Exit", padx=4, pady=2, bd=4, width=19, font=('arial', 17, 'bold'),
                              height=1, command=exit)
        self.btnExit.grid(row=0, column=2)
#######################################################rightframe################################################
        self.lbBPresult = Label(rightframe0, text="Blood Pressure:", font=('arial', 17, 'bold'), bd=2)
        self.lbBPresult.grid(row=1, column=0, padx=4)
        self.txtBPResult= Text(rightframe0, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20,height=1, relief='sunk')
        self.txtBPResult.grid(row=1, column=1)
        self.lbPulseResult = Label(rightframe0, text="Pulse Rate:", font=('arial', 17, 'bold'), bd=2)
        self.lbPulseResult.grid(row=2, column=0, padx=4)
        self.txtPulseResult= Text(rightframe0, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20, height=1, relief='sunk')
        self.txtPulseResult.grid(row=2, column=1)
        self.lbRBCResult = Label(rightframe0, text="RBC:", font=('arial', 17, 'bold'), bd=2)
        self.lbRBCResult.grid(row=3, column=0, padx=4)
        self.txtRBCResult= Text(rightframe0, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20, height=1, relief='sunk')
        self.txtRBCResult.grid(row=3, column=1)
        self.lbWBCResult = Label(rightframe0, text="WBC:", font=('arial', 17, 'bold'), bd=2)
        self.lbWBCResult.grid(row=4, column=0, padx=4)
        self.txtWBCResult= Text(rightframe0, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20, height=1, relief='sunk')
        self.txtWBCResult.grid(row=4, column=1)
        self.lbPlateletsResult = Label(rightframe0, text="Platelets:", font=('arial', 17, 'bold'), bd=2)
        self.lbPlateletsResult.grid(row=5, column=0, padx=4)
        self.txtPlateletsResult= Text(rightframe0, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20, height=1, relief='sunk')
        self.txtPlateletsResult.grid(row=5, column=1)
        self.lbHaemoglobinResult = Label(rightframe0, text="Haemoglobin:", font=('arial', 17, 'bold'), bd=2)
        self.lbHaemoglobinResult.grid(row=6, column=0, padx=4)
        self.txthaemoglobinResult= Text(rightframe0, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20, height=1, relief='sunk')
        self.txthaemoglobinResult.grid(row=6, column=1)
        self.lbUricAcidResult = Label(rightframe0, text="Uric Acid:", font=('arial', 17, 'bold'), bd=2)
        self.lbUricAcidResult.grid(row=7, column=0, padx=4)
        self.txtUricAcidResult= Text(rightframe0, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20, height=1, relief='sunk')
        self.txtUricAcidResult.grid(row=7, column=1)
        self.lbCholesterolResult = Label(rightframe0, text="Cholestrol:", font=('arial', 17, 'bold'), bd=2)
        self.lbCholesterolResult.grid(row=8, column=0, padx=4)
        self.txtCholesterolResult= Text(rightframe0, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20, height=1, relief='sunk')
        self.txtCholesterolResult.grid(row=8, column=1)
        self.lbBMIResult = Label(rightframe0, text="BMI:", font=('arial', 17, 'bold'), bd=2)
        self.lbBMIResult.grid(row=9, column=0, padx=4)
        self.txtBMIResult= Text(rightframe0, padx=15, pady=5, font=('arial', 17, 'bold'), bd=5, width=20, height=1, relief='sunk')
        self.txtBMIResult.grid(row=9, column=1)
## main driver for program
if __name__ == '__main__':
    root = Tk()
    application = FitnessApp(root)
    root.mainloop()
