# GCP-pipeline

**Steps to clone and run Flask - app.py through GCP Cloud Shell**

  - git clone https://github.com/saursing/GCP-pipeline.git
  - docker build --tag gcr.io/docker-flask-358409/python-docker .
  - docker push gcr.io/docker-flask-358409/python-docker
  - gcloud run deploy --project=docker-flask-358409 python-docker --image gcr.io/docker-flask-358409/python-docker


**To ceate and quey SQL database**

  - run:python app.py from one console.
  
  - from another console, get into python prompt:
  
  >> from app import db
  >> 
  >> db.create_all()
  >> 
  >> from app import Users
  >> 
  >> admin = Users(name='admin', email='admin@example.com')
  >> 
  >>   guest = Users(name='guest', email='guest@example.com')
  >>  
  >>  db.session.add(admin)
  >>  
  >>  db.session.add(guest)
  >>  
  >>  db.session.commit()
  >>  
  >>  Users.query.all()
  >>  
  [<Users 1>, <Users 2>]

**Repo clone commands:**
- gcloud iam service-accounts create sample-app
- git clone https://github.com/saursing/GCP-pipeline.git sample-app
- git push google main

**To update repo with new files checked into git:-**
- git pull origin main
- git push google main
