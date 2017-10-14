**Readme**

*What does this do?*

Sometimes you hang up on a scammer before you come up with the perfect thing to say. Fortunately for you, sometimes they don't block their number. Use this to call 'em back with your favourite song using Twilio's Voice API.

*I'm in. What do I need?*

Automated diallers should probably be legal in your country before you do this. Please check first. Sign up on Twilio, and add the necessary junk in here.

You also want a VPS or somewhere to host an xml file that points to an MP3 file, like below.. This will be called by the Twilio client call in your script as a callback.

```xml

<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play>http://mywebsite.com/x_gon_give_it_to_ya.mp3</Play>
</Response>

```
