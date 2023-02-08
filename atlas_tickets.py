import pandas as pd
import sys


#print(df)
#print(df["Project ID"])

employee_names = {"Finola Young": 500, "Juan Villagrana": 750, "Daniel Pollock": 500, "Cormac McCrory":500, "Manuel Montosa": 600}

#ticket_no_and_name = df.loc[[("Finola Young", 45910)], "Hours Spent"].sum()
#print(ticket_no_and_name)

def get_hours(csv):
    csv_str = str(csv)
    df = pd.read_csv(csv_str)

    all_tickets_li = list(df.loc[:, "IPC Number"].unique())

    for el in all_tickets_li:
        if pd.isna(el):
            all_tickets_li.remove(el)
            continue

    df.set_index(["Employee Name", "IPC Number"], inplace = True)

    sorted_tickets_di = dict()

    for num in all_tickets_li:
        num_di = {}
        for el in employee_names:
            if (el, num) in df.index:
                total_days = df.loc[[(el, num)], "Hours Spent"].sum() /7.5
                total_days_rounded = round(total_days, 3)

                num_di[el + ' no. days'] = total_days_rounded

                five_rate = round(total_days_rounded * 500,3)
                num_di[el +' 500 rate'] = five_rate

                dev_rate = round(total_days_rounded * employee_names[el], 3)
                num_di[el + " dev rate"] = dev_rate

                #num_di[el] = el_di
        sorted_tickets_di[num] = num_di
    
    new_df = pd.DataFrame.from_dict(sorted_tickets_di).transpose()

    new_df.to_csv('converted_' + csv_str)
#    for fl in hours_worked:
#        print(fl)
#        five_hundred_rate = str(hours_worked[fl] * 500)
#        print("Days worked at 500 rate: " + five_hundred_rate)
#        dev_rate  = str(hours_worked[fl] * employee_names[fl])
#        print("Days worked at dev rate: " + dev_rate + "\n")



arg1 = str(sys.argv[1])
#arg2 = 45910#int(sys.argv[2])

get_hours(arg1)