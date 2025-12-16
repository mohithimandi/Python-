import pandas as pd 
# Create a dictionary with five keys 
data_dict = { 
    'Name': ['Nitya', 'Nithika',  'Manasvi', 'Dikshitha', 'Reshma', 'Nimisha', 'Bhavishya'], 
    'Age': [25, 30, 28, 22, 35,  27, 24], 
    'Country': ['USA', 'UK',  'UK', 'Australia', 'Germany', 'USA', 'UK'], 
    'Score': [85, 90, 78,  95, 89, 84, 91], 
    'Grade': ['A', 'A', 'B',  'A', 'A', 'B', 'A'] 
} 
 
df = pd.DataFrame(data_dict) 
 
print(" Display DataFrame") 
print(df) 
print("# Display first five rows") 
print(df.head(5)) 
print("Select rows where Country == 'USA'") 
print(df[df['Country'] == 'USA']) 
print("Select rows where Age > 28") 
print(df[df['Age'] > 28]) 
