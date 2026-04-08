# dynamoCode.py
# helper functions for DynamoDB sighting logs
# my boyfriend helped me with the try-except method and Claude was used for incorporating the timestamps. 

import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('SanctuaryLog')

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

def add_sighting(display_name, animal_tag, sighting):
    """Adds a new sighting to the log. Create"""
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
    
def delete_sighting(display_name, timestamp):
    """Deletes a sighting by its partition + sort key. Delete"""
    try:
        table.delete_item(
            Key={
                'display_name': display_name,
                'timestamp': timestamp })
        return True
    except Exception as e:
        print("Error deleting sighting:", e)
        return False

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
    
