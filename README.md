# fyndHackingChallenge_IMDB

## Project Setup and Run
```
python3 -m virtualenv env
pip install -r requirements.txt
python manage.py migrate
python manage.py populate_movies
python manage.py runserver
```
### Tests

GET all movies: http://127.0.0.1:8000/imdb/movies

GET movie by name: http://127.0.0.1:8000/imdb/movies?search=the%20Wizard%20of%20Oz

For Admin Access: `python manage.py createsuperuser`

## Scaling Task
```
1. Use Auto Scaling Groups to spin up/ tear down instances as per network load.
2. Use Read Replicas of DB for the Read tasks. We can have a load balancer on top of this to further improve Reads' turnaround time.
3. Update DB data in Batches.
4. Update Read Replicas in intervals to reduce load. These intervals can be based upon the frequency of updates.
5. Use Caching to further reduce load on DB and to reduce turnaround time.
6. Use something like firehose for queuing Write tasks.

```
https://medium.com/@aashray18521/comprehensive-architecture-of-serverless-rest-services-for-scale-on-aws-162926d4cdc2