// ==UserScript==
// @name       Ignore Slackbot
// @namespace  http://use.i.E.your.homepage/
// @version    0.2
// @description  ignore slackbot, modified by Penagwin
// @copyright  CC0 by Penagwin, modified from Ross Murray
// ==/UserScript==

// @include https://lumios.slack.com/*
// @run-at document-end
// @grant unsafeWindow
var oldAddMsg = TS.view.addMsg;

//List of Bots to block
listOfBots = ['U09218631', 'U08C6H4JV', 'U0AJCLQ5R']

//Show new messages if they aren't from a bot
var filterSlackMsg = function(msg, c) {
    for (var i = 0; i < listOfBots.length; i++)
        if (msg.user == listOfBots[i]) return false
    return true;
};

TS.view.addMsg = function(h, c) {
    if (filterSlackMsg(h, c) == true) {
        return oldAddMsg(h, 0);
    }
}

//Remove all of the bots in the list
removeBots = function() {
    for (var i = 0; i < listOfBots.length; i++)
        $("a[data-member-id='" + listOfBots[i] + "']").parent().filter("div.message").hide();
}

//Remember how we display channels
var oldDisplayChannel = TS.channels.displayChannel;

//Display the channels normally, with a twist
TS.channels.displayChannel = function(a, b, c, d) {
    var r = oldDisplayChannel(a, b, c, d);
    removeBots()
    return r;
}

//Wait until after the page has loaded
setTimeout(removeBots, 5000)
