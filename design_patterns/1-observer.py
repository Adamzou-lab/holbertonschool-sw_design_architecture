#!/usr/bin/env python3
"""Observer pattern — adding a new subscriber."""


class NewsSubject:
    """Publishes news events to registered observers."""

    def __init__(self):
        self._observers = {}

    def subscribe(self, observer, topics=None):
        """Register an observer, optionally filtered by topics."""
        self._observers[observer] = topics

    def unsubscribe(self, observer):
        """Remove an observer from the registry."""
        self._observers.pop(observer, None)

    def notify(self, topic, data):
        """Notify all observers interested in the given topic."""
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Logs news events to stdout."""

    def update(self, topic, data):
        print(f"log:{topic}={data}")


class EmailObserver:
    """Sends news events via email (stdout simulation)."""

    def update(self, topic, data):
        print(f"email:{topic}={data}")


class SmsObserver:
    """Sends news events via SMS (stdout simulation)."""

    def update(self, topic, data):
        print(f"sms:{topic}={data}")


def main():
    subject = NewsSubject()

    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    subject.subscribe(log_obs, topics={"sports", "breaking"})
    subject.subscribe(email_obs)
    subject.subscribe(sms_obs, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
