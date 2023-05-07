# Mindstorage 🧠

## Instalation
- `pip3 install -r requirements.txt`
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser`
- `python3 manage.py runserver`

## Roadmap 🚧
- [ ] Frontend: 
  - [x] Login panel 
  - [x] Tech support button redirecting to tech support panel
  - [ ] "Forgot your password?" button
  - [ ] Login form must be resistant to brute force attacks
  - [ ] Account Activasion panel:
    * [ ] visible after entering the activation link sent after being invited by  administrator 
    * [ ] cosisting of:
     * [ ] password area 
     * [ ] "repeat the password" area 
     * [ ] "give password" button
  - [ ] Password reset panel 
  - [ ] Administrator panel:
     * [ ] usefull graphs, for example: statistics, ammount of users ect.
     * [ ] bookmarks
     * [x] logout button 
     * [ ] settings button 
  * [ ] Tabs:
       * [ ] users management:
         * [ ] presentation of users and information about them:
           * [ ] first name 
           * [ ] last name 
           * [ ] contact details - e-mail adress 
           * [ ] ammount of data used vs assigned data
          * [ ] ability to  invite new users 
          * [ ] ability to edit existing users 
          * [ ] ablity to allocate disk space to users 
        * [ ] disk management:
          * [ ] tab for managing general settings:
           * [ ] allowed extensions on the disk 
           * [ ] maximum user session time
        * [ ] submissions management: 
           * [ ] viewing submissions 
           * [ ] adding notes about the submission 
           * [ ] ability to close the submission 
  - [ ] user panel:
    * [ ] after logging in there is a visible "my files" tab 
    * [ ] on the pannel there must be visible:
      * [ ] favourites:
        * [ ] ability to add files to "favourites" tab, which are not showing on this list 
      * [ ] my files:
        * [ ] list of files sent on the disk 
      * [ ] shared:
        * [ ] list of shared files 
      * [ ] bin:
        * [ ] list of deleted files from "my files" screen 
        * [ ] they will be there untill the manual or automatic delete 
        * [ ] automatic delete time can be changed in settings 
      * [ ] settings:
        * [ ] 2fa
        * [ ] change password 
        * [ ] delete time change
  - [ ] occupied space view 
  - [ ] list of files in a format: file name, type, owner, size, upload date
  - [ ] each file can be downloaded, deleted, copied, shared (publicly in  the form of a link, within the organization - to a specific person)
  - [ ] ability to create and delete folders 
  - [ ] ability to download and share whole folders as ZIP
  - [x] ability to logout
- [ ] Backend:
  - [ ] authentication and authorization users 
  - [ ] secure data storage
  - [ ] data encryption using cryptographic keys (stored with using HSM)
  - [ ] sending e-mails 
  - [ ] 2fa using a minimum OTP code to email and QR code to TOTP (e.g. google authenticator)


## Team
- [Bykowskiolaf](https://github.com/bykowskiolaf) - Frontend
- [Laxmymow](https://github.com/laxmymow) - Backend
