import matplotlib.pyplot as plt
import pandas as pd

def barChart(file_path, dataType, heading, uname):
    # Lists to store data from the file
    labels = []
    values = []

    # Read the file and extract data
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into label and value
            parts = line.strip().split(',')
            labels.append(parts[0])
            values.append(int(parts[1]))
            
    label_colors = {
        'Lilydale': '#01528b',
        'Belgrave': '#01528b',
        'Glen Waverley': '#01528b',
        'Alamein': '#01528b',
        'Cranbourne': '#00a8e4',
        'Pakenham': '#00a8e4',
        'Hurstbridge': '#d1202f',
        'Mernda': '#d1202f',
        'Craigieburn': '#fdb917',
        'Upfield': '#fdb917',
        'Sunbury': '#fdb917',
        'Frankston': '#009645',
        'Stony Point': '#009645',
        'Werribee': '#009645',
        'Williamstown': '#009645',
        'Sandringham': '#f27fb2',
        'Flemington Racecourse': '#949797',
        'N/A': '#949797',
        'Unknown': '#949797',
        
        'Albury': '#7f3f98',
        'Ballarat/Maryborough/Ararat': '#7f3f98',
        'Bendigo/Echuca/Swan Hill': '#7f3f98',
        'Geelong/Warrnambool': '#7f3f98',
        'Seymour/Shepparton': '#7f3f98',
        'Traralgon/Bairnsdale': '#7f3f98',      
    }
    
    colors = [label_colors.get(label, 'white') for label in labels]

    # Create the bar graph
    plt.style.use('dark_background')
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color=colors)
    plt.xlabel(dataType)
    plt.title(heading)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # sabe  graph
    plt.savefig(f'temp/Graph{uname}.png')
    
def pieChart(file_path, heading, uname):
    # Lists to store data from the file
    labels = []
    values = []

    # Read the file and extract data
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into label and value
            parts = line.strip().split(',')
            labels.append(parts[0])
            values.append(int(parts[1]))
            
    label_colors = {
        'Lilydale': '#01528b',
        'Belgrave': '#01528b',
        'Glen Waverley': '#01528b',
        'Alamein': '#01528b',
        'Cranbourne': '#00a8e4',
        'Pakenham': '#00a8e4',
        'Hurstbridge': '#d1202f',
        'Mernda': '#d1202f',
        'Craigieburn': '#fdb917',
        'Upfield': '#fdb917',
        'Sunbury': '#fdb917',
        'Frankston': '#009645',
        'Stony Point': '#009645',
        'Werribee': '#009645',
        'Williamstown': '#009645',
        'Sandringham': '#f27fb2',
        'Flemington Racecourse': '#949797',
        'N/A': '#949797',
        'Unknown': '#949797',
        
        'Albury': '#7f3f98',
        'Ballarat/Maryborough/Ararat': '#7f3f98',
        'Bendigo/Echuca/Swan Hill': '#7f3f98',
        'Geelong/Warrnambool': '#7f3f98',
        'Seymour/Shepparton': '#7f3f98',
        'Traralgon/Bairnsdale': '#7f3f98',      
    }

    # Define a darker color palette
    colors = [label_colors.get(label, 'white') for label in labels]
    
    plt.style.use('dark_background')
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'
    
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.axis('equal')  
    plt.title(heading)
    plt.tight_layout()

    # Save the graph
    plt.savefig(f'temp/Graph{uname}.png')
    
def dayChart(csv_file, uname):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file, names=['Date', 'Number'])

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Set the 'Date' column as the index
    df.set_index('Date', inplace=True)

    # Create a new DataFrame with a daily frequency and fill missing values with 0
    daily_df = df.asfreq('D', fill_value=0)

    # Plotting
    plt.style.use('dark_background')  # Applying dark theme
    plt.figure(figsize=(10, 6))
    plt.plot(daily_df.index, daily_df['Number'], color='cyan')  # Adjust color for better visibility
    plt.xlabel('Date', color='white')  # Adjust label color
    plt.ylabel('Trips', color='white')  # Adjust label color
    plt.title(f'Trips per day - {uname}', color='white')  # Adjust title color
    plt.grid(True, color='gray')  # Adjust grid color
    plt.xticks(rotation=45, color='white')  # Adjust tick color
    plt.tight_layout()
    
    plt.savefig(f'temp/Graph{uname}.png')


