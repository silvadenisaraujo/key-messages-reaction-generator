import random
import csv

from faker import Faker

# create faker
fake = Faker()

# CONSTANTS
PERSONALITIES = ['curious', 'organized', 'outgoing', 'friendly', 'sensitive']
REACTIONS = ['POSITIVE', 'NEGATIVE', 'NEUTRAL']
KEY_MESSAGES = [
  {
    'id': 0,
    'message': 'KeyMessageA'
  },
  {
    'id': 1,
    'message': 'KeyMessageB'
  },
  {
    'id': 2,
    'message': 'KeyMessageC'
  },
  {
    'id': 3,
    'message': 'KeyMessageD'
  },
  {
    'id': 4,
    'message': 'KeyMessageE'
  },
  {
    'id': 5,
    'message': 'KeyMessageF'
  },]


# Script!

# Generate people
people = []
for i in range(300):
    person = {
      **fake.simple_profile(),
      'personality': random.choice(PERSONALITIES),
      'id': i
    }
    person['address'] = person['address'].replace('\n', ' ')
    people.append(person)


# Generate people reaction
reactions = []
for person in people:
  num_reactions = random.randint(1, len(KEY_MESSAGES))
  messages = random.sample(KEY_MESSAGES, num_reactions)
  for message in messages:
    reaction = random.choice(REACTIONS)
    person_reaction = {
      'person_id': person['id'],
      'message_id': message['id'],
      'reaction': reaction
    }
    reactions.append(person_reaction)

# Save to CSV

# Save people info
people_keys = people[0].keys()
with open('people.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, people_keys)
    dict_writer.writeheader()
    dict_writer.writerows(people)

# Save messages info
key_message_keys = KEY_MESSAGES[0].keys()
with open('key_messages.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, key_message_keys)
    dict_writer.writeheader()
    dict_writer.writerows(KEY_MESSAGES)

# Save relationship between people reaction and key message
reactions_keys = reactions[0].keys()
with open('key_message_reaction.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, reactions_keys)
    dict_writer.writeheader()
    dict_writer.writerows(reactions)