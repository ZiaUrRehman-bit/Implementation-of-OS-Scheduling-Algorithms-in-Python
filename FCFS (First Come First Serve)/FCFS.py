

# 1. Taking Input (Process Name, Arrival Time, CPU Time) form User

# 1.1 Enter Process Names

# In[3]:


print("Enter Name of Processes as P0, P1, P2...... with space separted")

# This will Make the list of Processes Names entered by user
processList = list(map(str, input().split()))

processList


# ##### 1.2 Enter Arrival Time 

# In[4]:


print("Enter Arrival Time for each Process mentioned above with space separted")

# This will Make the list of Processes arrival time entered by user
arrivalTime = list(map(float, input().split()))

arrivalTime


# ##### 1.3 Enter CPU Time 

# In[5]:


print("Enter CPU Time for each Process mentioned above with space separted")

# This will Make the list of Processes CPU time entered by user
CPUTime = list(map(float, input().split()))

CPUTime


# ##### 1.4 Display in the form Table

# In[37]:


import pandas as pd

data = {}

data["Process Name"] = processList
data["Arrival Time (AT)"] = arrivalTime
data["CPU Time / Burst Time"] = CPUTime

ECTMatrix = pd.DataFrame(data)

print("-----------------------------------------------------")
print("\t\t\tFCFS")
print("    Input Matirx with Arrival Time and CPU Time")
print("-----------------------------------------------------")
ECTMatrix


# #### 2. Sort the Data frame on the basis of arrival time

# In[62]:


sortedECTMatrix = ECTMatrix.sort_values('Arrival Time (AT)')

print("=====================================================")
print("\t\t\tFCFS")
print("\t\t    Sorted Matrix")
print("=====================================================")
sortedECTMatrix


# ##### 2.1 Reset the index values

# In[63]:


sortedECTMatrix.reset_index(drop=True, inplace=True)
sortedECTMatrix


# #### 3. Findng the start time and Completion time of each Process

# In[64]:


currentTime = sortedECTMatrix["Arrival Time (AT)"][0]
gantChart = []

for p in range(len(sortedECTMatrix)):

    gantChart.append([currentTime, currentTime + sortedECTMatrix["CPU Time / Burst Time"][p]])
    currentTime+= sortedECTMatrix["CPU Time / Burst Time"][p]

gantChart


# ##### 3.1 Add start time and Completion time of each process in data frame

# In[65]:


startTime = []
complTime = []

for i in range(0,len(sortedECTMatrix)):
    startTime.append(gantChart[i][0]) 
    complTime.append(gantChart[i][1])

sortedECTMatrix["Start Time"] = startTime
sortedECTMatrix["Completion Time"] = complTime

sortedECTMatrix


# #### 4. Find Turn Around time for each process and average Turn Around Time

#         Turn around Time  = Completion Time - Arrival Time 

# In[66]:


TurnAroundTime = []

for i in range(0,len(sortedECTMatrix)):

    TurnAroundTime.append(sortedECTMatrix["Completion Time"][i] - sortedECTMatrix["Arrival Time (AT)"][i])

TurnAroundTime


# ##### 4.1 Add Turn Around column in current data frame 

# In[67]:


sortedECTMatrix["Turnaround Time"] = TurnAroundTime

sortedECTMatrix


# ##### 4.2 Finding Average Turn Around Time and Maskespan

#         Average Turn Around Time = Sum of Turn around Time / Total no. of Process
#         Makespan = Maximum of Turn around Time 

# In[72]:


averageTurnAroundTime = sortedECTMatrix["Turnaround Time"].sum()/len(sortedECTMatrix)
makespan = max(sortedECTMatrix["Turnaround Time"])

print(f"The average turn around time: {averageTurnAroundTime}")
print(f"The Makespan is: {makespan}")


# #### 5. Finding the Weighting Time for each Process

#         Weighting Time = Turn Around Time - CPU Time

# In[73]:


WeightingTime = []

for i in range(0,len(sortedECTMatrix)):

    WeightingTime.append(sortedECTMatrix["Turnaround Time"][i] - sortedECTMatrix["CPU Time / Burst Time"][i])

WeightingTime


# ##### 5.1 Add Weighting Time column in current Data Frame

# In[74]:


sortedECTMatrix["Weighting Time"] = WeightingTime

sortedECTMatrix


# ##### 5.2 Average Weighting Time 

# In[75]:


averageWeightingTime= sortedECTMatrix["Weighting Time"].sum()/len(sortedECTMatrix)

print(f"The average weighting time: {averageWeightingTime}")


# %%
