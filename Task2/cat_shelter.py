import sys

def read_the_file(f_path):
    """This function reads the file and returns the data as a list"""
    try:
        with open(f_path, 'r') as file:
            read=file.readlines()
            return read
    except FileNotFoundError:
        print(f"Cannot open'{f_path}'")
        sys.exit(1)

def calc_time_diff(entry,exit):
    """This function calculates time difference between entry and exit times."""
    difference=exit-entry
    return difference

def time_formatting(minutes):
    """This function formats time in hour,minute format from minutes."""
    hours = minutes // 60
    minutes %= 60
    return f"{int(hours)} Hours, {int(minutes)} Minutes"

def data_analysis(f_path):
    """"This function perforns the analysis and returns the data obtained."""
    all_lines=read_the_file(f_path)
    our_cat=0
    others_cat=0
    total_time=0
    length_of_visits=[]

    for each_line in all_lines:
        if each_line.startswith('OURS'):
            our_cat+=1
            entry_time=int(each_line.split(',')[1])
            exit_time=int(each_line.split(',')[2].strip())
            length_of_visits.append(calc_time_diff(entry_time,exit_time))
            total_time+=calc_time_diff(entry_time,exit_time)
        elif each_line.startswith('THEIRS'):
            others_cat+=1
    if our_cat==0:
        print("No information about the cat's visit.")
        sys.exit(0)
    avg_visit=time_formatting(sum(length_of_visits)/our_cat)
    longest_visit_time=time_formatting(max(length_of_visits))
    shortest_visit_time=time_formatting(min(length_of_visits))
    total_time_our=time_formatting(total_time)
    return our_cat,others_cat,total_time_our,avg_visit,longest_visit_time,shortest_visit_time

def display_data(our_cat,others_cat,total_time_our,avg_visit,longest_visit_time,shortest_visit_time):
    """This function displays the data to be shown on terminal."""
    print("\t Log File Analysis\n")
    print(f"\t================\n")
    print(f"\tOur Cat Visited: {our_cat} Times")
    print(f"\tOther Cat Visited: {others_cat} Times")
    print(f"\tTotal Time Spent by Our Cat: {total_time_our}")
    print(f"\tAverage Visit Duration: {avg_visit}")
    print(f"\tLongest Visit Duration: {longest_visit_time}")
    print(f"\tShortest Visit Duration: {shortest_visit_time}\n")

#The main program starts here

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Missing command line argument")
        sys.exit(1)
    else:
        file_path=sys.argv[1]
        output_data=data_analysis(file_path)
        display_data(*output_data)


