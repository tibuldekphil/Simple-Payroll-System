# Navigation Revamp

### Problem
> there's a risk of circular import between classes

### Solution
> I've thought of making a hamburger button to hold the buttons responsible for navigation or switching between pages.
> Why? Since circular imports occur when classes import from each other at the same time, This solution will solve that by having all imports happen inside the main Class

#### Steps:
- ~~Create a Hamburger button beside the header~~
- ~~Create a collapsible sidebar to access the buttons for navigation~~
- Move Buttons to the sidebar # moving the back buttons to the sidebar might be a bad idea

# Database - Accepting Entries

### Task: Get all Entry Values
>Register Company
    > ~~Get the Entry Values and store them to variables~~
    > ~~Validate~~
    > ~~Auto Create default admin account in DB~~
>Login Page 
    > Authenticate Admin Login
