
meetings=[(1,4),(3,5),(0,6),(5,7),(8,9),(5,9)]
meetings.sort(key=lambda x:x[1])
selected_meetings=[]
last_end_time=meetings[0][1]
selected_meetings.append(meetings[0])
for i in range(1,len(meetings)):
    current_start=meetings[i][0]
    current_end=meetings[i][1]
    if current_start>last_end_time:
        selected_meetings.append(meetings[i])
        last_end_time=current_end
print("Meetings scheduled :",selected_meetings)