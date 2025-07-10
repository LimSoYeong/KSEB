from db.models import Event

def insert_event(session, event_data):
    event = Event(**event_data)
    session.add(event)
    session.commit()

def get_upcoming_events(session):
    return session.query(Event).all()

##예시