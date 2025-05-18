
class User:
    def __init__(self, username, password):
        self.__username = username 
        self.__password = password
        self.booked_tickets = []

    def check_login(self, username, password):
        return username == self.__username and password == self.__password

    def book_ticket(self, event):
        self.booked_tickets.append(event)

    def show_tickets(self):
        return self.booked_tickets


class PremiumUser(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.premium = True

    def show_tickets(self):
        return [f"Premium Ticket: {event}" for event in self.booked_tickets]


class Event:
    def __init__(self, name, date, price):
        self.name = name
        self.date = date
        self.price = price

    def __str__(self):
        return f"{self.name} on {self.date} for ${self.price}"



events = [
    Event("Music Concert", "2025-06-10", 50),
    Event("Art Exhibition", "2025-06-15", 30),
    Event("Tech Talk", "2025-06-20", 20),
]

def simulate_payment(amount):
   
    print(f"Processing payment of ${amount}...")

    return True



import streamlit as st

def main():
    st.title("Event Ticket Booking App")

   
    users = [
        User("user1", "pass1"),
        PremiumUser("premium1", "pass2"),
    ]

    
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        current_user = None
        for user in users:
            if user.check_login(username, password):
                current_user = user
                break

        if current_user:
            st.success(f"Welcome, {username}!")
            st.write("Available Events:")
            for idx, event in enumerate(events):
                st.write(f"{idx + 1}. {event}")
                if st.button(f"Book Ticket for {event.name}"):
                    if simulate_payment(event.price):
                        current_user.book_ticket(event)
                        st.success("Payment successful and ticket booked!")
        else:
            st.error("Invalid username or password")

    
    if 'current_user' in locals() and current_user:
        st.write("Your Booked Tickets:")
        tickets = current_user.show_tickets()
        if tickets:
            for ticket in tickets:
                st.write(ticket)
        else:
            st.write("No tickets booked yet.")

if __name__ == "__main__":
    main()
