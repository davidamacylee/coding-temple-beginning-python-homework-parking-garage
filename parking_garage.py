# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 


# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# By the end of this project each student should be able to:
# - Explain and/or demonstrate creating classes
# - Explain and/or demonstrate creating class methods
# - Explain and/or demonstrate class instantiation

class ParkingGarage():

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        print(f'There are {str(len(self.tickets))} tickets left.')
        print(f'There are {str(len(self.parkingSpaces))} parking spaces left.')
    
    def payForParking(self):
        payment = input('How much are you paying for your parking ticket? ')
        if payment != '':
            print('Your ticket has been paid. You have 15 minutes to leave the parking structure.')
            self.currentTicket['paid'] = True
        else:
            print('Payment failed, please try to pay for your ticket again.')

    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print('Thank you, have a nice day!')
            self.tickets.append('ticket')
            self.parkingSpaces.append('space')
            print(f'There are {str(len(self.tickets))} tickets left.')
            print(f'There are {str(len(self.parkingSpaces))} parking spaces left.')
        else:
            print('Payment failed, please try to pay for your ticket again.')

tickets_available = ['ticket', 'ticket', 'ticket', 'ticket']
parkingSpaces_available = ['space', 'space', 'space', 'space', 'space']
my_ticket = {
    'paid': False,
    'material': 'paper',
}

downtownParking = ParkingGarage(tickets_available, parkingSpaces_available, my_ticket)

downtownParking.takeTicket()
downtownParking.payForParking()
downtownParking.leaveGarage()