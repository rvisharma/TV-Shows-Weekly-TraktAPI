import json
import urllib.request
import time
 
print('Welcome, This Program returns the list of shows airing in next 7 days.')
print('\nNote: Your Username must be set to public to use this feature')

# Defaults
api_key = '7ccf64fd09f5710a8186363e08971ba1'
date = time.strftime('%Y%m%d')
days = '7'

# Prompt the user
def askusername():
    username = input('''\n\n    Enter your Trakt Username, If you do not have a trakt account
Press ENTER to get all of the Shows in this week: ''')
    if username == '': username = 'justin'
    return username

def askdays():
    days = input('\nHow many days forecast you want?, default is 7: ')
    if days == '':
        days = '7'
    return days
    
username = askusername()
days = askdays()

# take starting time
t1 = time.time()

# URL for obtaining JSON object
url = 'http://api.trakt.tv/user/calendar/shows.json/'+api_key+'/'+username+'/'+date+'/'+days

# Call the URL with Exception Handling
print('\nSearching for User...')
okay = 'True'
while okay:
    try:
        json_string = (urllib.request.urlopen(url).read().decode('utf-8'))
        print('\nSuccessfully Entered!\n')
        if username == 'justin':
            username = 'default'
        print('For Username: ' + username)
        print('For ' + days + ' days.')
        break
    except urllib.error.HTTPError as err:
        print('\nERROR OCCURED: ' + str(err.code) + ' Restart\n')
        okay = False
        break
            
# If error occurs, exit the program
if okay == False:
    print('Exiting The Program in 3 secs, Restart again')
    time.sleep(3)
    exit()

# loads the json string to json_data
json_data = json.loads(json_string)

file = open('this week.txt', 'w')
file.write('Date wise representation of shows airing this week for username -> ' + username + '\n\n')

def write_to_file():
    for i in range(len(show_title)):            
            file.write('\n')
            file.write('Show: ' + show_title[i])
            file.write('\nEpisode: ' + episode_title[i])
            file.write('\nSeason: ' +  str(season[i]) + ' - Episode: ' + str(number[i]))
            file.write('\n\n\n')
            file.write('Episode Overview\n' + episode_overview[i])
            file.write('\n\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')

for date in range(len(json_data)):
    
    show_title = []
    episode_title = []
    year = []
    number = []
    episode_overview = []
    runtime = []
    season = []
    number = []
    
    for i in range(len(json_data[date]['episodes'])):
        show_title.append(json_data[date]['episodes'][i]['show']['title'])
        year.append(json_data[date]['episodes'][i]['show']['year'])
        runtime.append(json_data[date]['episodes'][i]['show']['runtime'])
        season.append(json_data[date]['episodes'][i]['episode']['season'])
        number.append(json_data[date]['episodes'][i]['episode']['number'])
        episode_title.append(json_data[date]['episodes'][i]['episode']['title'])
        episode_overview.append(json_data[date]['episodes'][i]['episode']['overview'])

    file.write('Date: ' + json_data[date]['date'])
    file.write('\n======================\n======================\n')
    
    write_to_file()
    
# End time taken
t2 = time.time()
# total time taken
total_time = round(t2-t1, 3)

minutes = 0
if total_time > 60:
    minutes = time%60

print('\nDone')
print('This Program took : ' + str(minutes) + ' minutes '+ str(total_time) + ' seconnds')

file.write('This Program took : ' + str(total_time) + ' seconnds\n')
file.close()

print('Note: A Text file is created "this week.txt" in the same folder\n')
print('Exiting Program..')
time.sleep(4)
exit()
