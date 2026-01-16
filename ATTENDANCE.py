import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# PROJECT: ATTENDANCE MANAGEMENT ANALYZER
# DEVELOPED BY: Jagriti Balla


def main():
    print("------------------------------------------------")
    print("   ATTENDANCE ANALYSIS SYSTEM - BY JAGRITI BALLA")
    print("------------------------------------------------")

    # 1. SETUP DATA (Using Numpy)
   
    students = ['Aarav', 'Vihaan', 'Aditya', 'Reyansh', 'Saanvi']
    days = 10
    
   
    np.random.seed(42) 
    attendance_data = np.random.randint(0, 2, size=(5, days))

   
    cols = [f'Day_{i+1}' for i in range(days)]
    
    df = pd.read_csv("data.csv") if False else pd.DataFrame(attendance_data, columns=cols)
    df.insert(0, "Student_Name", students)

   
    df['Total_Present'] = df.iloc[:, 1:].sum(axis=1)
    df['Percentage'] = (df['Total_Present'] / days) * 100

   
    print("\nAttendance Records:")
    print(df)

    
    print("\n------------------------------------------------")
    print("SHORT ATTENDANCE ALERT (<75%):")
    short_attendance = df[df['Percentage'] < 75]
    
    if not short_attendance.empty:
        for index, row in short_attendance.iterrows():
            print(f"WARNING: {row['Student_Name']} has only {row['Percentage']}% attendance.")
    else:
        print("All students have good attendance.")
    print("------------------------------------------------")

    
    print("\nGenerating Performance Graph...")
    
    plt.figure(figsize=(10, 6)) # Set graph size
    colors = ['green' if p >= 75 else 'red' for p in df['Percentage']] # Red bars for low attendance
    
    plt.bar(df['Student_Name'], df['Percentage'], color=colors)
    
    plt.xlabel('Student Name')
    plt.ylabel('Attendance Percentage (%)')
    plt.title(f'Student Attendance Analysis\nProject by: Jagriti Balla')
    plt.ylim(0, 100) # Ensure Y-axis goes from 0 to 100
    
    
    plt.axhline(y=75, color='blue', linestyle='--', label='Min Requirement (75%)')
    plt.legend()
    
    plt.grid(axis='y', alpha=0.5)
    plt.show()

if __name__ == "__main__":

    main()
