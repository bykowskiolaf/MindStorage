# Mindstorage

## Instalation
- `pip3 install -r requirements.txt`
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser`
- `python3 manage.py runserver`

## MindStorage
- [ ] Frontend: 
  - [ ] Login panel consisting of:
    * [ ] Login form consisting of:
    *  [ ] Login area
    *  [ ] Password area
    *  [ ] Login button
  - [ ] Tech support button redirecting to tech support panel
  - [ ] "Forgot your password?" button
  - [ ] Login form must be resistant to brute force attacks
  - [ ] Tech supprot panel consisting of:
    * [ ] submissions form consisting of:
      * [ ] first name 
      *  [ ] last name 
      *  [ ] e-mail adress
      *  [ ] description of a problem 
      *  [ ] "send submission" button 
    *  [ ] form must be accessable before the login 
    *  [ ] form must implement anti spam mechanisms 
  - [ ] account activasion panel:
    * [ ] visible after entering the activation link sent after being invited by  administrator 
    * [ ] cosisting of:
     * [ ] password area 
     * [ ] "repeat the password" area 
     * [ ] "give password" button
  - [ ] password reset panel 
   * [ ] accesable after clicking "forgot your password?" button 
   * [ ] consisting of:
     * [ ] e-mail adress area
     * [ ] "reset password" area 
   * [ ] after clicking "reset password" button, the resseting password link is being sent to given adress 
   * [ ] after entering the link, redirects to giving new  password screen 
  - [ ] new password screen:
   * [ ] accesable after entering the link in an e-mail representing password reseting 
   * [ ] consisting of:
     * [ ] password area
     * [ ] "repeat the password" area 
     * [ ] "give password" area 
  - [ ] administrator panel:
   * [ ] after logging in, there is a visible dashboard consisting of:
     * [ ] usefull graphs, for example: statistics, ammount of users ect.
     * [ ] bookmarks
     * [ ] logout button 
     * [ ] settings button 
  * [ ] tabs:
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
    * [ ] ability to logout  
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
  - [ ] ability to logout 
- [ ] Backend:
  - [ ] authentication and authorization users 
  - [ ] secure data storage
  - [ ] data encryption using cryptographic keys (stored with using HSM)
  - [ ] sending e-mails 
  - [ ] 2fa using a minimum OTP code to email and QR code to TOTP (e.g. google authenticator)


## Team
- [Bykowskiolaf](https://github.com/bykowskiolaf) - Frontend
- [Laxmymow](https://github.com/laxmymow) - Backend
- [Alex]() - Dev/Ops 
- [Janusz]() - Pm

