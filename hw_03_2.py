import random

def generate_lottery_tickets(participant: list)-> dict:
    all_tickets = set()
    participant_tickets = {}

    for participant in participants:
        num_tickets = random.randint(1, 5)
        tickets = list()

        for _ in range(num_tickets):
            while True:
                ticket = tuple(sorted(random.sample(range(1, 50), k=6)))
                if ticket not in all_tickets:
                    all_tickets.add(ticket)
                    tickets.append(ticket)
                    break

        participant_tickets[participant] = tickets

    return participant_tickets

def pick_random_winner(participant_tickets):
    all_tickets = []
    for paticipant, tickets in participant_tickets.items():
        for ticket in tickets:
            all_tickets.append((participant, ticket))

    winner = random.choice(all_tickets)
    winner_name, winning_tickets = winner

    message = (
        f'Congratulation {winner_name}!\n'
        f'Your winning ticket {winning_tickets}'
    )

    return message

participants = ['Alex', 'Viktoriia', 'Jhon', 'Gwen']

participant_tickets = generate_lottery_tickets(participants)
for participant, tickets in participant_tickets.items():
    print(f'Participant:{participant}')
    print('Tickets:')
    for ticket in tickets:
        print(f'\t{ticket}')

print(pick_random_winner(participant_tickets))
