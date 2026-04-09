# dynamoCode.py
# helper functions for DynamoDB sighting logs
# my boyfriend helped me with the try-except method and Claude was used for incorporating the timestamps. 
# as i note for what i learned from the try-except structure, i need to use that a lot more because it stops the loop of errors that could be never ending which is great because i make it error in interesting ways all the time. 

# talks to dynamoDB
import boto3
# used google searches and claude helped me figure out automating timestamps. that's applicable to basically all datetime/timestamp part in sighting logs
from datetime import datetime

# connects to dynamoDB and which table
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('SanctuaryLog')

# get all sightings function - 
def get_all_sightings():
    """Returns all the sightings from the log. Read"""
    try:
        response = table.scan()
        items = response.get('Items', [])
        # sort by timestamp, newest first
        items.sort(key=lambda x: x['timestamp'], reverse=True)
        return items
    except Exception as e:
        print("Error fetching sightings:", e)
        return []

# add sighting function - makes a new sighting with unique records and keeps it in the database. CREATE 
def add_sighting(display_name, animal_tag, sighting):
    try:
        timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        table.put_item(
            Item={
                'display_name': display_name,
                'timestamp': timestamp,
                'animal_tag': animal_tag,
                'sighting': sighting})
        return True
    except Exception as e:
        print("Error adding sighting:", e)
        return False

# delete sighting function -  finds the name and sort key and deletes that sighting. DELETE 
def delete_sighting(display_name, timestamp):
    try:
        table.delete_item(
            Key={
                'display_name': display_name,
                'timestamp': timestamp })
        return True
    except Exception as e:
        print("Error deleting sighting:", e)
        return False

# update sighting function - updates the sighting log info and overwrites the old one. UPDATE 
def update_sighting(display_name, timestamp, new_sighting):
    """Updates the sighting text for an existing entry. Update"""
    try:
        table.update_item(
            Key={
                'display_name': display_name,
                'timestamp': timestamp},
            UpdateExpression='SET sighting = :s',
            ExpressionAttributeValues={':s': new_sighting})
        return True
    except Exception as e:
        print("Error updating sighting:", e)
        return False
    
