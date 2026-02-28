

# BookForMe

BookForMe is a centralized bilingual booking application designed to streamline informal bookings in Pakistan. The system includes a single application where users can log in either as **App Users** or **Vendors**, along with an AI Receptionist Agent that handles WhatsApp-based bookings.

## Project Overview

BookForMe allows people to discover services, check availability, and book time slots easily. Both customers and vendors use the same application, with role-based features. The AI Receptionist automates WhatsApp bookings by understanding user messages, confirming slot availability, and syncing with Firestore and Google Sheets.

## Core Components

1. **Unified Application (User + Vendor)**

   * **App User Mode:** Browse vendors, view availability, make bookings, manage profile, and use social features.
   * **Vendor Mode:** Manage business profile, set availability, track bookings, respond to customers, and view basic analytics.

2. **AI Receptionist Engine**
   An automated agent that interacts with WhatsApp users, processes booking requests through bilingual NLU, confirms slots, and updates Firestore and Google Sheets in real time.

## Definitions

**WhatsApp User**
A person who communicates with the AI Receptionist through WhatsApp to inquire or book services.

**App User**
A person using the BookForMe application to discover vendors, view availability, and book services or time slots.

**Vendor**
A service provider, business owner, or facility manager who lists their services on BookForMe and manages bookings, schedules, and customer interactions through the Vendor Mode within the same app.

## Tech Stack

* Flutter (single app with role selection)
* Firebase Firestore
* WhatsApp Cloud API
* Python or Node backend for the AI agent
* Google Sheets API

## Team

* Ahmad Hanif
* Jazib Waqas
* Muhammad Taqi
* Taha Hunaid

