import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r'C:\Users\kakil\OneDrive\Desktop\prodigy\task5\US_Accidents_Dec20.csv'
df = pd.read_csv(file_path)

print(df.info())

try:
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    df['End_Time'] = pd.to_datetime(df['End_Time'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
except ValueError as e:
    print(f"Error: {e}")

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Weather_Condition', order=df['Weather_Condition'].value_counts().index[:10])
plt.title('Distribution of Accidents by Weather Condition')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Road_Conditions', order=df['Road_Conditions'].value_counts().index[:10])
plt.title('Distribution of Accidents by Road Condition')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 8))
plt.scatter(df['Start_Lng'], df['Start_Lat'], alpha=0.1, s=5)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()


if 'Start_Time' in df.columns:
    df['Hour'] = df['Start_Time'].dt.hour
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Hour')
    plt.title('Accident Frequency by Time of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Accidents')
    plt.tight_layout()
    plt.show()


plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()
