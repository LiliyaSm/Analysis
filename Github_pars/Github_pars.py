import requests
import os
import csv
#from getpass import getpass

def get_req(url):
    username = os.environ['GITHUB_USERNAME']
    password = os.environ['GITHUB_KEY']
    
    commits = requests.get(url, auth=(username, password))
    
    
    return commits.json()


def write_csv(data):
     with open('authors1.csv', 'a', newline='') as file:
          
        order = ['login', 'date', "type", 'url']
        writer = csv.DictWriter(file, fieldnames=order)

        writer.writerow(data)


def write_csv_rows(data):
     with open('authors.csv', 'a', newline='') as file:
          
        order = ['login', 'date', "type", 'url']
        writer = csv.DictWriter(file, fieldnames=order)

        for row in data:
            writer.writerow(row)


def get_data(commits):    
    data = []
    for commit in commits:
           try: 
               login = commit["author"]["login"] 
           except: 
               login = "error"
           try: 
               date = commit["commit"]['author']["date"] 
           except: 
               date = "error"
           try: 
               type = commit["author"]["type"] 
           except: 
               type = "error"
           try:
               url = commit["author"]["url"] 
           except:
               url = "error"

           data.append({'login': login,
                'date': date,
                'type': type,
                'url': url})

    write_csv_rows(data)
         
#since  = {"since": "2019-01-0100:00:00Z"} #YYYY-MM-DDTHH:MM:SSZ  since = since_Date


def main():
    #clean file on start
    try:
        os.remove('authors.csv') #if os.path.exists("demofile.txt"):
    except:
        pass

    url = "https://api.github.com/repos/django/django/commits/master" #GET /repos/:owner/:repo/commits 

    first_commit = get_req(url) # для одного первого коммита                                  

    print(first_commit)

    first_commit_sha= first_commit["sha"]

    get_data([first_commit]) # записали первый коммит
    pagination_url = "https://api.github.com/repos/django/django/commits?per_page=100&sha=" + first_commit_sha #https://api.github.com/repos/django/django/commits?per_page=100&sha=514efa3129792ec2abb2444f3e7aeb3f21a38386
    next_commit_sha = 0

    while True:
   # while not first_commit_sha == next_commit_sha:      
        
        commits =  get_req(pagination_url)[1:] # без первого        
        get_data(commits) # записали остальные  
        #if not next_commit_sha ==0 :
        #    first_commit_sha = next_commit_sha
        next_commit_sha = commits[-1]["sha"]
        
        pagination_url = "https://api.github.com/repos/django/django/commits?per_page=100&sha=" + next_commit_sha

        print(pagination_url)

        if len(commits) < 99:
            break


if __name__ == '__main__':
    main()
       

