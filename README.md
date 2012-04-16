# Refugees United CLI - XMPP Chatbot Module #
## Produced in two days at the Rewired State Refugees United Hackday, 14/15th April 2012 ##
## For more info see [the main project page](http://github.com/toastwaffle/refutdcli)

### By [Samuel Littley](http://github.com/toastwaffle), [Robert Wright](http://www.github.com/PureEntropy), [Craig Snowden](http://github.com/CraigSnowden) and [Kevin Lewis](http://github.com/phazonoverload) ###

Released under the MIT License

An XMPP Chatbot Interaction Module for the Refugees United CLI. Users can text commands to a designated XMPP/Jabber account, and receive a reply message with the results. Also works with Facebook chat.

## Installation & Usage ##

### To install: ###

* Edit xmppchatbot.py, adding the jabber ID in the form <user@example.com>, the password, and the correct URLs for the CLI responder pages, usually 'register.php' and 'respond.php'. Ensure the path to the SQLite database is correct.
* Run with python2.7 (i.e. 'python2.7 xmppchatbot.py')

## Commands ##

Supported commands are:

* "search"/"find"/"look" <Search Term>
    * Searchs for <Search Term> and displays a list of numbered matches
    * Responding "more" will return extra results
    * Responding a number will return more details about the chosen person
* "update"/"set" <Field> <Value>
    * Updates the users profile
    * Valid fields are:
        * phone
        * email
        * lastname
        * physicaltraits
        * favoriteplace
        * favoritefood
        * favoriteactivity
        * hometown
        * dob
        * occupation
        * parentsnationality
        * familysize
        * firstname
        * gender
        * lastsighting
        * nickname
        * otherinformation
        * tribe
* "messages"/"inbox"/"unread"
    * Retrieves numbered list of (unread) messages
    * Responding more will return extra messages
    * Responding a number will display the chosen message
* sent"
    * Displays sent messages
    * Responding more will return extra messages
    * Responding a number will display the chosen message
* "message"/"email"/"e-mail"/"chat"/"call"/"mail"/"send" <Name>
    * Sends message to given person
    * TODO, NOT IMPLEMENTED. Only sends to self.
* details"/"info"/"whoami"
    * Retrieves and displays users profile
* "help"/"man" (<command>)
    * Displays help messages
    * If <command> not given, lists possible commands
    * If <command> given, gives help for command
        * TODO. Only "update" has help.

The system ignores "a"/"get"/"my"/"please" before any command, and "a"/"for"/"I'm"/"message"/"my"/"to" after any command.

## Copyright ##

Copyright (c) 2012 Samuel Littley, Robert Wright, Craig Snowden, Kevin Lewis.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.