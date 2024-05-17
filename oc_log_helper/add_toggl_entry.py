#!/usr/bin/env python

import re

from gi.repository import Gtk, Gdk

from .toggl import get_toggl_client

class Prompt(Gtk.Dialog):
    def __init__(self, ticket, description="Reading the comment.", minutes="1"):
        super().__init__()
        self.set_decorated(False)
        box = self.get_content_area()

        self.ticket_entry = Gtk.Entry()
        self.ticket_entry.set_text(ticket)
        self.ticket_entry.connect("destroy", Gtk.main_quit)
        self.ticket_entry.grab_focus()

        self.description_entry = Gtk.Entry()
        self.description_entry.set_text(description)
        self.description_entry.connect("destroy", Gtk.main_quit)

        self.minutes_entry = Gtk.Entry()
        self.minutes_entry.set_text(minutes)
        self.minutes_entry.connect("destroy", Gtk.main_quit)

        box.add(Gtk.Label(label="LOG TIME"))
        box.add(self.ticket_entry)
        box.add(self.description_entry)
        box.add(self.minutes_entry)


class NewTaskWindow(Prompt):
    def __init__(self):
        super().__init__(Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD).wait_for_text())
        self.ticket_entry.connect("activate", self.create_entry)
        self.description_entry.connect("activate", self.create_entry)
        self.minutes_entry.connect("activate", self.create_entry)

    def create_entry(self, *args):
        ticket = self.ticket_entry.get_text()
        description = self.description_entry.get_text()
        minutes = self.minutes_entry.get_text()

        self.create_time_entry(ticket, description, minutes)
        self.destroy()

    def extract_ticket(self, ticket):
        ticket = re.search(r"[A-Z]{2,}-\d+", ticket)
        if ticket:
            return ticket.group(0)
        raise ValueError("No ticket found in the input string.")

    def create_time_entry(self, ticket, description, minutes):
        client = get_toggl_client()
        client.createTimeEntry(
            int(minutes) / 60,
            wid="4325196",
            description=description,
            project_id="162120186",
            tag=self.extract_ticket(ticket),
        )
        print("Created.")


def show_prompt(prompt):
    prompt.show_all()
    Gtk.main()


def add_toggl_entry():
    show_prompt(NewTaskWindow())
