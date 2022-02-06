#!/usr/bin/env python

import re

from gi.repository import Gtk, Gdk
from toggl import api


class Prompt(Gtk.Dialog):
    def __init__(self, ticket, description="DESCRIPTION"):
        super().__init__()
        self.set_decorated(False)
        box = self.get_content_area()

        self.ticket_entry = Gtk.Entry()
        self.ticket_entry.set_text(ticket)
        self.ticket_entry.connect("destroy", Gtk.main_quit)

        self.description_entry = Gtk.Entry()
        self.description_entry.set_text(description)
        self.description_entry.connect("destroy", Gtk.main_quit)
        self.description_entry.grab_focus()

        box.add(Gtk.Label(label="START LOGGING"))
        box.add(self.ticket_entry)
        box.add(self.description_entry)


class NewTaskWindow(Prompt):
    def __init__(self):
        super().__init__(Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD).wait_for_text())
        self.ticket_entry.connect("activate", self.create_entry)
        self.description_entry.connect("activate", self.create_entry)

    def create_entry(self, *args):
        ticket = self.ticket_entry.get_text()
        description = self.description_entry.get_text()

        self.create_time_entry(ticket, description)
        self.destroy()

    def extract_ticket(self, ticket):
        ticket = re.search(r"[A-Z]{2,}-\d+", ticket)
        if ticket:
            return ticket.group(0)
        raise ValueError("No ticket found in the input string.")

    def create_time_entry(self, ticket, description):
        new_entry = api.TimeEntry.start_and_save(
            description=description,
            project=162120186,
            tags=[self.extract_ticket(ticket)],
        )
        new_entry.save()
        print("Created.")


def show_prompt(prompt):
    prompt.show_all()
    Gtk.main()


def start_toggl_tracking():
    show_prompt(NewTaskWindow())
